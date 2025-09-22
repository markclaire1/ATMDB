import sys
from atmDB import out2DB


# Parse arguments from command line
templatename = sys.argv[1]
pc = sys.argv[2]
reaction_file = sys.argv[3]
star_file = sys.argv[4]
settings_file = sys.argv[5]

#print(f"UpdateDB received: {templatename}, {pc}, {reaction_file}, {star_file}, {settings_file}")
out2DB(templatename, pc, reaction_file, star_file, settings_file)
