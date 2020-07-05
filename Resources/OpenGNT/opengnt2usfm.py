import os, re, codecs
import pandas as pd

path = "C:\\Users\\philo\\OneDrive\\Web\\Github\\Paratext\\Resources\\OpenGNT\\"
#csv_file = "OpenGNT_basic-minusHTML-sample.csv"
csv_file = "OpenGNT_basic-minusHTML.csv"

book_num_dict = {
    40:'MAT',
    41:'MRK',
    42:'LUK',
    43:'JHN',
    44:'ACT',
    45:'ROM',
    46:'1CO',
    47:'2CO',
    48:'GAL',
    49:'EPH',
    50:'PHP',
    51:'COL',
    52:'1TH',
    53:'2TH',
    54:'1TI',
    55:'2TI',
    56:'TIT',
    57:'PHM',
    58:'HEB',
    59:'JAS',
    60:'1PE',
    61:'2PE',
    62:'1JN',
    63:'2JN',
    64:'3JN',
    65:'JUD',
    66:'REV',
}

data = pd.read_csv(path + csv_file,sep="\t")
df = pd.DataFrame(data)

for k, v in book_num_dict.items():
    filename = "SFMs\\" + str(k + 1) + book_num_dict[k] + "OGNT" + ".sfm"
    full_filename = path + filename
    with codecs.open(full_filename, "w", "utf-8") as file:
        book_data = df.loc[df['BOOK'] == k]
        #print(f"\\id {book_num_dict[k]}")
        #print(book_data)
        file.write(f"\\id {book_num_dict[k]} - OpenGNT\n")
        for chap in book_data.CHAP.unique():
            chap_data = df.loc[(df['BOOK'] == k) & (df['CHAP'] == chap)]
            #print(f"\\c {chap}")
            file.write(f"\\c {chap}\n\\p ")
            for verse in chap_data.VERSE.unique():
                verse_data = df.loc[(df['BOOK'] == k) & (df['CHAP'] == chap) & (df['VERSE'] == verse), 'WORD']
                verse_words = verse_data.tolist()
                verse_contents = ' '.join(verse_words)
                verse_contents = verse_contents.replace("¬", "").replace("¶", "\n\\p ").replace("=", "").replace("+", "")
                #print(f"\\v {verse} {verse_contents}")
                file.write(f"\\v {verse} {verse_contents}\n")