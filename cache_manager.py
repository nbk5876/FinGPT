#------------------------------------------------------------
# cache_manager.py
# Purpose: The cache_manager.py script acts as an intermediary 
#          storage layer that holds onto important data 
#          temporarily. When a request is made that matches 
#          data already in the cache, it provides this data 
#          directly without needing to reach out to the 
#          external data source again
#------------------------------------------------------------
class CacheManager:
    def __init__(self):
        # Initialize your cache. This could be an in-memory cache or connected to a file/db
        self.cache = {}

    def get_cached_data(self, key):
        # Return data from cache if exists
        return self.cache.get(key, None)

    def cache_data(self, key, data):
        # Cache the data with the provided key
        self.cache[key] = data
