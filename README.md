# Simple Flask App

This is a simple flask app used for learning docker and kubernetes. Nothing fancy.

```docker
docker build -t simpleapp .
docker container run -it -p 8080:8080 simpleapp # interactive
docker container run -dp 8080:8080 simpleapp # background
```
