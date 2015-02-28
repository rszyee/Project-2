#!/usr/local/bin/python
import cgi #description
import cgitb
cgitb.enable()

form = cgi.FieldStorage()#description
import MySQLdb #description
sql="SELECT symbol, title FROM Genes where gene_id= %s" #description
db=MySQLdb.connect(db='rszyee', user='rszyee', passwd='_8ydr_sW') #description
cursor=db.cursor()#
cursor.execute(sql,form[''].value) #
result=cursor.fetchall() #
result

Expressionsql="SELECT DISTINCT accession FROM Sample INNER JOIN Expression On Sample.accession=Expression.accession INNER JOIN Probes ON Probes.reference=Expression.reference INNER JOIN Genes ON Genes.id=Probes.id WHERE id=%s and subset='seizure'" 
cursor.execute(Expressionsql,form[''].value)
Expressionresult=cursor.fetchall()
Expressionresult

Expression1sql="SELECT DISTINCT accession FROM Sample INNER JOIN Expression On Sample.accession=Expression.accession INNER JOIN Probes ON Probes.reference=Expression.reference INNER JOIN Genes ON Genes.id=Probes.id WHERE id=%s and subset='control'" 
cursor.execute(Expression1sql,form[''].value)
Expression1result=cursor.fetchall()
Expression1result

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
print "<html><head><TITLE>CGI form</TITLE></head>"
print "<body><H1>Form information</H1>"
print "<b>Gene ID: </b>"
#

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

