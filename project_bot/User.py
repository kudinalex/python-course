class User:
    def __init__(self, user_id, word, attempt_count=3):
        self.user_id = user_id
        self.word = word
        self.attempt_count = attempt_count
        self.shadow_form_word = len(self.word) * '*'

    def decrease_attempt_count(self):
        self.attempt_count -= 1

    def reveal_shadow_form_letter(self, letter):
        for i in range(len(self.shadow_form_word)):
            if letter == self.word[i]:
                self.shadow_form_word[i] = letter
