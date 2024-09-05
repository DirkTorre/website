# Intro

This is a personal project of mine to enhance my django Software Engineering skills.
The goal is to make a website with all kind of projects on it.
The main project for now is creating an personal version of the IMDb movie database website. Here I store information about movies I want to watch and have watched. I'm using Django class based views for this, which I'm new to, so there is a lot to learn. 

## sources

### templates

- [info on templates](https://dev.to/scofieldidehen/mastering-django-templates-a-guide-to-advanced-features-and-best-practices-25pe)
- [more info on templates](https://www.pythontutorial.net/django-tutorial/django-templates/)

### database

- [Django ORM Cheatsheet: Mastering Database Operations in Django](https://djangocentral.com/django-orm-cheatsheet/)

### Class based views

- [Create View](https://www.pythontutorial.net/django-tutorial/django-createview/)

## Notes

Pushed sqlite database django superuser to github.
That's fine for development, but bad for deployment.

## TODO's

- details:
    - delete database from main branch and replace with dummie database, provide instructions on how to setup
    - include environment file in commit

### plan

- reviews:
    - (done) create a update view
    - (done) create a delete view
    - (dropped) database model should return a link to the update view
    - (done) problem: note's can't be null
    - (done) problem: decimal scores are not possible

- movie add form:
    - (done) must give a warning if link isn't from imdb or ttconst isn't found.

- movie list:
    - list view with pagination.
    - links to detail views.
    - filtering (django-filter)



