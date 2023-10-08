import collections


def word_ladder(beginWord, endWord, wordList):
    def get_graph(words):
        graph = collections.defaultdict(list)
        for word in words:
            for i, character in enumerate(word):
                link_word = word[:i] + '*' + word[i + 1:]
                graph[link_word].append(word)
        return graph

    graph = get_graph(wordList)
    queue = collections.deque([[1, beginWord]])
    visited = {beginWord}
    while queue:
        distance, word = queue.popleft()
        if word == endWord:
            return distance
        for i, character in enumerate(word):
            link_word = word[:i] + '*' + word[i + 1:]
            if link_word in graph:
                for linked_word in graph[link_word]:
                    if linked_word not in visited:
                        visited.add(linked_word)
                        queue.append([distance + 1, linked_word])
    return -1


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(word_ladder(beginWord, endWord, wordList))
