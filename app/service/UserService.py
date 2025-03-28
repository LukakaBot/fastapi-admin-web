from sqlmodel import Session
from app.model.users import UserCreate, Users


def create_user(*, session: Session, user: UserCreate) -> Users:
    db_user: Users = Users.model_validate(
        {
            "username": user.username,
            "password": user.password,
            "phone": user.phone,
            "email": user.email,
        }
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user
