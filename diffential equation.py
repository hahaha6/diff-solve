# from sympy.abc import x
# from sympy import diff, dsolve, simplify, Function
# y = Function('y')
# eq = diff(y(x), x,2)+2 * diff(y(x),x) +2*y(x)
# con = {y(0): 0, diff(y(x), x).subs(x, 0):1}
# y = dsolve(eq, ics = con)
# print(simplify(y))
# from sympy.abc import x
# from sympy import Function, diff, dsolve, sin
# y = Function('y')
# eq = diff(y(x),x,2)+2*diff(y(x),x)+2*y(x)-sin(x)
# con = {y(0):0,diff(y(x),x).subs(x,0):1}
# y = dsolve(eq, ics = con)
# print(y)
# import sympy as sp
# t = sp.symbols('t')
# x1,x2,x3 = sp.symbols('x1,x2,x3',cls = sp.Function)
# eq = [x1(t).diff(t)-2*x1(t)+3*x2(t)-3*x3(t),
#       x2(t).diff(t)-4*x1(t)+5*x2(t)-3*x3(t),
#       x3(t).diff(t)-4*x1(t)+4*x2(t)-2*x3(t)]
# con={x1(0):1, x2(0):2,x3(0):3}
# s = sp.disolve(eq, ics = con)
# print(s)
import sympy as sp
t = sp.symbols('t')
x1,x2,x3 = sp.symbols('x1:4',cls = sp.Function)
x = sp.Matrix([x1(t),x2(t),x3(t)])
A = sp.Matrix([[2,-3,3],[4,-5,3],[4,-4,2]])
eq = x.diff(t)-A*x
s = sp.dsolve(eq,ics = {x1(0):1, x2(0):2,x3(0):3})
print(s)
