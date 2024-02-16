from fastapi import Depends, HTTPException, Response, status, APIRouter
from sqlalchemy.orm import Session

from .. import models, schemas, oauth2
from ..database import get_db


router = APIRouter(prefix="/votes", tags=["votes"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_post(
    vote: schemas.Vote,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(oauth2.get_current_user),
):
    found_vote = db.query(models.Vote).filter(
        models.Posts.id == vote.post_id, models.Vote.user_id == current_user.id
    )
    if vote.post_id == 1:
        if found_vote.first():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"user {current_user.id} has already voted on {vote.post_id}",
            )
        new_vote = models.Vote(post_id=vote.post_id, user_id=vote.user_id)
        db.add(new_vote)
        db.commit()

        return {"message": "Vote sucessed"}

    else:
        if not found_vote:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Vote didn't exist",
            )
        
        found_vote.delete(synchronize_session=False)
        db.commit()
            
        return {"message": "Vote sucessed"}
