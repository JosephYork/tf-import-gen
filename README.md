The import script will take an Azure DevOps pipeline log and parse it for terraform errors where a resource already exists.
The Azure DevOps pipeline log can be saved by navigating to the pipeline run, clicking view raw log, then saving the log as a text file.
Set the file variable to the pipeline log file and update the output filename.
Run the python script to generate the set of terraform import commands.

WARNING: REVIEW THE OUTPUT FILE CAREFULLY BEFORE RUNNING, WITH LARGE NUMBERS OF IMPORTS I HAVE SEEN THE ORDERING MESS UP, RESULTING IN WRONG RESOURCES IMPORTED TO WRONG TERRAFORM RESOURCES.