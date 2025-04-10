PLAY = 'Hi there we are here Hi there we are here Hi there we are here Hi there we are here'
def turn_text_into_wordslist(text):
    text = text.translate(str.maketrans('','','.,?!'))
    text = text.lower()
    return text.split(' ')

def catch_value_of_dict(item):
    return item[1]

def create_dictionary_number_of_words(list_of_words):
    words_dictionary = {}
    for word in list_of_words:
        if word not in words_dictionary:
            words_dictionary[word]=0
        words_dictionary[word] += 1
    return words_dictionary

def sort_dictionary(word_dict):
    return dict(sorted(word_dict.items(), key=catch_value_of_dict, reverse=True))

def print_50_top_words_and_counts(sorted_reverse_dict):
        count = 0
        for key, value in sorted_reverse_dict.items():
            if count >= 50:
                break
            print(f'{count+1}.{key}: {value}')
            count += 1

def main():
    list_of_words = turn_text_into_wordslist(PLAY)
    words_dictionary = create_dictionary_number_of_words(list_of_words)
    sorted_dictinary = sort_dictionary(words_dictionary)
    print_50_top_words_and_counts(sorted_dictinary)

if __name__ == '__main__':
    main()
