from tf.app import use
from bidi.algorithm import get_display
import codecs, os

path = "C:\\Users\\philo\\OneDrive\\Web\\Github\\Paratext\\Resources\\BHSA\\"

bhsa_book_list_with_ptx_ids = ['GEN', 'EXO', 'LEV', 'NUM', 'DEU', 'JOS', 'JDG', '1SA', '2SA', '1KI', '2KI', 'ISA', 'JER', 'EZK', 'HOS', 'JOL', 'AMO', 'OBA', 'JON', 'MIC', 'NAM', 'HAB', 'ZEP', 'HAG', 'ZEC', 'MAL', 'PSA', 'JOB', 'PRO', 'RUT', 'SNG', 'ECC', 'LAM', 'EST', 'DAN', 'EZR', 'NEH', '1CH', '2CH']
book_num_dict = {'GEN': '01', 'EXO': '02', 'LEV': '03', 'NUM': '04', 'DEU': '05', 'JOS': '06', 'JDG': '07', 'RUT': '08', '1SA': '09', '2SA': '10', '1KI': '11', '2KI': '12', '1CH': '13', '2CH': '14', 'EZR': '15', 'NEH': '16', 'EST': '17', 'JOB': '18', 'PSA': '19', 'PRO': '20', 'ECC': '21', 'SNG': '22', 'ISA': '23', 'JER': '24', 'LAM': '25', 'EZK': '26', 'DAN': '27', 'HOS': '28', 'JOL': '29', 'AMO': '30', 'OBA': '31', 'JON': '32', 'MIC': '33', 'NAM': '34', 'HAB': '35', 'ZEP': '36', 'HAG': '37', 'ZEC': '38', 'MAL': '39'}
ptx_ids_bhs_names = {'GEN': 'בראשית', 'EXO': 'שמות', 'LEV': 'ויקרא', 'NUM': 'במדבר', 'DEU': 'דברים', 'JOS': 'יהושע', 'JDG': 'שפטים', '1SA': 'שמואל א', '2SA': 'שמואל ב', '1KI': 'מלכים א', '2KI': 'מלכים ב', 'ISA': 'ישעיהו', 'JER': 'ירמיהו', 'EZK': 'יחזקאל', 'HOS': 'הושע', 'JOL': 'יואל', 'AMO': 'עמוס', 'OBA': 'עבדיה', 'JON': 'יונה', 'MIC': 'מיכה', 'NAM': 'נחום', 'HAB': 'חבקוק', 'ZEP': 'צפניה', 'HAG': 'חגי', 'ZEC': 'זכריה', 'MAL': 'מלאכי', 'PSA': 'תהלים', 'JOB': 'איוב', 'PRO': 'משלי', 'RUT': 'רות', 'SNG': 'שיר השירים', 'ECC': 'קהלת', 'LAM': 'איכה', 'EST': 'אסתר', 'DAN': 'דניאל', 'EZR': 'עזרא', 'NEH': 'נחמיה', '1CH': 'דברי הימים א', '2CH': 'דברי הימים ב'}
ptx_ids_latin_names = {'GEN': 'Genesis', 'EXO': 'Exodus', 'LEV': 'Leviticus', 'NUM': 'Numeri', 'DEU': 'Deuteronomium', 'JOS': 'Josua', 'JDG': 'Judices', '1SA': 'Samuel I', '2SA': 'Samuel II', '1KI': 'Reges I', '2KI': 'Reges II', 'ISA': 'Jesaia', 'JER': 'Jeremia', 'EZK': 'Ezechiel', 'HOS': 'Hosea', 'JOL': 'Joel', 'AMO': 'Amos', 'OBA': 'Obadia', 'JON': 'Jona', 'MIC': 'Micha', 'NAM': 'Nahum', 'HAB': 'Habakuk', 'ZEP': 'Zephania', 'HAG': 'Haggai', 'ZEC': 'Sacharia', 'MAL': 'Maleachi', 'PSA': 'Psalmi', 'JOB': 'Iob', 'PRO': 'Proverbia', 'RUT': 'Ruth', 'SNG': 'Canticum', 'ECC': 'Ecclesiastes', 'LAM': 'Threni', 'EST': 'Esther', 'DAN': 'Daniel', 'EZR': 'Esra', 'NEH': 'Nehemia', '1CH': 'Chronica I', '2CH': 'Chronica II'}
#num_book_dict = {'01': 'GEN', '02': 'EXO', '03': 'LEV', '04': 'NUM', '05': 'DEU', '06': 'JOS', '07': 'JDG', '08': 'RUT', '09': '1SA', '10': '2SA', '11': '1KI', '12': '2KI', '13': '1CH', '14': '2CH', '15': 'EZR', '16': 'NEH', '17': 'EST', '18': 'JOB', '19': 'PSA', '20': 'PRO', '21': 'ECC', '22': 'SNG', '23': 'ISA', '24': 'JER', '25': 'LAM', '26': 'EZK', '27': 'DAN', '28': 'HOS', '29': 'JOL', '30': 'AMO', '31': 'OBA', '32': 'JON', '33': 'MIC', '34': 'NAM', '35': 'HAB', '36': 'ZEP', '37': 'HAG', '38': 'ZEC', '39': 'MAL'}

A = use('bhsa', hoist=globals())

for i, b in enumerate(F.otype.s('book')):
    book = T.bookName(b)
    if "_" in book:
        book = book.replace("_", " ").replace("1", "I").replace("2", "II")              
    book_ptx_abrev = bhsa_book_list_with_ptx_ids[i]
    book_num = book_num_dict[book_ptx_abrev]
    book_heb = ptx_ids_bhs_names[book_ptx_abrev]
    book_latin = ptx_ids_latin_names[book_ptx_abrev]
    #if "Chron" in book:
    # print(book)
    # Write file
    filename = "SFMs\\" + book_num + book_ptx_abrev + "BHSA" + ".sfm"
    full_filename = path + filename
    with codecs.open(full_filename, "w", "utf-8") as file:
        file.write(f"\\id {book_ptx_abrev} - Biblia Hebraica Stuttgartensia (Amstelodamensis)\n\\h {book.title()}\n\\toc3 {book_ptx_abrev}\n\\toc2 {book.title()}\n\\toc1 {book_heb}\n\\mt1 {book_heb}\n\\mt2 {book_latin}\n\\mt3 {book.title()}\n")
        #print(book)
        for i, chap in enumerate(L.d(b, 'chapter')):
            #print(f"\\c {i+1}\n\\p")
            file.write(f"\\c {i+1}\n")
            for i, verse in enumerate(L.d(chap, 'verse')):
                #print(f"\\v {i+1}")
                #verse_text = get_display(T.text(verse))
                #file.write(f"\\v {i+1} {verse_text}\n")
                #file.write(f"{verse_text} {i+1} v\\\n")
                file.write(f"\\q \\v {i+1} {T.text(verse)}\n")
