# https://towardsdatascience.com/installing-apache-pyspark-on-windows-10-f5f0c506bea1
# subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil"])
# C:\Python_Utils\spark_hadoop>bin\spark-submit C:\Python_Utils\pyspark_connect.py

# Defining the environment variables 
import os
import sys
from datetime import datetime
start = datetime.now()
# os.environ["PYSPARK_PYTHON"] = "C:\\Python_Utils\\spark_hadoop\\python"
# os.environ["JAVA_HOME"] = "C:\\Program Files (x86)\\Java\\jdk1.8.0_181"
# os.environ["SPARK_HOME"] = "C:\\Python_Utils\\spark_hadoop"
# os.environ["PYLIB"] = os.environ["SPARK_HOME"] + "/python/lib"
# sys.path.insert(0, os.environ["PYLIB"] +"/py4j-0.10.7-src.zip")
# sys.path.insert(0, os.environ["PYLIB"] +"/pyspark.zip")

# import os
# os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
# os.environ["SPARK_HOME"] = "/content/spark-3.0.1-bin-hadoop2.7"

# import findspark
# findspark.init()

# Importing the SparkSession library

from pyspark.sql import SparkSession

MAX_MEMORY = "5g"

# Creating the SparkSession object

spark = SparkSession.builder \
                    .appName('apriori')\
                    .config("spark.executor.memory", MAX_MEMORY) \
                    .config("spark.driver.memory", MAX_MEMORY) \
                    .getOrCreate()


# Loading the data from Market_Basket_Optimisation.csv inside the dataframe
# %cd /content/drive/MyDrive/Colab Notebooks
transaction_df = spark.read.csv("C:\\Users\\User\\Downloads\\transactions.csv")

# Schema of the dataframe
transaction_df.printSchema()

# Print the first 20 transactions of the dataframe
transaction_df.show()   # added as part of assignment

# Function to remove the columns with duplicate values

def remove_duplicate_columns(x):
    # Length of the column
    col_len = len(x)
    
    # Empty RDD - set of values
    columns = set()
    
    # Removing any additional spaces from the elements and adding the elements into the column from RDD 'x'
    for col in range(col_len):
        x_col = str(x[col]).strip()
        columns.add(x_col)
    
    # To check if elements are present in the provided dataframe/RDD 
    if len(columns) < col_len:
        return []
    
    # Returning the sorted list of items in each element as tuple
    return [(tuple(sorted(columns)))]


# For the given dataset writing a function to return the list of distinct items in the dataset

def generate_unique_item_set(df):
    # empty dataframe
    total_item_set_df = None
    
    # Iteration over each column - 20 columns
    for col_index in range(20):
        
        # Loading the elements of each column individually
        _c_df = df.select("_c" + str(col_index))
        
        if total_item_set_df is None:
            # None for the first iteration in the loop
            total_item_set_df = _c_df
            
        else:
            # After the first iteration, appending the entries from each column to total_item_set_df
            total_item_set_df = total_item_set_df.union(_c_df)   # added union as part of assignment
            
    # Return Value: Dataframe with unique items (no repetition) and null values removed from the dataFrame
    # df.na provides all the null values; all the null values must be dropped
    # .rdd converts the DataFrame to RDD
    # remove_duplicate_columns must be applied to elements of RDD such that each item in transaction is a separate element 
    # Remember that the function 'remove_duplicate_columns' is applied to each element of the RDD, in short, every row of the dataframe should be passed into it. 
    return total_item_set_df.select("_c0").na.drop().rdd.flatMap(lambda x: remove_duplicate_columns(x)).distinct().toDF()  # added drop() and flatmap as a part of assignment


def filter_and_map_transaction(x, candidate_set_shared):
    
    c_k = []
    
    rows = len(candidate_set_shared.value)
    cols = len(candidate_set_shared.value[0])
    
    # Checking each transaction
    for row_i in range(rows):
        item_set = set()
        for col_i in range(cols):
            item_set.add(candidate_set_shared.value[row_i][col_i])
        
        # Map the condition with the correct value (1/0)
        if item_set.issubset(set(x)):
            c_k.append((candidate_set_shared.value[row_i], 1))  #added 1 as a part of assignment
        else:
            c_k.append((candidate_set_shared.value[row_i], 0))  #added 0 as a part of assignment
    return c_k


