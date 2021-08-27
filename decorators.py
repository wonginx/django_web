#
#
def decorator(func):
    def decorated(input_text):
        print('함수 시작!')
        func(input_text)
        print('함수 끝!')
    return decorated

# helloworld 사용X
@decorator
def hello_world(input_text):
    print(input_text)


hello_world('Hello World!')
#
# def decorator(func):
#     def decorated(input_text):
#         a, b = map(int, input("a, b 값 >").split())
#         result = 0
#         if a > 0 and b > 0:
#             func(module3())
#             func(module4())
# def module3(a, b):
#     result = (a*b/2)
#     return result
#
# def module4(a, b):
#     result = a*b
#     return result
# ----answer
# def check_integer(func):
#     def decorated(width, height):
#         if width >= 0 and height >= 0:
#             return func(width, height)
#         else :
#             raise ValueError('input must be positive value')
#     return decorated
#
#
#
# @check_integer
# def rect_area(width, height):
#     return width * height

