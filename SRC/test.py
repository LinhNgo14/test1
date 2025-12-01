class MyClass:
     "Đây là class thứ 2 được khởi tạo"
     a = 10
     def func(self):
        print('Xin chào')

# Output: 10
print(MyClass.a)

# Output: <function MyClass.func at 0x0000000003079BF8>
print(MyClass.func)

# Output: 'Đây là class thứ 2 được khởi tạo'
print(MyClass.__doc__)
