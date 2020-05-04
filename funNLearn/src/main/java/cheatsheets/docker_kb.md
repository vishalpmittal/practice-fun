## docker system level commands

``` bash
docker version
docker info                 (shows number of containers and images)
docker system prune
docker system prune -a      (clean up all cache)

ls /var/lib/docker/containers/contId/                 # all the json files for metadata
cat /var/lib/docker/containers/contId/config.json     # config information

# following two commands has a same effect
service docker start
/usr/bin/docker -d --log-level=fatal

service docker stop
docker -d -l debug &               # Logging levels: debug, info, error, fatal
```

## Docker images commands

``` bash
docker images
docker images -a
docker inspect imageId                 # Image low level detailed information
docker history img                     # shows everything/commands run earlier on image
docker pull coreos/etcd                # pull a particular image
docker --tree imageId                  # shows the image layers

# build a custom image, -rm (remove intermediate stages), --tag | -t (tag the image with name)
docker build --rm --tag aw-image --file Dockerfile .

docker tag imageId vishalDocHubId/helloworld:1.0   # this is actually the repo name
docker push vishalDocHubId/helloworld:1.0          # Only new layers gets pushed, existing images are skipped
docker rmi imageId1 imageId2 imageId3              # delete/remove images
docker pull vishalDocHubId/helloworld:1.0          # pull fresh image from doc hub
```

## Docker exec and run commands

``` bash
docker ps                                     # check docker containers running
docker ps -l                                  # shows last container running
docker run -it ubuntu:14.04 /bin/bash         # run a container interactively using ubuntu image
docker exec -it contId /bin/bash              # run bash terminal a running container 
root@contId :/# ctrl + P + Q                  # detach and come out to host
```

## Docker Container commands

``` bash
docker attach contId         (reattach the terminal to container command prompt)
docker stop contId           (stop containers with contId)
docker start contId          (start containers with contId)
docker restart contId        (restart containers with contId)
docker rm contId             (remove/delete a container, should be stopped earlier)
docker rm -f contId          (remove/delete a running container)
docker top contId            (processes running on container with more details)
docker logs contId           (docker logs for that container)
docker inspect contId | grep Pid

# run a container using aw-image, and name it aw-cont, port forwarded is 8000
docker run -d --name aw-cont -p 8000:8000 aw-image
```

## Private Registry

``` bash
# expose port 5000 from container to outside and launch the container
root@dockRegHost:~ docker run -d -p 5000:5000 registry      

# debian.... is the host name of private registry running as a container
root@dockHost1:~ docker images
root@dockHost1:~ docker tag imageId debian.docker.course:5000/priv-reg-test 

# image pushed to private repo 
root@dockHost1:~ docker push imageId debian.docker.course:5000/priv-reg-test       
   
# pulls the image and runs it
root@dockHost2:~ docker run -d debian.docker.course:5000/priv-reg-test  
```

## Docker Volumes

``` bash
docker run -it -v /test-vol --name=volVishal ubuntu:15.04 /bin/bash

# shows local container details from volVishal container
docker inspect volVishal        
"Volumes" : {
    "/test-vol" : "/var/lib/docker/vfs/dir/contId"
}, 
"VolumesRW" : {
    "/test-vol": true
}
... ..

# run container volPoorva with volVishal volume settings
docker run -it --volumes-from=volVishal --name=volPoorva ubuntu:15.04 /bin/bash
```

## Docker networking

### Attaching multiple networks to a container

``` bash
# Create the networks
docker network create --subnet 172.29.0.0/16 --ip-range 172.29.240.0/20 bluenet
docker network create --subnet 172.30.0.0/16 --ip-range 172.30.240.0/20 rednet

# Option1: directly run container with a network
docker run -itd --network bluenet --name c1 busybox sh

# Option2: Create the container with network and start later
docker create -it --network bluenet --name c1 busybox sh
docker start c1

# Option3: Create container and then attach network to it and then start
docker create -it --name c1 busybox sh
docker network connect --ip 172.29.0.2 rednet c1
docker network connect --ip 172.30.0.2 bluenet c1

docker create -it --name c2 busybox sh
docker network connect --ip 172.29.0.3 rednet c2
docker network connect --ip 172.30.0.3 bluenet c2

docker start c1
docker start c2

# Execute the container
docker exec -it c1 sh
/ $ ifconfig
eth0
eth1
lo

/ $ ip route
default via 172.29.0.1 dev eth0
172.29.0.0/16 dev eth0  src 172.29.0.2
172.30.0.0/16 dev eth1  src 172.30.0.2
```

