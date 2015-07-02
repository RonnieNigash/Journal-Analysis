import glob, os
os.chdir("Daily Journals")
new_file = open("data.txt", "w")

for file in glob.glob("*.rtf"):
	print(file)
	# First line is of format: "Day XXX" 
	# Found in index 7 of readlines
	# @TODO Fix Bug here! Our .readlines()[7] is not always off, we are getting an off-by one error sometimes
	first_line = open(file).readlines()[7][14:21]
	day_count = first_line[4:8]
	day_count = day_count.replace("\\", "")
	# End line is of format: "(XXXX words)"
	# Last index -> [-1]
	end_line = open(file).readlines()[-1][1:5]

	print(first_line)
	print(end_line)

	# Format Date
	date = file[-12:-10].strip() # String of 1, 2, ..., 31
	print(date)

	# Format Month
	month = file[5:-12].strip() # String of Jan, Feb, ..., Dec
	month_dict = {"Jan" : 1, "Feb" : 2, "Mar" : 3, "Apr" : 4, "May" : 5, "June" : 6, "July" : 7, "Aug" : 8, "Sep" : 9, "Oct" : 10, "Nov" : 11, "Dec" : 12}
	month = month_dict[month] # Integer of 1, 2, ..., 12
	print(month)

	# Format: "Month Date Day Words" -> All integers concatenated to string
	new_file.write(str(month) + " " + date + " " +  day_count + " " + end_line + "\n")

new_file.close()
