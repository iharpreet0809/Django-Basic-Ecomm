
# Electroshop- One-Stop Electronics Store

Project Description: A basic e-commerce website with an admin panel to manage product inventory using SQL or MySQL for the database. The admin have full CRUD functionality (Create, Read, Update, Delete) to manage product details, including product name, description, price, and images. The website should have a user-friendly frontend where customers can browse products in a well-organized layout.

## Note:-

First, of all Install Vs code/Any Editor open terminal/cmd. & Follow the below steps for the installation or workflow for the localhost.


## Run Locally:-
#### Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd Ecommerce
```

First step go to the project directory where manage.py file exist.
Ecommerce

  -/eccomerce
  
  -/media
  
  -/shop

  -/manage.py

  -/requirements.txt

Open the terminal Now and run the command below for the python environment.

1. create the python environment for installing the libraries
```bash
  python -m venv "your environment name"
  python -m venv env
```

2. Go to the bin folder first and then run second command ./activate 
```bash
   cd env/bin
   ./activate
``` 
3. Install now the all libraries exist in requirements file for run the project. Its a dependencies
Install dependencies:-
```bash
   "pip install -r requirements.txt"
``` 
4.  create migration files for any changes made to your models.
```bash
   "python manage.py makemigrations"
``` 
5. After creating migrations, apply them to the database using:
```bash
   "python manage.py migrate"
```
6. Create the superuser for the accessing the Admin Panel. add your username and password accordingly and remember them accessing the admin panel.
```bash
   "python manage.py createsuperuser"
```
7. Run the server for running the project in localhost
```bash
   "python manage.py runserver"
``` 

## Screenshots 

### 1. Actual View of the website after running the localhost server.
![Screenshot](Screenshots/Screenshot%20(140).png)

### 2. Admin Panel View accessed using http://127.0.0.1:8000/admin/ & also showing left side Products Table/Model
   --with the Create/Add Product on the upper right side
![Screenshot](Screenshots/Screenshot%20(141).png)

### 3. This is the view of the Products Model/Table and there is the list too of 3 products like Laptop, Mobile and Speaker
![Screenshot](Screenshots/Screenshot%20(142).png)

### 4. This is the Update View of the product where we can update the details of the speaker accordingly and save them using save button below.
![Screenshot](Screenshots/Screenshot%20(144).png)

### 5. This is the Delete View of the product/Products
![Screenshot](Screenshots/Screenshot%20(143).png)

## Contact Me:
If you occur any problem contact with me on mail- harpreetsingh9437@gmail.com 

[![Instagram](https://img.shields.io/badge/Instagram-s4smarty-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/s4smarty/)

   
