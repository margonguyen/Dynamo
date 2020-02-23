import pymysql

# Obtain connection string information from the portal
class dynoDb:
    def __init__(self):
        print('Database Initialized')
        self.host = "dynamo1.mysql.database.azure.com"
        self.user="jj1232727@dynamo1"
        self.password='Oiluj9999!'
        self.port=3306

    def getJobs(self, item):
        conn = pymysql.connect(host=self.host, user=self.user, port=self.port,passwd=self.password, db="dynamo")
        pycursor = conn.cursor()
        searchQuery = f"SELECT * FROM posts P, req R WHERE r.pid = P.pid AND category = '{item}'"
        data = pycursor.execute(searchQuery)
        row = pycursor.fetchall()
        jobList = []
        for rows in row:
            rValue = {'pid': rows[0], 'owner': rows[1], 'title':rows[2], 'income':rows[3], 'felon':rows[4], 'category':rows[5],'date':rows[6], 'Description':rows[7], 'perks':rows[8].split(',')}
            jobList.append(rValue)
        return jobList

    def getJobPid(self, pid):
        conn = pymysql.connect(host=self.host, user=self.user, port=self.port,passwd=self.password, db="dynamo")
        pycursor = conn.cursor()
        searchQuery = f"SELECT * FROM posts P, req R WHERE P.pid = {pid}"
        data = pycursor.execute(searchQuery)
        rows = pycursor.fetchone()        
        rValue = {'pid': rows[0], 'owner': rows[1], 'title':rows[2], 'income':rows[3], 'felon':rows[4], 'category':rows[5],'date':rows[6], 'Description':rows[7], 'perks':rows[8].split(',')}
        return rValue

    def findInfo(self, info, filter):
        conn = pymysql.connect(host=self.host, user=self.user, port=self.port,passwd=self.password, db="dynamo")

        pycursor = conn.cursor()
        searchQuery = ""
        #SELECT * FROM categories C, posts p WHERE C.name = "Tutoring" and C.cid = p.cid and (p.title REGEXP 'tutor|phys' or p.Description REGEXP 'tutor|phys');
        if(filter == "None"):
            searchQuery = "SELECT * FROM posts WHERE (title REGEXP '{}' or description REGEXP '{}');".format(info,info)
            data = pycursor.execute(searchQuery)
        else:
            print('works')
            searchQuery = "SELECT * FROM posts WHERE category = '{}' and (title REGEXP '{}' or Description REGEXP '{}');".format(filter,info,info)
            data = pycursor.execute(searchQuery)
        row = pycursor.fetchall()
        jobList = []
        if(len(row) > 0):
            for rows in row:
                rValue = {'pid': rows[0], 'owner': rows[1], 'title':rows[2], 'income':rows[3], 'felon':rows[4], 'category':rows[5],'date':rows[6], 'Description':rows[7], 'perks':rows[8].split(',')}
                jobList.append(rValue)
            return jobList
        else:
            return None

    def getCertificate(self,pid):
        # SELECT C.name, C.time
        # FROM posts P
        # INNER JOIN req R ON P.pid = R.pid
        # INNER JOIN certs C on c.cid = r.cid
        # WHERE P.pid = 1;
        conn = pymysql.connect(host=self.host, user=self.user, port=self.port,passwd=self.password, db="dynamo")

        pycursor = conn.cursor()
        searchQuery = f"SELECT C.name, C.time FROM posts P INNER JOIN req R ON P.pid = R.pid INNER JOIN certs C on c.cid = r.cid WHERE P.pid = {pid}"
        data = pycursor.execute(searchQuery)
        row = pycursor.fetchall()
        jobList = []
        for rows in row:
            rValue = {'name': rows[0], 'time': rows[1]}
            jobList.append(rValue)
        return jobList

    def RegisterUser(self, info):
        conn = pymysql.connect(host=self.host, user=self.user, port=self.port,passwd=self.password, db="dynamo")
        pycursor = conn.cursor()
        #INSERT INTO registered_user (username, password, address, phone) VALUES (registered_userregistered_user"Jay", "Pass", "123 LOLOL", "4087662626")
        insertStatement = "INSERT INTO users (first_name, last_name, password, email,income, interest, felon) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        #Hashing Here info[password] save to variable called pw
        

        pycursor.execute(insertStatement,(info['first'],info['second'],info['pass'],info['email'], info['income'], None, None))
        conn.commit()

    def LogInUser(self, info):
        conn = pymysql.connect(host=self.host, user=self.user, port=self.port,passwd=self.password, db="dynamo")
        pycursor = conn.cursor()
        #INSERT INTO registered_user (username, password, address, phone) VALUES (registered_userregistered_user"Jay", "Pass", "123 LOLOL", "4087662626")
        insertStatement = "INSERT INTO users (first_name, last_name, password, email,income, interest, felon) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        searchQuery = f"SELECT * from users WHERE email = '{info['email']}' AND '{info['password']}'"
        data = pycursor.execute(searchQuery)
        rows = pycursor.fetchone()        
        if rows:
            return True
        return False

    
