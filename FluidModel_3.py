import math
import numpy as np
import matplotlib.pyplot as plt

cos = math.cos
pi = math.pi
Gamma = 1.4
G = Gamma + 1
g = Gamma - 1
A_0 = 0.01
r = 0.01
w = pi/3
R_1 = 2*r
R_2 = 5*r
Theta_2 = 10/180*pi
T_0 = 50
p_0 = 10*(10)**5
A = -10
B = 10
di = 0.0001
dx = 0.0001

"""def A_from_x_Values(x, a = -10, b = 10):
		if x <= 0:
			return f_left(x)
		#print('left: ', f_left(i))
		else:
			return f_right(x)

#def f_left(x, A = r/2.0, B = r):
#	return r/2.0 * (1 - cos(w*x)) + r

#def f_right(x, A = Theta_2, B = r):
#	return Theta_2 * x + r"""

# x == M:

def A_from_M_pure(x):
	if x != 0:
		return ((2/G)**(G/(2*g)) * 1/x * (1 + (g/2)*x**2)**(G/(2*g)))
	
		#((2/G)**(G/(2*g)) * 1/x * (1 + (g/2)*x**2)**(G/(2*g)))

	else:
		return ((2/G)**(G/(2*g)) * 1/0.0001 * (1 + (g/2)*0.000001*0.000001)**(G/(2*g)))
	#else:
	#	return None

def A_from_M(x):
	if -3 < x <= 0:
		return (1/x * (2/G)**(G/(2*g)) * (1 + (g/2)*x*x)**(G/(2*g)) - (r/2.0 * (1 - cos(w*x)) + r)/A_0)
	elif x <= -3:
		return (1/x * (2/G)**(G/(2*g)) * (1 + (g/2)*x*x)**(G/(2*g)) - R_1)
	elif x >= 3:
		return (1/x * (2/G)**(G/(2*g)) * (1 + (g/2)*x*x)**(G/(2*g)) - R_2)
	else: 
		return (1/x * (2/G)**(G/(2*g)) * (1 + (g/2)*x*x)**(G/(2*g)) - (Theta_2 * x + r)/A_0)

def u_from_M(x):
	if G and x != 0:	 
		return (x*(2/G * (1 + g/2*x*x))**(-2)) 
	else:
		return (x*(2/G * (1 + g/2*x*x))**(-2))

def p_from_M(x):

	return (2/G * (1 + (g/2)*x*x))**(-Gamma/g)

def T_from_M(x):

	return (2/G*(1 + (g/2)*x*x))**(-1)


def Dichotomy(f, a, b, eps = 0.000000000000001):
	while abs(b - a) > eps:
		M = (a + b)/2
		fx = f(M)
		fa = f(a)
		#print('M = ', M, '\n', 'fx = ', fx, '\n', 'fa = ', fa)
		if (fx < 0 and fa < 0) or (fx > 0 and fa > 0):
			a = M

		else:
			b = M

	return abs(M)



#def Plot_A_from_M()

Solutions_for_M = []
for i in np.arange(A, B, di):		
	Solutions_for_M.append(Dichotomy(A_from_M, i, i + dx))
	#print('A = ', i, '\n', 'B = ', i + dx)
print(("M_i values :", '\n',Solutions_for_M))


A_from_M_Values = []
for k in Solutions_for_M:
	if A_from_M_pure(k) < 1000:
	#if A_from_M_pure(k) != 0:
		A_from_M_Values.append(A_from_M_pure(k))
	#print('==', A_from_M_Values)
	else:
		A_from_M_Values.append(A_from_M_pure(10))

#print("A(M) values :", '\n', A_from_M_Values)
print(Dichotomy(A_from_M_pure, A, B))
#####################################
X_Values = []
for j in np.arange(A, B, di):
	X_Values.append(j)

T_from_M_Values = []
for j in X_Values:
	T_from_M_Values.append(T_from_M(j))

p_from_M_Values = []
for l in X_Values:
	p_from_M_Values.append(p_from_M(l))

#print(len(A_from_M_Values))
#print(len(Solutions_for_M))

fig, axs = plt.subplots(2, 2)

axs[0,0].plot(Solutions_for_M, A_from_M_Values)
axs[0,0].set_title("A(M)/A* from M")
#plt.ylabel("A(M)/A*")
#plt.xlabel("M")
axs[1,0].plot(Solutions_for_M, p_from_M_Values)
axs[1,0].set_title("p/p*(M)")

axs[0,1].plot(Solutions_for_M, T_from_M_Values)
axs[0,1].set_title("T/T*(M)")

axs[1,1].plot(X_Values, Solutions_for_M)
axs[1,1].set_title("M(x)")

plt.show()



