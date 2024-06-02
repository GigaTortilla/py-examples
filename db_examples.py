import os
import sqlalchemy as db


def main(argv=None) -> int:
    print('SQLAlchemy Version: ', db.__version__)
    password = "rootsql"
    con_str = "mysql://root:" + password + "@127.0.0.1:3307/movie"
    engine = db.create_engine(con_str)
    connection = engine.connect()
    meta_data = db.MetaData()

    actor = db.Table(
        "actor", meta_data, 
        db.Column("id", db.Integer, primary_key=True, 
                  autoincrement=True, nullable=False),
        db.Column("first_name", db.String(50), nullable=False),
        db.Column("last_name", db.String(50), nullable=False),
        db.Column("age", db.Integer, nullable=False),
        db.Column("date_of_birth", db.Date, nullable=False),
        db.Column("active", db.Boolean, nullable=False)
    )
    meta_data.create_all(engine)

    data_list = [{"first_name":"John", "last_name":"Smith",
                  "age":50, "date_of_birth":"1969-04-05", "active":True},
                 {"first_name":"Brian", "last_name":"Morgan",
                  "age":38, "date_of_birth":"1981-02-11", "active":True},
                 {"first_name":"David", "last_name":"White",
                  "age":77, "date_of_birth":"1942-06-30", "active":False}]
    sql_query = db.insert(actor)
    result = connection.execute(sql_query, data_list)
    result = connection.commit()
    
    sel = db.select(actor.c.get('first_name'), actor.c.get('last_name'))
    query_result = connection.execute(sel)
    for row in query_result:
        print(row)


if __name__ == '__main__':
    raise SystemExit(main())
