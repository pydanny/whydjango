============
whydjango
============

whydjango is a site designed for advocacy of Django.

Applications
============

 - Books
 
    - List of published Django books

 - casestudies
 
    - Lists studies done on Django
    
 - core
 
    - Various utilities
    
 - homepage
 
    - The root page has special requirements and so gets its own application
 
 - vendors
 
    - A list of community approved vendors
    
Installation
============

Just follow these steps::

    git clone git@github.com:pydanny/whydjango.git
    cd whydjango
    python bootstrap.py
    ./bin/buildout
    cd src/whydjango
    ../../bin/django syncdb
    ../../bin/django loaddata fixtures/initial_data.json
    
Running the system
==================

As you would another buildout based Django app::

    ../../bin/django runserver