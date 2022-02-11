function say_hello () {
echo "Hello"
}

"""
declare -f ==> Lists details of a function
syntax: declare -f <function-name>
eg: declare -f say_hello

declare -xf say_hello ==> exports function so that function is available for child shell as well.say_hello

"""
