def count_words(text):
    split_words = text.split()
    return len(split_words)

def count_characters(text):
    character_dict = {}
    for c in text:
        lower = c.lower()
        if lower in character_dict:
            character_dict[lower] += 1
        else:
            character_dict.update({lower: 1})
    return character_dict

def sort_characters_to_list(char_dict):
    def sort_on(dict):
        return dict["count"]

    char_list = []
    for c in char_dict:
        char_list.append({ "character": c, "count": char_dict[c]})

    char_list.sort(reverse=True, key=sort_on)
    return char_list
