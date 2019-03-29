# Bash
- powertool, no undelete, no undo 
- system files are protected

## Bash Commands
- `mv *` will move all the files and directories in current dir 
   to the last dir in sorted order. 

### Brace expansion:
```bash
# will create 19 files with name my_doc-v1.txt and so on...
touch my_doc-v{1..19}.txt

# creates filea1.jpg, filea1.txt, filea2.jpg, ... so on.
touch file{a,b,c}{1,2,3}.{jpg,txt,pdf}
```

### echo 
- -n suppresses newline
- -e allows use of escape sequence
- \t for tab, \b for backspace

### printf
- no new line by default 
- in line formatting 
  ```bash
  printf "hello %s, now are you\n" $USER
  
  printf "hello %s, %s, %s\n" a b c      # prints one hello a, b, c 
  printf "hello %s,\n" a b c             # prints three line hello a, hello b and hello c 
  printf "|%20s | %20s |\n" $(ls)       # prints ls out in tabular column output
  printf -v myvar "hello %s, %s, %s\n" a b c   # saves output to variable myvar
  ```

### read
- -n or -N reads specific number of chars
- -s supress output 
- -r disallow escape sequence. a good habit 
- single line multi read
  ```bash
  read a b
  1 2 3 4                    # a will be '1' and b will be '2 3 4'
  ```

### Sort 
```bash
# sort reverse, numeric sort, on key(column) 2nd
sort -rnk2 myfile.txt
```

### uniq
```bash
# sort the file content, get only unique ones, also print count
# this is like group_by in sql
sort myfile.txt | uniq -c
```

### cut command
```bash
# shows column 3 data and cut's everything else.
cut -f 3 myfile.txt
```

### grep 
```bash
# matches all but empty line, sort them and find uniques
# "^$" is empty line 
grep -v "^$" myfilte.txt | sort | uniq

ls -l | grep "^d"              # list only directories
ls -l | grep -v "^d"           # list only files
```

### find
```bash
find /usr -name vishal
find . -name '*.txt'

# file names with content "curious"
find . -name '*.txt' -exec grep -l curious {} \;
```

### tr (text replace)
```bash
# replace capital S with small s in output
cat myfile.txt | tr S s

# same as above
tr S s < myfile.txt

# replace tab by semicolon in myfile.txt and save it back in myfile.txt
tr \\t \; < myfile.txt > myfile.txt
```
   
### sed (stream editor)

### paste
```bash
# puts line by line cobined data from all txt files
paste *file.txt
```

### join
```bash
# works more like sql joins. but files better be sorted
join file1.txt text2.txt
```

### env
command to see all environment variables
   
### type
```bash
# what is cp ? it's a file in /bin/cp
type cp
cp is /bin/cp
```

### aliasing
```bash
#quick way to change to fun_dir
alias fun_dir="cd /path/to/fun_dir"
```

### Command substitution 
```bash
# replaces command output for $()
echo "hello $(whoami)"
touch "today$(date)".txt
echo "you are currently on $(hostname)"
```

### End of options
- Use -- in commands to skip problems with symbols or - char in filenames 
```bash
touch -a.jpg          # Error illegal option
touch -- -a.jpg       # works fine
```

## short cut keys 
- ctrl + a : start of line
- ctrl + e : end of line
- ctrl + f : forward one character
- ctrl + b : back 1 character
- alt + f : forward 1 word
- alt + b : back 1 word
- .
- ctrl + D : delete a character
- ctrl + H : delete a char backwards
- alt + D : delete a word
- ctrl + W : delete word backwards
- ctrl + k : delete rest of line 
- ctrl + U : delete from start of line 

## Standard streams
- standard input: stdin, 0, /dev/stdin
- standard output: stdout, 1, /dev/stdout
- standard error: stderr, 2, /dev/stderr
- /dev/null discards all data sent to it, its like a trash can

