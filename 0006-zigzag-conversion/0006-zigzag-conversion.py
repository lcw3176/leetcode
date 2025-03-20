class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        lst = []
        
        offset = numRows + (numRows - 2)
        
        float_offset = offset

        for i in range(numRows):
            if float_offset == offset or float_offset == 0:
                index = i

                while index < len(s):
                    lst.append(s[index])
                    index += offset
                

            elif float_offset != offset:
                index = i

                while index < len(s):
                    lst.append(s[index])
                    index += float_offset

                    if index >= len(s):
                        break

                    lst.append(s[index])
                    index += offset - float_offset
            
            float_offset -= 2

        return "".join(lst)