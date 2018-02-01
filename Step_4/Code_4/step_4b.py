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


