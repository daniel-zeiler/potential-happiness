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


class AutocompleteNode:
    def __init__(self):
        self.children = collections.defaultdict(AutocompleteNode)
        self.words = set()
        self.word_heap = []
        self.limit = 3

    def add_to_node(self, word, weight):
        heapq.heappush(self.word_heap, (weight, word))
        if len(self.word_heap) > self.limit:
            heapq.heappop(self.word_heap)


class Autocomplete:
    def __init__(self):
        self.head = AutocompleteNode()
        self.cursor_node = self.head
        self.cache_counter = collections.defaultdict(int)
        self.input_string = ''

    def add(self, word, weight):
        self.cache_counter[word] += weight

        def add_recursive(node, word_remaining):
            if not word_remaining:
                node.words.add(word)
            else:
                letter = word_remaining[0]
                if letter not in node.children:
                    node.children[letter] = AutocompleteNode()
                node.words.add(word)
                add_recursive(node.children[letter], word_remaining[1:])

        add_recursive(self.head, word)

    def input_character(self, character):
        if character == '#':
            self.complete_word()
        else:
            self.input_string += character
            if self.cursor_node is not None and character in self.cursor_node.children:
                self.cursor_node = self.cursor_node.children[character]
                return sorted(self.cursor_node.words, key=lambda x: -self.cache_counter[x])
            return []

    def complete_word(self):
        self.add(self.input_string, 1)
        self.input_string = ''
        self.cursor_node = self.head


autocomplete = Autocomplete()
words = ['a', 'cat', 'catheter', 'cats', 'camp', 'cathay', 'camps']
weights = [1, 2, 3, 4, 5, 6, 7]
for word, weight in zip(words, weights):
    autocomplete.add(word, weight)

inputs = ['a', '#', 'c', 'a', 't', 's', '#']
for input in inputs:
    print(autocomplete.input_character(input))
