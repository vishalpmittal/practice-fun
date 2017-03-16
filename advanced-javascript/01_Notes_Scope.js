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


// ==============================
// this keyword
// ==============================

// eg. 1 
//-------

function foo() {
    console.log("gl " + this.bar);
}

var bar = "bar1";
var o2 = {bar : "bar2", foo: foo};
var o3 = {bar : "bar3", foo: foo};

var o4 = {
    bar : "bar4",
    foo : function() {
        console.log("o4 " + this.bar);
    }
};

var o5 = {bar : "bar5", foo:o4.foo};


// Implicit Binding
foo();              // "gl bar1"
o2.foo();           // "gl bar2"
o3.foo();           // "gl bar3"
o4.foo();           // "o4 bar4"
o5.foo();           // "o4 bar5"

// Explicit Binding
var o6 = {bar : "bar6"};
foo.call(o6);           // "gl bar6"

// Hard Binding
var o7 = {bar : "bar7"};
var o8 = {bar : "bar8"};

var orig = foo;
foo = function(){ orig.call(o7); };
foo.call(o8)            // "gl bar7"

foo = orig              // reset 
foo.call(o8)            // "gl bar8"

// Hard Binding2
function bind(fn, o) {
    return function() {
        fn.call(o);
    };
}

foo = bind(foo, o7);
foo.call(o8);            // "gl bar7"
foo = orig              // reset 
foo.call(o8)            // "gl bar8"

// Hard Binding3 (with return values and arguments)
if(!Function.prototype.bind3){
    Function.prototype.bind3 = 
        function(o) {
            var fn = this;        // the function we want to bind
            return function() {
                return fn.apply(o, arguments);
            };
        };
}

foo = foo.bind3(o7);
foo("baz");            // "gl bar7"

foo = orig              // reset 
foo.call(o8)            // "gl bar8"


// ========================================
// "new" key word
// ========================================
// 1. Brand new object is created
// 2. object gets linked to a different object
// 3. the new object get to this keyword for function call
// 4. implicitly return "this"

function foo() {
    var o2 = "o2";
    console.log(o1 + " " + this.o1 + ", " + o2 + " " + this.o2 + ", " + o3 + " " + this.o3 + ", " + o4 + " " + this.o4);
}

var o1 = "o1";
foo();               // "o1 o1, o2 undefined, undefined undefined, undefined undefined"
var o3 = "o3";
foo();               // "o1 o1, o2 undefined, o3 o3, undefined undefined"
var o4 = "o4";
new foo();           // "o1 undefined, o2 undefined, o3 undefined, o4 undefined"
foo();               // "o1 o1, o2 undefined, o3 o3, o4 o4"

// ========================================
// Rules to "this" keyword
// ========================================
// 1. was the function called with 'new' keyword. If yes this will belong to the new object
// 2. was the function called with 'call' or 'apply' specifying an explicit this?
// 3. was the function called via a containing/owning object (context)?
// 4. DEFAULT: global object (except strict model)





