#!/usr/bin/env python3

# Script goes here!

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Company, Dev, Freebie, Base

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Drop and recreate tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

dev1 = Dev(name="Anold")
dev2 = Dev(name="Lina")
company1 = Company(name="TechCorp", founding_year=2000)
company2 = Company(name="HackInc", founding_year=1995)

f1 = Freebie(item_name="T-shirt", value=20, dev=dev1, company=company1)
f2 = Freebie(item_name="Sticker", value=5, dev=dev2, company=company1)

session.add_all([dev1, dev2, company1, company2, f1, f2])
session.commit()
