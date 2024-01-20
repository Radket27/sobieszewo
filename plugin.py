def plugin(command,main_text,var,last_var,set_var,set_index_var,code,location,set_logical,end_logical):
    """
    Here you can add additional commands
    [input]
    command - name of command e.g. 'ADD' 5;
    main_text - value of command e.g. ADD '5';
    var - returns the entire list of variables;
    last_var - it is a list of data that will be displayed on output;
    set_var - returns selected variable;
    set_index_var - returns the location of the variable data;
    code - returns whole code;
    location - returns number of line of code;
    set_logical - returns name of logical variable;
    end_logical - returns a value whether to skip 'else' (ELS);
    """
    if(command == 'example'):
        pass
    return var,last_var,set_var,set_index_var,code,location,set_logical,end_logical

def empty():
    empty = True #change this to False if you want to use plugin
    return empty