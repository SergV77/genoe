# import os
# from flask_script import Manager
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
#
#
# app = Flask(__name__)
# manager = Manager(app)
# db = SQLAlchemy(app)
#
#
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'datasqlite.db')
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
#
#
#
# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True)
#     users = db.relationship('User', backref='role')
#
#     def __repr__(self):
#         return '<Role %r>' % self.name
#
#
# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), unique=True, index=True)
#     role_id = db.Column(db.Integer, db.ForieignKey('role_id'))
#
#     def __repr__(self):
#         return '<User %r>' % self.username
#
# if __name__ == '__main__':
#     manager.run()