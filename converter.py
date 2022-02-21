import csv
class CSVConverter:

    def __init__(self, filename):
        self.filename = filename
        self.data = []
        try:
            with open(filename, 'r') as read_obj:
                reader = csv.reader(read_obj)
                self.data = list(reader)
                read_obj.close()
        except:
            print("No filename Found")

    def GetData(self):
        return self.data

    def CreateData(self):
        fields = ["Item","Quantity","Price"]
        self.filename
        with open(self.filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = fields)
            writer.writeheader()
            csvfile.close()




