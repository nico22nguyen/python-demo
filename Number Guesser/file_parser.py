def parse_file(file_name):
    #open file
    raw_data = open(file_name, "r")

    #transform file into list of lines
    lines = raw_data.read().splitlines()
    raw_data.close()

    #set up data and label lists
    data = []
    labels = []

    #parse each line
    for line in lines:
        input_line = []                     #temporary list for data (since data is a list of lists)
        for digit in line[:256]:
            input_line.append(int(digit))   #populate single set of data
        data.append(input_line)             #add set to list of all datasets
        
        output_line = []                    #temporary list for labels (since labels is a list of lists)
        for digit in line[256:]:
            output_line.append(int(digit))  #populate single set of data
        labels.append(output_line)          #add set to list of all labels
    
    #return list with data at index 0 and labels at index 1
    return [data, labels]

def parse_file_no_label(file_name):
    #open file
    raw_data = open(file_name, "r")

    #transform file into list of lines
    lines = raw_data.read().splitlines()
    raw_data.close()

    #set up data and label lists
    data = []
    labels = []

    #parse each line
    for line in lines:
        input_line = []                     #temporary list for data (since data is a list of lists)
        for digit in line:
            input_line.append(int(digit))   #populate single set of data
        data.append(input_line)             #add set to list of all datasets
    
    return data

def parse_csv(file_name):
    #open file
    raw_data = open(file_name, "r")

    #transform file into list of lines
    lines = raw_data.read().splitlines()
    raw_data.close()

    #set up data and label lists
    data = []
    labels = []

    #parse each line
    for line in lines:
        target_as_vector = []               #temp list for vector
        for i in range(0, 10):
            if i == int(line[0]):
                target_as_vector.append(1)  #push 1 on the correct dimension
            else:
                target_as_vector.append(0)  #push 0 on all others
        labels.append(target_as_vector)     #add vector to labels
        
        input_line = []                     #temp list to hold all values
        for val in line[2:].split(','):
            input_line.append(int(val))     #add values as ints
        data.append(input_line)             #add temp list to data
    
    #return list with data at index 0 and labels at index 1
    return [data, labels]