import numpy as np
import paramiko
import time
import datetime
import sys
import os
#for some reason this has to be imported lastly...
import mysql.connector

start_time = time.time()


# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd, flush=True)
    # Print New Line on Complete
    if iteration == total: 
    print()

class MySQL_Connect():
    # Class for handeling interaction with MySQL database
    
    def __init__(username = 'Python', mySQLhost = '85.229.17.165', mySQLserverPort = 330, SQLpath = os.getcwd() + '/SQL.txt'):
        self.username = username
        self.mySQLhost = mySQLhost
        self.mySQLserverPort = mySQLserverPort
        self.SQLpath = SQLpath
        
        
    

    #---------------------------------------------------------------------------------------------
   
    def execute_query(self, db, query_str, connection_timeout = 100):
        
        # Method for executing query 
        # Arguments: 
        #           db (str) - name of database to run 
        #           query_str (str) - query to execute
        #           connection_timeout (optional) - see mysql.connector docs
        # Return: result of query

        # Läs in lösenorden från fil för att slippa skriva det i koden 
        # i avsikt att öka säkerheten
        SQLpath = os.getcwd() + '/SQL.txt'
        with open(SQLpath) as myfile:
            mySQLPW = myfile.read()

        #---------------------------------------------------------------------------------------------
        #Executes query in query_str
        try:
            cnx = mysql.connector.MySQLConnection(
                                                user = self.username,
                                                password = self.mySQLPW,
                                                host = self.mySQLhost,
                                                database = db,
                                                connection_timeout = connection_timeout,
                                                port = self.mySQLserverPort
                                                )
            
            cursor = cnx.cursor()
            cursor.execute(query_str)

            query_result = np.array(cursor.fetchall())
            print('Succesful connection')
        except mysql.connector.Error as e:
            print(e)
        finally:
            #cursor.close()
            cnx.close()
        return query_result
    
    #def call_procedure(self, )

