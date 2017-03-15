package main

import "fmt"

func printSlice(s []int) {
    fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}

/*
    The type [n]T is an array of n values of type T.
    
    The expression     var a [10]int
    declares a variable a as an array of ten integers.
    
    An array's length is part of its type, so arrays cannot be resized. 
*/
func testArrays1(){
    var a [2]string
    a[0] = "Hello"
    a[1] = "World"
    fmt.Println(a[0], a[1])
    fmt.Println(a)

    primes := [6]int{2, 3, 5, 7, 11, 13}
    fmt.Println(primes)
}

/*
    Slices
    -  An array has a fixed size. 
    -  A slice, on the other hand, is a dynamically-sized, flexible view 
       into the elements of an array. In practice, slices are much more common than arrays.
    -  The type []T is a slice with elements of type T.
    -  This expression creates a slice of the first five elements of the array a:
       a[0:5]
*/
func testSlices1(){
    primes := [6]int{2, 3, 5, 7, 11, 13}

    var s []int = primes[1:4]
    fmt.Println(s)
}

/*
    - Slices are like references to arrays
    - A slice does not store any data, it just describes a section of an underlying array.
    - Changing the elements of a slice modifies the corresponding elements of its underlying array.
    - Other slices that share the same underlying array will see those changes.
*/
func testSlices2(){
    names := [4]string{
        "John",
        "Paul",
        "George",
        "Ringo",
    }
    fmt.Println(names)

    a := names[0:2]
    b := names[1:3]
    fmt.Println(a, b)

    b[0] = "XXX"
    fmt.Println(a, b)
    fmt.Println(names)
}

/*
    Slice literals
    ============================
    - A slice literal is like an array literal without the length.
    - This is an array literal:
      [3]bool{true, true, false}
    - And this creates the same array as above, then builds a slice that references it:
      []bool{true, true, false}
*/
func testSlices3(){
    q := []int{2, 3, 5, 7, 11, 13}
    fmt.Println(q)

    r := []bool{true, false, true, true, false, true}
    fmt.Println(r)

    s := []struct {
        i int
        b bool
    }{
        {2, true},
        {3, false},
        {5, true},
        {7, true},
        {11, false},
        {13, true},
    }
    fmt.Println(s)
}

/*
    Slice defaults
    ======================
    - When slicing, you may omit the high or low bounds to use their defaults instead.

    - The default is zero for the low bound and the length of the slice for the high bound.

    - For the array
    - var a [10]int

    - these slice expressions are equivalent:
      a[0:10]
      a[:10]
      a[0:]
      a[:]
*/
func testSlices4(){
    s := []int{2, 3, 5, 7, 11, 13}

    s = s[1:4]
    fmt.Println(s)

    s = s[:2]
    fmt.Println(s)

    s = s[1:]
    fmt.Println(s)
}

/*
    - Slice length and capacity
    - The length of a slice is the number of elements it contains.
    - The capacity of a slice is the number of elements in the underlying array, 
      counting from the first element in the slice.
    - The length and capacity of a slice s can be obtained using the expressions
      len(s) and cap(s).
    - You can extend a slice's length by re-slicing it, provided it has sufficient capacity.
*/
func testSlices5(){
    s := []int{2, 3, 5, 7, 11, 13}
    printSlice(s)

    // Slice the slice to give it zero length.
    s = s[:0]
    printSlice(s)

    // Extend its length.
    s = s[:4]
    printSlice(s)

    // panic: runtime error: slice bounds out of range
    // s = s[:10]
    // printSlice(s)

    // Drop its first two values.
    s = s[2:]
    printSlice(s)

}

/*
    Nil slices
    -  The zero value of a slice is nil.
    -  A nil slice has a length and capacity of 0 and has no underlying array.
*/
func testSlices6(){
    var s []int
    fmt.Println(s, len(s), cap(s))
    if s == nil {
        fmt.Println("nil!")
    }
}

/*
    Dynamically-sized arrays / Creating a slice with make
    ==================================================
    -  Slices can be created with the built-in make function; 
       this is how you create dynamically-sized arrays.
    -  The make function allocates a zeroed array and returns a slice 
       that refers to that array:
       a := make([]int, 5)  // len(a)=5

    -  To specify a capacity, pass a third argument to make:

       b := make([]int, 0, 5) // len(b)=0, cap(b)=5

       b = b[:cap(b)] // len(b)=5, cap(b)=5
       b = b[1:]      // len(b)=4, cap(b)=4
*/



func main() {
    testArrays1()
    testSlices1()
    testSlices2()
    testSlices3()
    testSlices4()
    testSlices5()
    testSlices6()
}