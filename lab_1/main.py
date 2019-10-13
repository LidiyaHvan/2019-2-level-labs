"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""
text = '''
You said if you could fly
You would fly far - far into the sky
So all you'd ever know
Is that blue - that blue sky up above?
You've yet to learn what the pain from true sadness is like
You've only had but a taste
But you're a moth to the flame
When all my feelings reach you
They'll no longer be mute
For on that day
They'll live in spoken words
From in a dream
When you awake into the world
You no longer know
If you could only spread your wings and fly away
You said if you could fly
You would fly far - far into the sky
And you would set your aim
On the clouds all around that endless sky
The moment you break free
You'll finally find - find all you seek
And it's all waiting there
In that blue - in that blue sky up above
In that blue - in that blue sky up above
In that blue - in that blue sky up above
'''
def calculate_frequences(text: str) -> dict:
    """
    Calculates number of times each word appears in the text
    """
    if text is None or text == '':
        return {}
    if isinstance(text, int):
        return {}
    clear_text = ''
    for word in text:
        if word.isalpha():
            clear_text += word
        elif word == ' ' or word == '\n':
            clear_text += word
        else:
            clear_text += ' '
    clear_text = clear_text.lower()
    splitted_text = clear_text.split()
    freq_dict = {}
    for new_word in splitted_text:
        number_of_words = splitted_text.count(new_word)
        freq_dict[new_word] = number_of_words
    return freq_dict

def filter_stop_words(freq_dict: dict, stop_words: tuple) -> dict:
    """
    Removes all stop words from the given frequencies dictionary
    """
    if freq_dict is None and stop_words is None:
        return {}
    elif freq_dict is None and stop_words is not None:
        return {}
    elif freq_dict is not None and stop_words is None:
        return freq_dict
    filtered_dict = freq_dict.copy()
    for key in freq_dict:
        if not isinstance(key, str):
            del filtered_dict[key]
    for stop in stop_words:
        if stop in filtered_dict:
            del filtered_dict[stop]
    return filtered_dict


def get_top_n(filtered_dict: dict, top_n: int) -> tuple:
    """
    Takes first N popular words
    """
    if top_n > 0:
        list_of_words = list(filtered_dict.items())
        list_of_words.sort(key=lambda el_value: -el_value[1])
        top_words = []
        for elm in list_of_words:
            first_elm = elm[0]
            top_words.append(first_elm)
        fin_tuple = tuple(top_words[:top_n])
    else:
        fin_tuple = ()
    return fin_tuple


