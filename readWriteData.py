import glob, os
os.chdir("Daily Journals")
new_file = open("data.txt", "w")

for file in glob.glob("*.rtf"):
	print(file)
	# First line is of format: "Day XXX" 
	# Found in index 7 of readlines
	first_line = open(file).readlines()[7][14:21]
	# End line is of format: "(XXXX words)"
	# Last index -> [-1]
	end_line = open(file).readlines()[-1][1:5]

	print(first_line)
	print(end_line)
	# Format: "Month Date Day Words"
	new_file.write(file[5:-10] + " " + first_line[4:8] + " " + end_line + "\n")
new_file.close()
