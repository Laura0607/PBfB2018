# Aligment of photoperiodic genes and tree building 

*Written by: Laura van Rosmalen*
*January/February 2018*

Read this entire file before using the script.

Use a consistent structure for you project:
* A project directory that will include all steps of your project and the README file.
* Create subdirectories for each step of the project.
* Each subdirectory must include 3 directories: Data, Code, Results 

## Description:

## Step_1
### Purpose: Download a batch of FASTA files from NCBI and save it in a new directory.

Make a list of IDs of DNA sequences that you would like to download from NCBI.The IDs for genes can be found at the NCBI website by entering the gene name + species name. 
Save this list as a .txt file in the Data directory: **~/PBfB2018/Step1/Data**
Use this list as <genome_id_list> in the script **step_1.py**.

Import the tool "urllib2" to be able to download files from the internet:
```python
import urllib2
```

Import the tools for file, directory and path manipulations:
```python
import os
import sys
```

Import the time tool, in order to pause the python program.
```python
import time
```

The program will ask you to enter a <genome_id_list>, this is a .txt file containing the IDs from the genes of interest that you would like to download from NCBI.
The program will ask you to define <out_dir>, define here a name of a new outputdirectory where you would like to save the FASTA files.

The url_template is used to retrieve FASTA files from NCBI.
```python
url_template = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=%s&rettype=fasta&retmode=text"
```

The program retrieves for each ID in the list the FASTA file, and saves this as "ID#.fa" in the new directory. 


## Step_2
### Purpose: Combine the downloaded genes into one file named **"allgenes_genename.fa"**.

Use the command line in the terminal in order to combine the downloaded files into one FASTA file.
Save this new file in the Results directory within the Step2 directory:
```
cd ~/PBfB2018/Step1/Data
cat *fa > ~/PBfB2018/Step2/Results/allgenes_genename.fa
```

## Step_3
### Purpose: count the amount of DNA sequences, modify header names and count sequence lengths.

Run the shell script **step_3a.sh** in your terminal to count the amount of DNA sequences in your FASTA file

Run the python script **Step_3.py** in your terminal in order to determine the DNA sequence length for each ID.

Open the FASTA file in your texteditor (jEdit). Use regular expression in order to modify the header names.

Replace PREDICTED\s for nothing, in order to remove this part of the headers.

```
Search for: PREDICTED:\s
Replace with: 
```

Take a header name and define in regular expressions where to search for.

**>NM_009432.2 Mus musculus thyroid stimulating hormone, beta subunit (Tshb), transcript variant 1, mRNA**

```
Search for: (>)\w+.+\d+\.\d+\s(\w+)\s(\w+).+
Replace with:$1$2_$3
```

This gives: **>Mus_musculus** as new header.


Save the modified file as: ** *_mod.fasta**

## Step_4
### Purpose: Align genes and build a tree

Use the command "clustalw" in your terminal in order to start a CLUSTAL multiple sequence alignment.

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
Enter the name of the sequence file : allgenes_genename.fa
Sequence format is Pearson
Sequences assumed to be DNA


Sequence 1: NM_009432.2      645 bp
Sequence 2: XM_005357118.1   537 bp
Sequence 3: XM_013118100.2   499 bp
Sequence 4: XM_015999206.1  1518 bp



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
Enter a name for the CLUSTAL output file  [allgenes_genename.aln]: genes.aln
Start of Pairwise alignments
Aligning...

Sequences (1:2) Aligned. Score:  86
Sequences (1:3) Aligned. Score:  83
Sequences (1:4) Aligned. Score:  68
Sequences (2:3) Aligned. Score:  84
Sequences (2:4) Aligned. Score:  83
Sequences (3:4) Aligned. Score:  88
```

Enter a name for the output file containing the phylogenetic tree, ending with .dnd:
```
Enter name for new GUIDE TREE           file   [allgenes_genename.dnd]: genes.dnd

Guide tree file created:   [genes.dnd]

There are 3 groups
Start of Multiple Alignment

Aligning...
Group 1: Sequences:   2      Score:8910
Group 2: Sequences:   3      Score:9004
Group 3: Sequences:   4      Score:9441
Alignment Score 18863



Consensus length = 1525 

CLUSTAL-Alignment file created  [genes.aln]



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


Your choice: 



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
```

Open python in your terminal by just typing: "python"

```
Your choice: x
laura@laura-VirtualBox:~/PBfB2018/Step2/Results$ python
Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
Import the module Phylo from biopython and draw a phylogenetic tree from the output file (*.dnd) from the CLUSTAL multiple aligment that we just performed. 
```
>>> from Bio import Phylo
>>> tree = Phylo.read("genes.dnd", "newick")
>>> Phylo.draw_ascii(tree)
                            ____________________________________ NM_009432.2
  _________________________|
 |                         |_______ XM_005357118.1
_|
 |____ XM_013118100.2
 |
 |______________________________ XM_015999206.1

```






## Clone this repository
Clone this repository to be able to stark working immediately, just do:

```
git clone https://github.com/Laura0607/PBfB2018.git
```

## Scripts

1.
2.
3.
4.





