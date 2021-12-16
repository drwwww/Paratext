bw = ["GEN","EXO","LEV","NUM","DEU","JOS","JDG","RUT","1SA","2SA","1KI","2KI","1CH","2CH","EZR","NEH","EST","JOB","PSA","PRO","ECC","SOL","ISA","JER","LAM","EZE","DAN","HOS","JOE","AMO","OBA","JON","MIC","NAH","HAB","ZEP","HAG","ZEC","MAL","MAT","MAR","LUK","JOH","ACT","ROM","1CO","2CO","GAL","EPH","PHI","COL","1TH","2TH","1TI","2TI","TIT","PHM","HEB","JAM","1PE","2PE","1JO","2JO","3JO","JUD","REV","TOB","JDT","ESG","WIS","SIR","BAR","EPJ","PRA","SUS","BEL","1MA","2MA","3MA","4MA","1ES","4ES","PRM","PSX","ODE","PSS","LAO","SIP","JSA","JDA","DNG","TBS","SUT","DAT","BET",]
usfm = ["GEN","EXO","LEV","NUM","DEU","JOS","JDG","RUT","1SA","2SA","1KI","2KI","1CH","2CH","EZR","NEH","EST","JOB","PSA","PRO","ECC","SNG","ISA","JER","LAM","EZK","DAN","HOS","JOL","AMO","OBA","JON","MIC","NAM","HAB","ZEP","HAG","ZEC","MAL","MAT","MRK","LUK","JHN","ACT","ROM","1CO","2CO","GAL","EPH","PHP","COL","1TH","2TH","1TI","2TI","TIT","PHM","HEB","JAS","1PE","2PE","1JN","2JN","3JN","JUD","REV","TOB","JDT","ESG","WIS","SIR","BAR","LJE","S3Y","SUS","BEL","1MA","2MA","3MA","4MA","1ES","2ES","MAN","PS2","ODA","PSS","EZA","5EZ","6EZ","DAG","PS3","2BA","LBA","JUB","ENO","1MQ","2MQ","3MQ","REP","4BA","LAO",]

bw_not_in_usfm = []
usfm_not_in_bw = []

for i in bw:
	if i not in usfm:
		bw_not_in_usfm.append(i)

for i in usfm:
	if i not in bw:
		usfm_not_in_bw.append(i)

#print(bw_not_in_usfm)
#print(usfm_not_in_bw)

book_matches = zip(bw_not_in_usfm[:17], usfm_not_in_bw)
#print(list(book_matches))

book_string = ""
for bw, usfm in book_matches:
	book_string += "{}={}:".format(bw,usfm)

bw_joined = '|'.join(bw_not_in_usfm[:17])


print("Find: {}".format(bw_joined))
print("Dictionary:{}".format(book_string)) # Dictionary for regex dict lookup and replace

'''
1. Paste dictionary at the bottom of the file containing BW book abbreviations to be converted to USFM (remove string final colon)
2. Run regular expression FIND for (?s)(bw_joined)(?=.*:\1=(\w+)\b)
	Nb. insert bw_joined output in place of bw_joined
3. Replace (in EditPadPro 8): \g<2>
4. Remove pasted dictionary from end of file.
'''
