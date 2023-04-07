#!/usr/bin/env python3
import ipdb

class MyString:
  def __init__(self,value=""):
    self.value = value
    
  #Define the value property   
  def get_value(self):
    return self._value
  
  def set_value(self,value):
    if type(value)==str:
      self._value = value
    else:
      print("The value must be a string.")
  
  value = property(get_value, set_value)

 
  #!Define the the is_sentence method
  def is_sentence(self):
    if self.value.endswith("."):
      return True
    else:
      return False
  #!Define the the is question method 
  def is_question(self):
    if self.value.endswith("?"):
      return True
    else:
      return False
  #!Define the the is exclamation method 
  def is_exclamation(self):
    if self.value.endswith("!"):
      return True
    else:
      return False
    
  def count_sentences(self):
    value = self.value
    for punc in ['!','?']:
        value = value.replace(punc, '.')
    
    sentences = [s for s in value.split('.') if s]
    
    return len(sentences)
    
  
    
    
  
    

    
  
    
  

