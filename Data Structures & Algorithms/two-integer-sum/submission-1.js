class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {

        for (let i = 0; i < nums.length; i++) {
            for (let j = i; j < nums.length; j++) {
                if (i !== j && nums[j] + nums[i] === target) {
                    return [i,j]
                }
            }
        }


    }
}
