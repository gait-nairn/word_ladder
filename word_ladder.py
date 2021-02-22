#!/bin/python3
from collections import deque
import copy


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny',
    'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty',
    'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''

    d = open(dictionary_file)
    words = d.read()
    words = words.split('\n')

    ls = [start_word]
    qu = deque()
    qu.append(ls)

    if start_word == end_word:
        return [start_word]
    else:
        while len(qu) != 0:
            w = qu.popleft()
            for i in words:
                if _adjacent(w[-1], i):
                    if i == end_word:
                        w.append(i)
                        return w
                    ls_copy = copy.deepcopy(w)
                    ls_copy.append(i)
                    qu.append(ls_copy)
                    words.remove(i)


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if ladder == []:
        return False
    b = True
    for i in range(len(ladder)-1):
        b = _adjacent(ladder[i], ladder[i+1])
        if not b:
            return False
    return b


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if len(word1) != len(word2):
        return False

    dif = 0

    for i in range(len(word1)):
            if word1[i] != word2[i]:
                dif += 1
    if dif == 1:
        return True
    else:
        return False
