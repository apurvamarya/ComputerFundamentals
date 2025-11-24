def simple_intrest(p, r, t):
    #computes simple intrest for principal p, rate r, time t
    return p*r*t / 100

#Use the Function
p = int(input("Principal: "))
r = float(input("Rate %: "))
t = float(input("Time (years): "))
print("Intrest = ", simple_intrest(p, r, t))


#FUNCTIONS PACKAGE LOGIC. THEY IMPROVE REUSE, TESTING AND REDABLITY
