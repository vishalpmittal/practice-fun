package main

// ServiceMonitor is the interface required by the main class
type ServiceMonitor interface {
	MTTR() float64
	ApiHistogram()  map[string]int64
	IncidentDetails() map[string][]map[string]string
}

// GetServiceMonitor will return a fully processed service monitor
func GetServiceMonitor(eventStream *EventStream) ServiceMonitor {
	// ToDo: PUT YOUR SOLUTION HERE
	return nil
}
