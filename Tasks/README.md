# Coding-Exercises
Name: Sachin Sarath Y Kothandaraman

## Dependencies

The code requires python3 with pandas and matplotlib libraries.
To create a reproducible environment, I have generated a conda environment yaml file with the necessary dependencies set up.
You can choose to install these dependencies directly in your local linux environment or download Miniconda as instructed below:

download and install Miniconda from https://conda.io/en/latest/miniconda.html

Example for installing Miniconda for Linux :

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh
rm  Miniconda3-latest-Linux-x86_64.sh
```
Create and activate a conda environment using the yml file provided:

```
#Create environment after downloading yml file
conda env create -f conda_env.yml

#Activate the conda environment:
conda activate conda_env
```
 ## Instructions

TASK 1:
Input csv files to be placed under Tasks/Data
Colors.csv to be placed under Tasks

Output csv and pdf will be generated under Tasks

```
python ./Tasks/Task1.py
```

TASK 2:
The filepath of the input and output csv files need to be specified in the command line
Please ensure not to provide space after comma when specifying the colors.
```
python ./Tasks/Task2.py -i ./Tasks/Output.csv -o ./Tasks/SummaryStats.csv -c Red,Blue,Orange
```
for any further information please run the help command
```
python ./Tasks/Task2.py -h
```
