import re

# The input file
path = input("Path to XRF file (add trailing slash): ")
top_num = int(input("Top how many? "))
xref_db_list = [ # List of tuples
    ("The_Works_nt_ot.xrf","chapter and verses"), # Full chapter and verse ref
    ("The_Works_nt_ot.xrf","chapters"), # Chapter only, not specific verses
]

# Loopy McLooperton
for xref_db, output in xref_db_list: # Directly access tuples in list
    xref_file = path + xref_db # Build full filename with path
    refs_dict = {} # Dict for storage
    with open(xref_file, 'r') as file: # Opens file and closes when done
        for line in file: # Implicitly goes line by line through file
            if "verse" not in output: # Look at ref chapter only
                findr = re.compile(r"(?!^)(?<=[{\s])[\w\d]{3}\.\d+") # Matches GEN.29
            else: # Look at ref chapter and verse
                findr = re.compile(r"(?!^)(?<=[{\s])[\w\d]{3}\.\d+:\d+") # Matches GEN.29:14 EPH.5:28 1CO.11:8
            list_of_refs = findr.findall(line) # Create list of findr regex matches
            for ref in list_of_refs: # Loop through list of matches
                if ref not in refs_dict: # If ref not already in dict...
                    refs_dict[ref] = 1 # Add that ref with 1 occurrence
                else: # Otherwise...that ref is already in dict, so...
                    refs_dict[ref] += 1 # Increases its occurrences by uno

    # Sort that dict
    sorted_refs_dict = {k:v for k, v in sorted(refs_dict.items(), key=lambda item: item[1], reverse=True)}

    # Announce the results
    print()
    print("The top {} most referenced {} in {} are:".format(top_num,output, xref_db))

    # Results
    for count, (ref, occs) in enumerate(sorted_refs_dict.items()):
        print("{}. {} - {}x".format(count+1,ref,occs))
        if count >= top_num-1: # Because dicts don't have indexes?
            break
