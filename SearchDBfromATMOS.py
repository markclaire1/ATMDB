import sys
from atmDB import searchDB


# Parse arguments from command line
templatename = sys.argv[1]
pc = sys.argv[2]
reaction_file = sys.argv[3]
star_file = sys.argv[4]
settings_file = sys.argv[5]
v = sys.argv[6]

#print(f"Arguments received: {templatename}, {pc}, {reaction_file}, {star_file}, {settings_file}, {v}")
note = searchDB(templatename, pc, reaction_file, star_file, settings_file, v)
with open("PHOTOCHEM/OUTPUT/searchDB_result.txt", "w") as f:
    f.write(note)