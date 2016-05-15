README
======

Local database setup
--------------------

 #. Create PostgreSQL user with id matching your UNIX username::

    $ sudo -u postgres createuser $(whoami) -SDR

 #. Create a database owned by this user::

    $ sudo -u postgres createdb -E UTF-8 -O $(whoami) hba1c

 #. Check we can connect to this database::

    $ /usr/bin/psql hba1c
    psql (9.1.2)
    Type "help" for help.
    
    hba1c=> \q

 #. Create empty tables, etc.::

    $ ./manage.py syncdb
    $ ./manage.py migrate --all
