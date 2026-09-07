# Operation on comparison values
a=10
print(a>7)
print(4==7)
print(4!=7)
print(10>=7)
info="first print shows greater than 7, second print shows 4 is not equal to 7, third print shows 4 is not equal to 7, fourth print shows 10 is greater than or equal to 7"
print(5>=7)
print(a<=20)
Info="fifth print shows 5 is not greater than or equal to 7, sixth print shows 10 is less than or equal to 20"

#Based on ASCII values  
print("aB">"ab")
INFO="The skipping of the first character in the comparison is done based on the ASCII value of the characters. The ASCII value of 'a' is 97 and 'A' is 65. Since 65 is less than 97, 'A' is considered less than 'a'. Therefore, 'aB' is greater than 'ab' because the first character 'a' is greater than 'A'."
print("aB"<"ab")
info2="the skipping of first character is same as a is at both place so we move to the next character and compare B and b. The ASCII value of 'B' is 66 and 'b' is 98. Since 66 is less than 98, 'B' is considered less than 'b'. Therefore, 'aB' is less than 'ab' because the second character 'B' is less than 'b'."
#A=65,B=66,C=67,D=68,E=69,F=70,G=71,H=72,I=73,J=74,K=75,L=76,M=77,N=78,O=79,P=80,Q=81,R=82,S=83,T=84,U=85,V=86,W=87,X=88,Y=89,Z=90
# a=97,b=98 ,c=99,d=100,e=101,f=102,g=103,h=104,i=105,j=106,k=107,l=108,m=109,n=110,o=111,p=112,q=113,r=114,s=115,t=116,u=117,v=118,w=119,x=120,y=121,z=122


#Logical operators
a=" "
b=None
print(bool(a))
print(bool(b or a))
print(bool(b and True))
print(bool(not(" " and True or False and" " or None and (0 or " " and 1) or True and 0)))
Info3="The first print statement evaluates the boolean value of the variable 'a', which is a non-empty string, so it returns True. The second print statement evaluates the boolean value of the expression 'b or a', which returns True because 'a' is a non-empty string. The third print statement evaluates the boolean value of the expression 'b and True', which returns False because 'b' is None. The fourth print statement evaluates a complex logical expression, which ultimately returns False."
Info4="The fourth print statement evaluates the boolean value of the expression 'not(" " and True or False and" " or None and (0 or " " and 1) or True and 0)'. The expression inside the 'not' operator is evaluated as follows: ' " " and True' evaluates to True, 'False and" " evaluates to False, 'None and (0 or " " and 1)' evaluates to None, and 'True and 0' evaluates to 0. Therefore, the entire expression evaluates to True, and the 'not' operator negates it to return False." 