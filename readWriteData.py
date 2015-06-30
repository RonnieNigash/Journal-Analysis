import glob, os
os.chdir("Daily Journals");
for file in glob.glob("*.rtf"):
    print(file)
