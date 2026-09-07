# 7. Reverse Integer

### Difficulty: Medium

## Description
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 
Example 1:


Input: x = 123
Output: 321


Example 2:


Input: x = -123
Output: -321


Example 3:


Input: x = 120
Output: 21


 
Constraints:


	-231 <= x <= 231 - 1

## Submission Details
- **Status**: Accepted
- **Runtime**: 20
- **Memory**: 12188000
- **Language**: python

## Code
```python
class Solution:

    def reverse(self, x):
        # Number ka sign save kar lo (+1 ya -1)
        sign = -1 if x < 0 else 1
        x = abs(x)

        # String me convert karke reverse karo aur fir int me badlo
        reversed_x = int(str(x)[::-1]) * sign

        # 32-bit signed integer limits check [-2^31, 2^31 - 1]
        if reversed_x < -(2**31) or reversed_x > (2**31 - 1):
            return 0

        return reversed_x
```
