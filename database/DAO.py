from database.DB_connect import DBConnect
from model.state import State


class DAO():

    @staticmethod
    def getAnni():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select distinct extract(year from s.datetime) as anno
                    from sighting s"""

        cursor.execute(query,)
        for row in cursor:
            result.append(row['anno'])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodes():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from state s"""

        cursor.execute(query, )
        for row in cursor:
            result.append(State(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdges(anno, giorni, idMap):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select state1, state2, count(*) as peso
                    from neighbor n, sighting s1, sighting s2
                    where n.state1 < n.state2
                    and s1.state = n.state1 and s2.state = n.state2
                    and extract(year from s1.`datetime`) = %s 
                    and extract(year from s2.`datetime`) = %s
                    and abs(datediff(s1.`datetime`, s2.`datetime`)) <= %s
                    group by state1, state2"""

        cursor.execute(query, (anno, anno, giorni))
        for row in cursor:
            result.append((idMap[row['state1']],
                           idMap[row['state2']],
                           row['peso']))

        cursor.close()
        conn.close()
        return result
