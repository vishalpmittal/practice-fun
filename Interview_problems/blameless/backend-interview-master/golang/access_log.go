package main

import "math"

// AccessLog represents a simulated access log for one or more APIs.  The simulation
// is driven by repeated calls to `generate()`.  Each call will return a single access log
// line from a single API, where that API is the next to generate an event in the simulation.
type AccessLog struct {
	apiSpecs []*APISpec
	currIdx int
	currTime float64
	nextDraws []*APIEvent
	minIdx int
}

// initialDraws will populate the next firing event for all API endpoints
func initialDraws(apiSpecs []*APISpec, currTime float64) []*APIEvent {
	apiEvents := make([]*APIEvent, len(apiSpecs))
	for i, apiSpec := range apiSpecs {
		apiEvents[i] = apiSpec.Generate(currTime)
	}
	return apiEvents
}

// NewAccessLog will return an instance of the simulated access log
func NewAccessLog(apiSpecs []*APISpec, startTime float64) *AccessLog {
	return &AccessLog{
		apiSpecs: apiSpecs,
		currIdx: 0,
		currTime: startTime,
		nextDraws: initialDraws(apiSpecs, startTime),
		minIdx: 0,
	}
}

// GetCurrTime will return the current simulation time
func (accessLog *AccessLog) GetCurrTime() float64 {
	return accessLog.currTime
}

// Generate will return the next access event in the simulation
func (accessLog *AccessLog) Generate() string {
	draw := accessLog.getNextLine()
	accessLog.currTime = draw.Ts
	return draw.Event
}

// getNextLine will return the next API event for the simulated access log
func (accessLog *AccessLog) getNextLine() *APIEvent {
	draw := accessLog.nextDraws[accessLog.minIdx]
	accessLog.nextDraws[accessLog.minIdx] = accessLog.apiSpecs[accessLog.minIdx].Generate(draw.Ts)
	accessLog.updateMinIndex()
	return draw
}

// updateMinIndex will update the internally managed min index to match the next firing event.  This is
// a O(N) operation, which is fine.  Another option would be to use a PQ to ensure O(log N).  This is
// not really an issue ATM, since the num,ber of APIs is in the 10s
func (accessLog *AccessLog) updateMinIndex() {
	minDraw := math.MaxFloat64
	for i, draw := range accessLog.nextDraws {
		if draw.Ts < minDraw {
			accessLog.minIdx = i
			minDraw = draw.Ts
		}
	}
}
