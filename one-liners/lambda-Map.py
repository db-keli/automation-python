lambda x, y: x*y

txt = ['Get the fuck out of here',
       'Do not say the word fuck',
       'I never said it']

detect = map(lambda s: (True, s ) if 'fuck' in s else (False, s), txt)
print(list(detect))

