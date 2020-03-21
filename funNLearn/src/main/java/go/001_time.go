package main
import (
    "fmt"
    "time"
)


func main() {
    fmt.Println("Welcome to the playground!")

    //Time in the Go playground always appears to start at 2009-11-10 23:00:00 UTC
    // the first version of the playground, launched in 2010
    // The current time was fixed at 10 November 2009
    fmt.Println("The time is", time.Now())
}

