#! /bin/bash
#step_6
#Purpose: Building a phylogenetic tree with "phyml"
#Written by: Laura van Rosmalen
#Date: 31.01.2018

cd ~/PBfB2018/Step_6/Data_6

phyml -i trim_TSHb.nex -d nt -n 1 -m HKY85 #estimating the best phylogenetic tree
#plot the tree and export it as a pdf picture file
nw_topology -I trim_TSHb.nex_phyml_tree | nw_display -s - > tree_TSHb.phy_phyml_tree.pdf  #-S -v 50 -b ’opacity:1’ -i ’font-size:8’ #trim_TSHb.nex_phyml_tree > tree_TSHb.phy_phyml_tree.svg 

nw_topology -I trim_TSHb.nex_phyml_tree | nw_display -s - > tree_TSHb.phy_phyml_tree.svg  #-S -v 50 -b ’opacity:1’ -i ’font-size:8’ #trim_TSHb.nex_phyml_tree > tree_TSHb.phy_phyml_tree.svg 

ln -s /home/laura/PBfB2018/Step_6/Data_6* /home/laura/PBfB2018/Step_6/Results_6/.

