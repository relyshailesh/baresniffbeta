Django project layout, for deployment on the Google App Engine
#################################################################
Well, every time I had to develop a Django project for the GAE, I always had to
do everything from scratch. And that doesn't include the project itself. But
the configuration for the GAE testing and deployment. Which is a major pain in
the a*s. 

So I've built this small package, which does everything for us. All we have to
do is develop the django project itself, and not worry about anything else.

The sample project implements a super simple Rest API, using `django_icetea  <https://github.com/stargazer/django-icetea>`_, on top of `django-nonrel <https://bitbucket.org/wkornewald/django-nonrel/wiki/Home>`_.

How to
********

1. Clone the repository::
    
    git clone git@github.com:stargazer/gae-vanilla-project.git

2. cd into the repository::

    cd gae-vanilla-project

3. Edit the buildout.cfg::

    vim buildout.cfg

4a. You need to set the following parameters::

    [buildout]
    extends = project-buildout/buildout.cfg

    [config]
    mode = <Either ``development`` or ``production``>
    static-root = <Folder within the django project that contains static assets>
    static-url = <Domain offset which will serve static assets>
    local-port = <Port that the local instance of the GAE server will use>
    gae-app-id = <GAE application ID>

    [source-paths]
    django-project = <Path of root folder of Django project. Usually it's where
    the file setup.py is>
    django-project-code = <Path of source code folder of Django project>

4b. An example could be::

    [buildout]
    extends = project-buildout/buildout.cfg

    [config]   
    mode = development        
    static-root = static       
    static-url = static  
    local-port = 6789 
    gae-app-id = gae_app_123  

    [source-paths]  
    django-project = ${paths:src}/django-project   
    django-project-code = ${source-paths:django-project}/project 

3. Bootstrap::
   
    python project-buildout/bootstrap.py -d

4. Run Buildout::

    bin/buildout

The file ``app.yaml`` has been parsed by the buildout script, and copied in
the django project folder.

Another file, ``extra_settings.py``, has been parsed by the buildout script and copied in the Django project folder. All parameters in this file module should be imported by the Django project's ``settings.py`` file.


Run application locally
**********************************

In order to run the application locally::

    bin/dev_appserver

The sample django-project is reachable in the following endpoints::

    <local server ip>:<local gae server port>/api/test/
    eg. localhost:6789/api/test/

The static files are reachable in::

    <local server ip>:<local gae server port>/static/<filename>
    eg. localhost:6789/static/readme.txt


Deploy on Google App Engine
**********************************

In order to deploy the application on the GAE::

    bin/appcfg update <path/to/django/project/code>
    eg. bin/appcfg update src/django-project/project

The sample django-project is reachable in the following endpoints::

    http://<gae-app-id>.appspot.com/api/test/
    eg. http://gae_app_123.appspot.com/api/test/


The static files are reachable in::

    http://<gae-app-id>.appspot.com/static/<filename>
    eg. http://gae_app_123.appspot.com/static/README.txt


