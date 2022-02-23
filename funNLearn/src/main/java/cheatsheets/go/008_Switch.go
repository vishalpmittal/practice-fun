package main

import (
	"fmt"
	"runtime"
	"time"
)

func testSwitch1() {
	fmt.Print("Go runs on ")
	switch os := runtime.GOOS; os {
	case "darwin":
		fmt.Println("OS X.")
	case "linux":
		fmt.Println("Linux.")
	default:
		// freebsd, openbsd,
		// plan9, windows...
		fmt.Printf("%s.", os)
	}
}

/*
	Switch cases evaluate cases from top to bottom, 
	stopping when a case succeeds.
	
	(For example,
	switch i {
	case 0:
	case f():
	}
	
	does not call f if i==0.)
*/
func testSwitch2() {
	fmt.Println("When's Saturday?")
	today := time.Now().Weekday()
	switch time.Saturday {
	case today + 0:
		fmt.Println("Today.")
	case today + 1:
		fmt.Println("Tomorrow.")
	case today + 2:
		fmt.Println("In two days.")
	default:
		fmt.Println("Too far away.")
	}
}

/*
Switch with no condition
Switch without a condition is the same as switch true.
*/
func testSwitch3() {
	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("Good morning!")
	case t.Hour() < 17:
		fmt.Println("Good afternoon.")
	default:
		fmt.Println("Good evening.")
	}
}


func main() {
	testSwitch1()
	testSwitch2()
	testSwitch3()
}
