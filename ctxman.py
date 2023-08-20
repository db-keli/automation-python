from contextlib import contextmanager

@contextmanager
def Open_file(filename, mode):
    try:
        File = open(filename, mode)
        yield File
    finally:
        File.close()
        
with Open_file('learn.txt', 'a') as File:
    File.write('\nMike is King')
    
print(File.closed)
    

class OpenFile():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__ (self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__ (self, exec_type, exc_val, traceback):
        self.file.close()
        
with OpenFile('learn.txt', 'a') as f:
    f.write('\nThere was no need overwritting')

print(f.closed)