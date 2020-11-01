import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	DEBUG = False
	TESTING = False
	CSRF_ENABLED = True
	SECRET_KEY = 'this-really-needs-to-be-changed'


class ProdCon(Config):
	DEBUG = False


class DevConf(Config):
	DEVELOPMENT = True
	DEBUG = True
