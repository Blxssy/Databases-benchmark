import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy import URL
from config import user, password, host, db_name, port, testCount, queries
import time
import numpy


def query_SQLAlchemy():
    try:
        urlObj = URL.create(
            "postgresql",
            username=user,
            password=password,
            host=host,
            port=port,
            database=db_name
        )

        engine = create_engine(urlObj)
        connection = engine.connect()

        res = []

        times = []
        for i in range(testCount):
            startTime = time.time()
            connection.execute(text(queries[0]))
            endTime = time.time()
            times.append(endTime - startTime)
        res.append(numpy.mean(times))

        times = []
        for i in range(testCount):
            startTime = time.time()
            connection.execute(text(queries[1]))
            endTime = time.time()
            times.append(endTime - startTime)
        res.append(numpy.mean(times))

        times = []
        for i in range(testCount):
            startTime = time.time()
            connection.execute(text(queries[2]))
            endTime = time.time()
            times.append(endTime - startTime)
        res.append(numpy.mean(times))

        times = []
        for i in range(testCount):
            startTime = time.time()
            connection.execute(text(queries[3]))
            endTime = time.time()
            times.append(endTime - startTime)
        res.append(numpy.mean(times))

        connection.close()

        return res
    except create_engine.Error as err:
        print("SQLAlchemy error")
        print(err)
        return []