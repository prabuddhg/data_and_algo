"""
ransom_note = "aaab"
magazine = "baaa"
True
"""
ransom_note = "aaab"
magazine = "bb"

def validate(ransom_note, magazine):
    string_dict = {}
    ransom_note_list = [i for i in ransom_note]
    magazine_list = [i for i in magazine]
    for each_char in ransom_note_list:
        if each_char in string_dict:
            string_dict[each_char] += 1
        else:
            string_dict[each_char] = 1
    for each_char in magazine:
        if each_char not in string_dict:
            return False
        else:
            string_dict[each_char] -= 1
            if string_dict[each_char] < 0:
                return False
    #print(string_dict)
    return True

print(f"output = {validate(ransom_note, magazine)}")
