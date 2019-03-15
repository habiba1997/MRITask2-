with open("test.txt", "rb") as fp:   # Unpickling
     b = pickle.load(fp)    

t2 = b.pop()
t1= b.pop()
phantomm = b.pop