import os
basedir = os.path.abspath(os.path.dirname(__file__))

#folder with db file
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#folder with migration 
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

WTF_CSRF_ENABLED = True
SECRET_KEY = 'VeryH4rdT00Gue55'