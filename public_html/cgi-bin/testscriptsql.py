#!/usr/local/bin/python
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
print "<html><head><TITLE>CGI script output</TITLE></head>"
print "<body><H1>Form values</H1>"
print "<table><tr><th>Key</th><th>Value</th></tr>"

for k in form.keys():
        print "<tr><td>%s</td><td>%s</td></tr>"%(k, form[k])

sql="SELECT expession from expression e inner join 
gene g on e.gene_id=g.gene_id where gene_id= %s"

db=MySQLdb.connect(....)
cursor=db.cursor()
cursor.execute(sql, form[geneid].value)

gene=Gene(form[geneid].value()
results=gene.getExpression()



print "</table>"

print "</body></html>"
