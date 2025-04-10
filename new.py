

PLAY = 'Hi there we are here Hi there we are here'
def turn_text_into_wordslist(text):
    return text.split(' ')


def create_dictionary_number_of_words(list_of_words):
    words_dictionary = {}
    for word in list_of_words:
        if word not in words_dictionary:
            words_dictionary[word]=0
        words_dictionary[word] += 1
    return words_dictionary

def top_n_words(freq):
    current_frequent_word_count = 0
    current_frequent_word = ''
    for key, value in freq.items():
        if value > current_frequent_word_count:
            current_frequent_word_count = value
            current_frequent_word = key
    return current_frequent_word, current_frequent_word_count

def remover_top_freq_word(freq_word_list, frequent_word):
        return freq_word_list.pop(frequent_word)

def print_50_top_words_and_counts(most_freq_word, count_of_word, count_of_print):
    return print(f'{count_of_print}.{most_freq_word}: {count_of_word}')

def main():
    count = 1
    number_of_print = 50
    list_of_words = turn_text_into_wordslist(PLAY)
    words_dict = create_dictionary_number_of_words(list_of_words)
    while count <= number_of_print:
            top_freq_word, top_freq_word_count = top_n_words(words_dict)
            if len(words_dict):
                remover_top_freq_word(words_dict,top_freq_word)
                print_50_top_words_and_counts(top_freq_word, top_freq_word_count, count)
            else:
                print('End of the text')
                break
            count += 1
if __name__ == '__main__':
    main()