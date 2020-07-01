from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from create import Data
import numpy as np 



Parcels_input=np.loadtxt('./input_parcel.csv',delimiter="\n",dtype=str)


engine = create_engine('sqlite:///parcel.db', echo=True)

Session = sessionmaker(bind = engine)
session = Session()

for parcel in Parcels_input:
    c1 = Data(Parcel_id = parcel)
    session.add(c1)
session.commit()
