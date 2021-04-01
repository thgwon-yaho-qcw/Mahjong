import os


def find_earliest_nonzero_index(arr, index=0):
    while index < len(arr) and arr[index] == 0:
        index += 1
    return index


def modify_list(arr, indices, val):
    for index in indices:
        arr[index] += val


def snake_to_camel(snake):
    return ''.join(word.title() for word in snake.split('_'))


def camel_to_snake(camel):
    return ''.join(['_'+c.lower() if c.isupper() else c for c in camel]).lstrip('_')


PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))