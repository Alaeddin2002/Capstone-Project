import ctypes                                      # provides low-level arrays

class DynamicArray:

    def __init__(self):
        self._n = 0                                    # count actual elements
        self._capacity = 1                             # default array capacity
        self._A = self._make_array(self._capacity)  # low-level array


    def __len__(self):
        return self._n


    def __getitem__(self, k):
        if 0 <= k < self._n:
            return self._A[k]                        # retrieve from array
        elif k < 0 and self._n+k >= 0:
            return self._A[self._n+k]
        else:
            return IndexError('Invalid index.')

    def append(self, obj):
        if self._n == self._capacity:                  # not enough room
            self._resize(2 * self._capacity)             # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):                            # nonpublic utitity
        B = self._make_array(c)                        # new (bigger) array
        for k in range(self._n):                       # for each existing value
            B[k] = self._A[k]
        self._A = B                                    # use the bigger array
        self._capacity = c

    def _make_array(self, c):                        # nonpublic utitity
         return (c * ctypes.py_object)()               # see ctypes documentation

    def insert(self, k, value):
        if self._n == self._capacity:                  # not enough room
            self._resize(2 * self._capacity)             # so double capacity
        for j in range(self._n, k, -1):                # shift rightmost first
            self._A[j] = self._A[j-1]
        self._A[k] = value                             # store newest element
        self._n += 1

    def insertEfficient(self, k, value):

        if k<0 or k>self._n:
            print("please enter appropriate index..")
            return

        if self._n == self._capacity:
            self._capacity = (2 * self._capacity)
            self._A = self._make_array(self._capacity)

        for j in range(self._n-1, k, -1):
            if self._A[j+1] is None:
                return
            self._A[j+1] = self._A[j]
        self._A[k] = value
        self._n += 1


    def remove(self, value):# note: we do not consider shrinking the dynamic array in this version
        for k in range (self._n):
            if self._A[k] == value:              # found a match!
                for j in range(k, self._n - 1):    # shift others to fill gap
                    self._A[j] = self._A[j+1]
                self._A[self._n - 1] = None        # help garbage collection
                self._n -= 1                       # we have one less item
                return                             # exit immediately
        raise ValueError('value not found')    # only reached if no match

    def removeAll(self, value):
        for i in range((self._n)):
            if value == self._A[i]:
                self.remove(value)
        return
        raise ValueError('value not found')
