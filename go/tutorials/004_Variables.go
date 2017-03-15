package main

import (
	"fmt"
)

//The var statement declares a list of variables;
//as in function argument lists, the type is last.
var c1, python1, java1 bool

//If an initializer is present, the type can be omitted;
//the variable will take the type of the initializer.
var c2, python2, java2 = true, false, "no!"

var i3, j3 int = 1, 2

func main() {
	var i4 int
	fmt.Println(i3, c1, python1, java1)
	fmt.Println(i4, c2, python2, java2)

	// Inside a function, the := short assignment statement can be used in
	// place of a var declaration with implicit type.
	// Outside a function, every statement begins with a keyword (var, func, and so on)
	// and so the := construct is not available.
	k5 := 3
	c5, python5, java5 := true, false, "no!"

	fmt.Println(i3, j3, k5, c5, python5, java5)

	/*
	 * Zero values
	 * Variables declared without an explicit initial value are given their zero value.
	 *
	 * The zero value is:
	 *
	 * 0 for numeric types,
	 * false for the boolean type, and
	 * "" (the empty string) for strings.
	 */
	var i6 int
	var f6 float64
	var b6 bool
	var s6 string
	fmt.Printf("%v %v %v %q\n", i6, f6, b6, s6)

	/*
	Constants
	- Constants are declared like variables, but with the const keyword.
	- Constants can be character, string, boolean, or numeric values.
	- Constants cannot be declared using the := syntax.
	*/
	const Pi = 3.14
	const World = "世界"
	fmt.Println("Hello", World)
	fmt.Println("Happy", Pi, "Day")

	const Truth = true
	fmt.Println("Go rules?", Truth)


}
