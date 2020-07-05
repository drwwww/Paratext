import os, re, json

# Find number of verses in each chapter of the Bible
verses_by_chapter_dict = {}
path = "C:\\My Paratext 8 Projects\\MP1\\"
for file in os.listdir(path):
    if file.endswith(".SFM"):
        full_path = path + file
        with open(full_path, 'r') as sfm_book:
            contents = sfm_book.read()
            find_book_id = re.compile(r"(?<=\\id\s)[\w\d]{3}(?=\s)")
            book_id_list = find_book_id.findall(contents)
            book_id = book_id_list[0]
            #print(book_id)
        with open(full_path, 'r') as sfm_book:
            count = 0
            for line in sfm_book:
                count += 1
                findr = re.compile(r"\\v") # Matches \v
                list_verses = findr.findall(line)
                if len(list_verses) > 0:
                    ref = f"{book_id}.{count-1}"
                    #print(f"{book_id}.{count-1} - {len(list_verses)}")
                    verses_by_chapter_dict[ref] = len(list_verses)

# Write to a file
json = json.dumps(verses_by_chapter_dict)
f = open("verses_by_chapter.json","w")
f.write(json)
f.close()
