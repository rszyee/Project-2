#the parser reads the dataset and creates new text files for future storage in the MySQL database
#!/usr/bin/python

infile = 'GDS4854_full.soft'
fh = open(infile)
#opens the dataset file

line = fh.readline()
while line[:20] != '!dataset_table_begin': 
  line=fh.readline() 
#the first line is read 

header= fh.readline().strip() #the header is read 

colnames={}#the column names are read

index=0
for title in header.split('\t'):
  colnames[title]=index
  print '%s\t%s'%(title,index)
  index=index+1

#open our output files, one per table.
genefile=open('genes.txt', 'w')
probefile=open('probes.txt', 'w')
expressionfile=open('expression.txt', 'w')

genefields=['Gene ID', 'Gene symbol', 'Gene title']
samples=header.split('\t')[2:int(colnames['Gene title'])] #When read until 'Gene title', the header will be split with '\t'
probefields=['ID_REF','Gene ID']
#selects and places columns into created output files.

def buildrow(row, fields):
  '''fill in'''
  newrow=[]
  for f in fields:
    newrow.append(row[int(colnames[f])])
  return "\t".join(newrow)+"\n"

def build_expression(row, samples):
  '''fill in'''
  exprrows=[]
  for s in samples:
    newrow=[s,]
    newrow.append(row[int(colnames['ID_REF'])])
    newrow.append(row[int(colnames[s])])
    exprrows.append("\t".join(newrow))
  return "\n".join(exprrows)+"\n"

rows=0

#writing the datafile into created output text files
for line in fh.readlines():
  try:
    if line[0]=='!':
      continue
    row=line.strip().split('\t')
    genefile.write(buildrow(row, genefields))
    probefile.write(buildrow(row,probefields))
    expressionfile.write(build_expression(row, samples))
    rows=rows+1
  except:
    pass

#close the created text files with data written in them
genefile.close()
probefile.close()
expressionfile.close()

#print number of rows processed to check if parser worked in reading and writing datafile into new textfiles
print '%s rows processed'%rows
