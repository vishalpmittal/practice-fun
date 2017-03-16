// =========================
// Scope and execution
// =========================

var foo = "bar";

function bar() {
    var foo = "baz";

    function baz(foo) {
        foo = "bam";
        bam = "yay";

        console.log(foo);            //"bam"
        console.log(bam);            //"yay"
    }
    baz();

    console.log(foo);            //"baz" 
    console.log(bam);            //"yay" 

}

bar();
console.log(foo);            //"bar"
console.log(bam);            //"yay"
baz();              // ERROR!!! : uncaught reference error: baz is not defined


// =========================
// Function Expression
// =========================

var foo = function bar(){
    var foo = "baz";

    function baz(foo){
        foo = bar;
        console.log(foo);  // prints the function
    }
    baz();
    console.log(foo);      // "baz"
}

console.log(foo);       // prints the function
foo();                  // calls the function
console.log(foo);       // prints the function
bar();                  // Uncaught ReferenceError: bar is not defined(...)

// =========================
// eval
// Do not use !!!!!!!!
// =========================
var bar = "bar"

function foo(str) {
    eval(str);               // Cheating
    console.log(bar);        //42

}

foo("var bar = 42;");
console.log(bar);            //"bar"

// =========================
// with
// Do not use !!!!!!!!
// =========================





// =========================
// let vs var
// let is local to even "if" or "for" blocks
// Block-scoped declarations (let, const, function, class) not yet supported outside strict mode(…)
// =========================

// eg. 1
//----------
function foo() {
    var bar = "bar";

    for (let i =0; i<bar.lenth; i++){
        console.log(bar.charAt(i));
    }

    for (var j =0; j<bar.lenth; j++){
        console.log(bar.charAt(j));
    }

    console.log(j);                // 0
    console.log(i);                // Reference Error
}
foo();

// eg. 2
//----------
function foo() {
    if (bar) {
        let baz = bar;
        if (baz) {
            let bam = baz; 
        }
        console.log(bam);                // Reference Error
    }
    console.log(baz);                // Reference Error
}

// eg. 3
//----------
function foo(bar) {
    if (bar) {
        console.log(baz);               // Reference Error
        let baz = bar;
    }
}
foo(bar);

// =========================
// IIFE Pattern
// Immediately invoked function pattern
// =========================

// eg. 1
//------
var foo = "foo";

(function (){
    var foo = "foo2";
    console.log(foo);      //"foo2"
}
)();

console.log(foo);          //"foo"

// eg. 2
//------
var foo = "foo";

(function(bar){
    var foo = bar;
    console.log(foo);      //"foo"
}
)(foo);

console.log(foo);          //"foo"

// =========================
// Dynamic Scoping (Not supported in JS)
// Try to find variable in some other scope 
// eg. where this function is called from
// =========================

function foo() {
    console.log(bar);
}

function baz(){
    var bar = "bar";
    foo();
}

baz();


// =========================
// Hoisting, the order of compiling and then execution
// =========================

// ----------
// eg1. 
// ---code----
a;
b;
var a = b;
var b = 2;
b;
a;

// ---JS Engine execution----
var a;
var b;
a;
b;
a = b;
b = 2;
b;
a;
// ----------

// ----------
// eg. 2
// ---code----
var a = b();
var c = d();
a;
c;

function b() {
    return c;
}

var d = function() {
    return b();
}


// ---JS Engine execution----
function b() {
    return c;
}

var a; 
var c; 
var d;

a = b();
c = d();

a;
c;

d = function() {
    return b();
};

// ----------







