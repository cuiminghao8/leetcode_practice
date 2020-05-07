class Solution:
    def minCount(self, coins):
        return sum(num % 2 + num // 2 for num in coins)


def main():
    result = Solution()
    coins = [4, 2, 1,273,29348,10]
    print(result.minCount(coins))


if __name__ == "__main__":
    main()