def get_all_possible_candidate_sets(candidate_item_sets_k, candidate_item_sets_0):
    
    # Convert the elements of the candidate_item_sets_k from the list format into tuple
    # You can refer to the commands below to check why only the first element is used for conversion
    candidate_item_sets_k = candidate_item_sets_k.map(lambda x: tuple(x[0])).toDF()
    # toDF() converts the rdd into a dataFrame
    
    # Returning the k+1 order
    return candidate_item_sets_k.crossJoin(candidate_item_sets_0).rdd.flatMap(remove_duplicate_columns).distinct()
    # crossJoin will help to combine one element of one dataFrame with all the elements of another dataFrame


# Function to generate frequent itemset

def get_freq_item_sets(total_records, candidate_sets_shared, transaction_df_rdd, min_support):

    """
    Attributes
    ----------
    total_records: Total number of records in the dataFrame
    
    candidate_sets_shared: List of items in the transaction base
    
    transaction_df_rdd: Transactions dataFrame converted into an RDD
    
    min_support: Minimum support threshold
    ----------
    
    """
    
    filtered_item_set = transaction_df_rdd.flatMap(lambda x: filter_and_map_transaction(x, candidate_sets_shared)) \
    .reduceByKey(lambda a,b : a+b)   \
    .map(lambda item: item[0]) \
    .map(lambda item:(item[0],item[1]/total_records))  \
    .filter(lambda item: item[1] >= min_support)
    
    # added above 3 lines together it was creating intention issue below.
                                          
                                          # Sample output from filter_and_map_transaction function can be seen above
                                          # Now complete the function to generate the frequent item set
                                          # support value = Frequency of the item in the transactions/total number of transactions
                                          
                                          # 1. function to calculate frequency of each item in the transaction base
                                          #.reduceByKey(lambda a,b : a+b) \
                                          
                                          # 2. funciton to calculate the support value (formula in comments above) 
                                          # You are expected to provide the total number of records when you call the function.
                                          #.map(lambda item: item[1]/total_records)\
                                          
                                          # 3. funciton to filter the items that have support value greater than the min_support
                                          # You are expected to provide the min_support when you call the function.
                                          #.filter(lambda item: item[1] >= min_support )
    
    return filtered_item_set


# Function to check if "freq_item_sets" has relevant values (Not empty and all the values are not None)

# The first condition is defined to check if there are elements in the itemset. 
# There might be a case that elements are present but all of them are none.
# The second condition checks if all the elements of the itemset are not none.

def is_freq_item_set_not_empty(freq_item_sets):
  return freq_item_sets is not None and freq_item_sets.count() > 0  # added & as a part of assignment    
  # Provide the correct logical operator in the condition above 


from pyspark.sql.types import StructType, ArrayType, StructField, DoubleType, StringType

def apriori(item_sets, transaction_df_rdd, min_support):
    
    """
    Attributes
    ----------
    item_sets: DataFrame that has all the items present in the transactions
    
    transaction_df_rdd: Transacations in the form of an RDD
    
    min_support: Minimum support threshold
    -----------
    """
    
    # Calculate the total number of transactions in the dataset and store the count in total_records
    total_records = transaction_df_rdd.count()  #added as a part of assignment

    # Defining a blank list that will store the frequent itemsets
    freq_item_sets_all_orders = []

    # Candidate sets of order 1 will be the complete item list from the transactions
    # As you can see, broadcast function is used here. It is used to broadcast a variable on all the executors.
    candidate_sets_order_1 = spark.sparkContext.broadcast(item_sets.collect())
    
    #get_freq_item_sets(total_records, candidate_sets_shared, transaction_df_rdd, min_support)
    # Complete the function to generate the filtered item set of order 1. Check the function definition of 'get_freq_item_sets' to understand the attributes.
    frequent_item_sets_order_1 = get_freq_item_sets(total_records,candidate_sets_order_1, transaction_df_rdd, min_support) #added parameter as a part of assignment
    
    # Appending the results of frequent_item_sets_order_1 in the freq_item_sets_all_orders
    freq_item_sets_all_orders.append(frequent_item_sets_order_1) #added append as part of assignment
    
    # Convert the elements of the rdd 'frequent_item_sets_order_1' into a dataFrame with each element as tuple
    frequent_item_sets_order_1_df = frequent_item_sets_order_1.map(lambda x: tuple(x)).toDF()  # added tuple(x) as part of assignment

    print('frequent_item_sets_order_1_df -> ',frequent_item_sets_order_1_df.head())
    print('$'*100)
    
    # Generating higher order rules
    k = 0
    
    # Loop will run till higher order item sets can be generated
    while is_freq_item_set_not_empty(freq_item_sets_all_orders[k]):
        # Generating candidate sets of order k+1 
        print(k)
        current_candidate_sets = get_all_possible_candidate_sets(freq_item_sets_all_orders[k], frequent_item_sets_order_1_df)
        
        # Broadcasting candidate sets
        current_candidate_sets = spark.sparkContext.broadcast(current_candidate_sets.collect())
        
        # Filtering candidate sets to get the frequent item sets of order 'k+1' 
        current_frequent_item_sets = get_freq_item_sets(total_records, current_candidate_sets, transaction_df_rdd, min_support)
        
        # Appending the list 'freq_item_sets_all_orders' with the frequent itemset of order k+1
        freq_item_sets_all_orders.append(current_frequent_item_sets)
        
        # freq_item_sets_all_orders is a list of RDDs where the element k stores the frequent item set of order k+1  
        
        # increasing k by 1
        k += 1        
    
    
    return freq_item_sets_all_orders