### redirect examples
```bash
cmd 2> /dev/null       # discard all errors
1>&2                   # send output to stderr
>&2                    # send output to stderr
2>&1                   # redirects stderr into stdout
cmd >logfile 2>&1      # send stdout to logfile, then redirect stderror to stdout, 
                       # thus send both error and output to a single logfile

2>&1 >logfile cmd    # redirect stderr to stdout, send stdout to logfile 
                     # thus sends stderr to stdout(terminal) and stdout to logfile

# they both are same, takes stdin from inputfile, and sends stdout to outputfile
cmd < inputfile > outputfile
>outputfile cmd < inputfile

echo "bad variable value" > /dev/stderr      # sends error to stderr
```

### DO NOT USE!
```bash
cmd > logfile 2> logfile    # this will override the logfile with errors
&> or >&                    # depricated.
```

## Bash Options 
- set
  - -x : prints each command with its arguments as it is executed
  - -u : gives an error when using an uninitialized variable and exits script
  - -n : read commands but do not execute
  - -v : print each command as it is read
  - -e : exits script whenever a command fails (but not with if, while, until, ||, &&) 
  - set -o noclobber: Don't overwrite files on redirection operations.

- shopt
  - Can set many options with -s, unset with -u
  - shopt -s nocaseglob: Ignore case with pathname expansion 
  - shopt -s extglob: Enable extended pattern matching
  - shopt -s dotglob: Include hidden files with pathname expansion 
  
## Running scripts:

- Need execution permissions 
  - myscript

- do not need execution permissions. These read file and executes each line on cli. 
  - bash myscript 
  - bash -x myscript
  - source myscript
  - .myscript

- exec
  - redirect i/o for whole script. useful for logging

### Multitasking
- fg : bring job to foreground
- bg : send job to background, keeps sending logs to screen
- &  : background job, should be put at the very end of command

### background
- & lets your script run in background but kills on exiting terminal session
```bash
# run myscript in background, save logs to output.log
./my_script > output.log &
```

- nohup, keeps your script running when you exit the terminal session
```bash
nohup myscript &
```

- nice, run myscript with lower priority.
```bash
# run myscript in background with lower priority and keep it running
# on terminal session end
nohup nice myscript &
```

### scheduling / cron
- at: execute at a specific time
  - at -f myscript noon tomorrow
- Cron
- launchd (only on mac)
- upstart (only on ubuntu)

### Exit codes
- 0 is success code 
- rest 1-255 are unix error codes 

# Shell scripting

