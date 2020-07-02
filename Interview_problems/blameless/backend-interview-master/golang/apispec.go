package main

import "fmt"

// APISpec encapsulates all of the properties associated with a simulated API endpoint
type APISpec struct {
	name string
	email string
	verb string
	resource string
	rate float64
	errorDist *UniformDist
	errorProb float64
	bugged bool
	slo float64
	window uint
	secsPerRequest float64
	tolerance float64
	timeDist *UniformDist
}

// APIEvent encapsulates the properties of an event
type APIEvent struct {
	Ts float64
	Event string
}

// NewAPISpec will create a new APISpec object from the given arguments
func NewApiSpec(seed int64, name, email, verb, resource string, rate float64, slo float64, window uint) *APISpec {
	return &APISpec{
		name: name,
		email: email,
		verb: verb,
		resource: resource,
		rate: rate,
		errorDist: NewUniformDist(seed),
		errorProb: 0.0,
		bugged: false,
		slo: slo,
		window: window,
		secsPerRequest: 1.0 / rate,
		tolerance: 0.1 / rate,
		timeDist: NewUniformDist(seed),
	}
}

// getNextTime will draw the next event time from the time distribution
func (apiSpec *APISpec) getNextTime(currTime float64) float64 {
	return currTime + apiSpec.timeDist.Random(apiSpec.secsPerRequest - apiSpec.tolerance, apiSpec.secsPerRequest + apiSpec.tolerance)
}

// Generate a new access log line based on the current state of this API object
func (apiSpec *APISpec) Generate(currTime float64) *APIEvent {
	status := 200
	newTime := apiSpec.getNextTime(currTime)
	if apiSpec.errorDist.Random(0.0, 1.0) < apiSpec.errorProb {
		status = 500
	}
	return &APIEvent{
		newTime,
		fmt.Sprintf("%.4f %s %s %d", newTime, apiSpec.verb, apiSpec.resource, status),
	}
}

// IntroduceBug simulates the introduction of a bug in this API, which generates an error at a given probability
func (apiSpec *APISpec) IntroduceBug(errorProb float64) {
	apiSpec.bugged = true
	apiSpec.errorProb = errorProb
}

// FixBug simulates a bug being fixed
func (apiSpec *APISpec) FixBug() {
	apiSpec.bugged = false
	apiSpec.errorProb = 0.0
}

// HasBug will return true is there is an ongoing bug in this API
func (apiSpec *APISpec) HasBug() bool {
	return apiSpec.bugged
}

// ToDict will return the dictionary representation of this API specification
func (apiSpec *APISpec) ToDict() map[string]string {
	return map[string]string {
		"name": apiSpec.name,
		"email": apiSpec.email,
		"verb": apiSpec.verb,
		"resource": apiSpec.resource,
		"slo": fmt.Sprintf("%f", apiSpec.slo),
		"window": fmt.Sprintf("%d", apiSpec.window),
	}
}


