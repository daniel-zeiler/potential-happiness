"""
Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end
with a special character '#').

You are given a string array sentences and an integer array times both of length n where sentences[i] is a previously
typed sentence and times[i] is the corresponding number of times the sentence was typed. For each input character
except '#', return the top 3 historical hot sentences that have the same prefix as the part of the sentence already
typed.

Here are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before. The
returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have
the same hot degree, use ASCII-code order (smaller one appears first). If less than 3 hot sentences exist,
return as many as you can. When the input is a special character, it means the sentence ends, and in this case,
you need to return an empty list. Implement the AutocompleteSystem class:

AutocompleteSystem(String[] sentences, int[] times) Initializes the object with the sentences and times arrays.
List<String> input(char c) This indicates that the user typed the character c. Returns an empty array [] if c == '#'
and stores the inputted sentence in the system. Returns the top 3 historical hot sentences that have the same prefix
as the part of the sentence already typed. If there are fewer than 3 matches, return them all.


Example 1:

Input
["AutocompleteSystem", "input", "input", "input", "input"]
[[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]
Output
[null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]

Explanation AutocompleteSystem obj = new AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"],
[5, 3, 2, 2]); obj.input("i"); // return ["i love you", "island", "i love leetcode"]. There are four sentences that
have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and
'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot
sentences, so "ironman" will be ignored. obj.input(" "); // return ["i love you", "i love leetcode"]. There are only
two sentences that have prefix "i ". obj.input("a"); // return []. There are no sentences that have prefix "i a".
obj.input("#"); // return []. The user finished the input, the sentence "i a" should be saved as a historical
sentence in system. And the following input will be counted as a new search.

"""
import collections
import heapq
from typing import List


class SentenceObj:
    def __init__(self, sentence, value):
        self.sentence = sentence
        self.value = value

    def __lt__(self, nxt):
        if self.value != nxt.value:
            return self.value < nxt.value
        else:
            for self_char, next_char in zip(self.sentence, nxt.sentence):
                if ord(self_char) != ord(next_char):
                    return ord(self_char) > ord(next_char)
            return len(self.sentence) > len(nxt.sentence)

    def __repr__(self):
        return self.sentence


class AutoCompleteNode:
    def __init__(self, letter=None, value=0):
        self.letter = letter
        self.value = value
        self.sentence = None
        self.top_three = []
        self.children = collections.defaultdict(AutoCompleteNode)


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.input_string = ''
        self.head = AutoCompleteNode('')
        self.pointer = self.head
        for sentence, time in zip(sentences, times):
            self.add_word(sentence, time)

    def add_word(self, sentence, time):
        def add_word_recursive(node, sentence_remaining):
            if not sentence_remaining:
                node.sentence = sentence
                node.value += time
                node.top_three = [SentenceObj(sentence, node.value)]
                return node.top_three
            letter = sentence_remaining[0]
            if letter not in node.children:
                node.children[letter] = AutoCompleteNode(letter)
            child_top_three = add_word_recursive(node.children[letter], sentence_remaining[1:])
            if node.value is not 0:
                heapq.heappush(child_top_three, SentenceObj(node.sentence, node.value))
            if len(node.top_three) > 3:
                heapq.heappop(child_top_three)
            node.top_three = child_top_three
            return node.top_three

        add_word_recursive(self.head, sentence)

    def input(self, c: str) -> List[str]:
        node = self.pointer
        if c == '#':
            self.add_word(self.input_string, 1)
            self.pointer = self.head
            self.input_string = ''
            return []
        self.input_string += c
        if self.pointer and c in node.children:
            self.pointer = node.children[c]
            return self.pointer.top_three
        self.pointer = None
        return []


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

autocomplete = AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2])
print(autocomplete.input('i'))
print(autocomplete.input(' '))
print(autocomplete.input('a'))
print(autocomplete.input('#'))
print('~~~~~')
print(autocomplete.input('i'))
print(autocomplete.input(' '))
print(autocomplete.input('a'))
print(autocomplete.input('#'))
print('~~~~~')
print(autocomplete.input('i'))
print(autocomplete.input(' '))
print(autocomplete.input('a'))
print(autocomplete.input('#'))
print('~~~~~')
print(autocomplete.input('i'))
print(autocomplete.input(' '))
print(autocomplete.input('a'))
print(autocomplete.input('#'))
print('~~~~~')

print(autocomplete.input('i'))
print(autocomplete.input(' '))
print(autocomplete.input('a'))
print(autocomplete.input('#'))
print('~~~~~')

print(autocomplete.input('i'))
print(autocomplete.input(' '))
print(autocomplete.input('a'))
print(autocomplete.input('#'))
print('~~~~~')

print(autocomplete.input('i'))
print(autocomplete.input(' '))
print(autocomplete.input('a'))
print(autocomplete.input('#'))
print('~~~~~')
