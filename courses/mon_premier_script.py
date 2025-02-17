from typing import List

def count_long_names(names: List[str]) -> int:
    """Count names with more than seven characters."""
    LONG_NAME_THRESHOLD = 7
    long_names_count = 0
    
    for name in names:
        if len(name) > LONG_NAME_THRESHOLD:
            long_names_count += 1
            print(f"{name} est un prénom avec un nombre de lettres supérieur à {LONG_NAME_THRESHOLD}")
        else:
            print(f"{name} est un prénom avec un nombre de lettres inférieur ou égal à {LONG_NAME_THRESHOLD}")
            
    return long_names_count
class TestNameLength(unittest.TestCase):
    def test_count_long_names(self):
        test_names = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        result = count_long_names(names=test_names)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()