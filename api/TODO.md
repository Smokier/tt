# TODO

## PENDING

- [ ] Implement the Change password endpoint.
- [ ] Implement the Verify email module.
    - [ ] Implement the email sender.
    - [ ] Design the email template.
    - [ ] Implement the email verifier endpoint.
- [ ] Implement the Reset password module.
    - [ ] Implement the password reset endpoint.


# IN PROCCESS

- [ ] Implement the Project Model module
    - [ ] Implement the Register Project Model endpoint.
    - [ ] Implement the Update active Project Model endpoint.
    - [ ] Implement the Get active Project Models endpoint.
    - [ ] Implement the Get active Project Model enpoints.
    - [ ] Implement the Delete (set inactive) active Project Model.
    - [ ] Implement the Update Inactive Project Model endpoint.
    - [ ] Implement the Get inactive Project Models endpoint.
    - [ ] Implement the Get inactive Project Model enpoints.
    - [ ] Implement the Delete (set active) inactive Project Model.

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
    - [x] Implement the email sender.
    - [x] Design the email template.
- [x] Implement the Customer module.
    - [x] Implement the Register customer endpoint.
    - [x] Implement the Update active customer endpoint.
    - [x] Implement the Get active customers endpoint.
    - [x] Implement the Get active customer enpoints.
    - [x] Implement the Delete (set inactive) active customer.
    - [x] Implement the Update Inactive customer endpoint.
    - [x] Implement the Get inactive customers endpoint.
    - [x] Implement the Get inactive customer enpoints.
    - [x] Implement the Delete (set active) inactive customer.
- [x] Implement the isActiveUser permission
- [x] Implement the Project module.
    - [x] Implement the Register project endpoint.
    - [x] Implement the Update active project endpoint.
    - [x] Implement the Get active projects endpoint.
    - [x] Implement the Get active project enpoints.
    - [x] Implement the Delete (set inactive) active project.
    - [x] Implement the Update inactive project endpoint.
    - [x] Implement the Get inactive projects endpoint.
    - [x] Implement the Get inactive project enpoints.
    - [x] Implement the Delete (set inactive) inactive project.
- Implement the data type module.
    - [x] Implement the Register data type endpoint.
    - [x] Implement the Update active data type endpoint.
    - [x] Implement the Get active data types endpoint.
    - [x] Implement the Get active data type enpoint.
    - [x] Implement the Delete (set inactive) active data type.
    - [x] Implement the Update inactive data type endpoint.
    - [x] Implement the Get inactive data types endpoint.
    - [x] Implement the Get inactive data type enpoints.
    - [x] Implement the Delete (set active) inactive data type.
- [x] Implement the Maintenance module.
    - [x] Implement the Assign project endpoint.
    - [x] Implement the Unassign project endpoint.
    - [x] Implement the Get all the assigned projects endpoint.
    - [x] Implement the Get all the assigned projects of a user enpoint.
    - [x] Implement the Get an assigned project endpoint.
