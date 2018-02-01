# Alignment of photoperiodic genes and tree building 

*Written by: Laura van Rosmalen*
*January/February 2018*

Read this entire file before using the script.

Use a consistent structure for you project:
* A project directory that will include all steps of your project and the README file.
* Create subdirectories for each step of the project.
* Each subdirectory must include 3 directories: Data, Code, Results 

## Description: 
**Alignment of (photoperiodic) genes, tree building and SNP calling**
Retrieve DNA sequences of (photoperiodic) genes from NCBI | count them | count the sequence lengths | modify header names | multiple sequence alignment | cleaning and trimming | build phylogenetic tree | plot tree | export images

## Step_1: Download a batch of FASTA files containing genes of interest from NCBI and save it in a new directory.
Make a list of IDs of DNA sequences that you would like to download from NCBI.The IDs for genes can be found at the NCBI website by entering the gene name + species name. 
Save this list as a .txt file in the Data_1 directory: **~/PBfB2018/Step_1/Data_1**
In this example I will make a list with the gene "TSHb" for different rodent species and save this list as **TSHb.txt**.

Use this list as <genome_id_list> in the script **step_1.py**.

Run the python script **step_1.py** in order to download the FASTA files from NCBI.

Make sure your current working directory is the same directory as where your input file is located.
The program will automatically change the working directory into **~/PBfB2018/Step_1/Data_1/.**.
The program loops trough the commands and retrieves the FASTA file for each ID, listed in the input file, and saves this as "ID#.fa" in the new directory. 

### See below the content of script ***step_1.py*** + annotation:
```python
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

os.chdir("/home/laura/PBfB2018/Step_1/Data_1") #change working directory into directory where the input file is located.

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
```

The program will ask you to enter a <genome_id_list>, this is a .txt file containing the IDs from the genes of interest that you would like to download from NCBI.
In this example we will enter: "TSHb.txt" here.
The program will ask you to define <out_dir>, define here a name of a new output directory where you would like to save the FASTA files.
In this example we will enter: **~/PBfB2018/Step_1/Results_1/OutputTSHb**


## Step_2: Combine the downloaded DNA-sequences into one file named **"all_genename.fa"**.

Run the fowllowing script: **step_2.sh**:

This program will first link your results from step_1 to the directory Data_2.
Change the working directory into the directory where your fasta files are linked to.
Use the "cat" command in order to concatenate all sequences into 1 FASTA file.
Save this new file in the Results_2 directory with the name **all_TSHb.fa**

### See below the content of script ***step_2.sh*** + annotation:
```
#! /bin/bash
#step_2
#Purpose: combine FASTA files into 1 file
#Written by: Laura van Rosmalen
#Date: 31.01.2018

#linking your results from step_1 to the directory Data_2
ln -s /home/laura/PBfB2018/Step_1/Results_1/OutputTSHb/* /home/laura/PBfB2018/Step_2/Data_2/.
cd ~/PBfB2018/Step_2/Data_2/ #change directory into the directory where your input file is located.
cat *.fa > ~/PBfB2018/Step_2/Results_2/all_TSHb.fa #save all fasta files within that directory as a new file

#linking your results from step_2 to the directory Data_3
ln -s /home/laura/PBfB2018/Step_2/Results_2/all_TSHb.fa /home/laura/PBfB2018/Step_3/Data_3/.
```

## Step_3: Count the amount of DNA-sequences, count sequence lengths and modify header names.

Run the python script **step_3a.py** in your terminal in order to determine the DNA sequence length for each ID and save this as a .txt file..
Furthermore this programme prints the amount of sequences in your fasta file.

### See below the content of script ***step_3a.py*** + annotation:
```python
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
```

To modidy the header names in the FASTA file, run the shell script: **step_3b.sh**.

