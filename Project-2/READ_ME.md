# BS32011 BIOINFORMATICS PROJECT

This Read_me file is the lab book of the Bioinformatics project. It details the timeline of the project, the various folders containing codes and how to use those folders.

#FOLDERS


#1. Data
This folder contains the raw dataset (GDS4854_full.soft)

#2. Parser template
This folder contains the parser template for extraction of the raw data and the text files that were created.

#3. SQL tables
This folder contains the code used to create tables in the SQL database using the text files from the 2nd folder.

#4. Classes.py
This folder contains the file to create the classes. 

#5. Public_html
This folder contains the website created for this project and the cgi form linking the website to the SQL database.



#TIMELINE
Week 1 - Introduction to Unix
       - Revising Python
       - Learning how to use git
       - Selecting a dataset from GEO NCBI(GDS4854_full.soft)
       
Week 2 - Downloaded dataset into repository
       - Wrote a parser for the GEO datafile (Used parser_template.py provided by Dr Martin to read dataset)
       - Parser could work: print rows - 52894 rows processed
       - Created 3 text files; expression.txt, genes.txt, probes.txt using parser and created another file on my own: samples.txt

Week 3 - Chose to represent data using various tables
       - Used MySQL to create tables; Genes, Probes, Sample, Expression and imported data into tables
       - Used Python to retrieve data from MySQL

Week 4 - Created a webpage about the paper regarding the dataset
       - Learnt how to use CSS and create a web form

Week 5 - Learnt how to use CGI code to allow queries on web form that interacts with SQL database and to be answered with web viewable results. 