# Function to generate all possible subsets from a set
# You can google powerset if you want to read more about it

def powerset(s):
    slist = list(s)
    result = [[]]
    for x in slist:
        
        # Here, you may want to explore what the purpose of function 'extend' is
        # Note that it is a reccursive function that adds elements to a list. It is similar to the extend() function in Python.
        result.extend([subset + [x] for subset in result])
        
    return [item_set for item_set in result if (len(item_set) > 0 and len(item_set) < len(slist))]


from pyspark.sql import Row

def generate_rules_with_confidence(x, k, freq_item_sets_map_all_orders_shared, min_confidence):
    
    """
    Attributes
    ----------
    
    x: freq_item_sets_all_orders; list that stores the frequent item set with the confidence score
    
    k: order of the frequent item set
    
    freq_item_sets_map_all_orders_shared: broadcasted map (key-value pair) of frequent item sets where 
    - key is the subset and 
    - value is the corresponding support
    
    min_confidence: Threshold confidence value 
    
    """
    
    # first column of the RDD is extracted as a frequent item set
    freq_item_set = set(x[0])
    print('freq_item_set ->',freq_item_set)
    print('#'*100)
    
    # all_subsets stores all the subsets from the freq_item_set
    all_subsets = powerset(freq_item_set)
    
    # Defining an empty list to store the rules
    rules = []
    
    # Converting the broadcasted values in the required format (elements as tuple)
    freq_item_set_support = freq_item_sets_map_all_orders_shared[k].value[tuple(sorted(freq_item_set))]
    
    # Generated rules contain single element as antecendent. The reason is we used cross join for generating candidate
    # itemsets instead of doing or operation of two candidate sets as the for the later completely distributed approach
    # cannot be implemented.
    
    candidate_set_key = ''
    subset_k = 0
    for subset in all_subsets:
        antecedent = set(subset)
        
        # Consequent is generated by removing the antecedent from the frequent item set
        consequent = freq_item_set - set(antecedent)
    
        # Different calculation when there is a single element in consequent
        if (len(set(antecedent)) == 1):
            single_item = set(antecedent).pop()
            candidate_set_key = Row(_1=single_item)
            subset_k = 1
            set(antecedent).add(single_item)
        else:
            candidate_set_key = tuple(sorted(set(antecedent)))
            subset_k = len(set(antecedent))

        # support value for the consequent
        # value.get helps you to obtain only the value from the key-value pair
        antecedent_support = freq_item_sets_map_all_orders_shared[subset_k-1].value.get(candidate_set_key)
        
        if (antecedent_support is not None):
            
            # Calculating confidence value for the rule
            confidence = freq_item_set_support/antecedent_support
        
            # Addition of rule if the confidence value is above threshold
            if (confidence >= min_confidence):
                rules.append((list(antecedent), list(consequent), confidence))      

    return rules


def generate_association_rules_for_k_order(k, freq_item_sets_order_k, \
                                           freq_item_sets_map_all_orders_shared, min_confidence):
    """
    Attributes
    ----------
    
    k: order of the frequent item set
    
    freq_item_sets_map_all_orders_shared: broadcasted map (key-value pair) of frequent item sets where 
    - key is the subset and 
    - value is the corresponding support
    
    min_confidence: Threshold confidence value 
    
    """
    for x in freq_item_sets_order_k.collect():
      print(generate_rules_with_confidence(x,k,freq_item_sets_map_all_orders_shared, min_confidence))

    # Function generate_rules_with_confidence is called as flat map operation over the frequent itemsets of order k
    return freq_item_sets_order_k.flatMap(lambda x: generate_rules_with_confidence(x, \
                                  k,freq_item_sets_map_all_orders_shared, \
                                  min_confidence)) \
 .toDF(('Antecedent', 'Consequent', 'Confidence'))
                                  # Converting the RDD into Dataframe and changing the column names
                                 #.toDF(('Antecedent', 'Consequent', 'Confidence'))    


