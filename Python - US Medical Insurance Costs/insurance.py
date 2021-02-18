import csv
import string
from operator import lt, le, eq, ne, gt, ge
letters = string.ascii_letters

class Insurance_Data:
    
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.age_data = []
        self.sex_data = []
        self.bmi_data = []
        self.children_data = []
        self.smoker_data = []
        self.region_data = []
        self.charges_data = []
        self.data = {}
        
    def __len__(self):
        return len(self.data)
    
    def __repr__(self):
        return repr(self.data)
        
    def get_csv_data(self):
        
        """Retrieves and cleans data from csv file
        
        Data is retrieved from csv using csv.DictReader and loaded to separate lists
        for formatting purposes--convert float and int values.
        """
        
        with open(self.csv_file) as csv_data:
            csv_contents = csv.DictReader(csv_data)
            fields = csv_contents.fieldnames
            
            key = 1

            for line in csv_contents:
                dict_value = {}
                for field in fields:
                    line_value = line[field]
                    line_value_type = None

                    for letter in letters:
                        if letter in line_value:
                            line_value_type = 'string'
                            break
                        elif letter not in line_value and '.' not in line_value:
                            line_value_type = 'int'
                        else:
                            line_value_type = 'float'

                    if line_value_type == 'int':
                        dict_value[field] = int(line_value)
                    elif line_value_type == 'float':
                        dict_value[field] = float(line_value)
                    else:
                        dict_value[field] = line_value
                self.data.update({key: dict_value})
                key = key + 1
            


    def search(self, charges_op=eq, bmi_op=eq, children_op=eq, age_op=eq, **search_criteria):
        
        """Allows searching of records based on kwargs as search criteria
        
        Returns a list of self.data.keys() where the kwargs criteria are true.
        For float and int values, the comparison operators are defaulted to eq 
        (==) unless updated (le, lt, ne, gt, ge).
        """
        
        results = {}
        
        for patient, record in self.data.items():
            criteria_match = 1
            for key, value in search_criteria.items():
                
                if type(value) is int or type(value) is float: # handles int and float comparison
                    if key == 'charges' and charges_op(record[key], value):
                        criteria_match *= 1
                    elif key == 'children' and children_op(record[key], value):
                        criteria_match *= 1
                    elif key == 'age' and age_op(record[key], value):
                        criteria_match *= 1
                    elif key == 'bmi' and bmi_op(record[key], value):
                        criteria_match *= 1
                    else:
                        criteria_match *= 0
                else: # for other data types
                    if record[key] == value:
                        criteria_match *= 1
                    else:
                        criteria_match *=0
            
            if criteria_match == 1:
                results.update({patient: record})
        
        return results
    
    def get_patient_data(self, patient_name):
        return self.data.get(patient_name)
    
    def count_frequency(self, **search_criteria):
        return len(self.filter_data(**search_criteria))
    
    def percent_of_total(self, **search_criteria):
        percent = self.count_frequency(**search_criteria) / self.record_count * 100
        return f'{percent}%'
    
    def calculate_total(self, record_key, data_dictionary=None):
        if data_dictionary == None:
            data_dictionary = self.data
        total = 0
        for item in data_dictionary.values():
            total += item.get(record_key)
        return total
    
    def calculate_average(self, record_key, data_dictionary=None):
        if data_dictionary == None:
            data_dictionary = self.data
        return self.calculate_total(record_key, data_dictionary) / len(data_dictionary)


my_data = Insurance_Data('insurance.csv')
my_data.get_csv_data()
print(my_data)