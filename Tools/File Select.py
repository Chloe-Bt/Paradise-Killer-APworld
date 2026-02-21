input_file = "/home/chloe/git/Paradise-Killer-APworld/Tools/UE4SS_ObjectDump.txt"
output_file = "/home/chloe/git/Paradise-Killer-APworld/Tools/InventoryItem.txt"
search_string = "InventoryItem"

with open(input_file, "r", encoding="utf-8") as infile, \
     open(output_file, "w", encoding="utf-8") as outfile:
    
    for line in infile:
        if search_string.lower() in line.lower():
            outfile.write(line)

print("Done! Filtered lines written to", output_file)