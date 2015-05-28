from app import db

class User (db.Model):
	__tablename__ = "users"
	id = db.Column('user_id', db.Integer, primary_key=True)
	username = db.Column('username',db.String(64), index = True, unique=True)
	password = db.Column('password',db.String(64), index = True, unique=True)
	#email = db.Column(db.String(120), index = True, unique=True)
	#registered_on = db.Column('registered_on', db.DateTime)

	def __init__(self, username, password):
		self.username = username
		self.password = password
		#self.registered_on = datetime.utcnow()

	def is_authenticated (self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)

	def __repr__(self):
		return '<< %r >>' % (self.nick)