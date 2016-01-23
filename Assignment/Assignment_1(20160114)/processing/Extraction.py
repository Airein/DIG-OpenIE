import csv

class Extraction:
    def __init__(self, ipt):
        self.ipt = ipt

    def load_data(self, ipt):        
        input_data = open(ipt, 'rU')
        idx = 1
        data = []
        tmp = []
        for line in input_data:
            line = line.strip('\n')
            line = str(line)
            if idx == 6 or idx == 7 or idx == 8 or idx == 16:
                tmp.append(line)
            idx += 1
            if idx > 21:
                idx = 1
                # print tmp
                tmp = []
                data.append(tmp)
        return data


    def write_data(self, data):
        with open('test.csv', 'wb') as csvfile:
            spamwriter = csv.writer(csvfile,dialect='excel')
            for dt in data:
                spamwriter.writerow(dt)
            
if __name__ == '__main__':
    # ipt = sys.argv[1]
    ipt = "test.output"

    e = Extraction(ipt)
    data = e.load_data(ipt)
    e.write_data(data)
    