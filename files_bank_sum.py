b= ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
f=open("file question3.txt","w")
f.write("kotak\nHDFC\nRBL\nSBI\nBank of Boroda")
f.close()

b= ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
f=open("file question3.txt","w")
i=0
while i <len(b):
    f.write(b[i]+"\n")
    i=i+1
    
# def fun(a):
#     b=a.split()
#     prin(b)
# my("my name")

list="my name"
b=list.split()
print(b)
