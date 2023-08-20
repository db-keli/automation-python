from contextlib import contextmanager

@contextmanager
def Open_file(filename, mode):
    try:
        File = open(filename, mode)
        yield File
    finally:
        File.close()
        
with Open_file('learn.txt', 'w') as File:
    File.write('Mike is King')
    
print(File.closed)
    