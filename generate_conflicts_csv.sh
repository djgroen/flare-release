#!/bin/bash

: '
The script runs Flare to generate conflict.csv files
'

# input directory contains location and link data (i.e., locations.csv and links.csv)
input_dir='test_input_csv'
input_dir='input_csv_mali'


output_dir='SWEEP'

#variable cwd = the current working directory
cwd=$(pwd)


end_time=300
generate_cnt=20

check_input_parameters()
{
	
	if [ -z "$input_dir" ] ; then
		printf "the input directory variable (\$input_dir) is empty\n"
		exit
	elif [ ! -d "$cwd/$input_dir" ]; then
		printf "The input directory (%s) doesn't exist !!! \n" "$cwd/$input_dir"
		exit
	fi
	# clear output directory
	if [ -d "$output_dir" ]; then
		rm -rf ./$output_dir/*
	else
		mkdir $output_dir
	fi
	# generate SWEPP subdirectories from [0] ... [generate_cnt-1]

	for (( cnt=0; cnt<$generate_cnt; cnt++ ))
	do
		mkdir -p ./$output_dir/$cnt/input_csv
	done

	# clear log.out for logging the test_flare.py output
	rm -f log.out
}

run_Flare()
{
	for (( cnt=0; cnt<$generate_cnt; cnt++ ))
	do
		printf "\toutput test_flare.py for run = %s \n\n" "$cnt" >> log.out
		
		python3 test_flare.py $end_time $cwd/$input_dir &>> log.out
		mv flare-out.csv ./$output_dir/$cnt/input_csv/conflicts.csv
		printf "save conflicts.csv -->  ./%s/%s/input_csv \n" "$output_dir" "$cnt"
		
		printf "%0.s-" {1..80} >> log.out
		printf "\n" >> log.out
	done
}


check_input_parameters

run_Flare
