
def execute_operations(ops):
    # -m -l -c  -w
    if ops[0] == "-m":
        get_characters(ops)
    elif ops[0] == "-l":
        get_lines(ops[1])
    elif ops[0] == "-c":
        get_size(ops[1])
    elif ops[0] == "-w":
        get_words(ops[1])
    else:
        get_lines(ops[1])
        get_words(ops[1])
        get_size(ops[1])


def get_characters(ops):
    
    with open(ops[1],'+rb') as file:
        content = file.read().decode()
        print(len(content))

def get_words(file_name):
    words=0
    with open(file_name, 'r') as f:
        data=f.read()
        lines=data.split()
        words+=len(lines)
        print(words)

def get_lines(file_name):
    with open(file_name, 'r') as f:
        print(len(f.readlines()))

def get_size(file_name):

    import os
    print(os.path.getsize(file_name))