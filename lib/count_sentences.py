#!/usr/bin/env python3

import ipdb

class MyString:

  def __init__(self, value = ""):
    self._value = value if type(value) == str else None

  def get_value(self):
    return self._value

  def set_value(self, value):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")
      return None

  def ends_with(self, sentence, end_char):
    if sentence[-1] == end_char:
      return True
    else: 
      return False

  def is_sentence(self):
    return self.ends_with(self._value, '.')
 
  def is_question(self):
    return self.ends_with(self._value, '?')

  def is_exclamation(self):
    return self.ends_with(self._value, '!')

  def count_sentences(self):
    counter = 0
    split_sentence = self._value.split(' ')
    for sentence in split_sentence:
      if(len(sentence) > 0):
        string = MyString(sentence)
        counter += 1 if string.is_sentence() or string.is_question() or string.is_exclamation() else 0

    return counter

  value = property(get_value, set_value)

  pass