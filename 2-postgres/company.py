from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    state_name = Column(String)
    zip_code = Column(String)

    def __repr__(self):
        return f"<Company(name={self.name}, state_name={self.state_name}, zip_code={self.zip_code})>"




