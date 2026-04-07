# def introduce(name, age):
#     return f'My name is {name} and I am {age} years old.'

# inp1 = input('Enter your name: ')
# inp2 = input('Enter your age: ')

# result = introduce(inp1,inp2)
# print(result)

data = [1, 2, 3, 4, 5, 6, 7, 8]
batch_size = 3

def batch_generator(batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

x = batch_generator(batch_size)
print(next(x))
