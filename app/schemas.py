import datetime
from pydantic import BaseModel
# from typing import Optional

class Posts(BaseModel):
    # id: Optional[int] = None
    title: str
    content: str
    published: bool = True
        