def generate_association_rules(freq_item_sets_all_orders, min_confidence):
    
    """
    Attributes
    ----------
    
    freq_item_sets_all_orders: list of all frquent itemsets (calculated above) of different orders
    
    min_confidence: Threshold confidence value 
    
    """

    # As you can see, broadcast function is used here. It is used to broadcast a variable on all the executors.
    freq_item_sets_map_all_orders_shared = [spark.sparkContext.broadcast(freq_item_sets.collectAsMap()) \
                                                                     for freq_item_sets in freq_item_sets_all_orders]
    
    l = len(freq_item_sets_map_all_orders_shared)    
    # Calling the function defined above to generate rules from frequent itemset of order 2
    # ___________
    association_rules_df = generate_association_rules_for_k_order(0, freq_item_sets_all_orders[0], \
                                                                  freq_item_sets_map_all_orders_shared, \
                                                                  min_confidence)
    
    for k in range(2, l):
        if is_freq_item_set_not_empty(freq_item_sets_all_orders[k]):
            # Creating union of all association rules for different frequent itemsets
            
            association_rules_df = association_rules_df.union(generate_association_rules_for_k_order(k, \
                                                        freq_item_sets_all_orders[k], \
                                                        freq_item_sets_map_all_orders_shared, min_confidence))
    return association_rules_df        


try:	
	# Syntax structure: item_sets = function(dataframe)
	item_sets = generate_unique_item_set(transaction_df)   #added function as a part of assignment

	# Print the first twenty rows of the item_sets dataframe
	item_sets.show()  # added as a part of assignment

	# Give the number of unique items in the transaction dataset
	item_sets.count() # added as a part of assignment

	## Testing grid -- please ignore    
	transaction_df_rdd = transaction_df.rdd

	total_records = transaction_df_rdd.count()  #added as a part of assignment

	# Defining a blank list that will store the frequent itemsets
	#freq_item_sets_all_orders = []

	# Candidate sets of order 1 will be the complete item list from the transactions
	# As you can see, broadcast function is used here. It is used to broadcast a variable on all the executors.
	candidate_sets_order_1 = spark.sparkContext.broadcast(item_sets.collect())

	#get_freq_item_sets(total_records, candidate_sets_shared, transaction_df_rdd, min_support)
	# Complete the function to generate the filtered item set of order 1. Check the function definition of 'get_freq_item_sets' to understand the attributes.
	frequent_item_sets_order_1 = get_freq_item_sets(total_records,candidate_sets_order_1, transaction_df_rdd, 0.01)    

	## Testing grid -- please ignore
	#frequent_item_sets_order_1_df = frequent_item_sets_order_1.map(lambda x: tuple(x)).toDF()
	#frequent_item_sets_order_1_df.show()

	# Generate the frequent item set using the apriori function created above.
	# Minimum support = 0.01
	# Check the format in which each attribute must be provided
	transaction_df_rdd = transaction_df.rdd  #added as a part of assignment
	freq_item_sets_all_orders = apriori(item_sets, transaction_df_rdd, 0.01)  # apriori(item_sets, transaction_df_rdd, 0.01) added as a part of assignment

	# freq_item_sets_all_orders is a list of RDDs where the element k stores the frequent item set of order k+1
	# Print freq_item_sets_all_orders to check the structure

	print(freq_item_sets_all_orders)

	# First order itemsets that have support value greater than the threshold (Print 20 rows)
	#print(freq_item_sets_all_orders[0].take(10)) # added print statement as a part of the assignment -- need to check correctness
	freq_item_sets_all_orders[0].toDF().show()

	# Second order itemsets that have support value greater than the threshold (Print 20 rows)
	# freq_item_sets_all_orders[1].toDF().show() # added statement as a part of the assignment

	# Applying the generate_association_rules function over the list of all frequent itemsets with threshold confidence
	# score as 0.099 - Values greater than 1 will be used in the marketing strategies

	association_rules = generate_association_rules(freq_item_sets_all_orders, 0.099)

	association_rules.show(300, truncate=False)
except Exception as e:
	print('Error as ',str(e))
	print('Elapsed time -> ',datetime.now() - start)