### See below the content of ***step_3b.sh*** + annotation:
```
#! /bin/bash
#step_3c
#Purpose: Modify header names in a FASTA file
#Written by: Laura van Rosmalen
#Date: 31.01.2018

#Linking the Data_3 to Results_3.
ln -s /home/laura/PBfB2018/Step_3/Data_3/* /home/laura/PBfB2018/Step_3/Results_3/.
cd ~/PBfB2018/Step_3/Results_3 #Change the working directory into the directory where the input file (all_TSHb.fa) is located.

#Command line expression using perl for conducting a search / replace using regular expressions.
perl -pe 's/PREDICTED:\s//g' all_TSHb.fa > all_TSHb2.fa #Replace all "PREDIDCTED:\s" by nothing and save it in a new file.
perl -pe 's/^(>)\w+.+\d+\.\d+\s(\w+)\s(\w+).+/\1\2_\3/g' all_TSHb2.fa > all_TSHb3.fa #Modify the header names by using regular expressions and save the output into a new file.
grep ">" ~/PBfB2018/Step_3/Results_3/all_TSHb3.fa #Print the header names to check whether the names are modified in a proper way:
echo "the FASTA file with modified header names has been saved as: all_TSHb3.fa" #Confirm that the program has been finished and files are saved:

```

This gives: **">Mus_musculus"** as new header.

or:

Open the FASTA file in your texteditor (jEdit). Use regular expression in order to modify the header names.

Replace PREDICTED\s for nothing, in order to remove this part of the headers.

```
Search for: PREDICTED:\s
Replace with: 
```

Take a header name and define in regular expressions where to search for.

*>NM_009432.2 Mus musculus thyroid stimulating hormone, beta subunit (Tshb), transcript variant 1, mRNA*

```
Search for: (>)\w+.+\d+\.\d+\s(\w+)\s(\w+).+
Replace with:$1$2_$3
```
This gives: **">Mus_musculus"** as new header.
Save the modified file as: **all_TSHb3.fa**


## Step_4: Multiple sequence alignment and building a tree. 

Use the tool **clustalw** to perform a multiple sequence alignment.
This tool is build into the script: **step_4a.sh**
Runs this script in order to perform a multiple alignment, the output file will be saved as 2 files with a different format: NEXUS and PHYLIP.
However, this might be changed into another format by changing the script. 

### See below the content of script ***step_4a.sh*** + annotation.
```
#! /bin/bash
#step_4a
#Purpose: Multiple sequence alignment by using clustalw
#Written by: Laura van Rosmalen
#Date: 31.01.2018

ln -s /home/laura/PBfB2018/Step_3/Results_3/all_TSHb3.fa /home/laura/PBfB2018/Step_4/Data_4/.
cd ~/PBfB2018/Step_4/Data_4 #change directory to the directory where your input file is located

clustalw -INFILE=all_TSHb3.fa -TYPE=DNA -OUTFILE=msa_TSHb.nex -OUTPUT=NEXUS #the output file is saved as NEXUS format, which can be used as input file in many other programs. 
clustalw -INFILE=all_TSHb3.fa -TYPE=DNA -OUTFILE=msa_TSHb.phy -OUTPUT=PHYLIP #the output file is saved as PHYLIP format, which can be used as input file in many other programs. 

echo "multiple sequence alignment is completed" 
echo "the output file has been saved with both a NEXUS and PHYLIP format" 

ln -s /home/laura/PBfB2018/Step_4/Data_4/* /home/laura/PBfB2018/Step_4/Results_4/.
ln -s /home/laura/PBfB2018/Step_4/Results_4/* /home/laura/PBfB2018/Step_5/Data_5/.
```

or: 
Use the command ***"clustalw"*** in your terminal in order to start a CLUSTALW multiple sequence alignment.

```
laura@laura-VirtualBox:~/PBfB2018/Step2/Results$ clustalw


 **************************************************************
 ******** CLUSTAL 2.1 Multiple Sequence Alignments  ********
 **************************************************************


     1. Sequence Input From Disc
     2. Multiple Alignments
     3. Profile / Structure Alignments
     4. Phylogenetic trees

     S. Execute a system command
     H. HELP
     X. EXIT (leave program)


Your choice: 1


Sequences should all be in 1 file.

7 formats accepted: 
NBRF/PIR, EMBL/SwissProt, Pearson (Fasta), GDE, Clustal, GCG/MSF,                  RSF.
```

