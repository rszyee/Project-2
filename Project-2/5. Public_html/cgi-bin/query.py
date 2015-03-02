#!/usr/local/bin/python
import cgi #enables us to use the cgi module
import cgitb
cgitb.enable()
#activates a special exception handler that will display detailed reports on the Web browser if any errors occur

form = cgi.FieldStorage()#using the FieldStorage class enables us to get submitted form data
import MySQLdb #imports MySQLdb
sql="SELECT symbol, title FROM Genes where gene_id= %s" #query gene symbol and title using SQL
db=MySQLdb.connect(db='rszyee', user='rszyee', passwd='_8ydr_sW') #connecting to MySQLdb
cursor=db.cursor()
cursor.execute(sql,form[''].value) #queries the SQL database
result=cursor.fetchall() #fetches the results from the SQL database
result

Expressionsql="SELECT DISTINCT accession FROM Sample INNER JOIN Expression On Sample.accession=Expression.accession INNER JOIN Probes ON Probes.reference=Expression.reference INNER JOIN Genes ON Genes.id=Probes.id WHERE id=%s and subset='seizure'" #query accession from MySQLdb for subset seizure
cursor.execute(Expressionsql,form[''].value)#queries the SQL database
Expressionresult=cursor.fetchall()#fetches the results from the SQL database
Expressionresult

Expression1sql="SELECT DISTINCT accession FROM Sample INNER JOIN Expression On Sample.accession=Expression.accession INNER JOIN Probes ON Probes.reference=Expression.reference INNER JOIN Genes ON Genes.id=Probes.id WHERE id=%s and subset='control'" #query accession from MySQLdb for subset seizure
cursor.execute(Expression1sql,form[''].value)#queries the SQL database
Expression1result=cursor.fetchall()#fetches the results from the SQL database
Expression1result

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
print "<html><head><TITLE>CGI form</TITLE></head>"
print "<body><H1>Form information</H1>"
print "<b>Gene ID: </b>"
#page formatting using HTML

print "<table><tr><th>Key</th><th>Value</th></tr>"

for k in form.keys():
        print "<tr><td>%s</td><td>%s</td></tr>"%(k, form[k].value)
#to print the table
print "</table>"
print "<b> Gene symbol, Gene title:</b>"
print result
print "<p><b> Expression Values of Patients with Seizure:</b></p>"
print Expressionresult
print "<p><b> Expression Values of Patients with No Seizure:</b></p>"
print Expression1result
print "</body></html>"

