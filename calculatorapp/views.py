from django.shortcuts import render
import re
import math
# Create your views here.
def standard_calculator(request):
    expression = ''
    result = ''
    if request.method == 'POST':
        expression = request.POST.get('expression', '')
        try:
            if re.fullmatch(r'[0-9+\-*/(). ]+', expression):
                result = eval(expression)
            else:
                result = 'Invalid input'
        except:
            result = 'Error'
    return render(request, 'standard.html', {'expression': expression, 'result': result})

# Scientific calculator view
def scientific(request):
    expression = ''
    result = ''
    error = ''

    if request.method == 'POST':
        expression = request.POST.get('expression', '')

        # Allow only safe characters (digits, operators, letters, parentheses, dots, spaces)
        if not re.fullmatch(r"[0-9+\-*/().^√πe\sA-Za-z]+", expression):
            error = "Invalid characters in expression"
        else:
            try:
                # Replace user-friendly tokens with Python equivalents
                safe_expr = expression.replace('^', '**') \
                                      .replace('√', 'math.sqrt') \
                                      .replace('π', 'math.pi') \
                                      .replace('e', 'math.e') \
                                      .replace('sin', 'math.sin') \
                                      .replace('cos', 'math.cos') \
                                      .replace('tan', 'math.tan') \
                                      .replace('log', 'math.log')

                # Evaluate expression safely
                result = eval(safe_expr, {'__builtins__': None, 'math': math})
            except Exception as e:
                error = f"Error: {str(e)}"

    context = {
        'expression': expression,
        'result': result,
        'error': error,
    }
    return render(request, 'scientific.html', context)
def home(request):
    return render(request, "home.html")