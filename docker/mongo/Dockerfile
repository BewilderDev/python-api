FROM mongo:latest

COPY mongod.conf /etc/mongod.conf

COPY init-mongo.js /docker-entrypoint-initdb.d/

RUN chmod 755 /docker-entrypoint-initdb.d/init-mongo.js