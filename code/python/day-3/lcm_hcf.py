a=[]
print("Enter Four Numbers")
for i in range(1, 5):
        a.append(int(input()))

    
def hcf_of_nums(x,y):
        for i in range(1,max(x,y)+1):
            if (x%i==0 and y%i==0):
                hcf=i
        return hcf

def lcm_of_nums(a, b):
        gcd = hcf_of_nums(a,b)
        lcms = (a*b)/gcd
        return int(lcms)

hcf=a[0]
lcm=a[0]
    
for i in range(0,len(a)):
        hcf=hcf_of_nums(hcf,a[i])
        lcm=lcm_of_nums(lcm,a[i])

    
print('HCF: '+str(hcf))
print('LCM: '+str(lcm))