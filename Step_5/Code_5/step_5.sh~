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
