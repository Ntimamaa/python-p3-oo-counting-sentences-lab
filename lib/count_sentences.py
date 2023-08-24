class MyString:
    def __init__(self, value=None):
        if value is not None and not isinstance(value, str):
            print("The value must be a string.")
            return
        self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        if self.value is None:
            return 0
        sentences = self.value.split('.')
        sentences = [s.strip() for s in sentences if s.strip()] 
        return len(sentences)

string1 = MyString("Hello")
print(string1.is_sentence()) 
print(string1.is_question())  
print(string1.is_exclamation()) 
print(string1.count_sentences())  

# getting 2 errors still but dont know how to go about it  but the code works as expected