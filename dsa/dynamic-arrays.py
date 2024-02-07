import ctypes


class Dynamic_Array(object):
    def __init__(self) -> None:
        """
        Constructor for the class. Initializes the _n, _capacity, and _A attributes.
        """
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
    
    
    def __len__(self) -> int:
        """
        Return the length of the object. No parameters are taken. Returns an integer.
        """
        return self._n
    
    
    def __getitem__(self, k) -> int:
        """
        Get the item at the specified index.

        Parameters:
            k (int): The index of the item to retrieve.

        Returns:
            int: The item at the specified index.
        """
        if not 0 <= k < self._n:
            return IndexError('invalid index')
        
        return self._A[k]
    
    
    def _append(self, obj) -> None:
        """
        Appends an object to the array. If the array is full,
        it will be resized to double its current capacity.
        """
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1
        
    
    def _resize(self, c) -> None:
        """
        Resize the array to the specified capacity.

        Parameters:
            c: int - The new capacity of the array.

        Returns:
            None
        """
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c
    
    
    def _make_array(self, c):
        """
        Create and return an array of the specified type and length.
        """
        return(c * ctypes.py_object)()
        

arr = Dynamic_Array()

for i in range(10):
    arr._append(i)

