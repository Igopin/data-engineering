import psycopg2
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from company import Company, Base as CompanyBase

engine = create_engine("postgresql+psycopg2://postgres:@localhost/test", echo=True)
Session = sessionmaker(bind=engine)


def run():
    CompanyBase.metadata.create_all(engine)
    with open("data.csv") as file:
        session = Session()
        reader = csv.DictReader(file)

        for row in reader:
            session.add(Company(name=row["Company"], state_name=row["State Name"], zip_code=row["Zip Code"]))

        session.commit()


if __name__ == "__main__":
    run()
