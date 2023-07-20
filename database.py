from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

connetion_string = "mysql+mysqlconnector://root:@localhost:3306/allridesdb"
engine = create_engine(connetion_string, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
