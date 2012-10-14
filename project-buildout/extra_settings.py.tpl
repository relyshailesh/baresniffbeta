DEBUG = ${parts.config.mode == 'development' and 'True' or 'False'}

STATIC_URL = '${parts.config['static-url']}'
STATIC_ROOT = '${parts.config['static-root']}'
