//Go has only one looping construct, the for loop.

package main

import "fmt"

func main() {
    sum := 0
    for i := 0; i < 10; i++ {
        sum += i
    }
    fmt.Println(sum)

    //The init and post statement are optional.
    sum1 := 1
    for ; sum1 < 1000; {
        sum1 += sum1
    }
    fmt.Println(sum1)

    // Also used as While
    sum2 := 1
    for sum2 < 1000 {
        sum2 += sum2
    }
    fmt.Println(sum2)

    // infinite loop  or forever
    // for {
    // }
}
