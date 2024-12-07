# INSTALLATION

## Docker 

### Mysql

 - docker pull mysql:latest
 - docker run -d --name test-mysql -e MYSQL_ROOT_PASSWORD=root -p 3307:3306 mysql

### Fast-API

 - docker build -t fastapi .
 - docker run -d --name test-fastapi -p 80:80 fastapi

## Swagger

 - http://localhost/docs