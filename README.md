# useful commands for working with this project


building the dockerfile

```shell
$ docker build -f Dockerfile.flask -t docker-flask:test .
```

`-f`: for specifying docker file  
`-t`: docker image name and tag

running the image from last command

```shell
$ docker run -it --rm -p 8000:5000 --name flask docker-flask:test
```

`-it`: opens a interactive terminal into the container omit this if you
don't need it  
`--rm`: remove the container when it exit.  
`-p 8000:5000`: publish 5000 port inside container to 8000 in the host.
you would see the container in 8000 port (`localhost:8000`) in your computer.  
`docker-flask:test` is the name of the image we want to run.  
`--name flask`: a human readable name for our container

for attaching a volume to the container
we need the volume for our development, so every file you edit get updated
in the container automatically, otherwise you have to build the image and run it again
every time you change a file.

```shell
$ docker run -it --rm -p 8000:5000 -v ${PWD}:/app docker-flask:test
```

`-v ${PWD}:/app`: mount current working directory to the app directory inside the container.  


attack a bash to the running container. this is helpful for seeing what's going on inside the container.

```shell
docker exec -it flask bash
```

`-it`: for interactive terminal.
`bash`: what command to run inside the container. in our case we want to open a
bash inside a container named flask.
