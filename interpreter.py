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
    i = 0
    set_logical = ''
    end_logical = False
    while(i < len(list1)):
        has = list1[i]
        var, last_var, set_var, set_index_var, list1, set_logical, end_logical = commands_1(has,var,last_var,set_var,set_index_var,list1,i,set_logical, end_logical)
        i += 1
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

def commands_1(main,var,last_var,set_var,set_index_var,code,location,set_logical,end_logical):
    """
    standard commands input/output
    """
    main_split = main.split(' ',2)
    command = main_split[0]
    main_text = main_split[1]
    #plugin
    from plugin import plugin, empty
    if(empty() == False):
        var,last_var,set_var,set_index_var,code,location,set_logical,end_logical = plugin(command,main_text,var,last_var,set_var,set_index_var,code,location,set_logical,end_logical)

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
        try:
            main_text = float(main_text)
        except ValueError:
            main_text = str(main_text)
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
            elif(type(main_text) == type("A")):
                if(type(var[(var.index(main_text))+1]) == type(0)):
                    var.append(int(var[(var.index(main_text))+1]))
                    end = False
                elif(type(var[(var.index(main_text))+1]) == type(0.0)):
                    var.append(float(var[(var.index(main_text))+1]))
                    end = False
        if(end == True):
            try:
                if(type(var[set_index_var+1]) == type(0)):
                    var[set_index_var+1] = (var[set_index_var+1] + int(main_text))
                elif(type(var[set_index_var+1]) == type(0.0)):
                    var[set_index_var+1] = (var[set_index_var+1] + float(main_text))
            except ValueError:
                if(type(var[(var.index(main_text))+1]) == type(0)):
                    var[set_index_var+1] = (var[set_index_var+1] + int(var[(var.index(main_text))+1]))
                elif(type(var[(var.index(main_text))+1]) == type(0.0)):
                    var[set_index_var+1] = (var[set_index_var+1] + float(var[(var.index(main_text))+1]))
    elif(command == 'PRT'):
        before = var.index(main_text)
        last_var.append(str(var[before+1]))
    elif(command == 'NPRT'):
        before = var.index(main_text)
        print(str(var[before+1]))
    elif(command == 'SUB'):
        try:
            main_text = float(main_text)
        except ValueError:
            main_text = str(main_text)
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
            elif(type(main_text) == type("A")):
                if(type(var[(var.index(main_text))+1]) == type(0)):
                    var.append(int(var[(var.index(main_text))+1]))
                    end = False
                elif(type(var[(var.index(main_text))+1]) == type(0.0)):
                    var.append(float(var[(var.index(main_text))+1]))
                    end = False
        if(end == True):
            try:
                if(type(var[set_index_var+1]) == type(0)):
                    var[set_index_var+1] = (var[set_index_var+1] - int(main_text))
                elif(type(var[set_index_var+1]) == type(0.0)):
                    var[set_index_var+1] = (var[set_index_var+1] - float(main_text))
            except ValueError:
                if(type(var[(var.index(main_text))+1]) == type(0)):
                    var[set_index_var+1] = (var[set_index_var+1] - int(var[(var.index(main_text))+1]))
                elif(type(var[(var.index(main_text))+1]) == type(0.0)):
                    var[set_index_var+1] = (var[set_index_var+1] - float(var[(var.index(main_text))+1]))
    elif(command == 'MUL'):
        try:
            main_text = float(main_text)
        except ValueError:
            main_text = str(main_text)
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
            elif(type(main_text) == type("A")):
                if(type(var[(var.index(main_text))+1]) == type(0)):
                    var.append(int(var[(var.index(main_text))+1]))
                    end = False
                elif(type(var[(var.index(main_text))+1]) == type(0.0)):
                    var.append(float(var[(var.index(main_text))+1]))
                    end = False
        if(end == True):
            try:
                if(type(var[set_index_var+1]) == type(0)):
                    var[set_index_var+1] = (var[set_index_var+1] * int(main_text))
                elif(type(var[set_index_var+1]) == type(0.0)):
                    var[set_index_var+1] = (var[set_index_var+1] * float(main_text))
            except ValueError:
                if(type(var[(var.index(main_text))+1]) == type(0)):
                    var[set_index_var+1] = (var[set_index_var+1] * int(var[(var.index(main_text))+1]))
                elif(type(var[(var.index(main_text))+1]) == type(0.0)):
                    var[set_index_var+1] = (var[set_index_var+1] * float(var[(var.index(main_text))+1]))
    elif(command == 'DIV'):
        try:
            main_text = float(main_text)
        except ValueError:
            main_text = str(main_text)
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
            elif(type(main_text) == type("A")):
                if(type(var[(var.index(main_text))+1]) == type(0)):
                    var.append(int(var[(var.index(main_text))+1]))
                    end = False
                elif(type(var[(var.index(main_text))+1]) == type(0.0)):
                    var.append(float(var[(var.index(main_text))+1]))
                    end = False
        if(end == True):
            try:
                if(type(var[set_index_var+1]) == type(0)):
                    var[set_index_var+1] = (var[set_index_var+1] / int(main_text))
                elif(type(var[set_index_var+1]) == type(0.0)):
                    var[set_index_var+1] = (var[set_index_var+1] / float(main_text))
            except ValueError:
                if(type(var[(var.index(main_text))+1]) == type(0)):
                    var[set_index_var+1] = (var[set_index_var+1] / int(var[(var.index(main_text))+1]))
                elif(type(var[(var.index(main_text))+1]) == type(0.0)):
                    var[set_index_var+1] = (var[set_index_var+1] / float(var[(var.index(main_text))+1]))
    elif(command == 'MOR'):
        try:
            main_text = float(main_text)
            if(main_text < float(var[set_index_var+1])):
                end_logical = True
        except ValueError:
            main_text = str(main_text)
            if(float(var[(var.index(main_text))+1]) < float(var[set_index_var+1])):
                end_logical = True
        if(end_logical == False):
            i = location
            while((code[i] != (f'ELS {set_logical}')) or (code[i] != f'SEE {set_logical}')):
                code.pop(i)
                if(code[i] == f'ELS {set_logical}' or code[i] == f'SEE {set_logical}'):
                    break
    elif(command == 'MOQ'):
        try:
            main_text = float(main_text)
            if(main_text <= float(var[set_index_var+1])):
                end_logical = True
        except ValueError:
            main_text = str(main_text)
            if(float(var[(var.index(main_text))+1]) <= float(var[set_index_var+1])):
                end_logical = True
        if(end_logical == False):
            i = location
            while((code[i] != (f'ELS {set_logical}')) or (code[i] != f'SEE {set_logical}')):
                code.pop(i)
                if(code[i] == f'ELS {set_logical}' or code[i] == f'SEE {set_logical}'):
                    break
    elif(command == 'SML'):
        try:
            main_text = float(main_text)
            if(main_text > float(var[set_index_var+1])):
                end_logical = True
        except ValueError:
            main_text = str(main_text)
            if(float(var[(var.index(main_text))+1]) > float(var[set_index_var+1])):
                end_logical = True
        if(end_logical == False):
            i = location
            while((code[i] != (f'ELS {set_logical}')) or (code[i] != f'SEE {set_logical}')):
                code.pop(i)
                if(code[i] == f'ELS {set_logical}' or code[i] == f'SEE {set_logical}'):
                    break
    elif(command == 'SMQ'):
        try:
            main_text = float(main_text)
            if(main_text >= float(var[set_index_var+1])):
                end_logical = True
        except ValueError:
            main_text = str(main_text)
            if(float(var[(var.index(main_text))+1]) >= float(var[set_index_var+1])):
                end_logical = True
        if(end_logical == False):
            i = location
            while((code[i] != (f'ELS {set_logical}')) or (code[i] != f'SEE {set_logical}')):
                code.pop(i)
                if(code[i] == f'ELS {set_logical}' or code[i] == f'SEE {set_logical}'):
                    break
    elif(command == 'EQL'):
        try:
            main_text = float(main_text)
            if(main_text == float(var[set_index_var+1])):
                end_logical = True
        except ValueError:
            main_text = str(main_text)
            if(float(var[(var.index(main_text))+1]) == float(var[set_index_var+1])):
                end_logical = True
        if(end_logical == False):
            i = location
            while((code[i] != (f'ELS {set_logical}')) or (code[i] != f'SEE {set_logical}')):
                code.pop(i)
                if(code[i] == f'ELS {set_logical}' or code[i] == f'SEE {set_logical}'):
                    break
    elif(command == 'IFF'):
        set_logical = main_text
    elif(command == 'ELS'):
        if(end_logical == True):
            i = location
            end1 = False
            while(code[i] != f'SEE {set_logical}'):
                code.pop(i)
                if(code[i] == f'SEE {set_logical}'):
                    break
    elif(command == 'GOT'):
        before = int(main_text)
        x = location - before
        for i in range(x+1):
            code.insert(location+1+i,code[before+i])
    elif(command == 'SEE'):
        end_logical = False
    elif(command == 'NTEX'):
        print(str(main_text))
    return var,last_var,set_var,set_index_var,code,set_logical,end_logical

def print_something(something):
    """
    print lists
    """
    for i in something:
        print(i)


if(__name__ == "__main__"):
    commands=open_file(file_transport())
    print_something(file_decode_commands(commands))
    