def backtrack(path):
     
     if len(path) == 3:
        print(path)
        return
     
     for i in range(1,4):
        path.append(i)
        backtrack(path)
        path.pop()

backtrack([])