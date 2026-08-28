# fixed size capacity
capacity = 3
stack = []
top = -1

# push logic functon
def push_item(element):
    global top
    if(top == capacity - 1):
        print(f"OVERFLOW ! stack is full. { element} don't push this element")
    else:
        top += 1
        stack.append(element)
        print(f"pushed : {element} | current top index: {top}")


# pop logic function
def pop_item():
    global top
    if( top == -1):
        print("UNDERFLOW! stack is allready empty")
    else:
        removed = stack.pop()
        top -= 1
        print(f"popped : {removed} | current top Index : {top}")

# test cases

push_item(10) # top = 0
push_item(20) # top = 1
push_item(30) # top = 2 (full)

#  push 4th item stack is full (stack overflow)
push_item(40)
print("current stack :", stack)