/* ========================================
Closure :
Closure is when a function "remembers" its lexical scope even when 
the function is executed outside that lexical scope.
===========================================*/

/*------------
Example 1:
-------------*/
function foo() {
    var bar = "bar";

    function baz() {
        console.log(bar);
    }

    bam(baz);
}

function bam(baz){
    baz();                        // "bar"
}

foo();
/*-----------*/

/*------------
Example 2:
-------------*/
function foo() {
    var bar = "bar";

    return function() {
        console.log(bar);
    };
}

function bam(){
    foo()();                        // "bar"
}

bam();
/*-----------*/


/*------------
Example 3:
-------------*/
function foo() {
    var bar = "bar";

    setTimeout(function() {
        console.log(bar);
    }, 1000);
}

foo();
/*-----------*/

/*------------
Example 4:
-------------*/

function foo() {
    var bar = "bar";

    $("#btn").click(function(evt){
        console.log(bar);
    })
}

foo();
/*-----------*/

/*------------
Example 5:
-------------*/
function foo() {
    var bar = 0;

    setTimeout(function(){
        console.log(bar++);
    }, 100);

    setTimeout(function(){
        console.log(bar++);
    }, 200);
}

foo();         // 0  1
/*-----------*/

/*------------
Example 6: Nested Closure
-------------*/
function foo() {
    var bar = 0;

    setTimeout (function(){
        var baz = 1;
        console.log(bar++);

        setTimeout(function(){
            console.log(bar + baz);
        }, 200);
    }, 100);
}

foo();           // 0   2
/*-----------*/

/*------------
Example 7 :
-------------*/
for (var i=1; i <= 5; i++){
    setTimeout(function(){
        console.log("i: " + i);          // print i: 6, for 5 times. 
    }, i*1000);
}

for (var i=1; i <= 5; i++){
    (function(i){
        setTimeout(function(){
            console.log("i: " + i);          // print i: 1....5, in series
        }, i*1000);
    })(i);
}

for (let i=1; i <= 5; i++){
    setTimeout(function(){
        console.log("i: " + i);          // print i: 1....5, in series
    }, i*1000);
}
/*-----------*/



/*==========================================
 Module Pattern
===========================================*/
/*------------
Example : Classic Module Pattern
-------------*/
var foo = (function(){
    var o = {bar : "bar"};

    return {
        bar: function() {
            console.log(o.bar);
        }
    };
})();

foo.bar();             // "bar"

/*-----------*/

/*------------
Example : Modified Module Pattern, with same reference
-------------*/
var foo = (function(){
    var publicAPI = {
        bar: function(){
            publicAPI.baz();
        },
        baz : function(){
            console.log("baz");
        }
    };
    return publicAPI;
})();

foo.bar();

/*-----------*/


/*------------
Example : Modern Module Pattern,
-------------*/
define("foo", function(){
    var o = {bar : "bar"};

    return{
        bar: function(){
            console.log(o.bar);
        }
    };
});

/*-----------*/

/*------------
Example : ES6+ Module Pattern
-------------*/
//foo.js
var o = {bar : "bar"};

export function bar() {
    return o.bar;
}

// myProgram.js
// importing style 1, import only bar
import bar from "foo";
bar();                // "bar"

// importing style 2, import the whole module
module foo from "foo";
foo.bar();            // "bar"

/*-----------*/



/*==========================================

===========================================*/


/*------------
Example :
-------------*/


/*-----------*/



