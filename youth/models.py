from sqlalchemy import Column, Integer, String, Date, DateTime,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from .database import Base


class Plans(Base):
    __tablename__ = "plans"

    plan_id = Column(Integer, primary_key=True, nullable=False)
    plan_name = Column(String, nullable=False)
    plan_start_date = Column(Date, nullable=False)
    plan_end_date = Column(Date, nullable=False)
    plan_status = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    plan_created_by  = Column(Integer, nullable=False)
    plan_created_date  = Column(Date, nullable=False)
    plan_last_modified_by  = Column(Integer, nullable=False)
    plan_last_modified_date  = Column(DateTime(timezone=True), nullable=False, server_default=text('now()'))
    plan_deleted_at  = Column(DateTime, nullable=True)

    owner = relationship("User")

class Goals(Base):
    __tablename__ = "goals"

    goal_id  = Column(Integer, primary_key=True, nullable=False)
    goal_name = Column(String, nullable=False)
    theme_id  = Column(Integer, nullable=False)
    plan_id  = Column(Integer, default="true", index=True)
    goal_description  = Column(String, nullable=False)
    goal_period  = Column(Integer, nullable=False)
    goal_created_by  = Column(Integer, nullable=False)
    goal_created_date  = Column(Date, nullable=False)
    goal_last_modified_date  = Column(DateTime(timezone=True), nullable=False, server_default=text('now()'))
    goal_last_modified_by  = Column(Integer, nullable=False)
    goal_deleted_at  = Column(DateTime, nullable=True)


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, nullable=False)
    user_email = Column(String, unique=True, nullable=False)
    user_password = Column(String, nullable=False)
    user_created_by  = Column(Integer, nullable=False)
    user_created_date  = Column(Date, nullable=False)
    user_last_modified_date  = Column(DateTime(timezone=True), nullable=False, server_default=text('now()'))
    user_last_modified_by  = Column(Integer, nullable=False)
    user_deleted_at  = Column(DateTime, nullable=True)


