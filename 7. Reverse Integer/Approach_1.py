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