import stack

prec={}
prec['+'] = 1
prec['-'] = 1
prec['*'] = 2
prec['/'] = 2

def evaluate(n1,n2,top):
    if top == '+':
        result=n1+n2
    elif top == '-':
        result=n1-n2
    elif top == '*':
        result=n1*n2
    else:
        result = n1/n2
    return result

op_stack = stack.Stack()
num_stack = stack.Stack()

expression = input('Enter expression: ')

terms = list(expression)

for term in terms:
    if term not in ['+','-','/','*']:
        num_stack.push(int(term))
    else:
        done = False
        while not done:
            top = op_stack.top()
            if top == None:
                op_stack.push(term)
                done = True
            elif (prec[term] > prec[top]):
                op_stack.push(term)
                done=True
            else:
                n2 = num_stack.pop()
                n1 = num_stack.pop()
                top = op_stack.pop()
                result = evaluate(n1,n2,top)
                num_stack.push(result)
done=False
while not done:
    top = op_stack.pop()
    if top == None:
        done = True
    else:
        n2 = num_stack.pop()
        n1 = num_stack.pop()
        result = evaluate(n1,n2,top)
        num_stack.push(result)

print('result = ' + str(num_stack.pop()))
    
