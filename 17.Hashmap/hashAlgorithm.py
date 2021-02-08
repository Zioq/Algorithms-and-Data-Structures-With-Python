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
        hashed_key = 10 # hash(key) % self.size # Now we have an index of our bucket in this hash table 
        
        # save this reference index in bucket
        bucket = self.hash_table[hashed_key] 

        # so our `bucket` variable simply be used to point to the bucket that was chosen to add a record 

        # process of collision
        found_key = False
        for index, record in enumerate(bucket):
            record_key , record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key: # key exists
            bucket[index] = (key,value)
        else: # key does not exists 
            bucket.append((key, value)) # Save data as a tuple 
         


    def get_val(self,key):
        pass

    def __str__(self):
        #return "Hello"
        return "".join(str(item) for item in self.hash_table)

hash_table = HashTable(256)
hash_table.set_val('robert@gmail.com', 'some value')
hash_table.set_val('shawn@gmail.com', 'some other value')
print(hash_table)
# update exists data
hash_table.set_val('shawn@gmail.com', 'updated new value')
print(hash_table)