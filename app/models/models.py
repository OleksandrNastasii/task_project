from datetime import datetime
from app.database.database import Base
from sqlalchemy import Column, Integer, String, DateTime

class UserModel(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    email = Column(String(120), unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def show_user(self):
        return {
            'id': self.id,
            'name' : self.name,
            'email' : self.email,
            'created_at' : self.created_at
        }