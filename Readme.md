# Django Local Environment Setup

## Pre-requisites

Before you can start working locally you need to make sure that you have >= Python 3.6 installed. If you are on OSX you likely already do. You can by terminal and typing:

    python3

and then hitting that `tab` key a few times. If you see `python3.X` in that list you're good to go.

## Environment Setup

In this directory you need to create a virtual environment for our work. This basically acts as a sandbox for us to play in. You only need to perform this task the first time you are building your environment. After that you can skip it.

    python3 -m venv venv

Once your environment is built you need to tell your terminal to use it. To do that you use the `source` command. Before starting work you will always need to run this command.

    source venv/bin/activate && ./manage.py runserver

Now that you have an environment to play around in, you need to install Django.

## Installation

After you've done the activate step, the first thing you need to do install the latest version of PIP. PIP is to Python as NPM is to Javascript. Its a way to install packages and manage dependencies.

    pip install --upgrade pip

Next you can install the project dependencies.

    pip install -r requirements.txt

## Database Migrations

Next we need to run all of migrations to get the database set up. We'll initially use SQLite so that we don't have any configuration to worry about.

    ./manage.py migrate

## Running the Application

Everything is all set. You can now start the server with

    ./manage.py runserver

and then access it at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Create a Super User

In order to log in to the Django admin interface you'll need to create a super user.

    ./manage.py createsuperuser

Follow the prompts on the screen. After that, start the server up and try to log in at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).
# one
