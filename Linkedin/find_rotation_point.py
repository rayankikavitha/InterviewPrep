import unittest


def find_rotation_point(words):

    # Find the rotation point in the list
    first_word = words[0]
    low = 0
    high = len(words) -1
    while low <high:
        mid = low + (high-low)//2
        # rotation on the right
        if words[mid] >=first_word:
            low = mid
        else:
            high = mid
        if low+1 == high:
            return high


    












select ua.customer_id,c.util_internal_id, ua.util_account_id, re.attribute_value, re.start_date,re.end_date ,ua.updated_at,c.updated_at
from re_utility_account_attribute re 
join utility_acct ua on ua.id = re.utility_account_id and ua.inactive_date is NULL
join customer c on c.id = ua.customer_id 
where attribute_key ='PEAK_TIME_REBATE' 
and ua.customer_id in (850519,594850,78221,287223);





# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)