#A four-digit integer is given. Find the number of odd digits in it.
a=int(input())
P=(a%10)%2
O=((a//10)%10)%2
L=((a//100)%10)%2
I=(a//1000)%2
#Create a variable "var_int" and assign it a four-digit integer value.
F=P+O+L+I
#Print the number of odd digits in the variable "var_int".
print(F)