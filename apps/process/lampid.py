from flask_sqlalchemy import SQLAlchemy

users = db.session.execute(db.select(User).order_by(User.username)).scalars()
