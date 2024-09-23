# Django website project

## Intro

This is a personal project of mine to enhance my django Software Engineering skills.
The goal is to make a website with all kind of projects on it.
The main project for now is creating an personal version of the IMDb movie database website. Here I store information about movies I want to watch and have watched. I'm using Django class based views for this, which I'm new to, so there is a lot to learn.

## Setup

Create a venv from the pip requirements in `requirements.txt`.
Or create a conda environment from `spec-file.txt`.
In a later version I will transfer the whole project to a venv instead of a conda environment.
When that happens I will include instructions on how to install the venv.

Populating the database can be done with `python manage.py create_reviews`.

## sources

### templates

- [info on templates](https://dev.to/scofieldidehen/mastering-django-templates-a-guide-to-advanced-features-and-best-practices-25pe)
- [more info on templates](https://www.pythontutorial.net/django-tutorial/django-templates/)

### database

- [Django ORM Cheatsheet: Mastering Database Operations in Django](https://djangocentral.com/django-orm-cheatsheet/)

### Class based views

- [Create View](https://www.pythontutorial.net/django-tutorial/django-createview/)

### forms

- [Form choices](https://www.b-list.org/weblog/2007/nov/02/handle-choices-right-way/)

## Notes

Pushed sqlite database django superuser to github.
That's fine for development, but bad for deployment.

## TODO's
