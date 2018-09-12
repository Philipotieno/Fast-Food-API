#### Fast-Food-Fast

[![Build Status](https://travis-ci.org/Philipotieno/Fast-Food-API.svg?branch=heroku)](https://travis-ci.org/Philipotieno/Fast-Food-API)

[![Coverage Status](https://coveralls.io/repos/github/Philipotieno/Fast-Food-API/badge.svg?branch=develop)](https://coveralls.io/github/Philipotieno/Fast-Food-API?branch=develop)

Fast-Food-Fast is a food delivery service app for a restaurant

## Features
- Users can create an account.
- Signed up users can log into their account.
- Users can post orders.
- Users can get history of orders.
- Users can get a specific order.
- Users can modify an order.
- Users can can delete a specific order.

## Prerequisites
- [Python3](https://www.python.org/) (A programming language)
- [Flask](http://flask.pocoo.org/) (A Python microframework)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/) (Stores all dependencies used in the project)
- [Pivotal Tracker](www.pivotaltracker.com) (A project management tool)
- [Pytest](https://docs.pytest.org/en/latest/) (Tool for testing)


## Getting Started:

**To start the following app, please follow the instructions below:**

**On your terminal:**

Install pip:

  $ sudo apt-get install python-pip

Clone this repository:

  $ git clone https://github.com/Philipotieno/Fast-Food-API.git

Get into the root directory:

  $ cd Fast-Food-API/

Install virtualenv:

  $ pip install virtualenv

Create a virtual environment in the root directory:

  $ virtualenv -name of virtualenv-
  
 Note: If you do not have python3 installed globally, please run this command when creating a virtual environment:
 
   $ virtualenv -p python3 -name of virtualenv-

Activate the virtualenv:

  $ source name of virtualenv/bin/activate

Install the requirements of the project:

  $ pip install -r requirements.txt

Run the application:

  $ python run.py

Test the endpoints in postman

To run tests:

  $ pytest