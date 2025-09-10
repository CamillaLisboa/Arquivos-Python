DEBUG = True

USERNAME = 'root'
PASSWORD = 'root'
SERVER = 'localhost:3306'
DB = 'library'

sqlalchemy_database_uri = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
sqlalchemy_track_modifications = False