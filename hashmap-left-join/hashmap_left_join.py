from hash.hashtabels1 import Hashtable

def hashmap_left_join(table1: Hashtable, table2: Hashtable):
    """
    Function to left join two hashmaps.

    Args:
        table1 (Hashtable): Hashtable to be joined.
        table2 (Hashtable): Hashtable to join with.

    Returns:
        Hashtable: Hashtable containing the left join result with keys from table1 and values from both tables.
    """
    result = Hashtable()
    for key in table1.keys():
        value1 = table1.get(key)
        value2 = table2.get(key)
        result.set(key, [value1, value2])
    return result
