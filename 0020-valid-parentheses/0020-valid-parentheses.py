class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        data = list(s)

        for i in data:
            stack.append(i)

            if len(stack) >= 2:
                right = stack.pop()
                left = stack.pop()

                if left == "(" and right == ")":
                    continue
                
                if left == "[" and right == "]":
                    continue
                
                if left == "{" and right == "}":
                    continue

                stack.append(left)
                stack.append(right)
            
        return len(stack) == 0
