Dockerfile :
is an definition of the docker image




1.  FROM:
    -----
    The FROM instruction initializes a new build stage and sets the base image for subsequent instructions.
    A valid Dockerfile must start with FROM instruction.

    Usage:
        FROM <image> [AS <name>]
            AS is optional where you give name to the new build stage.
        FROM <image>[:<tag>] [AS <name>]

2.  RUN:
    ----
    RUN has two forms.
    form 1:
    -------
        RUN <command> : shell form
        command run in a shell.which is by default /bin/sh -c on Linux and cmd /S and /C on Windows.

        The RUN instruction will execute any commands in a new layer on top of the current image and commits the results.
        The resulting committed image will be used for the next step in the Dockerfile.

    form 2:
    -------
        RUN ["executable", "param1", "param2"] (exec form)
        ex :
             RUN ["/bin/sh", "-c" "ls"]
             RUN ["/bin/bash", "-c", "echo hello"]

Note:
docker build --no-cache : to not to store any intermediate builds.


3.  CMD:
    ----
    CMD instructions has three forms:
    forms:
    -------
        CMD ["executable","param1","param2"] (exec form, this is the preferred form)
        CMD ["param1","param2"] (as default parameters to ENTRYPOINT)
        CMD command param1 param2 (shell form)

    Note:
        There should be only one CMD in a Dockerfile. if there are more than CMD instruction then last CMD instruction
        will take the effect.

    Note: Don’t confuse RUN with CMD. RUN actually runs a command and commits the result;
    CMD does not execute anything at build time, but specifies the intended command for the image.

4.  LABEL:
    ------
    Label instruction adds metadata to an image.
    A label is a key-value pair. To include spaces within a LABEL value, use quotes and blackslashes.

    Syntax:

    LABEL <key>=<value> <key>=<value>

    LABEL version = "1.0"
    LABEL "Image Name" = "NEW Linux Image"
    LABEL description = "This Image is for \
                        running linux dependent applications"

    Note:
        Labels are included in the base image or parental images [FROM instruction in the Dockerfile] are inherited by
         your image. if a label already exists but with a different value , the nost recently added value overrides the
         previously set value.

    To View Image's Labels:

    docker inspect.

    output:
        "Labels": {
                    "com.example.vendor": "ACME Incorporated"
                    "com.example.label-with-value": "foo",
                    "version": "1.0",
                    "description": "This text illustrates that label-values can span multiple lines.",
                    "multi.label1": "value1",
                    "multi.label2": "value2",
                    "other": "value3"
                    },

5.  MAINTAINER: [DEPRECATED]:
    -------------------------
    The MAINTAINER instruction sets the author field of the generated image.

    example:

    LABEL maintainer = "Dayananda.DR@emc.com"

    This will be visible from the docker inspect.


6.  EXPOSE:
    ------
    The "EXPOSE" instruction informs Docker that the container listens on the specified network port at runtime.
    We can specify whether the port listens on TCP or UDP protocol.
    By default it listens on TCP.

    The EXPOSE instruction does not actually expose the PORT. It acts as a documentation between the person who built
    image and the person who runs the container.

    To actually the publish the port in a running a cotainer, use -p flag in the docker run command.

    EXPOSE 80/udp    ---> if you don't specify then it is TCP.

    To expose on both TCP and UDP.

    EXPOSE 80/TCP
    EXPOSE 80/UDP

    Usage:

    docker run <image> -p 80:80/tcp -p 80/80udp ........


7.  Difference between ADD and COPY:
    --------------------------------
    COPY and ADD are both Dockerfile instructions that serve almost the same. They let you copy from src to destination.

    COPY : copies local file <src> to the docker image <destination>.

    ADD: It serves the same but src can it be either url or archieved folder. It copies the data and extracts the data
            at the destination.


8.  ENTRYPOINT:
    -----------
    is a base command for executing in any container.

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



