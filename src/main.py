from configuration import engine, connection_string
from sqlalchemy import text, select, func
from sqlalchemy.orm import Session


if __name__ == "__main__":

    with Session(engine) as session:
        # 1. show that db is works.
        result = session.execute(
            text(
                "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';"
            )
        )
        print(result.all())
