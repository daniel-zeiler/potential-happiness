class TextEditorState:
    def __init__(self, selection, text, cursor):
        self.selection = selection
        self.text = text
        self.cursor = cursor


class TextEditor:
    def __init__(self, text=''):
        self.text = text
        self.cursor = 0
        self.selection = []
        self.copy_text = ''
        self.state = []
        self.state_pointer = 0
        self.update_state()

    def update_state(self):
        self.state = self.state[:self.state_pointer + 1]
        self.state.append(TextEditorState(self.selection, self.text, self.cursor))
        self.state_pointer = len(self.state) - 1

    def undo(self):
        self.state_pointer -= 1
        previous_state = self.state[self.state_pointer]
        self.text = previous_state.text
        self.selection = previous_state.selection
        self.cursor = previous_state.selection
        return self.text

    def redo(self):
        self.state_pointer += 1
        next_state = self.state[self.state_pointer]
        self.text = next_state.text
        self.selection = next_state.selection
        self.cursor = next_state.cursor
        return self.text

    def append(self, a_string):
        if self.selection:
            self.text = self.text[:self.selection[0]] + a_string + self.text[self.selection[1]:]
            self.selection = []
        else:
            self.text = self.text[:self.cursor] + a_string + self.text[self.cursor:]
            self.cursor += len(a_string)
        self.update_state()
        return self.text

    def move(self, position):
        self.cursor = position
        self.selection = []
        return self.text

    def backspace(self):
        if self.selection:
            self.text = self.text[:self.selection[0]] + self.text[self.selection[1]:]
            self.selection = []
        else:
            if len(self.text) == 0:
                self.update_state()
                return self.text
            else:
                self.text = self.text[:self.cursor - 1] + self.text[self.cursor:]
                self.cursor -= 1
        self.update_state()
        return self.text

    def select(self, start, end):
        self.selection = [max(0, start), min(end, len(self.text))]

    def copy(self):
        self.copy_text = self.text[self.selection[0]:self.selection[1]]

    def paste(self):
        if self.copy_text:
            self.append(self.copy_text)
        return self.text

    def cut(self):
        if self.selection:
            self.copy_text = self.text[self.selection[0]:self.selection[1]]
            self.text = self.text[:self.selection[0]] + self.text[self.selection[1]:]
            self.selection = []
        self.update_state()
        return self.text


text_editor = TextEditor()
text_editor.append("Hello, world!")
text_editor.select(7, 12)
print(text_editor.backspace())
print(text_editor.undo())
print(text_editor.undo())
print(text_editor.redo())
print(text_editor.redo())
