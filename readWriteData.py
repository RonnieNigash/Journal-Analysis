import glob, os
os.chdir("Daily Journals")
new_file = open("data.txt", "w")

for file in glob.glob("*.rtf"):
	print(file)
	# First line is of format: "Day XXX" 
	# Found in index 7 of readlines
	first_line = open(file).readlines()[7]
	# End line is of format: "(XXXX words)"
	# Last index -> [-1]
	end_line = open(file).readlines()[-1]

	print(first_line[14:21])
	print(end_line)
	new_file.write(file + " " + first_line + " " + end_line + "\n")
new_file.close()
