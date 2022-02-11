# Local Variables are available to that shell and not to the commands triggered from that shell

#create a local variable
name=dayananda
#or
set name=dayananda

#To list all local variables
set | grep name

#Environment available all over the place.
export name="dayananda"

#To list environment variable
env | grep name



