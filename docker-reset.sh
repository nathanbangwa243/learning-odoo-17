#!/bin/bash

# delete odoo docker instance
echo "**********[STOP ODOO DOCKER INSTANCES]*********"
docker stop postgres_local

echo "**********[DELETE ODOO DOCKER INSTANCES]*********"
docker rm -f odoo17Learning postgres_odoo17Learning

# delete all volumes
echo "**********[DELETE ODOO DOCKER VOLUMES]*********"
docker volume rm learning-odoo-17_odoo-db-data learning-odoo-17_odoo-web-data learning-odoo-17_odoo-db-pgdata

# execute the project
echo "**********[START ODOO DOCKER INSTANCES]*********"
docker compose up -d --force-recreate