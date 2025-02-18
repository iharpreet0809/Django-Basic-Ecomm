
# Electroshop- One-Stop Electronics Store

Project Description: A basic e-commerce website with an admin panel to manage product inventory using SQL or MySQL for the database. The admin have full CRUD functionality (Create, Read, Update, Delete) to manage product details, including product name, description, price, and images. The website should have a user-friendly frontend where customers can browse products in a well-organized layout.

## Note:-

First, of all Install Vs code/Any Editor open terminal/cmd. & Follow the below steps for the installation or workflow for the localhost.


## Run Locally:-
Clone the project

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
6. Run the server for running the project in localhost
```bash
   "python managepy runserver"
``` 

## Screenshots 

1. Actual View of the website after running the localhost server.

2. 
