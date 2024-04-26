import matplotlib.pyplot as plt
from diffeq import solve_diffeq_2cc

h0 = 100
steps = 1000
t = 100

lambda1 = lambda t: t
lambda2 = lambda t: t

plt.figure(figsize=(8, 6))
sol = solve_diffeq_2cc(t, steps, h0, lambda1, lambda2)
plt.plot(sol.t, sol.y[0])

plt.xlabel('t')
plt.ylabel('h(t)')
plt.title('Solution of dh/dt for different x at t=0')
#plt.savefig('1.png')
plt.show()