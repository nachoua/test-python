
num1=float(input("enter the first number : ")) 
num2=float(input("enter the second number :")) 

def Add(num1, num2):
	return float(num1) +float(num2)



def Mul(num1, num2):
	return float(num1)*float(num2)


def Sub(num1, num2):
	return float(num1)-float(num2)


def Div(num1, num2):
  return float(num1)/float(num2) 

choose=float(input(print("please enter you'are operation number : ")))  #for know what is the operation mode (sum or multip or div ...) 

if (choose == 1 ):

		print("the result for Addition is :" ,Add(num1, num2))
        
elif (choose == 2):

		print("the result for Multiplication is :" ,Mul(num1, num2))


elif (choose == 3):

		print("the result is Subtraction:" ,Sub(num1, num2))
		

elif (choose == 4):

		print("the result Division is :" ,Div(num1, num2))
	
