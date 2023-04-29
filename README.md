
# Nbyula_Assignment1_SDE

This is a web application that allows terraformers to schedule appointments with each other, update their profiles, and see their respective upcoming appointments. The application is built using Django.

## Features

- Sign up and login functionality for terraformers
- Schedule appointments with other terraformers
- Appointments contain a title, agenda, time, and guest
- Appointments can only be scheduled if the guest is available
- View upcoming appointments
- Update profile name and password

## Feature trade-off
- Mark off-hours on profile page




## Technology used

- Django
- HTML
- CSS
- Bootstrap

## Design Decisions:

- For the Terraformers app, I decided to use the Django framework due to its robustness, security, and scalability. I also used HTML/CSS for front-end styling.

- In terms of the database schema, I created models for the terraformers, appointments. 

- Terraformers have a one-to-many relationship with appointments (as they can schedule multiple appointments).

- Terraformers can only look up to 7 working days from their current date to book an appointment with other.

- Terraformers can book only the free time slots from 10 AM to 4 PM, each slot being 1 hour each.

## Scalability Concerns:

- The potential increase in the number of appointments and users concurrently. Need to work on solving this concern.

- The potential need for more features in the future is addressed by designing the code to be modular and extensible, with clear separation of concerns and reusable code.

## Trade-offs

- This application was built without any knowledge on how hosting works and I wish to learn more about it now.

- This application uses Django because of its built-in security features and other feautures present in it, other back-end frameworks could have been used to make it more robust and ready for actual use.

## Getting Started
- Clone the repository.
- Install the required dependencies using,
```bash
 pip install -r requirements.txt
 ```
- Set up the database by running 
```bash
python manage.py migrate
```
- Start the development server with 
```bash
python manage.py runserver
```
- Visit http://localhost:8000 in your web browser to use the application.

## Screenshots

![image](https://user-images.githubusercontent.com/90385192/235311932-53ce86f1-b3b2-4e9b-85a7-e18d7e0bab61.png)


![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