Enter the name of the sequence file which includes all genes of interest:
```
Enter the name of the sequence file : all_TSHb.fa
Sequence format is Pearson
Sequences assumed to be DNA


Sequence 1: NM_009432.2      645 bp
Sequence 2: XM_003479258.3  5224 bp
Sequence 3: XM_004581882.1   520 bp
Sequence 4: XM_004641668.2  2831 bp
Sequence 5: XM_004667534.1   481 bp
Sequence 6: XM_004853785.2   841 bp
Sequence 7: XM_005357117.1   556 bp
Sequence 8: XM_008761373.2  3070 bp
Sequence 9: XM_008834013.1   570 bp
Sequence 10: XM_010631214.1   552 bp
Sequence 11: XM_013024632.1   417 bp
Sequence 12: XM_013118100.2   499 bp
Sequence 13: XM_013516550.1  2777 bp
Sequence 14: XM_015502221.1  1542 bp
Sequence 15: XM_015999206.1  1518 bp
Sequence 16: XM_016965986.1   558 bp
Sequence 17: XM_020157368.1  7031 bp
Sequence 18: XM_021158911.1   551 bp
Sequence 19: XM_021196788.1   556 bp
Sequence 20: XM_021732975.1  3977 bp



 **************************************************************
 ******** CLUSTAL 2.1 Multiple Sequence Alignments  ********
 **************************************************************


     1. Sequence Input From Disc
     2. Multiple Alignments
     3. Profile / Structure Alignments
     4. Phylogenetic trees

     S. Execute a system command
     H. HELP
     X. EXIT (leave program)


Your choice: s


Enter system command: 





 **************************************************************
 ******** CLUSTAL 2.1 Multiple Sequence Alignments  ********
 **************************************************************


     1. Sequence Input From Disc
     2. Multiple Alignments
     3. Profile / Structure Alignments
     4. Phylogenetic trees

     S. Execute a system command
     H. HELP
     X. EXIT (leave program)


Your choice: 1


Sequences should all be in 1 file.

7 formats accepted: 
NBRF/PIR, EMBL/SwissProt, Pearson (Fasta), GDE, Clustal, GCG/MSF,                  RSF.


Enter the name of the sequence file : all_TSHb.fa
Sequence format is Pearson
Sequences assumed to be DNA


Sequence 1: NM_009432.2      645 bp
Sequence 2: XM_003479258.3  5224 bp
Sequence 3: XM_004581882.1   520 bp
Sequence 4: XM_004641668.2  2831 bp
Sequence 5: XM_004667534.1   481 bp
Sequence 6: XM_004853785.2   841 bp
Sequence 7: XM_005357117.1   556 bp
Sequence 8: XM_008761373.2  3070 bp
Sequence 9: XM_008834013.1   570 bp
Sequence 10: XM_010631214.1   552 bp
Sequence 11: XM_013024632.1   417 bp
Sequence 12: XM_013118100.2   499 bp
Sequence 13: XM_013516550.1  2777 bp
Sequence 14: XM_015502221.1  1542 bp
Sequence 15: XM_015999206.1  1518 bp
Sequence 16: XM_016965986.1   558 bp
Sequence 17: XM_020157368.1  7031 bp
Sequence 18: XM_021158911.1   551 bp
Sequence 19: XM_021196788.1   556 bp
Sequence 20: XM_021732975.1  3977 bp



 **************************************************************
 ******** CLUSTAL 2.1 Multiple Sequence Alignments  ********
 **************************************************************


     1. Sequence Input From Disc
     2. Multiple Alignments
     3. Profile / Structure Alignments
     4. Phylogenetic trees

     S. Execute a system command
     H. HELP
     X. EXIT (leave program)


Your choice: 2



****** MULTIPLE ALIGNMENT MENU ******


    1.  Do complete multiple alignment now Slow/Accurate
    2.  Produce guide tree file only
    3.  Do alignment using old guide tree file

    4.  Toggle Slow/Fast pairwise alignments = SLOW

    5.  Pairwise alignment parameters
    6.  Multiple alignment parameters

    7.  Reset gaps before alignment? = OFF
    8.  Toggle screen display          = ON
    9.  Output format options
    I. Iteration = NONE

    S.  Execute a system command
    H.  HELP
    or press [RETURN] to go back to main menu


Your choice: 8



****** MULTIPLE ALIGNMENT MENU ******


    1.  Do complete multiple alignment now Slow/Accurate
    2.  Produce guide tree file only
    3.  Do alignment using old guide tree file

    4.  Toggle Slow/Fast pairwise alignments = SLOW

    5.  Pairwise alignment parameters
    6.  Multiple alignment parameters

    7.  Reset gaps before alignment? = OFF
    8.  Toggle screen display          = OFF
    9.  Output format options
    I. Iteration = NONE

    S.  Execute a system command
    H.  HELP
    or press [RETURN] to go back to main menu


Your choice: 1
```

