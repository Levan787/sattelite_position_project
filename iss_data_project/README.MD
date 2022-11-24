# SATELLITE_POSITION 

Description:

The main idea of the project is to create and working in POSTGRESQL and private docker image.


This project shows how to build private image without pulling it from docker hub and run your program using that image.

## COMMANDS
Here is the commands which help user working with docker and dockerfile.

1) Build docker image with private data for security.

```docker build --build-arg USER_NAME=username --build-arg PASSWORD=user_password --build-arg DB_NAME=user_database_name -t my_postgres_image .```

2) How to run docker image with user_port and local port

```docker run -p ''user_port':5432 -d my_postgres_image```

