# TODO

## PENDING
- [ ] Implement the Change password endpoint.
- [ ] Implement the Verify email module.
    - [ ] Implement the email sender.
    - [ ] Design the email template.
    - [ ] Implement the email verifier endpoint.
- [ ] Implement the Reset password module.
    - [ ] Implement the password reset endpoint.
- [ ] Implement the Maintenance module.
    - [ ] Implement the assign project endpoint.
    - [ ] Implement the unassign project endpoint.
- [ ] Implement the Project Model module.
    - [ ] Implement the Register project model endpoint.
    - [ ] Implement the Update project model endpoint.
    - [ ] Implement the Get project models of a specific project endpoint.
    - [ ] Implement the Get project model endpoint.
    - [ ] Implement the Delete (set inactive) project model.
- Implement the data type module.
    - [ ] Implement the Register data type endpoint.
    - [ ] Implement the Update data type endpoint.
    - [ ] Implement the Get data types endpoint.
    - [ ] Implement the Get data type enpoints.
    - [ ] Implement the Delete (set inactive) data type.


# IN PROCCESS
- Implement the Project module.
    - [ ] Implement the Register project endpoint.
    - [ ] Implement the Update project endpoint.
    - [ ] Implement the Get projects endpoint.
    - [ ] Implement the Get project enpoints.
    - [ ] Implement the Delete (set inactive) project.



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
- [x] Implement the Active Customer module.
    - [x] Implement the Register active customer endpoint.
    - [x] Implement the Update active customer endpoint.
    - [x] Implement the Get active customers endpoint.
    - [x] Implement the Get active customer enpoints.
    - [x] Implement the Delete (set inactive) active customer.
- [x] Implement the Inactive Customer module.
    - [x] Implement the Update Inactive customer endpoint.
    - [x] Implement the Get inactive customers endpoint.
    - [x] Implement the Get inactive customer enpoints.
    - [x] Implement the Delete (set active) inactive customer.
