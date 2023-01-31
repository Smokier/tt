# TODO

## PENDING
- [ ] Implement the Change password endpoint.

# IN PROCCESS

- [ ] Implement the Reset password module.
    - [ ] Implement the password reset endpoint.

# DONE

## Docker
- [x] Create a docker-compose file to admin the API services.
- [x] Integrate the docker container for the Django service.
- [x] Create an .env file for the Django service.
- [x] Integrate the docker container for the Postgis service.
- [x] Integrate the docker container for the rabbitmq service.
- [x] Integrate the docker container for the celery/celery-beat service.

# Django
- [x] Start the Django project for the API.
- [x] Connect Django with the Posgres database.
- [x] Implement the database as Django Models.
- [x] Integrate Swagger for the API docs.
- [x] Create the communication between Celery, Django and Rabbitmq.
- [x] Implement the Auth module.
    - [x] Implement the signup endpoint.
    - [x] Implement the login endpoint.
    - [x] Implement the logout endpoint.
    - [x] Implement the logoutall endpoint.
- [ ] Implement the Reset password module.
    - [x] Create the endpoint to request the password reset.
    - [x] Implement the email sender
