class HashTable:

    def __init__(self,size):
        self.size = size
        # Make a list which has size which user defined
        self.hash_table = self.create_buckets()
        

    def create_buckets(self):
        return [ [] for _ in range(self.size)]
    
    def set_val(self, key, value):
        # Create index using a built-in hash function
        # hash function create a very big number which is larger than our list size. So use `%` to get the proper index number.
        hashed_index = hash(key) % self.size # Now we have an index of our bucket in this hash table 
        
        # save this reference index(hashed_index) in `bucket` variable
        bucket = self.hash_table[hashed_index] 
        # so our `bucket` variable simply be used to point to the bucket that was chosen to add a record 

        # Process of add new data/ update data 
        # Set the flag 
        found_key = False 
        for index, record in enumerate(bucket):
            record_key , record_value = record # break tuble
            if record_key == key: ## If same
                found_key = True
                break # Return index where the record exists.
        if found_key: # key exists
            bucket[index] = (key,value)
        else: # key does not exists 
            bucket.append((key, value)) # Save data as a tuple 

    def get_val(self,key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key , record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            return record_value
        else:
            return "No record found with that email address"

    def __str__(self):
        #return "Hello"
        return "".join(str(item) for item in self.hash_table)

hash_table = HashTable(256)
hash_table.set_val('robert@gmail.com', {'first_name': "Robert", "last_name": "Han"})
hash_table.set_val('shawn@gmail.com', {'first_name': "Shawn", "last_name": "Jeong"})
hash_table.set_val('jane@gmail.com', {'first_name': "Jane", "last_name": "Richard"})
hash_table.set_val('tylor@gmail.com', {'first_name': "Tylor", "last_name": "Smith"})
print(hash_table)
# update exists data
#hash_table.set_val('shawn@gmail.com', 'updated new value')

# Test get.val
print(hash_table.get_val('robert@gmail.com'))
print(hash_table.get_val('tylor@gmail.com'))