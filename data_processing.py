import pandas

def import_file(csv):
    
    file = pd.read_csv(csv)
    print("Data was imported.")
    
    return file

def process_file(file):
    
    file = file[(file['output']=='Alumina')&(file['facility_type']=='Refinery')&(file['input']=='Nepheline ore, Limestone')]
    print("Data was filtered.")
    
    file = file.dropna(axis=1)
    print("Dropping empty columns.")
    
    file = file[['id', 'year', 'output_value_tonnes']]
    print("Year and production was selected for the output file.")
    
    ton_to_tonne_ratio = 1.1
    file['output_value_tonnes'] = file['output_value_tonnes'].values*ton_to_tonne_ratio
    print("Converting processing output from tonne to ton.")
    
    return file

def export_file(file):
       
    file.to_csv(r"C:\Users\pfaprado\Documents\GitHub\unit-testing\data\processing_deliverable.csv", encoding='latin-1')
    print("Creating output file.")
    
    return

raw_file = import_file(r"C:\Users\pfaprado\Documents\GitHub\unit-testing\data\processing.csv")
processed_file = process_file(raw_file)
export_file(processed_file)


#import pandas as pd

#file = pd.read_csv(r"C:\Users\pfaprado\Documents\GitHub\unit-testing\data\processing.csv")
#print("Data was imported.")

#file = file[(file['output']=='Alumina')&(file['facility_type']=='Refinery')&(file['input']=='Nepheline ore, Limestone')]
#print("Data was filtered.")

#file = file.dropna(axis=1)
#print("Dropping empty columns.")

#file = file[['id', 'year', 'output_value_tonnes']]
#print("Year and production was selected for the output file.")

#ton_to_tonne_ratio = 1.1
#file['output_value_tonnes'] = file['output_value_tonnes'].values*ton_to_tonne_ratio
#print("Converting processing output from tonne to ton.")

#file.to_csv(r"C:\Users\pfaprado\Documents\GitHub\unit-testing\data\processing_deliverable.csv", encoding='latin-1')
#print("Creating output file.")