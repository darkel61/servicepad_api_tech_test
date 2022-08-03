sample_text = "Hi how are things? How are you?  Are you a developer? I am also a developer"

def word_counter(string):
    string = string.replace('?', '') 
    string = string.lower()
    array_of_words = string.split(' ')
    dict_counter = {}

    for word in array_of_words:
        if not word:
            continue
        if word in dict_counter:
            dict_counter[word] += 1
        else:
            dict_counter[word] = 1

    return(dict_counter) 

print(word_counter(sample_text))