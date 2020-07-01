from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///parcel.db', echo=True)
Base = declarative_base()


class Data(Base):

    __tablename__ = "data"

    id = Column(Integer, primary_key=True)
    Parcel_id = Column(String)  
    Tax_Name = Column(String)  
    Tax_Mailing_Address = Column(String)  
    Tax_Address = Column(String)  
    Tax_City = Column(String)  
    Tax_State = Column(String) 
    Tax_State = Column(String) 
    Tax_Zip_Code= Column(String) 
    Property_Address= Column(String)
    PropertyCity=Column(String)
    PropertyState=Column(String)
    PropertyPostalCode=Column(String)
    Occupancy_Class=Column(String)
    Payment=Column(String)
    Charges_Tax_Bill=Column(String)
    Balunce_Due=Column(String)
    Bedrooms=Column(String)
    Living_Area_Total=Column(String)
    Age=Column(String)

Base.metadata.create_all(engine)