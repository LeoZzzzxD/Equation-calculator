import sympy as sp
import numpy as np

Filename = "func_data.txt"

def deriv(x, prepared_func, e):
    return ((prepared_func(x + e) - prepared_func(x - e)) / (2 * e))
    
def deriv2(x, prepared_func, e):
    return ((prepared_func(x + 2*e) - 2 * prepared_func(x) + prepared_func(x - 2*e) / (4 * e ** 2)))

def alg(*args):
    try:
        np.seterr(all='raise') 
        results_x = list()
        results_y = list()
        prepared_func = sp.lambdify("x", sp.parse_expr(args[2]), "numpy")
        x_until = args[0]
        x = x_until
        results_x.append(x)
        #if abs(prepared_func(x_until) * deriv2(x_until, prepared_func=prepared_func, e=args[1])) / (deriv(x_until, prepared_func=prepared_func, e=args[1]) ** 2) >= 1:
              #return "error", 1
        while True:
            
            x_until = x
            x = x_until - (prepared_func(x_until) / deriv(x_until, prepared_func=prepared_func, e=args[1]))
            results_x.append(x)
            if prepared_func(x) == 0 or (abs(prepared_func(x)) <= args[1] and abs(x - x_until) <= args[1]) or abs((prepared_func(x) - prepared_func(x_until)) / deriv(x, prepared_func=prepared_func, e=args[1])) <= args[1]:
                break 
        
        for value in results_x:
            results_y.append(prepared_func(value))
            
        write_data(results_x, results_y)
        return x, prepared_func
    
    except  FloatingPointError:
        return 1
    except TypeError:
        return "error_", 1
    except Exception:
        return 1

def write_data(x, y):
    
    with open(Filename, "w") as file:
       
       file.write("x: ")
       for value in x:
           file.write(str('{:.4f}'.format(value) + " "))
       
       file.write("\n")
       file.write("y: ")
       for value in y:
           file.write(str('{:.4f}'.format(value) + " "))
