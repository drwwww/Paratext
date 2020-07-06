from tf.app import use
from bidi.algorithm import get_display
import codecs, os

path = "C:\\Users\\philo\\OneDrive\\Web\\Github\\Paratext\\Resources\\BHSA\\"

book_num_dict = {'01': 'GEN', '02': 'EXO', '03': 'LEV', '04': 'NUM', '05': 'DEU', '06': 'JOS', '07': 'JDG', '08': 'RUT', '09': '1SA', '10': '2SA', '11': '1KI', '12': '2KI', '13': '1CH', '14': '2CH', '15': 'EZR', '16': 'NEH', '17': 'EST', '18': 'JOB', '19': 'PSA', '20': 'PRO', '21': 'ECC', '22': 'SNG', '23': 'ISA', '24': 'JER', '25': 'LAM', '26': 'EZK', '27': 'DAN', '28': 'HOS', '29': 'JOL', '30': 'AMO', '31': 'OBA', '32': 'JON', '33': 'MIC', '34': 'NAM', '35': 'HAB', '36': 'ZEP', '37': 'HAG', '38': 'ZEC', '39': 'MAL'}

A = use('bhsa', hoist=globals())

for i, b in enumerate(F.otype.s('book')):
    book = T.bookName(b)
    if "Ruth" in book:
        book_num = str(f"{i+1:02d}")
        # Write file
        filename = "SFMs\\" + str(i+1) + book_num_dict[book_num] + "BHSA" + ".sfm"
        full_filename = path + filename
        with codecs.open(full_filename, "w", "utf-8") as file:
            file.write(f"\\id {book_num_dict[book_num]} - BHSA\n\\h {book}\n\\toc2 {book_num_dict[book_num]}\n\\toc1 {book}\n\\mt {book}\n")
        #print(book)
            for i, chap in enumerate(L.d(b, 'chapter')):
                #print(f"\\c {i+1}\n\\p")
                file.write(f"\\c {i+1}\n\\p ")
                for i, verse in enumerate(L.d(chap, 'verse')):
                    #print(f"\\v {i+1}")
                    verse_text = get_display(T.text(verse))
                    file.write(f"\\v {i+1} {verse_text}\n")
