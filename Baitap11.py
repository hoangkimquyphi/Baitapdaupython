#bai2
mu = 1
dau = 1
first = 1
second = first + dau * ((((first+1)*(first+2))/2)*x**mu)
while (math.fabs(first - second) > eps):   
    mu += 1
    dau = -dau
    first = second
    second = first + dau * ((((first+1)*(first+2))/2)*x**mu)
print(first)

# Bai3 
mu = 1
first = - 1
second = first - (x**mu)/mu
while (math.fabs(first - second) > eps):   
    mu += 1
    first = second
    second = first - (x**mu)/mu
print(first)

# bai4
mu = 1
dau = 1
first = 1
second = first + dau * tichle(mu * 2 - 2)/ tichchan(mu * 2) * x**mu
while (math.fabs(first - second) > eps):   
    mu += 1
    dau = -dau
    first = second
    second = first + dau * tichle(mu * 2 - 2)/ tichchan(mu * 2) * x**mu
print(first)

# Bai5
mu = 1
dau = 1
first = -1
second = first + dau * tichle(mu * 2 - 2)/ tichchan(mu * 2) * x**mu
while (math.fabs(first - second) > eps):   
    mu += 1
    dau = -dau
    first = second
    second = first + dau * tichle(mu * 2 - 2)/ tichchan(mu * 2) * x**mu
print(first)

# Bai6
mu = 1
dau = -dau
first = x
second = first + dau*(x**mu)/factorial(mu)
while (math.fabs(first - second) > eps):   
    mu += 2
    dau = dau
    first = second
    second = first + dau*(x**mu)/factorial(mu)
print(first)

# Bai7
mu = 1
dau = -dau
first = 1
second = first + dau*(x**mu)/factorial(mu)
while (math.fabs(first - second) > eps):   
    mu += 2
    dau = dau
    first = second
    second = first + dau*(x**mu)/factorial(mu)
print(first)

# Bai8
mu = 3
first = x
second = first * tichle(mu - 2)/ tichchan(mu - 1) * x**mu / mu
while (math.fabs(first - second) > eps):   
    mu += 2
    first = second
    second = first * tichle(mu - 2)/ tichchan(mu - 1) * x**mu / mu  
print(first)

# Bai9
mu = 1
dau = -dau
first = 1
second = first + dau*(x**mu)/factorial(mu+1)
while (math.fabs(first - second) > eps):   
    mu += 2
    dau = dau
    first = second
    second = first + dau*(x**mu)/factorial(mu+1)
print(first)


#Bai10
mu = 1
dau = 1
first = 0
second = first + dau * x ** mu / mu
while (math.fabs(first - second) > eps):   
    mu += 2
    dau = -dau
    first = second
    second = first + dau * math.pow(x,mu) / mu
print( first)

# Bai 11
mu = 1
dau = -dau
first = x
second = first + dau*(x**mu)/factorial(mu)
while (math.fabs(first - second) > eps):   
    mu += 1
    dau = dau
    first = second
    second = first + dau*(x**mu)/factorial(mu)
print(first)
# Bai 12
mu = 1
first = 1
second = 2 * (first * (mu + 2) * x**mu / mu)
while (math.fabs(first - second) > eps):   
    mu += 2
    first = second
    second = 2 * (first * (mu + 2) * x**mu / mu)
print(first)