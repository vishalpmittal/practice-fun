//Programs start running in package main.
package main

import (
    "fmt"
    "math/rand"
    “math”
)

func main() {
    fmt.Println("My favorite number is", rand.Intn(10))
    fmt.Printf("Now you have %g problems.", math.Sqrt(7))
    fmt.Println(math.pi)
}
