def file_transport():
    """
    Convert argv into array
    """
    from sys import argv
    name = []
    if(len(argv) == 1):
        print("Set arguments")
        exit()
    for i in range(len(argv)):
        if(i == 0):
            pass
        else:
            name.append(argv[i])
    return name[0]

def file_decode_commands(list1):
    """
    it decode commands
    works with commands_1() 
    """
    var = []
    last_var = []
    set_var = ''
    set_index_var = 0
    for i in range(len(list1)):
        has = list1[i]
        var, last_var, set_var, set_index_var = commands_1(has,var,last_var,set_var,set_index_var)
    return last_var

def open_file(arg):
    """
    open file and return list
    """
    files = open(arg,"r")
    loop = []
    for i in files:
        loop.append(i.rstrip())
    files.close()
    return loop

def commands_1(main,var,last_var,set_var,set_index_var):
    """
    standard commands input/output
    """
    main_split = main.split(' ',2)
    command = main_split[0]
    main_text = main_split[1]
    #plugin
    from plugin import plugin, empty
    if(empty() == False):
        var,last_var,set_var,set_index_var = plugin(command,main_text,var,last_var,set_var,set_index_var)
    
    


    if(command == 'SET'):
        try:
            before = var.index(main_text)
            if(type(before) == type(0)):
                set_var = main_text
                set_index_var = var.index(set_var)
        except ValueError:
            var.append(main_text)
            set_var = main_text
            set_index_var = var.index(set_var)
    elif(command == 'ADD'):
        main_text = float(main_text)
        end = True
        try:
            var[set_index_var+1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var+1] = (var[set_index_var+1] + int(main_text))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var+1] = (var[set_index_var+1] + float(main_text))
    elif(command == 'PRT'):
        before = var.index(main_text)
        last_var.append(str(var[before+1]))
    elif(command == 'SUB'):
        main_text = float(main_text)
        end = True
        try:
            var[set_index_var+1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var+1] = (var[set_index_var+1] - int(main_text))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var+1] = (var[set_index_var+1] - float(main_text))
    elif(command == 'MUL'):
        main_text = float(main_text)
        end = True
        try:
            var[set_index_var+1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var+1] = (var[set_index_var+1] * int(main_text))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var+1] = (var[set_index_var+1] * float(main_text))
    elif(command == 'DIV'):
        main_text = float(main_text)
        end = True
        try:
            var[set_index_var+1]
        except IndexError:
            if(type(main_text) == type(0)):
                var.append(int(main_text))
                end = False
            elif(type(main_text) == type(0.0)):
                var.append(float(main_text))
                end = False
        if(end == True):
            if(type(var[set_index_var+1]) == type(0)):
                var[set_index_var+1] = (var[set_index_var+1] / int(main_text))
            elif(type(var[set_index_var+1]) == type(0.0)):
                var[set_index_var+1] = (var[set_index_var+1] / float(main_text))
    
    return var,last_var,set_var,set_index_var

def print_something(something):
    """
    print lists
    """
    for i in something:
        print(i)


if(__name__ == "__main__"):
    commands=open_file(file_transport())
    print_something(file_decode_commands(commands))
    