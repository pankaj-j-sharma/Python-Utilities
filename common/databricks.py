 %py
import os
import pandas as pd

# provided we mount the storage at testmount below is the code to read and write to storage
rootpath='/dbfs/mnt/testmount/'
path='/dbfs/mnt/testmount/testComplete/'
schema_file_name = '/msvmp100_schema.txt'
mapping_file_name = '/mapping.txt'
header_file = '/Header.txt'
parquePath = '/dbfs/mnt/testmount/output_parquet/'

#df=pd.read_csv(txtfile,sep="|",low_memory=False)
#print(df.head())

df_list=[]
columns=[]
concat_contents=[]


def gen_data_dict(filename):

  lines = open(filename, 'r').read().splitlines()  
  # skipping blank lines if any and also the header line
  lines_list = [line for line in lines if line][1:]
  #convert list into dictionary
  lines_dict = dict(line.split(',') for line in lines_list)
  return lines_dict


def generate_parque_for_folder(path):
  # create content list with headers 
  with open(path+header_file,'r') as header:
    for line in header:
      concat_contents.append(line)

  #print(concat_contents)
  for file in os.listdir(path):
      if file.endswith(".txt") and file not in ('Header.txt','mapping.txt') and not file.endswith('_schema.txt'):
        print("File => ",os.path.join(path,file))
        df=pd.read_csv(os.path.join(path,file),sep="|",low_memory=False,header=None,names=concat_contents[0].split('|'))
        #print("Columns => ",df.columns)
        df_list.append(df)

  df_final=pd.concat(df_list,ignore_index=True)
  # df_final.to_csv(path+"tempoutfile.csv")  
  # load the values in the dictionary from the corresponding files 

  schema_dict = gen_data_dict(path+schema_file_name)
  mapping_dict = gen_data_dict(path+mapping_file_name)
  dtype={col:mapping_dict[value] for (col,value) in schema_dict.items()}

  type_cast_df = {}

  for col in df_final.columns:
    mapped_col_value = str(mapping_dict[schema_dict[col]])
    type_cast_df[col] = mapped_col_value

  df_final = df_final.astype(type_cast_df)
  parqueFile=parquePath+path.split('/')[-1]+'.parq.snappy'
  print("parquepath => "+parqueFile)
  df_final.to_parquet(parqueFile,engine='pyarrow',compression='snappy')


if __name__=='__main__':
  for root, dirs, files in os.walk(rootpath):
    for d in dirs:
      tmp=os.path.join(root,d)
      if d=='testComplete':
        print('directory =>',d)
        generate_parque_for_folder(tmp)
    