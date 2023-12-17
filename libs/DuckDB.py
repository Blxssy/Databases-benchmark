import duckdb
from config import file_name, testCount
import time
import numpy

def query_duckdb():
    try:
        connection = duckdb.connect()

        res = []

        times = []
        for i in range(testCount):
            startTime = time.time()
            connection.execute(f"SELECT VendorID, count(*) FROM {file_name} GROUP BY 1;")
            endTime = time.time()
            times.append(endTime - startTime)
        res.append(numpy.mean(times))

        times = []
        for i in range(testCount):
            startTime = time.time()
            connection.execute(f"SELECT passenger_count, avg(fare_amount) FROM {file_name} GROUP BY 1;")
            endTime = time.time()
            times.append(endTime - startTime)
        res.append(numpy.mean(times))

        times = []
        for i in range(testCount):
            startTime = time.time()
            connection.execute(f"SELECT passenger_count, extract(year from tpep_pickup_datetime), count(*) FROM {file_name} GROUP BY 1, 2;")
            endTime = time.time()
            times.append(endTime - startTime)
        res.append(numpy.mean(times))

        times = []
        for i in range(testCount):
            startTime = time.time()
            connection.execute(f"SELECT passenger_count, extract(year from tpep_pickup_datetime), round(trip_distance), count(*) FROM {file_name} GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;")
            endTime = time.time()
            times.append(endTime - startTime)
        res.append(numpy.mean(times))

        connection.close()
        return res

    except duckdb.Error as err:
        print("DuckDB error")
        print(err)
        return []