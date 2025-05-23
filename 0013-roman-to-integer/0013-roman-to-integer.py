class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I": 1, 
            "V": 5, 
            "X": 10, 
            "L": 50, 
            "C": 100,
            "D": 500, 
            "M": 1000, 
            }
        
        special_dic = {
            "IV": 4, 
            "IX": 9, 
            "XL": 40, 
            "XC": 90, 
            "CD": 400, 
            "CM": 900
            }

        i = 0
        answer = 0
        while i < len(s):
            word = s[i]

            if i < len(s) - 1:
                special_word = s[i:i+2]

                if special_word in special_dic:
                    answer += special_dic[special_word]
                    i += 2
                    continue
            
            answer += dic[word]
            i += 1

        return answer

        