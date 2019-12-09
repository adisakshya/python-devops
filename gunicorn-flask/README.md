# Gunicorn Flask

Build the image using the following command

```
$ docker build -t gunicorn-flask:latest .
```

Run the Docker container using the command shown below.

```
$ docker run -d -p 5000:5000 gunicorn-flask
```

The application will be accessible at http://**docker-machine-ip**:5000