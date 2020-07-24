# -*- coding: utf-8 -*-
'''Strings and Text

double-quotes or single-quotes
调试时不要盯着代码看，仿佛想一下就会弄明白某段代码的作用一样。要动手破坏和调试代码。

'''

my_name = 'Alex'
sentence = f"My name is {my_name}"
print(f"I said: {sentence}")

hilarious = False
joke_evaluation = "Isn't that joke so funny? {}"
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
print(w + e)  # + notation can combine string
