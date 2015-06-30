import glob, os
os.chdir("Daily Journals")
for file in glob.glob("*.rtf"):
	print(file)
	end_line = open(file).readlines()[-1]
	print(end_line)
