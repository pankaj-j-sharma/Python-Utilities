class Dictionary:
    def __init__(self):
        self.max=20
        self.arr=[None for i in range(self.max)]

    def get_hash(self,key):
        hash=0
        for chr in key:
            hash+=ord(chr)
        return hash%self.max

    def __getitem__(self,key):
        hash = self.get_hash(key)
        return self.arr[hash]

    def __setitem__(self,key,val):
        hash = self.get_hash(key)
        self.arr[hash] = val

    def __delitem__(self,key):
        hash = self.get_hash(key)
        self.arr[hash] = None

dct = Dictionary()
dct['name']='Pankaj'        
dct['last']='Sharma'
print(dct.arr)
del dct['last']
print(dct.arr)