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