Enter a name for the CLUSTAL output file, ending with .aln:
```
Enter a name for the CLUSTAL output file  [all_TSHb.aln]: TSHb.aln
Start of Pairwise alignments
Aligning...

Sequences (1:2) Aligned. Score:  59
Sequences (1:3) Aligned. Score:  73
Sequences (1:4) Aligned. Score:  60
Sequences (1:5) Aligned. Score:  85
Sequences (1:6) Aligned. Score:  62
...
...
...
Sequences (18:20) Aligned. Score:  74
Sequences (19:20) Aligned. Score:  73
```

Enter a name for the output file containing the phylogenetic tree, ending with .dnd:
```
Enter name for new GUIDE TREE           file   [all_TSHb.dnd]: TSHb.dnd

Guide tree file created:   [TSHb.dnd]

There are 19 groups
Start of Multiple Alignment

Aligning...
Group 1: Sequences:   2      Score:7163
Group 2: Sequences:   2      Score:8028
Group 3: Sequences:   4      Score:33361
Group 4: Sequences:   2      Score:22264
Group 5: Sequences:   3      Score:30146
Group 6: Sequences:   4      Score:8312
Group 7: Sequences:   8      Score:20744
Group 8: Sequences:   2      Score:9814
Group 9: Sequences:   3      Score:9665
Group 10: Sequences:   4      Score:10134
Group 11: Sequences:   2      Score:9558
Group 12: Sequences:   3      Score:8891
Group 13: Sequences:   7      Score:13287
Group 14: Sequences:   8      Score:9316
Group 15: Sequences:   2      Score:9756
Group 16: Sequences:   3      Score:10468
Group 17: Sequences:   4      Score:9334
Group 18: Sequences:  12      Score:9399
Group 19: Sequences:  20      Score:12163
Alignment Score 608432


Consensus length = 9379 

CLUSTAL-Alignment file created  [TSHb.aln]
```

Run the script **step_4b.py** to print a phylogenetic tree for your multiple sequence alignment.

### See below the content of script **step_4b.py** + annotation:
```python
#!/usr/bin/python
#Step_4b
#Purpose: Build a phylogenetic tree by using the Biopython tool Phylo
#Written by: Laura van Rosmalen
#Date: 31.01.2018

import os
os.chdir("/home/laura/PBfB2018/Step_4/Data_4") #change working directory into directory where the input file is located.

from Bio import Phylo #import the module Phylo

tree = Phylo.read("all_TSHb3.dnd", "newick") #read the input file in the PHYLIP format.
Phylo.draw_ascii(tree) #draw the phylogenetic tree from your input file

print "Phylogenetic tree for the TSHb gene for different rodent species is depicted above" 
```
The phylogenetic tree will be depicted in your terminal as shown below.

or:
Open python in your terminal by just typing: "python"

```
Your choice: x
laura@laura-VirtualBox:~/PBfB2018/Step2/Results$ python
Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Import the module Phylo from biopython and draw a phylogenetic tree from the output file (*.dnd) from the CLUSTAL multiple alignment that we just performed. 
```
>>> from Bio import Phylo
>>> tree = Phylo.read("all_TSHb3.dnd", "newick")
>>> Phylo.draw_ascii(tree)
              ____________ Mus_musculus
              |
           ___|            ______________________ Rattus_norvegicus
          |   |     ______|
          |   |____|      | Mus_pahari
         ,|        |
         ||        | Mus_caroli
         ||
         ||    , Mesocricetus_auratus
      ___||____|
     |   |     |       _______________________ Peromyscus_maniculatus
     |   |     |______|
     |   |            | Cricetulus_griseus
     |   |
  ___|   |_____ Microtus_ochrogaster
 |   |
 |   |            _______ Heterocephalus_glaber
 |   |    _______|
 |   | __|       |____ Fukomys_damarensis
 |   ||  |
 |   ||  |_______________ Chinchilla_lanigera
 |    |
 |    |___ Nannospalax_galili
 |
 |              ___________________ Cavia_porcellus
 |       ______|
 |    __|      |__________ Marmota_marmota
 |   |  |
 |___|  |__________________ Octodon_degus
_|   |
 |   |______ Ochotona_princeps
 |
 |   _____ Jaculus_jaculus
 |__|
 |  |_________________ Ictidomys_tridecemlineatus
 |
 |  , Dipodomys_ordii
 |__|
    |_________________ Castor_canadensis
    