## Shebang
  - line  (#!), pronounced hash bang
  - first line bash interpreter specifying 
  ```bash
  #!/bin/bash
  ```

## Variables

### Integar variables 
```bash
declare -i num           # $num can only hold numbers, 
                         # setting it to string will set it to 0
declare +i num           # unset attribute with +

p="4+5"; echo $p                      # prints 4+5
declare -i p; p="4+5"; echo $p        # prints 9
```
- -r read only variable

### Arrays 

```bash
declare -a x         # declare an array x
x[0]="some"          # store value some at 0th index
${x[0]}              # retrieve value at 0
${x[@]}              # retrieve all value as a single string
${x[*]}              # retrieve all value as a single string

ar=(1 2 3 a b c)     # initialize whole array

${#array[@]}         # length of array

ar[1]="a"; ar[4]="b"; ar[15]="c"
echo ${#ar[@]}         # prints 3 and not 15

${!ar[@]}         # list of all indices in an array prints 1 4 15 

```

-  bash 4 supports associative arrays

### Exporting variables
- by default variables are only available in the script. 

    To make them available outside you have to export the var. 

- Exporting a var to inner scope

   For eg. if script1 calls script2 which calls script3
   defining these in script2 will make them available to script3 and not to script1
   ```bash
   export var="vishal"
   declare -x var="vishal"
   ```

### Variable Arguments 
  ```bash
  $0                     # holds the name of the script as it was called
  $1, $2 ....$9, ${10}....${25}....$n   #holds n-th command line argument
  $#                     # number of script arguments
  $?                     # exit status of last command
  ${#var}                # length of variable value
  $*                     # all arguments combined as a string
  $@                     # all arguments combined as a string, preferred usage

  for a in "$@"; do echo $a; done
  ./myscript "arg 1" "arg 2" "arg 3"
  arg 1
  arg 2
  arg 3

  for a in "$*"; do echo $a; done
  ./myscript "arg 1" "arg 2" "arg 3"
  arg 1    arg 2    arg 3
  ```

### Shifting Arguments
- shift removes $1 and shifts $2 -> $1, $3->$2 .. and so on
- each shift lowers $# by one
- 'shift 3' removes $1, $2 and $3 and shifts $4->$1
- following will keeping shifting argument value left every time loops is run

```bash
while [[ $1 ]]; do
    echo "current argument is $1"
    shift
done
```

### getopts
- Utility to accept cli arguments
- getopts get options and the argument values provided
- "b:s:r" can be used but doesn't handle OPTARG errors.
- ":b:s:r" is better as 
  - If value of -b is missing it puts option as ":" and value in OPTARG variable
  - so it's easy to handle it in code.
- OPTIND stores the option index number
- see count_v1.sh and count_v2.sh examples.

## Strings
- ${#var} : length of $var

### sub string removal
- ${var#pattern} : removes shortest match from begin of string
- ${var##pattern} : removes longest match from begin of string
- ${var%pattern} : removes shortest match from end of string
- ${var%%pattern} : removes longest match from end of string

```bash
st="/Users/vishalm/test.txt"
${st#*/}       # Users/vishalm/test.txt (removes first / and anything before /)
${st##*/}      # test.txt (removes all / and anything before /)
${st%.*}       # /Users/vishalm/test (removes last . and anything after)
${st%/*}       # /Users/vishalm (removes last / and anything after)
```

### substitution/replace
- ${var/pattern/string} : substitute first match with string
- ${var//pattern/string} : substitute all match with string
- ${var/#pattern/string} : matches beginning of string
- ${var/%pattern/string} : matches end of string

```bash
i="mytxt.txt"
echo ${i/txt/jpg}          # myjpg.txt
echo ${i/%txt/jpg}         # mytxt.jpg
echo ${i//%txt/jpg}        # mytxt.txt
echo ${i//%txt/}           # mytxt.txt
echo ${i/%txt/}            # mytxt.
echo ${i//txt/}            # my.
echo ${i//[yx]/a}          # matat.tat
```

### default values
- default values
  - ${var:-value} : evaluate to "value" if var is empty or unset
  - ${var-value}  : similar, but only if var is unset
- default assignments
  - ${var:=value} : if var was empty or unset, this evaluates to "value" and assigns it to var
  - ${var=value}  : similar, but only if var is unset

```bash
declare MY_HOME=${MYDIR:-$HOME}    # if MYDIR is empty/unset $HOME is assigned to MY_HOME
```

## Arithmetic expressions 

### command (( .. ))
- typically used in if, while, until loops for arithmetic decisions
- also used inline assignments
  ```bash
  (( p=x/100 ))
  (( p=$(ls|wc -l)* 10 ))                # saves line count * 10 in p
  ```

### substitution or assignment $(( .. ))
- 
  ```bash
  p=$(( x/100 ))
  ```

### difference
```bash
vishalm$ declare -i x
vishalm$ x=100/2
vishalm$ echo $x
50
vishalm$ $((++x))
-bash: 51: command not found
vishalm$ ((++x))
vishalm$ echo $x
52
vishalm$ x=$((x+1))
vishalm$ echo $x
53
```

-  read 
```bash
read -p "your name please!" note         # read's user input in variable $note
```

## Conditional expressions:
- All you need to know about supported conditional expressions
```bash
help test
help [[
```
-  comparison operators like =, < , > etc. work on strings only
-  for numbers use eq, ne, lt, le, gt, ge, etc. 

### Binary operators
-  do not use -a, -o for and and or respectively. These were used in older systems
-  spaces around expression between [[ expression ]] are important
-  it separates out expression and [[ for linux system
   ```bash
   [[ $str ]]               # str is not empty
   [[ $str="something" ]]   # str is equal to something
   [[ -e $filename ]]       # if filename exists
   [[ -d $dirname ]]        # if dirname exists
   [[ ! $1 ]]               # if missing first argument for the script
   [[ $# -ne 2 ]]           # if number of arguments not exactly 2
   ```

### Patterns
- ==, != operators in [[ .. ]] do pattern matching
- == and = are same 
```bash
# pattern matching, without ""
[[ $filename==*.txt ]]   # returns true if file is a text file

# string matching, with ""
[[ $var=="[0-9]*" ]]     # matches string "[0-9]*"
```

### Regular Expression Matching
- =~ is used
```bash
declare -r num_re='^[0-9]+$'     # starts with 0-9 digit, has 1 or more occurrence and ends with it
if [[ $1 =~ $num_re ]]; then 
    echo "is a number"
else 
    echo "not a number"
fi
```

## Control Flow 

### if then elif then else fi
  - One line 
    ```bash
    if testcode; then successcode; else failcode; fi
    ```

  - Multiline 
    ```bash
    if [[ $my_var ]]; then
        echo "yes"
    elif [[ $your_var ]]; then
        echo "you"
    else
        echo "no"
    fi
    ```

  - command output > as if condition 
    ```bash
    if mkdir "$my_dir"; then
       echo "created dir $my_dir"
    else
       echo "could not create $my_dir"
    fi
    ```

### While, 
 repeat as long as test returns true
 ```bash
 while test; do
    ;; code to be repeated
 done
 ```

### Until
 repeat until test returns true
 ```bash
 until test; do
     ;;   code to be repeated
 done
 ```

### For
```bash
for var in words; do
    ;; code to be repeated
done
```

- One liner 
  ```bash
  for i in these are different words of a list for shell; do echo $1; done

  for i in "printed on one line"; do echo $1; done
  ```

- Wildcard for eg, change extension of the files
  - ./mvext txt pdf will chagne extensions of all txt files to pdf
  - remove echo to stop dry run and actually run it
    ```bash
    #!/bin/bash

    if [[ $# -ne 2 ]]; then
    echo "need exactly two arguments"
    fi

    for f in *"$1"; do
    base=$(basename "$f" "$1")
    echo mv "$f" "${base}$2"
    done
    ```

- For loop, C style:
  ```bash
  for (( INIT; TEST; UPDATE )); do
      ;; loop code
  done 
  
  
  for (( i=0; i<length; i++ )); do
      printf "="
  done
  ```

### break
### continue
### case
  ```bash
  case $tarfile in
      *.tgz|*.gz|*.gzip)
          echo "using gzip" >$2;;         # print diagnostic mesg to stderr
      *.bz|*.bz2|*.bzip|*.bzip2)
          echo "using bzip2" >$2;;
      *.Z)
          echo "using compress" >$2;;
      *.tar)
          echo "no compression used" >$2;;
      *)
          echo "unknown extension" >&2
          exit 3;;
  esac
  ```

### Combining cmds
- && and || and { cmd1; cmd2; cmd3 }
-  these can also be used without conditions
-  eg: one line if statement for num of arg check.
   ```bash
   [[ $1 ]] || { echo "missing argument">&2; exit1; }
   [[ $# -ne 2 ]] && { echo "Need exactly two arguments" >&2; exit 1 }
   ```

## Functions

### Function arguments:
- $1, $2 ... represents function arguments
- $? represents the return value
  ```bash
  #!/bin/bash
  sum() {
      return $(( $1 + $2 ))
  }

  sum 4 5
  echo $?
  ```

- Returns
```bash
starts_with_a () {
    [[ $1 == [aA]* ]];
    return $?                     # return the output of command before.
}

starts_with_a () {
    [[ $1 == [aA]* ]];           # same effect as above. by default it returns the cmd out
}

if starts_with_a "ax"; then echo "yes"; else "no"; fi
```

### exit vs. return
 - exit exit's the whole program, while return returns to previous calling place
 - to return out of a function use return

### scope
- variables are scoped inside the functions
```bash
declare -i x=0
my_func () {
    x=1
    printf $x         # prints 1
}
my_func
printf $x             # prints 0
```
      
## Are you sure:
following script repeats untill there is an answer either yes or no
```bash
#!/bin/bash

echo -n "Are you sure (Y/N)? "
answered=
while [[ ! $answered ]]; do
    read -r -n 1 -s answer
    if [[ $answer = [Yy] ]]; then
        answered="yes"
    elif [[ $answer = [nN] ]]; then
        answered="no"
done
printf "\n%s\n" $answered
```
