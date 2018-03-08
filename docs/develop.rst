#######################################
Develop cradmin_legacy, or run the demo
#######################################

To develop cradmin-legacy, or to run the demo, you will have to do the following.


******************
Clone the git repo
******************
You will find the URL on our github project page.


*******************
Create a virtualenv
*******************
::

    $ mkvirtualenv -p /path/to/python3 cradmin_legacy


************************************
Install the development requirements
************************************
::

    $ workon cradmin_legacy
    $ pip install -r requirements/python3.txt


************************
Create the demo database
************************
::

    $ workon cradmin_legacy
    $ inv recreate_devdb


**************************
Run the development server
**************************
::

    $ workon cradmin_legacy
    $ python manage.py runserver

Open http://localhost:8000 and login with::

    email: grandma@example.com
    password: test


*************
Run the tests
*************
::

    $ workon cradmin_legacy
    $ DJANGOENV=test python manage.py test cradmin_legacy
