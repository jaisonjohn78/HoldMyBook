
# Hold-My-Book [OLMS]
# (Online eLibrary Management System)

Online Library Management System is an Automated Library System that handles the various functions of the library. It provides a complete solution to the library management software.

## Documentation

[documentation.ppt](https://github.com/jaisonjohn78/HoldMyBook/blob/master/Final_presentation_Group_30.pptx?raw=true)


## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/) 

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)

[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Run Locally

Clone the project

```bash
  git clone https://github.com/jaisonjohn78/HoldMyBook.git
```

Go to the project directory

```bash
  cd HoldMyBook
```

Install pip and pipenv for evertual envirment

```bash
  pip install pipenv
```

Check outs
```bash
  python --version
  pipenv --venv
```


Migrate Tables
```bash
  python manage.py migrate
```

Create Super-user
```bash
  python manage.py createsuperuser
```



## Run Server

To deploy this project run

```bash
  python manage.py runserver
```


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Acknowledgements

 - [Django ReadDoc Pdf](https://buildmedia.readthedocs.org/media/pdf/django/3.0.x/django.pdf)
 - [Django Offical Doc 4.1.5](https://docs.djangoproject.com/en/4.1/)
 - [Django Project Doc 4.1.5](https://www.djangoproject.com/start/)

