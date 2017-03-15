
package main
import "fmt"

//A function can take zero or more arguments. 
//Notice that the type comes after the variable name.
func add(x int, y int) int {
    return x + y
}

//When two or more consecutive named function parameters share a type,
// you can omit the type from all but the last.
func add1(x, y int) int {
    return x + y
}

//A function can return any number of results.
func swap(x, y string) (string, string) {
    return y, x
}

/*
    Go's return values may be named. 
    If so, they are treated as variables defined at the top of the function.
    A return statement without arguments returns the named return values. 
    This is known as a "naked" return.
*/
func split(sum int) (x, y int) {
    x = sum * 4 / 9
    y = sum - x
    return
}

/*
    defer
    A defer statement defers the execution of a function until 
    the surrounding function returns.
    
    The deferred call's arguments are evaluated immediately, 
    but the function call is not executed until the surrounding function returns.
*/
func testDefer() {
    defer fmt.Println("world")

    fmt.Println("hello")
}

/*
    Stacking defers

    Deferred function calls are pushed onto a stack. 
    When a function returns, its deferred calls are executed in last-in-first-out order.
*/
func testDefer1() {
    fmt.Println("counting")

    for i := 0; i < 10; i++ {
        defer fmt.Println(i)
    }

    fmt.Println("done")
}

func main() {
    fmt.Println(add(42, 13))

    fmt.Println(add1(42, 13))

    a, b := swap("hello", "world")
    fmt.Println(a, b)

    fmt.Println(split(17))

    testDefer()
    testDefer1()
}
