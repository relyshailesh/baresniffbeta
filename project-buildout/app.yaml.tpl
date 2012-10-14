application: ${parts.config['gae-app-id']}
version: 1
runtime: python
api_version: 1

builtins:
- remote_api: on

# Different urls, will be served from different applications
handlers:
- url: /_ah/queue/deferred
  script: djangoappengine/deferred/handler.py
  login: admin   
- url: /stats.*
  script: $$PYTHON_LIB/google/appengine/ext/appstats/ui.py
- url: /admin/.*
  script: $$PYTHON_LIB/google/appengine/ext/admin
  login: admin

- url: /${parts.config['static-url']}
  static_dir: ${parts.config['static-root']}

# Django backend.
- url: /api/.*
  script: djangoappengine/main/main.py

# Enable warmup requests (keeps the instances from going idle)
inbound_services:
- warmup

skip_files: 
 - ^.git
 - ^.swp
 - ^google_appengine       
