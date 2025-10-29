#  decorator is a function which takes another function as an argument and extends the behaviour of the latter function without explicitly modifying it
#  like icing on a cake cake is a function  and icing is a decorator which adds more flavour to cake without modifying it

def decorate(func):
    def wrapper():
        print("This is my   cake before icing  ")
        func()
        print("This is my  cake after icing  ")
    return wrapper     


# @ is used for creating decorator 
@decorate
def hello():
    print("This is my orginal cake ")


hello()

# decorate function will take func as a parameter
def decoratedemo(func):
#     #  here wrapper will take all arguments in a func 
    def wrapper(a,b):
        print("Additon is processing...")
        func(a,b)
        print('Hope you liked it ')
    return wrapper
@decoratedemo
# whenevr additon is called then wrapper returns and stores in addition 
def addition(a,b):
    print(f"The sum is {a+b}")

addition(10,23)


#  Here we are using concept of args and kargs 
def decoratePractice(func):
    def wrapper(*args,**kwargs):
        print('Before Function ')
        func(*args,**kwargs)
        print('After function ')
    return wrapper

@decoratePractice
def multiple_para_addition(*args,**kwargs):
    sum=0
    if(args):
        for i in args:
            sum+=i
    if(kwargs):
        for i in kwargs:
            sum+=kwargs[i]
    print(sum)

multiple_para_addition(10,20,30,d=10,e=20)