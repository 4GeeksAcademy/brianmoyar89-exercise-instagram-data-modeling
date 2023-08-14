from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    full_name = Column(String(100))
    posts = relationship('Post', back_populates='user')

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    caption = Column(String(280))
    created_at = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='posts')
    comments = relationship('Comment', back_populates='post')
    media = relationship('Media', back_populates='post')

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    text = Column(String(280), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post', back_populates='comments')

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    url = Column(String(255), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post', back_populates='media')

# Replace 'sqlite:///instagram.db' with your preferred database connection string
engine = create_engine('sqlite:///instagram.db')
Base.metadata.create_all(engine)

try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e



