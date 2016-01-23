

def load_rv_data(filename):
    reverb_file = open(filename, 'rU')
    for line in reverb_file:
        # row = str(line)
        line = line.split('\t')
        print line
