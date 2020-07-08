# Paratext book abbreviations in Western/Protestant order
books = "GEN,EXO,LEV,NUM,DEU,JOS,JDG,RUT,1SA,2SA,1KI,2KI,1CH,2CH,EZR,NEH,EST,JOB,PSA,PRO,ECC,SNG,ISA,JER,LAM,EZK,DAN,HOS,JOL,AMO,OBA,JON,MIC,NAM,HAB,ZEP,HAG,ZEC,MAL"
book_list = books.split(",")

# Paratext book abbreviations in BHSA book order
bhsa_book_order = "GEN,EXO,LEV,NUM,DEU,JOS,JDG,1SA,2SA,1KI,2KI,ISA,JER,EZK,HOS,JOL,AMO,OBA,JON,MIC,NAM,HAB,ZEP,HAG,ZEC,MAL,PSA,JOB,PRO,RUT,SNG,ECC,LAM,EST,DAN,EZR,NEH,1CH,2CH"
bhsa_book_list = bhsa_book_order.split(",")
#print(bhsa_book_list)

# Latin book names in BHS order
latin_book_names = "Genesis,Exodus,Leviticus,Numeri,Deuteronomium,Josua,Judices,Samuel I,Samuel II,Reges I,Reges II,Jesaia,Jeremia,Ezechiel,Hosea,Joel,Amos,Obadia,Jona,Micha,Nahum,Habakuk,Zephania,Haggai,Sacharia,Maleachi,Psalmi,Iob,Proverbia,Ruth,Canticum,Ecclesiastes,Threni,Esther,Daniel,Esra,Nehemia,Chronica I,Chronica II"
latin_book_list = latin_book_names.split(",")

# Hebrew book names in BHS order
bhs_book_names = [
"בראשית",
"שמות",
"ויקרא",
"במדבר",
"דברים",
"יהושע",
"שפטים",
"שמואל א",
"שמואל ב",
"מלכים א",
"מלכים ב",
"ישעיהו",
"ירמיהו",
"יחזקאל",
"הושע",
"יואל",
"עמוס",
"עבדיה",
"יונה",
"מיכה",
"נחום",
"חבקוק",
"צפניה",
"חגי",
"זכריה",
"מלאכי",
"תהלים",
"איוב",
"משלי",
"רות",
"שיר השירים",
"קהלת",
"איכה",
"אסתר",
"דניאל",
"עזרא",
"נחמיה",
"דברי הימים א",
"דברי הימים ב"]

# Paratext book numbers in Western/Protestant order
nums = ("01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39")

#dicty = dict(zip(nums, book_list))
# dicty = dict(zip(book_list, nums))
# print(dicty)

# Print bhsa_book_list with bhs_book_names as dict
# dicty = dict(zip(bhsa_book_list, bhs_book_names))
# print(dicty)

# Print bhsa_book_list with latin_book_list with as dict
dicty = dict(zip(bhsa_book_list, latin_book_list))
print(dicty)