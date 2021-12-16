import json

path = "C:\\Users\\philo\\OneDrive\\Web\\Github\\Paratext\\Examples\\"
verses_by_chapter = "verses_by_chapter.json"
v_b_c_full = path + verses_by_chapter
most_pop_refs = "most-popular-refs-chaps.json"
pop_refs_full = path + most_pop_refs

list_of_tuples = []
with open(v_b_c_full) as json_file:
    verses_by_chapter_data_dict = dict(json.load(json_file))

    with open(pop_refs_full) as json_file2:
        most_pop_refs_data_dict = dict(json.load(json_file2))
   
    for ref, v_num in verses_by_chapter_data_dict.items():
        ref_citations_verses_tuple = (ref, most_pop_refs_data_dict[ref], v_num)
        list_of_tuples.append(ref_citations_verses_tuple)

refs_ratio_dict = {}
for ref, citations, verses in list_of_tuples:
    ratio = citations / verses
    refs_ratio_dict[ref] = ratio

# Sort it
sorted_refs_ration_dict = {k:v for k, v in sorted(refs_ratio_dict.items(), key=lambda item: item[1], reverse=True)}

# Announce the results
print()
print("By ratio")
top_num = int(input("Top how many? "))
print()
# Results
for count, (ref, ratio) in enumerate(sorted_refs_ration_dict.items()):
    print("{}. {} - {:.2f}".format(count+1,ref,ratio))
    # print("{}".format(ref))
    if count >= top_num-1: # Because dicts don't have indexes?
        break