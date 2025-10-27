
# By default r read mode is present 
p=open('C:/Users/Rishabh/OneDrive/Documents/demoFile.txt')
print(p.read())

x=open('Day2/lists.py')
print(x.read())

# here w means write it will create a file or overwrite the existing file  
# need to use close otherwise file will remain open 
y=open('Day3/demo.txt','w')
y.write("Hello Demo")
y.close()

y=open('Day3/demo.txt')
print(y.read())
y.close()

# a stands for append this will just add the content a the end will not overwrite things 

y=open('Day3/demo.txt','a')
y.write('New  content ')

#  x will create a file if it does not exist otherise if exist then throw error 

# y=open('Day3/demo.txt','x')
# y=open('Day3/demo1.txt','x')
# y.close()

y=open('Day3/demo1.txt','w')
y.write('New Content in demo1 ')

