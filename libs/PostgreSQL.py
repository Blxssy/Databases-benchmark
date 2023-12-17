import psycopg2
import time
import numpy

from config import user, password, host, port, db_name, testCount

def query_Pg():
    try:
        connection = psycopg2.connect(
            user = user,
            password = password,
            host = host,
            port = port,
            database = db_name
        )

        cursor = connection.cursor()

        res = []

        #first query
        times = []
        for i in range(testCount):
            startTime = time.time()
            cursor.execute("SELECT vendorid, count(*) FROM trips GROUP BY 1;")
            endTime = time.time()
            times.append(endTime - startTime)
        res.append(numpy.mean(times))

        #second query
        times = []
        for i in range(testCount):
            startTime = time.time()
            cursor.execute("SELECT passenger_count, avg(fare_amount) FROM trips GROUP BY 1;")
            endTime = time.time()
            times.append(endTime - startTime)
        res.append(numpy.mean(times))

        #third query
        times = []
        for i in range(testCount):
            startTime = time.time()
            cursor.execute("SELECT passenger_count, extract(year from tpep_pickup_datetime), count(*) FROM trips GROUP BY 1, 2;")
            endTime = time.time()
            times.append(endTime - startTime)
        res.append(numpy.mean(times))

        #fourth query
        times = []
        for i in range(testCount):
            startTime = time.time()
            cursor.execute("SELECT passenger_count, extract(year from tpep_pickup_datetime), round(trip_distance), count(*) FROM trips GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;")
            endTime = time.time()
            times.append(endTime - startTime)
        res.append(numpy.mean(times))

        cursor.close()
        connection.close()

        return res

    except psycopg2.Error as err:
        print("Error")
        print(err)
        return []




