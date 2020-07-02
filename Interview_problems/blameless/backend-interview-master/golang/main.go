package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"time"
)

type Args struct {
	seed int64
	maxEvents int64
	probBug float64
	probError float64
}

func getArgs() *Args {
	seed := flag.Int64("seed", 1337, "RNG seed value")
	maxEvents := flag.Int64("maxEvents", 100000, "Max number of events to generate")
	probBug := flag.Float64("probBug", 0.1, "Probability that a change introduces a bug")
	probError := flag.Float64("probError", 0.05, "Probability of an error, given a bug was introduced")

	return &Args {
		seed: *seed,
		maxEvents: *maxEvents,
		probBug: *probBug,
		probError: *probError,
	}
}

func main() {
	args := getArgs()
	currTime := float64(time.Now().Unix())

	eventStream := NewEventStream("fizzbuzz", currTime, args.maxEvents, args.seed, 0.1, args.probBug, args.probError)

	serviceMonitor := GetServiceMonitor(eventStream)
	fmt.Println(serviceMonitor.MTTR())
	apiHistogram := serviceMonitor.ApiHistogram()
	apiHistogramJson, err := json.Marshal(apiHistogram)
	if err != nil {
		panic(fmt.Sprintf("Error converting API histpogram to JSON: %v", err))
	}
	fmt.Printf("%s\n", apiHistogramJson)
	incidentDetails := serviceMonitor.IncidentDetails()
	incidentDetailsJson, err := json.Marshal(incidentDetails)
	if err != nil {
		panic(fmt.Sprintf("Error converting incident details to JSON: %v", err))
	}
	fmt.Printf("%s\n", incidentDetailsJson)
}