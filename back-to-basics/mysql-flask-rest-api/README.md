# Flask My-SQL REST API

Build the application and database image using the following command

```
$ docker-compose build
```

To run the dockerized application, execute the following command from the terminal

```
$ docker-compose up
```

## API

Use POSTMAN to test the HTTP Requests by using URL: http://**docker-machine-ip-address**:5000

    - GET: 
        - Returns all user credentials
    
    - PUT:
        - Insert new user credential
