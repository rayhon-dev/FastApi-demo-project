from sqlalchemy import Table, Column, Integer, String, Text, ForeignKey, DateTime, func
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

class Author(BaseModel):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=True)
    bio = Column(Text, nullable=True)
    posts = relationship("Post", back_populates="author")


class Category(BaseModel):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text, nullable=True)
    posts = relationship("Post", back_populates="category")


post_tag_table = Table(
    "post_tag", Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True)
)


class Tag(BaseModel):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    posts = relationship(
        "Post",
        secondary=post_tag_table,
        back_populates="tags"
    )


class Post(BaseModel):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False, unique=True)
    slug = Column(String(255), unique=True, index=True)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", back_populates="posts")
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="posts")
    tags = relationship("Tag",secondary=post_tag_table,back_populates="posts")
    comments = relationship("Comment", back_populates="post")


class Comment(BaseModel):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    post = relationship("Post", back_populates="comments")
    author_name = Column(String(100), nullable=False)
    author_email = Column(String(100), nullable=False, index=True)
    content = Column(Text, nullable=False)
