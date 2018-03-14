FROM golang:1.9-alpine

CMD ["/go/bin/hello"]

COPY main.go /go/src/github.com/chrishiestand/docker-go-hello-world/

RUN cd /go/src/github.com/chrishiestand/docker-go-hello-world && \
    go get && \
    CGO_ENABLED=0 GOOS=linux go build -a -o /go/bin/hello main.go
