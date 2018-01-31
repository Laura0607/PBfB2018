# Alignment of photoperiodic genes and tree building 

*Written by: Laura van Rosmalen*
*January/February 2018*

Read this entire file before using the script.

Use a consistent structure for you project:
* A project directory that will include all steps of your project and the README file.
* Create subdirectories for each step of the project.
* Each subdirectory must include 3 directories: Data, Code, Results 

## Description:

## Step_1: Download a batch of FASTA files containing genes of interest from NCBI and save it in a new directory.

Make a list of IDs of DNA sequences that you would like to download from NCBI.The IDs for genes can be found at the NCBI website by entering the gene name + species name. 
Save this list as a .txt file in the Data_1 directory: **~/PBfB2018/Step_1/Data_1**
In this example I will make a list with the gene "TSHb" for different rodent species and save this list as **TSHb.txt**.

Use this list as <genome_id_list> in the script **step_1.py**.

Run the python script **step_1.py** in order to download the FASTA files form NCBI

The following parts are included in this script:

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
In this example we will enter: "TSHb.txt" here.
The program will ask you to define <out_dir>, define here a name of a new outputdirectory where you would like to save the FASTA files.
In this example we will enter: **~/PBfB2018/Step_1/Results_1/outTSHb**

Make sure your current working directory is the same directory as where your input file is located.
So we will enter in the terminal: 
```
laura@laura-VirtualBox:~/PBfB2018/Step_1/Data_1$ step_1.py TSHb.txt ~/PBfB2018/Step_1/Results_1/outTSHb

```

The url_template is used to retrieve FASTA files from NCBI.
```python
url_template = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=%s&rettype=fasta&retmode=text"
```

The program retrieves the FASTA file for each ID in the input list, and saves this as "ID#.fa" in the new directory. 


## Step_2: Combine the downloaded genes into one file named **"all_genename.fa"**.

Use the command line in the terminal in order to combine the downloaded files into one FASTA file.
Save this new file in the Results_2 directory within the Step_2 directory:
```
cd ~/PBfB2018/Step_1/Data_1/outTSHb/
cat *fa > ~/PBfB2018/Step_2/Results_2/all_TSHb.fa
```
	or
Run the fowllowing script: **step_2.sh**

## Step_3: Count the amount of DNA sequences, count sequence lengths and modify header names.

Run the shell script **step_3a.sh** in your terminal to count the amount of DNA sequences in your FASTA file

Run the python script **step_3b.py** in your terminal in order to determine the DNA sequence length for each ID and save this as a .txt file..
Furthermore this programme prints the amount of sequences in your fasta file.

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

This gives: **">Mus_musculus"** as new header.


Save the modified file as: **all_genename_mod.fa**

## Step_4: Multiple sequence alignments and building a tree. 

Use the tool **clustalw** to perform a multiple sequence alignment
This tool is build in in the script: **step_4.sh**
Runs this script in order to perform a multiple alignment, the output file will be saved as a PHYLIP file.
However, this might be changed into another format by changing the script. 

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
>>> tree = Phylo.read("test.dnd", "newick")
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

or:
Run the script **step_4b.py** to print a phylogenetic tree for your multiple sequence alignment.

## Step_5: Cleaning and trimming a multiple sequence alignment by using " trimAl"

Run the script **step_5.sh** to trim the alignment.
In this script the trimAl tool is used combined with an automatic method to decide the optimal thresholds for trimming.
Parameters can be changed by changing the script.
Output will be saved as a file with a PHYLIP format. 
Also a HTML file will be created containing the trimAl's trimming summary.

## Step_6: Building a phylogenetic tree with "phyml" 

Run the shell script **step_6.sh** to build a phylogenetic tree with "phyml".

### step_6.sh:
Estimating the best phylogenetic tree:
```
phyml -i trimtest.phy -d nt -n 1 -m HKY85
```

Plot the tree and export it as a SVG picture file:
```
nw_display -s -S -v 25 -b ’opacity:0’ -i ’font-size:8’ trimtest.phy_phyml_tree > test.phy_phyml_tree.svg
```

![Phylogenetic tree](/test.phy_phyml_tree.svg)

## Step_7: Building a tree with the R package "ape".












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






