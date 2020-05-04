
## Requirements

* python3
* virtualenv
* django==3.0.5


## Build Instructions

### Mac
```bash
$ virtualenv -p python3 ~/vpmittal_venv
$ . ~/vpmittal_venv/bin/activate
$ pip install django==3.0.5
$ cd ~/github/vpmittal

$ python manage.py runserver
```

### Docker
```bash
$ cd ~/github/vpmittal

# build the docker image
$ docker build --rm --tag vpmittal-image --file DOCKERFILE .

# run the docker image
$ docker run -d --name vpmittal-cntnr -p 8000:8000 vpmittal-image
```



