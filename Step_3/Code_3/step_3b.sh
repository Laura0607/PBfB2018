#! /bin/bash
#step_3c
#Purpose: Modify header names in a FASTA file
#Written by: Laura van Rosmalen
#Date: 31.01.2018

ln -s /home/laura/PBfB2018/Step_3/Data_3/* /home/laura/PBfB2018/Step_3/Results_3/.
cd ~/PBfB2018/Step_3/Results_3

perl -pe 's/PREDICTED:\s//g' all_TSHb.fa > all_TSHb2.fa
perl -pe 's/^(>)\w+.+\d+\.\d+\s(\w+)\s(\w+).+/\1\2_\3/g' all_TSHb2.fa > all_TSHb3.fa
grep ">" ~/PBfB2018/Step_3/Results_3/all_TSHb3.fa
echo "the FASTA file with modified header names has been saved as: all_TSHb3.fa"


