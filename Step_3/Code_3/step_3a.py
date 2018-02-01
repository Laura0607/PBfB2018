#!/usr/bin/python
#Step_3
#Purpose: This program determines the sequence lengths and saves the output in a new .txt file
#Written by: Laura van Rosmalen
#Date: 29.01.2018


#for FASTA files, the record identifier is the first word on the >line

import os
os.chdir("/home/laura/PBfB2018/Step_3/Data_3") #change working directory into directory where the input file is located.

from Bio import SeqIO #import the module Sequence Input/Output

#InFileName = raw_input("Enter a filename") #user input --> insert filename on which to run the script
InFileName = "all_TSHb.fa"

#This calculates the number of sequences of a fasta file
count = 0
for line in file("all_TSHb.fa", 'r'):
    if line.startswith('>'):
        count += 1


#InFileName = "all_TSHb.fa" #give the file name for which you would like to determine the sequence lengths.

OutFileName=InFileName + ".txt" #the output file will be saved as a text file with the same name as the inputfile.
OutFile=open(OutFileName, 'w') #to open the OutFile, and make the file writable. 

#modified from: https://github.com/peterjc/biopython_workshop/blob/master/reading_sequence_files/README.rst
for record in SeqIO.parse(InFileName, "fasta"): #For each record in the fasta file
    Output = ("Record " + record.id + ", length " + str(len(record.seq))) #print record ID + the sequence length.
    print(Output)
    OutFile.write(Output+ "\n") #write the output to the OutFile 
    
print "The file contains", count, "sequences" #prints the amount of sequences that the fasta file contains
print("The sequence lengths have been saved as all_TSHb.txt") #confirms that the output file has been saved