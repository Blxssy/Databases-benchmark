import time

from libs import Pandas, PostgreSQL, SQLAlchemy, SQLite, DuckDB

while True:
    print("Benchmark")
    print("1: SQLite")
    print("2: Pandas")
    print("3: SqlAlchemy")
    print("4: PostgresSQL")
    print("5: DuckDB")

    userInput = input()

    if userInput == 'x': # Quit
        break

    elif userInput == '1': # SQLite
        print("Benchmarking SQLite")
        print(SQLite.query_sqlite())


    elif userInput == '2': # Pandas
        print("Benchmarking Pandas")
        print(Pandas.query_pandas())

    elif userInput == '3':
        print("Benchmarking SqlAlchemy")
        print(SQLAlchemy.query_SQLAlchemy())


    elif userInput == '4':
        print("Benchmarking PostgreSQL")
        print(PostgreSQL.query_Pg())


    elif userInput == '5':
        print("Benchmarking DuckDB")
        print(DuckDB.query_duckdb())