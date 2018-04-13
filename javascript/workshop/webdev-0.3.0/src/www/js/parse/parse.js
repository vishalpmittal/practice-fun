/******************************************************************************/
// EXERCISE:
//
// The `parse' function below will be called multiple times with a
// varying number of arguments.  The function should return the number
// of arguments that could successfully be parsed as integers.
function parse() {

  // Your code here...
  var count = 0;
  for (var i = 0; i < arguments.length; ++i) {
    if (isFinite(parseInt(arguments[i]))) {
      count += 1;
    }
  }
  return count;
}