from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


class AuthorBase(BaseModel):
    name: str
    email: EmailStr
    bio: Optional[str] = None

class AuthorCreate(AuthorBase): # for author create/update
    pass

class AuthorResponse(AuthorBase): # for list/detail
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]
    posts_count: int = 0

    class Config:
        orm_mode = True


class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class TagResponse(TagBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]
    posts_count: int = 0

    class Config:
        orm_mode = True


class CommentBase(BaseModel):
    content: str
    author_name: str
    author_email: EmailStr

class CommentCreate(CommentBase): # for comment create
    post_id: int

class CommentResponse(CommentBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    author_id: int
    category_id: int
    tag_ids: List[int] = Field(default_factory=list)

class PostResponse(PostBase):
    id: int
    slug: str
    created_at: datetime
    updated_at: Optional[datetime]
    author: AuthorResponse
    category: CategoryResponse
    tags: List[TagResponse]
    comments_count: int = 0

    class Config:
        orm_mode = True



