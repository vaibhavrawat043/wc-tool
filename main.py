from wc import execute_operations

def parse_cmd(cmd: str):
    args = None

    if " " not in cmd:
        print("Invalid command")
        return

    args = cmd.split()
    command = None
    option = None
    file_name = None
    
    if len(args) >= 2 and len(args) < 4:

        if args[0] != "ccwc":
            print_error()

        command = args[0]
        if "." in args[1]:
            file_name = args[1]
        else:
            file_name = args[2]
            option = args[1]

        return (option, file_name)
    else:
        print_error()


def print_error():
    print("Invalid command")


if __name__ == "__main__":

    cmd = input(">")
    ops = parse_cmd(cmd)
    execute_operations(ops)
