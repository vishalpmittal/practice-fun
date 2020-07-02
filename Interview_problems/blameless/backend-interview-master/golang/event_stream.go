package main

import (
	"bufio"
	"fmt"
	"os"
)

// EventStream is the simulation for change and access log events
type EventStream struct {
	name string
	apiSpecs []*APISpec
	accessLog *AccessLog
	changeLog *ChangeLog
	maxEvents int64
	numEvents int64
}

type Event struct {
	Type string
	Value string
}

// getApiSpecs will read a file containing API specs and return a list of API specs
func getApiSpecs(filename string, seed int64) []*APISpec {
	var apiSpecs []*APISpec
	var name, email, verb, resource string
	var rate, slo float64
	var window uint

	fd, err := os.Open(filename)
	if err != nil {
		panic(fmt.Sprintf("Could not open API spec file: '%s'", filename))
	}
	scanner := bufio.NewScanner(fd)

	for scanner.Scan() {
		line := scanner.Text()
		fmt.Sscanf(line, "%s %s %s %s %f %f %d", &name, &email, &verb, &resource, &rate, &slo, &window)
		apiSpec := NewApiSpec(seed, name, email, verb, resource, rate, slo, window)
		apiSpecs = append(apiSpecs, apiSpec)
	}
	if err := scanner.Err(); err != nil {
		panic(fmt.Sprintf("Error reading from '%s': %s", filename, err.Error()))
	}
	return apiSpecs
}

// NewEventStream will return a new instance of an event stream simulation
func NewEventStream(name string, startTime float64, maxEvents int64, seed int64,
	changeRate, probOfBug, probOfError float64) *EventStream {
		apiSpecs := getApiSpecs("./api_specs", seed)
		return &EventStream {
			name: name,
			apiSpecs: apiSpecs,
			accessLog: NewAccessLog(apiSpecs, startTime),
			changeLog: NewChangeLog(seed, apiSpecs, changeRate, probOfBug, probOfError),
			maxEvents: maxEvents,
			numEvents: 0,
		}
}

// GenerateEvent will generate a new access or change event
func (eventStream *EventStream) GenerateEvent() *Event {
	if eventStream.numEvents >= eventStream.maxEvents {
		return &Event{
			Type: "end-of-stream",
			Value: "end-of-stream",
		}
	}

	currTime := eventStream.accessLog.GetCurrTime()
	eventStream.numEvents++

	changeLogEvent := eventStream.changeLog.Generate(currTime)
	if len(changeLogEvent) > 0 {
		return &Event{
			Type: "change",
			Value: changeLogEvent,
		}
	}

	accessLogEvent := eventStream.accessLog.Generate()
	return &Event{
		Type: "access",
		Value: accessLogEvent,
	}
}

// GetAPISpecs will return all of the API specs for this simulation
func (eventStream *EventStream) GetAPISpecs() []*APISpec {
	return eventStream.apiSpecs
}

// GetInfo will return the dict-format of all of the API specs for this simulation
func (eventStream *EventStream) GetInfo() []map[string]string {
	infos := make([]map[string]string, len(eventStream.apiSpecs))

	for i, apiSpec := range eventStream.apiSpecs {
		infos[i] = apiSpec.ToDict()
	}
	return infos
}
