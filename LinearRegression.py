x=[10,12,2,0,8,5]
y=[70,65,96,94,75,82]
x2=[]
for i in x:
    x2.append(i*i)
xy=[]
for i in range(len(x)):
    xy.append(x[i]*y[i])
ssxx = sum(x2) - sum(x)*sum(x)/len(x)
ssxy = sum(xy) - sum(x)*sum(y)/len(x)
beta1 = ssxy/ssxx
beta0 = sum(y)/len(y) - beta1*sum(x)/len(x)
print("the line corresponding to the given data set is : y = "+str(beta1)+"x + "+str(beta0) )
x = int(input("Enter x to predict y"))
print("y = "+str(beta1*x+beta0))
