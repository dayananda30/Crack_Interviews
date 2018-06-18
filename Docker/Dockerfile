Dockerfile :
is an definition of the docker image



ENTRYPOINT: is a base command for executing in any container.

CMD : is optional parameter to ENTRY POINT command.

Example:

    .Dockerfile
    From Ubuntu:14:04
    ENTRYPOINT "uname"
    CMD "-a"

    #Building the Docker Image with the name myImage
    docker build -t myImage .

    #Run the myImage Image without parameter
    docker run -it myImage
    Output:
        output : uname -a is the output

    #Run the myImage Image with parameter, which inturn suppress the CMD parametes
    docker run -it myImage -v
    Output:
        output: -v is suppressed by -a parameter









