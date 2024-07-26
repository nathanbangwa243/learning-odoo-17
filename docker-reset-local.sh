#!/bin/bash

# delete odoo docker instance
echo "**********[DELETE ODOO DOCKER INSTANCES]*********"
docker rm -f postgres_local

# delete all volumes
echo "**********[DELETE ODOO DOCKER VOLUMES]*********"
docker volume rm learning-odoo-17_local-db-pgdata

# execute the project
echo "**********[START ODOO DOCKER INSTANCES]*********"
docker compose -f docker-compose-local.yml up -d --force-recreate

# odoo test launcher
# odoo17 -c config/odoo-local.conf -i estate --test-enable

# run all the tests of account, and modules installed by account
 # the dependencies already installed are not tested
 # this takes some time because you need to install the modules, but at_install
 # and post_install are respected
# odoo-bin -i account --test-enable
 # run all the tests in this file
# odoo-bin --test-file=addons/account/tests/test_account_move_entry.py
 # test tags can help you filter quite easily
# odoo-bin --test-tags=/account:TestAccountMove.test_custom_currency_on_account_1# run all the tests of account, and modules installed by account
 # the dependencies already installed are not tested
 # this takes some time because you need to install the modules, but at_install
 # and post_install are respected
# odoo-bin -i account --test-enable
 # run all the tests in this file
# odoo-bin --test-file=addons/account/tests/test_account_move_entry.py
 # test tags can help you filter quite easily
# odoo-bin --test-tags=/account:TestAccountMove.test_custom_currency_on_account_1