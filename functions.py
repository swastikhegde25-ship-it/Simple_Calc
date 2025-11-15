# functions.py

current_expression = "" 

def evaluate_expression(expression):
    try:
        # eval() executes the string as a Python expression
        result = str(eval(expression))
        return result
    except ZeroDivisionError:
        return "Error: Div by zero"
    except Exception:
        return "Error"

def handle_button_press(value, display_var):
    # Ithis takes the button value and the StringVar to update the GUI.
    global current_expression
    
    if value == '⟳': 
        current_expression = ""
        display_var.set("")
        
    elif value == '=': 
            result = evaluate_expression(current_expression)
            current_expression = result 
            display_var.set(result)
            
    else: # takes the new value to the current expression
        current_expression += value
        display_var.set(current_expression)
