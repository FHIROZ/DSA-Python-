class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_val = 1
        sum_val = 0
        # Convert number to string to loop through digits
        for digit in str(n):
            val = int(digit)
            product_val *= val
            sum_val += val
        return product_val - sum_val
