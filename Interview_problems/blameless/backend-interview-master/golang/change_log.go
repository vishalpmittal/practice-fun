package main

import (
	"encoding/hex"
	"fmt"
	"github.com/google/uuid"
	"time"
)

// ChangeEntry encapsulates the properties of a change event
type ChangeEntry struct {
	name string
	email string
	ts float64
	commit string
}

// ChangeLog simulates a sequence of change events
type ChangeLog struct {
	timeBetweenChanges float64
	lastChangeTs float64
	apiSpecs []*APISpec
	probOfBug float64
	probOfError float64
	bugDist *UniformDist
	apiSelector *UniformDist
}

// NewChangeEntry will return a new change event
func NewChangeEntry(name, email string, ts float64) *ChangeEntry {
	commitUuid := uuid.New()
	// Note: error is always nil, so no point in tracking it
	uuidBytes, _ := commitUuid.MarshalBinary()

	return &ChangeEntry{
		name: name,
		email: email,
		ts: ts,
		commit: hex.EncodeToString(uuidBytes),
	}
}

// ToDict will return a map representation of a change event
func (changeEntry *ChangeEntry) ToDict() map[string]string {
	return map[string]string {
		"name": changeEntry.name,
		"email": changeEntry.email,
		"commit": changeEntry.commit,
		"ts": fmt.Sprintf("%.4f", changeEntry.ts),
	}
}

// ToLogEntry will return a Git-like string for a change event
func (changeEntry *ChangeEntry) ToLogEntry() string {
	str := "commit: " + changeEntry.commit + "\n"
	str += "Author: <" + changeEntry.email + ">\n"
    str += fmt.Sprintf("Date: %s\n", time.Unix(int64(changeEntry.ts), 0).Format(time.UnixDate))
	str += "Service: " + changeEntry.name + "\n"
	return str
}

// ToString will return a simple structured string representation of a change event
func (changeEntry *ChangeEntry) ToString() string {
	return fmt.Sprintf("'name': %s, 'email': %s, 'ts': %f, 'commit': %s", changeEntry.name, changeEntry.email,
		changeEntry.ts, changeEntry.commit)
}

// NewChangeLog will return a new instance of a simulated change log
func NewChangeLog(seed int64, apiSpecs []*APISpec, changeRate, probOfBug , probOfError float64) *ChangeLog {
	return &ChangeLog {
		timeBetweenChanges: 1.0 / changeRate,
		lastChangeTs: 0.0,
		apiSpecs: apiSpecs,
		probOfBug: probOfBug,
		probOfError: probOfError,
		bugDist: NewUniformDist(seed),
		apiSelector: NewUniformDist(seed),
	}
}

// Generate a change log event
func (changeLog *ChangeLog) Generate(currTime float64) string {
	apiSpec := changeLog.apiSpecs[changeLog.apiSelector.RandomInt(len(changeLog.apiSpecs))]

	// Only create changes at the prescribed rate
	if currTime - changeLog.lastChangeTs < changeLog.timeBetweenChanges {
		return ""
	}

	// Assume this change fixed the previous bug
	if apiSpec.HasBug() {
		apiSpec.FixBug()
	} else if changeLog.bugDist.Random(0.0, 1.0) < changeLog.probOfBug {
		apiSpec.IntroduceBug(changeLog.probOfError)
	}

	changeLog.lastChangeTs = currTime

	return NewChangeEntry(apiSpec.name, apiSpec.email, currTime).ToLogEntry()
}
