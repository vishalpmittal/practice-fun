# Atomwise django app usage

## Usage

- after unzipping build and run the docker container using following commands

```bash
# Unzip the file and go to the directory
vishalm$ pwd
/Users/vishalm/Downloads/atomwise

# build the docker image
vishalm$ docker build --rm --tag aw-image --file Dockerfile .

# run the docker image
vishalm$ docker run -d --name aw-cont -p 8000:8000 aw-image
```

- From a browser on host go to following urls to test the environment setup.

  - localhost:8000/admin
  - localhost:8000/wine
