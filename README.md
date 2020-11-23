# Flask REST API Seed
this is a simple project can be used as a seed of rest api projects using flask

## setting up the enviroment
- make sure you have python 3.8+ (newest version)
- create a new virtual environment, prefered in the project directory under name **.venv**
    ```
    python -m venv .venv
    ```
- activate the virtual environment
    ```
    source .venv/bin/activate
    ```
- run command to install required libs and frameworks
    ```
    pip install -r requirements.txt
    ```

## setting up the database
- create a Postgres database with login user
- the connection string of the database should like below
    ```
    postgresql://<user>:<password>@<db-host>:<port>/<database>
    ```

## setting up environment variables
- create in the root directory **.env** file
- open **.env.example** file, copy all variables names and paste them in the **.env** file
- fill the variables names with their values to match your development environment, like the database uri, paste in it the connection string

## database migrations
- make sure you are in the project directory
- make sure you have the **DATABASE_URI** in **.env** has value
- make sure the virtual environment activated
- run these cmds:
    ```
    ./bootstrap.sh init
    ./bootstrap.sh migrate
    ./bootstrap.sh upgrade
    ```

## run flask app
- run command
    ```
    ./bootstrap.sh
    ```

## run on Docker container
- make sure you are in the project directory
- make sure you have the **DATABASE_DOCKER_URI** in **.env** has value
- to run docker web and database in containers using docker compose:
    - to build the images:
        ```
        docker-compose build
        ```
    - to run the images:
        ```
        docker-compose up
        ```

## tests

- make sure you are in the project directory
- create a new database for testing, here we create new database for testing, and we have ***DATABASE_TESTING_URI*** in **.env**
- run this cmd:
    ```
    ./test.sh
    ```
