'''Classes to represent our gene expression objects'''
#Import the MySQL module
import MySQLdb
#Creates classes
class DBHandler():
'''The static database connection - avoids overuse of resources'''
  connection=None
  dbname='rszyee'
  dbuser='rszyee'
  dbpassword='_8ydr_sW'

  def __init__(self):
    '''Initialise database'''
    if DBHandler.connection == None:
      DBHandler.connection = MySQLdb.connect(db=DBHandler.dbname, user=DBHandler.dbuser, passwd=DBHandler.dbpassword)

  def cursor(self):
    return DBHandler.connection.cursor()

class Genes():
  '''A class that describes an individual gene'''
  id=''
  symbol=''
  title=''
  probelist=[]

  def __init__(self,id):
    '''Init method for Genes'''
    db=DBHandler()
      self.id=id
      cursor=db.cursor()
      sql='SELECT symbol, title FROM Genes WHERE id=%s'
      cursor.execute(sql,(id,))
      #this queries the database
      result=cursor.fetchone()
      #gets result from query and populate the class fields
      self.symbol=result[0]
      self.title=result[1]
      #fetching the probes
      probesql='SELECT reference FROM Probes WHERE id=%s'
      cursor.execute(probessql,(id,))
      for result in cursor.fetchall():
      self.probeslist.append(result[0])
  
  def get_expression(self, value):
    '''Retrieve expression values for a given experiment for this gene'''
    db=DBHandler()
      self.value=value
      cursor=db.cursor()
      Expressionsql='SELECT reference and accession FROM Expression WHERE value=%s'
      cursor.execute(Expressionsql,(value))
      result=cursor.fetchall()
      self.reference =result[0]
      self.accession=result[1]

print("Classes.py are created")
