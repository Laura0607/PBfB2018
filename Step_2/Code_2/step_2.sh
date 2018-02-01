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

