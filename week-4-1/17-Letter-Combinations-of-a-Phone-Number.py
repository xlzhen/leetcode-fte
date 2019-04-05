class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        interpret_digit = {'1': '',
                           '2': 'abc',
                           '3': 'def',
                           '4': 'ghi',
                           '5': 'jkl',
                           '6': 'mno',
                           '7': 'pqrs',
                           '8': 'tuv',
                           '9': 'wxyz'}
        if digits: 
            all_combinations = ['']
        else:
            all_combinations = []
        for digit in digits:
            current_combinations = []
            for letter in interpret_digit[digit]:
                for combination in all_combinations:
                    current_combinations.append(combination+letter)
            all_combinations = current_combinations
        return all_combinations
