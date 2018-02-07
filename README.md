# WikiToLearn pages backend

Run instructions:

* Build all docker containers with: `docker-compose -f docker-compose.yml  -f docker-compose-dev-deps.yml build`
* Run all docker containers with: `docker-compose -f docker-compose.yml  -f docker-compose-dev-deps.yml up`

Tests run instructions:

* Build all docker containers with: `docker-compose -f docker-compose.yml  -f docker-compose-dev-deps.yml -f docker-compose-tests.yml build`
* Run all docker containers with: `docker-compose -f docker-compose.yml  -f docker-compose-dev-deps.yml -f docker-compose-tests.yml up`
