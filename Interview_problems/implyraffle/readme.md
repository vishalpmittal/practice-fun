# Imply raffle ticket test django app usage

## Usage

- after unzipping build and run the docker container using following commands

```bash
# Unzip the file and go to the directory
vishalm$ pwd
/Users/vishalm/Downloads/implyraffle

# build the docker image
vishalm$ docker build --rm --tag imply-image --file Dockerfile .

# run the docker image
vishalm$ docker run -d --name imply-cont -p 8000:8000 imply-image
```

- From a browser or curl from command line on host go to following urls to test the environment setup.
```bash
$ curl "http://localhost:8000/raffle/newgame"
"{'Success': 'New Raffle Game Started!'}

$ curl "http://localhost:8000/raffle/participants"
{}

$ curl "http://localhost:8000/raffle/issue?user=matt&tickets=2"
{'Sucess: Alloted 2 tickets to user matt'}

$ curl "http://localhost:8000/raffle/issue?user=paul&tickets=3"
{'Sucess: Alloted 3 tickets to user paul'}

$ curl "http://localhost:8000/raffle/issue?user=tom&tickets=5"
{'Sucess: Alloted 5 tickets to user tom'}

$ curl "http://localhost:8000/raffle/participants"
{'matt': {1001, 1002}, 'paul': {1003, 1004, 1005}, 'tom': {1006, 1007, 1008, 1009, 1010}}

$ curl "http://localhost:8000/raffle/transfer?donor=tom&recipient=paul&tickets=1"
{'Success: Transferred 1 tickets from tom to paul'}

$ curl "http://localhost:8000/raffle/transfer?donor=tom&recipient=matt&tickets=2"
{'Success: Transferred 2 tickets from tom to matt'}

$ curl "http://localhost:8000/raffle/transfer?donor=tom&recipient=paul&tickets=2"
{'Success: Transferred 2 tickets from tom to paul'}

$ curl "http://localhost:8000/raffle/participants"
{'matt': {1008, 1001, 1002, 1007}, 'paul': {1003, 1004, 1005, 1006, 1009, 1010}}

$ curl "http://localhost:8000/raffle/draw"
{'Winner': 'Hurreyy!!! Congratulations matt:1001'}

$ curl "http://localhost:8000/raffle/participants"
{'matt': {1008, 1002, 1007}, 'paul': {1003, 1004, 1005, 1006, 1009, 1010}}

$ curl "http://localhost:8000/raffle/draw"
{'Winner': 'Hurreyy!!! Congratulations matt:1007'}

$ curl "http://localhost:8000/raffle/participants"
{'matt': {1008, 1002}, 'paul': {1003, 1004, 1005, 1006, 1009, 1010}}

$ curl "http://localhost:8000/raffle/newgame"
{'Success': 'New Raffle Game Started!'}

$ curl "http://localhost:8000/raffle/participants"
{}
```