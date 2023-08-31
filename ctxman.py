from contextlib import contextmanager


@contextmanager
def open_file(filename, mode):
    try:
        file = open(filename, mode)
        yield file
    finally:
        file.close()


with open_file('learn.txt', 'a') as File:
    File.write('\nMike is King')
    
print(File.closed)
    

class OpenFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exec_type, exc_val, traceback):
        self.file.close()


with OpenFile('learn.txt', 'a') as f:
    f.write('\nThere was no need over writing')

print(f.closed)
