# --- FUNCIÓN DE PRUEBA ---
# Usamos una función simple, por ejemplo: f(x) = x^3 - 3x^2 + x - 1
# (La misma ecuación de la Pregunta 4 del examen)
def f(x):
    print(f"   -> [INVOCO A LA FUNCIÓN]: f(x) está calculando para x = {x}")
    return x**3 - 3*x**2 + x - 1


# --- EL CÓDIGO ORIGINAL SIN CAMBIOS ---
def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    x_prev = x0
    x_curr = x1
    iter_count = 0
    
    x_prev = f(x_prev)
    x_curr=f(x_curr)
    # El bucle original de la Pregunta 7 del examen
    while abs(f(x_curr)) > tol and iter_count < max_iter:
        print(f"\n=== ITERACIÓN {iter_count} ===")
        print(f" x_prev actual = {x_prev}")
        print(f" x_curr actual = {x_curr}")
        
        # Calculate the next approximation using the secant method formula
        x_next = x_curr - f(x_curr) * (x_curr - x_prev) / (f(x_curr) - f(x_prev))
        
        print(f" Nuevo x_next calculado = {x_next}")
        
        # Update variables for the next iteration
        x_prev = x_curr
        x_curr = x_next
        iter_count += 1
        
    return x_curr, iter_count


# --- EJECUCIÓN DEL SCRIPT ---
if __name__ == "__main__":
    # Usamos los puntos de inicio que menciona el Ejemplo 1 del examen: x0 = 2, x1 = 3
    x0_inicial = 2.0
    x1_inicial = 3.0
    
    print("Iniciando el Método de la Secante original...")
    print("Presta atención a cómo se repiten las llamadas con los mismos números de x:\n")
    
    raiz, total_iteraciones = secant_method(f, x0_inicial, x1_inicial)
    
    print("\n===============================================")
    print(f"Raíz final encontrada: {raiz}")
    print(f"Iteraciones ejecutadas: {total_iteraciones}")