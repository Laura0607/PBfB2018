#!/usr/bin/python
#step_1
#Purpose: Download a batch of Fasta files from NCBI
#Modified by Laura van Rosmalen from https://github.com/adina/cibnor-2017/blob/master/scripts/fetch-genomes.py
#Date 29.01.2018

#import the tool "urllib2" for downloading files from the internet
import urllib2 

#import the "os" and "sys" tools for file, directory and path manipulations
import os
import sys

#import the time tool 
import time

#to count the number of arguments
if len(sys.argv) != 3: #checks whether you at least entered 3 arguments
    print "USAGE: step_1.py <genome_id_list> <out_dir>" #prints how the 
    	#script should be used. provide a list of IDs (genomelist.txt) and where 
    	#you want to save your files (the output directory) 
    sys.exit(1) #exit the function when the text has been printed

#url template, used to retrieve FASTA files from NCBI
url_template = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=%s&rettype=fasta&retmode=text"

os.mkdir(sys.argv[2]) #creates a new directory named sys.argv with numeric mode 2

for id in open(sys.argv[1]): #runs trough every ID.For each ID# in the list of IDs 
    id = id.strip() #Return a copy of the string (for each ID)
    if id == "": #When all IDs in the list are gone trough the loop, continue. 
        continue

    sys.stdout.write("Fetching %s..." % id) #prints for each ID: "Fetching ID$#..." so you know the program is running.
    sys.stdout.flush()
    out_file = os.path.join(sys.argv[2], id + ".fa") #Defines the outputfile (Output (FASTA)files will be saved in the directory provided by the user, with "ID#.fa" as file namer
    if os.path.exists(out_file): #If the output directory already exists, than print "already fetched"
        print "already fetched"

    open(out_file, "w").write(urllib2.urlopen(url_template % id).read()) #open the output file for writing. Write the output of the script to a new FASTA file.
    #write the data from the url_template from the ID# to a new FASTA file in the defined new directory. 
    print "Done" #prints done after each ID# in the terminal. so you know it is running
    time.sleep(1.0/3) #Pauses the python programme for 1/3 seconds before starting the loop for the next ID# in the list of IDs given

