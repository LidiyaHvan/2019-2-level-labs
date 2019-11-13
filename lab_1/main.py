"""
Labour work #2. Levenshtein distance.
"""


def generate_edit_matrix(num_rows: int, num_cols: int) -> list:
    edit_matrix = []
    if isinstance(num_cols, int) and isinstance(num_rows, int):
        for elm in range(num_rows):
            edit_matrix.append([0] * num_cols)
    return edit_matrix


def initialize_edit_matrix(edit_matrix: tuple, add_weight: int, remove_weight: int) -> list:
    i = 0
    j = 0
    edit_matrix = list(edit_matrix)
    if isinstance(add_weight, int) and isinstance(remove_weight, int) and edit_matrix and edit_matrix[0]:
        for cols in edit_matrix:
            edit_matrix[0][0] = 0
            edit_matrix[i][0] = edit_matrix[i - 1][0] + remove_weight
            i += 1
        for rows in edit_matrix[0]:
            edit_matrix[0][0] = 0
            edit_matrix[0][j] = edit_matrix[0][j - 1] + add_weight
            j += 1
        return edit_matrix
    else:
        return edit_matrix
    pass


def minimum_value(numbers: tuple) -> int:
    if isinstance(numbers, tuple):
        return min(numbers)
    else:
        return 0
    pass


def fill_edit_matrix(edit_matrix: tuple,
                     add_weight: int,
                     remove_weight: int,
                     substitute_weight: int,
                     original_word: str,
                     target_word: str) -> list:
    if isinstance(add_weight, int) and isinstance(remove_weight, int) and isinstance(substitute_weight, int) \
            and original_word and target_word and isinstance(original_word, str) and isinstance(target_word, str):
        for i in range(1, len(edit_matrix)):
            for j in range(1, len(edit_matrix[i])):
                rem_val = edit_matrix[i - 1][j] + remove_weight
                add_val = edit_matrix[i][j - 1] + add_weight
                if original_word[i - 1] == target_word[j - 1]:
                    sub_val = edit_matrix[i-1][j-1]
                else:
                    sub_val = edit_matrix[i - 1][j - 1] + substitute_weight
                edit_matrix[i][j] = minimum_value((rem_val, add_val, sub_val))
        return list(edit_matrix)
    else:
        return list(edit_matrix)
    pass


def find_distance(original_word: str,
                  target_word: str,
                  add_weight: int,
                  remove_weight: int,
                  substitute_weight: int) -> int:
    if (isinstance(original_word, str) and isinstance(target_word, str) and isinstance(add_weight, int)
            and isinstance(remove_weight, int) and isinstance(substitute_weight, int)):
        num_rows, num_cols = len(original_word) + 1, len(target_word) + 1
        matrix = tuple(generate_edit_matrix(num_rows, num_cols))
        new_matrix = tuple(initialize_edit_matrix(matrix, add_weight, remove_weight))
        final_matrix = fill_edit_matrix(new_matrix,
                                        add_weight,
                                        remove_weight,
                                        substitute_weight,
                                        original_word,
                                        target_word)
        return final_matrix[-1][-1]
    else:
        return -1


print(find_distance(original_word = 'length', target_word = 'kitchen',
                     add_weight = 1,
                     remove_weight = 1,
                     substitute_weight = 2))

def save_to_csv(edit_matrix: tuple, path_to_file: str) -> None:
    if not isinstance(edit_matrix, tuple) or not isinstance(path_to_file, str):
        return None
    file = open(path_to_file, 'w')
    a = ''
    for line in edit_matrix:
        for i in line:
            a += str(i) + ','
        file.write(a + '\n')
    file.close()
    pass

def load_from_csv(path_to_file: str) -> list:
    file = open(path_to_file, 'r')
    matrix = []
    for line in file:
        row = list(line)
        row_fin = []
        for i in row:
            row_fin.append(i)
        matrix.append(row_fin)
    file.close()
    return matrix
    pass
