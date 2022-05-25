
import os
import pandas as pd


# provided we mount the storage at testmount below is the code to read and write to storage
rootpath='/dbfs/mnt/prod_data/'
#path='/dbfs/mnt/prod_data/'
schema_file_name = '/schema.txt'
mapping_file_name = '/dbfs/mnt/prod_data/OUTPUT_PARQUET_FILES/mapping.txt'
header_file = '/Header.txt'
parquePath = '/dbfs/mnt/prod_data/OUTPUT_PARQUET_FILES/'
parquetDatatypeFile = '/dbfs/mnt/prod_data/OUTPUT_PARQUET_FILES/datatype.csv'
fileRows=0
indDfRows=0


def gen_data_dict(filename):

  lines = open(filename, 'r').read().splitlines()  
  # skipping blank lines if any and also the header line
  lines_list = [line for line in lines if line][1:]
  #convert list into dictionary
  lines_dict = dict(line.split(',') for line in lines_list)
  return lines_dict


def generate_parque_for_folder(path):

  df_list=[]
  columns=[]
  concat_contents=[]

  print("1 concat contents => ",len(concat_contents)," ",path+header_file)
  # create content list with headers
  with open(path+header_file,'r') as header:
    for line in header:
      concat_contents.append(line)
      print("2 concat contents => ",len(concat_contents)," ",path+header_file)
  print("*"*50)
  print(concat_contents)
  print("*"*50)
  for file in os.listdir(path):
      if file.endswith(".txt") and file not in ('Header.txt','mapping.txt') and not file.endswith('schema.txt'):
        print("file size ",os.path.getsize(os.path.join(path,file)))
        print("File => ",os.path.join(path,file))
        if not os.path.getsize(os.path.join(path,file)) > 0 :
          print("Skipping Empty file ",os.path.join(path,file))
          continue
        df=pd.read_csv(os.path.join(path,file),sep="|",encoding='utf-8',low_memory=False,header=None,error_bad_lines=False,quoting=3,escapechar='/')
        with open(os.path.join(path,file),'r') as f:
          fileRows=len(list(f))
          print("number of rows in the file ",fileRows)
        indDfRows=df.shape[0]  
        print("Individual number of dataframe rows",indDfRows)
        if(fileRows != indDfRows):
          print("ERROR: File not loaded completely")
          return
        print("Columns in file => ",len(concat_contents[0].split('|')))
        print("Columns loaded  => ",len(df.columns))
        if(len(concat_contents[0].split('|')) != len(df.columns)):
            print("ERROR: Columns mismatch ")
            return
        else:
          df.columns = concat_contents[0].split('|')
          df_list.append(df)

  df_final=pd.concat(df_list,ignore_index=True)
  print("Final number of dataframe rows",df_final.shape)
  # df_final.to_csv(path+"tempoutfile.csv")  
 
  # load the values in the dictionary from the corresponding files

  schema_dict = gen_data_dict(path+schema_file_name)
  print("Schema dict file => ",path+schema_file_name)
 
  mapping_dict = gen_data_dict(mapping_file_name)
  dtype={col:mapping_dict[value] for (col,value) in schema_dict.items()}

  type_cast_df = {}

  print('*'*100)
  print(mapping_dict.keys(),"\n")
  print(schema_dict.keys(),"\n")
  print(df_final.columns,"\n")
  print('*'*100)
  for col in df_final.columns:
    mapped_col_value = str(mapping_dict[schema_dict[col]])
    type_cast_df[col] = mapped_col_value
   
  # only for debugging
  #print('typecast df => ',type_cast_df)
  #print(df_final.columns)
  df_final = df_final.astype(type_cast_df)
  #print(df_final.dtypes)
  parqueFile=parquePath+path.split('/')[-1]+'.parq.snappy'
  print("parquepath => "+parqueFile)
  print("\n"*2)
  df_final.to_parquet(parqueFile,engine='pyarrow',compression='snappy')
  df_final=pd.read_parquet(parqueFile,engine='pyarrow')
  dt=df_final.dtypes
  dt.to_csv(parquetDatatypeFile,header=True)


if __name__=='__main__':
  for root, dirs, files in os.walk(rootpath):
    for d in dirs:
      tmp=os.path.join(root,d)
      if d not in ['OUTPUT_PARQUET_FILES']:
        print('directory =>',d)
        generate_parque_for_folder(tmp)
