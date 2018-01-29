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
Purpose: Download a batch of FASTA files from NCBI.

Make a list of IDs that you would like to download from NCBI. Save this list as a .txt file.
Use this list as <genome_id_list> in the script step_1.py.

Import the tool "urllib2" to be able to download files from the internet:
```
import urllib2
```

Import the tools for file, directory and path manipulations:
```
import os
import sys
```

Import the time tool, in order to pause the python program.
```
import time
```

The program will ask you to enter a <genome_id_list>, this is a .txt file including the IDs that you would like to download from NCBI
The program will ask you to define <out_dir>, define here the outputdirectory where you would like to save the FASTA files.

The url_template is used to retrieve FASTA files from NCBI.
```
url_template = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=%s&rettype=fasta&retmode=text"
```

The program retrieves for each ID in the list the FASTA file, and saves the new files as "ID#.fa" in the new directory. 













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





