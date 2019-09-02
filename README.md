# flask-MySQL-Interaction-CURD
This is python built application, is for connecting MySQL database with flask without using SQLAlchemy.


## Contents
1. **Introduction**
>>1.1 How to use this application


2. **Application Requirements and Installations**

  

>>2.1     [Python 3.7.4](https://www.python.org/downloads/)  

  

>>2.2 [flask 1.1.1](https://flask.palletsprojects.com/en/1.1.x/installation/)

  

>>>2.2.1 [Installation](https://flask.palletsprojects.com/en/1.1.x/installation/#install-flask)

  

>>>2.2.2. [flask-mysqldb](https://flask-mysqldb.readthedocs.io/en/latest/)

  

>>>2.2.3. [flask-wtf](https://flask-wtf.readthedocs.io/en/stable/install.html)

>>> 2.2.4 [flask-forms](https://flask-wtf.readthedocs.io/en/stable/install.html)

  

>>2.3  [.yaml file](https://pyyaml.org/wiki/PyYAMLDocumentation)

  

>>2.4 [8.0.12 MySQL Community Server - GPL](https://downloads.mysql.com/archives/community/)

  

>>2.5 [Git and GitHub](https://git-scm.com/download/win)

  

3. **References**
 
 ## 1. Introduction
 This a simple application for learners, those who just started learning python.
 In this application you may learn about __"Routing"__ which is a decorator related topic in python language, __"MySQl Database-CRUD operations"__ , __"HTML Templates"__, __"Jinja2 template Engine and  blocks "__, __"flask"__ which is a micro framework used to develop a python application and some other modules like __flask-wtf, flask-forms and flask-mysqldb__. This is the about the tools used to develop this app.
 
### 1.1 How to use this application
 
>The main purpose of this application is to maintain a Database for the employees working in an organization. This application is for the person who is assign to maintain particulars (i.e Name,Designation,Address and Phone)  of each employee. Data can be searched from the Database, inserted, fetch back and can be modified based on the requirement. 

## 2. Application Requirements and Installations

### 2.1 [Python 3.7.4](https://www.python.org/downloads/)

> To check availability of python in your System(__Windows__), __go to command prompt and type python__, if a message pops up saying the below message then python is not available in your system,
>> __'python' is not recognized as an internal or external command, operable program or batch file.__

> **Installing Python-**
>> click on __"Python 3.7.4"__ heading to land on the official website if Python, based on your 'OS' select the options and download it and install it. In the installation setup you will see __pip__, which will be used to install python packages.

> __NOTE:__ Type __python__ in command prompt and python interpreter will open or type __python --version__, the version installed will be displayed.

### 2.2 [flask 1.1.1](https://flask.palletsprojects.com/en/1.1.x/installation/)
>This is a micro framework which will sitting upon on your python application.
>
> ***Installing flask***
> >__pip install flask__

>__NOTE:__ Type __flask --version__ in command prompt and, the version installed will be displayed or, open __python interpreter__ and use __help()__ to see the install package and modules.

 **2.2.2 [flask-mysqldb](https://flask-mysqldb.readthedocs.io/en/latest/)**

> ***Installing flask-mysqldb***

> >__pip install flask-mysqldb__

This package will be used to establish connection between your __MySQL Database__ and __flask__   

**2.2.3 [flask-wtf](https://flask-wtf.readthedocs.io/en/stable/install.html)**

> ***Installing flask-wtf***

> >__pip install flask-wtf__

This package will be used for __form classes validations__ in this application development.

**2.2.3 [flask-forms](https://flask-wtf.readthedocs.io/en/stable/install.html)**

> ***Installing flask-forms***

> >__pip install flask-forms__

This package will be used create __form classes__ in this application development.

### 2.3  [.yaml file](https://pyyaml.org/wiki/PyYAMLDocumentation)

> ***Installing 'yaml' or 'Pyyaml'***

> >__pip install Pyyaml  -> Python 3.6.x and above__

> ***[Please refer the Documentation for more information on 'yaml files']*** 

> OR
> >__pip install yaml  -> Python 2.x.x__

For this application, Python 3.7.4 is being used. In this application __".yaml files"__  is used to config __Database URL, User, Password, secret key( for CSRF) and Database Created in the MySQL server 8.0__, and stored as file with .yaml extension  . 

### 2.4 [8.0.12 MySQL Community Server - GPL](https://downloads.mysql.com/archives/community/)

To store data a database is required and with that a bridge can be built to perform CRUD operations. In this application MySQL Databases is used to store incoming employee data.

### 2.5 [Git and GitHub](https://git-scm.com/download/win)

> https://git-scm.com/download/win is the link to install __Git__ on your System(Windows). 

This is used to create a repository on a System, in which your project will be saved and modifications on the project can be monitored and can be linked up with GitHub.   





 