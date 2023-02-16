class Solution:

  def isHappy(self, n: int) -> bool:
    if (n == 1):
      return True

    def calnumber(num):
      sum = 0
      while (num > 0):
        sum += (num % 10)**2
        num = num // 10
      return sum

    num_list = []
    while (n != 1):
      n = calnumber(n)
      if n in num_list:
        return False
      elif n == 1:
        return True
      else:
        num_list.append(n)

    return False


answer = Solution().isHappy(19)
print(answer)
answer = Solution().isHappy(2)
print(answer)
