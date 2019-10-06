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
    frequencies = {}
    if text == None:
        return frequencies
    else:
        if type(text) is int:
            return frequencies
        elif len(text) == 0:
            return frequencies
        else:
            splitted = (text.replace('\n', ' ')).split(' ')
            prohibited_marks = ['-', '.', '!', ',', '?', '"', "'", ':', ';', '/', '*', '%', '$', '(', ')', '_']
            res = []
            for word in splitted:
                if not word.isdigit() and word not in prohibited_marks:
                    clear_word = ''
                    for elem in word:
                        if elem not in prohibited_marks:
                            clear_word += elem
                    if clear_word is not '':
                        res.append(clear_word)
            for key in res:
                if key in frequencies:
                    frequencies[key] += 1
                else:
                    frequencies[key] = 1
    return frequencies
stop_words = ('ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about',
              'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be',
              'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself',
              'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the',
              'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through',
              'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should',
              'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all',
              'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in',
              'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over',
              'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has',
              'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few',
              'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing',
              'it', 'how', 'further', 'was', 'here', 'than')
def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict:
    """
    Removes all stop words from the given frequencies dictionary
    """
    filtered_dict = {}
    if frequencies is None or len(frequencies) == 0:
        filtered_dict = {}
        return filtered_dict
    else:
        for key, value in filtered_dict.items():
            if key not in stop_words or isinstance(key, str):
                filtered_dict[key] = value
    print(filtered_dict)
    return filtered_dict

top_n = 4

def get_top_n(filtered_dict: dict, top_n: int) -> tuple:
    """
    Takes first N popular words
    """
    if filtered_dict == {} or top_n <= 0:
        return ()
    elif top_n > len(filtered_dict):
        top_n = len(filtered_dict)
    top_list = sorted(filtered_dict.items(), key=lambda n: n[1], reverse=True)
    done = tuple(top_list[:top_n])
    return done