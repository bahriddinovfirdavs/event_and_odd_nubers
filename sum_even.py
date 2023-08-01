#A four-digit integer is given. Find the sum of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value

#Create a variable "sum_even" and assign it 0.

#Find the sum of the even digits in the variable "var_int".
n=int(input())
s=0
x1=n%10
s+=x1*(1-x1%2)
n//=10

x2=n%10
s+=x2*(1-x2%2)
n//=10

x3=n%10
s+=x3*(1-x3%2)
n//=10

x4=n%10
s+=x4*(1-x4%2)
n//=10
print(s)