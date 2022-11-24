FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN su root
RUN apt-get -y update
RUN apt-get update && apt-get install -y gnupg2
ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=DontWarn

ARG USER_NAME
ARG PASSWORD
ARG DB_NAME

ENV PSQL_USER=$USER_NAME
ENV PSQL_PASSWORD=$PASSWORD
ENV PSQL_DB=$DB_NAME

# Add the PostgreSQL PGP key to verify their Debian packages.
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8
RUN apt-get -y install wget ca-certificates
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |  apt-key add

# Add PostgreSQL's repository. It contains the most recent stable release
RUN apt -y install lsb-core
RUN sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main"  \
    > /etc/apt/sources.list.d/pgdg.list'

RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN apt-get update

#install latest version
RUN apt-get -y install postgresql

RUN apt-get install -y software-properties-common postgresql postgresql-client postgresql-contrib

USER postgres

# Create a PostgreSQL role named ``user_role_name`` with ``user_password`` as the password and
# then create a database `user_database` owned by the ``user`` role.
RUN    /etc/init.d/postgresql start &&\
    psql --command "CREATE USER $PSQL_USER WITH SUPERUSER PASSWORD '$PSQL_PASSWORD';" &&\
    createdb -O $PSQL_USER $PSQL_DB

# Adjust PostgreSQL configuration so that remote connections to the
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/15/main/pg_hba.conf

# And add ``listen_addresses``
RUN echo "listen_addresses='*'" >> /etc/postgresql/15/main/postgresql.conf

# Add VOLUMEs to allow backup of config, logs and databases
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql/data"]

# Set the default command to run when starting the container
CMD ["/usr/lib/postgresql/15/bin/postgres", "-D", "/var/lib/postgresql/15/main","-c", "config_file=/etc/postgresql/15/main/postgresql.conf"]
EXPOSE 5432