>>> 
```


## Step_5: Cleaning and trimming a multiple sequence alignment(MSA) by using " trimAl".

Run the script **step_5.sh** to trim the alignment.
In this script the trimAl tool is used combined with an automatic method to decide the optimal thresholds for trimming.
Parameters can be changed by changing the script.
Output will be saved as a file with a PHYLIP and NEXUS format. 
Also a HTML file will be created containing the trimAl's trimming summary.

### See below the content of script ***step_5.sh*** + annotation:
```
#! /bin/bash
#step_5
#Purpose: Cleaning and trimming a multiple sequence alignment by using "trimAl".
#Written by: Laura van Rosmalen
#Date: 31.01.2018

cd ~/PBfB2018/Step_5/Data_5

trimal -in msa_TSHb.nex -htmlout trim_TSHb.html -out trim_TSHb.nex -gappyout
trimal -in msa_TSHb.phy -htmlout trim_TSHb.html -out trim_TSHb.phy -gappyout
#gappyout uses an automatic method to decide optimal thresholds, based in the gap percentage count over the whole alignment.
#Gets the trimAl's trimming summary in an HTML file. 

ln -s /home/laura/PBfB2018/Step_5/Data_5/* /home/laura/PBfB2018/Step_6/Data_6/.
ln -s /home/laura/PBfB2018/Step_5/Data_5/* /home/laura/PBfB2018/Step_5/Results_5/.
```

## Step_6: Building a phylogenetic tree with "phyml" 

Run the shell script **step_6.sh** to build a phylogenetic tree with "phyml" and save it as .svg and .pdf image..

remove "gap" from the NEXUS file that you have created in the previous step before running step_6.sh

### See below the content of script ***step_6.sh*** + annotation:
```
#! /bin/bash
#step_6
#Purpose: Building a phylogenetic tree with "phyml"
#Written by: Laura van Rosmalen
#Date: 31.01.2018

cd ~/PBfB2018/Step_6/Data_6

phyml -i trim_TSHb.nex -d nt -n 1 -m HKY85 #estimating the best phylogenetic tree
#remove distance numbers, plot the tree and export it as a .pdf and .svg image file.
nw_topology -I trim_TSHb.nex_phyml_tree | nw_display -s - > tree_TSHb.phy_phyml_tree.pdf  #-S -v 50 -b ’opacity:1’ -i ’font-size:8’ #trim_TSHb.nex_phyml_tree > tree_TSHb.phy_phyml_tree.svg 
nw_topology -I trim_TSHb.nex_phyml_tree | nw_display -s - > tree_TSHb.phy_phyml_tree.svg  #-S -v 50 -b ’opacity:1’ -i ’font-size:8’ #trim_TSHb.nex_phyml_tree > tree_TSHb.phy_phyml_tree.svg 
```
[Phylogenetic tree TSHb](file:///home/laura/PBfB2018/Step_6/Data_6/tree_TSHb.phy_phyml_tree.svg)

## Step_7: Building a phylogenetic tree with the R package "ape".

Install and load the following R packages:
* install.packages('ape')
* install.packages('ctv')
* install.views('Phylogenetics')

library(ape)










## Step_7: Combine a reference DNA sequence and short DNA sequences from different samples in 1 FASTA file.

The same procedure as in Step_2 will be used in order to combnine the files. 
Use the command line in the terminal in order to combine the files into one FASTA file.
Save this new file in the Results_7 directory within the Step_7 directory:

```
cd ~/PBfB2018/Step_7/Data_7/
cat *fa > ~/PBfB2018/Step_7/Results_7/all.fa
```

## Step_8: Multiple sequence alignment and trimming the alignments.

Perform a multiple sequence alignment by using the tool **"clustalw"** as shown in Step_4.
Since the reference DNA sequence is much longer compared to the other sequences, it will be useful to trim the alignments in such a way that only the covered part will be visible.





## Clone this repository
Clone this repository to be able to stark working immediately, just do:

```
git clone https://github.com/Laura0607/PBfB2018.git
```

## Scripts

1. step_1.py		Download FASTA files from NCBI 
2. step_3a.sh		Count the number of sequences in a FASTA file
3. step_3b.py		Determines sequence length 
4. step_4a.sh		Multiple sequence alignment (clustalw)
5. step_4b.py		Build a phylogenetic tree (Phylo)
6. step_5.sh		Cleaning and trimming a multiple sequence alignment (trimAl)
7. step_6.sh		Build a phylogenetic tree (phyml)






