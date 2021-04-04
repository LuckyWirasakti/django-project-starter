![Octocat](https://github.githubassets.com/images/icons/emoji/octocat.png)

[![Build Status](https://travis-ci.com/LuckyWirasakti/django-project-starter.svg?branch=master)](https://travis-ci.com/github/LuckyWirasakti/django-project-starter) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/LuckyWirasakti/django-project-starter/blob/master/LICENSE) [![GitHub release](https://img.shields.io/badge/release-v1.1.1-blue)](https://github.com/LuckyWirasakti/django-project-starter/releases/tag/1.1.1)  [![Maintaner](https://img.shields.io/badge/maintainer-LuckyWirasakti-blue)](mailto:luckywirasakti@gmail.com) 


This is a normal paragraph following a header. GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.

### Installation Guide

- Before installing this project, make sure your computer already installed application in the `requirements` First.

- Clone this project to your local Computer

- Duplicate `.env.example` file and rename to `.env`

- Run `docker-compose up` and add flag `--build` for build image, you can ignore flag if has already build image.

- Create superuser 

	```python
	./manage.py createsuperuser
	```

### List Package In This Project

*   Django==3.1.7
*   django-environ==0.4.5
*   psycopg2-binary==2.8.6
*   djangorestframework==3.12.4
*   django-cors-headers==3.7.0
*   django-oauth-toolkit==1.5.0
*   django-rest-framework-social-oauth2==1.1.0
*   drf-yasg==1.20.0
*   whitenoise==5.2.0
*   gunicorn==20.1.0
*   rollbar==0.15.2
