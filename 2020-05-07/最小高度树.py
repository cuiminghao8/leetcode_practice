# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        if not len(nums):
            return
        nums.sort() #列表升序排列，这样列表中间的元素一定就是中位数
        mid = len(nums) // 2
        root = TreeNode(nums[mid])  #取列表中位数为root，左边都比他小，右边都比他大。再对左右迭代进此方法，直到len(nums)为0
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root



def main():
    nums = [-10, -3, 0, 5, 9]
    BST = Solution()
    BST.sortedArrayToBST(nums)



if __name__ == "__main__":
    main()
