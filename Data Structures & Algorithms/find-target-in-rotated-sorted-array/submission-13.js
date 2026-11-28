class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {

        let left = 0
        let right = nums.length - 1

        while (left < right) {
            let mid = Math.floor((left + right) / 2)
            //console.log(`LEFT: ${left} MID: ${mid} RIGHT: ${right}`)

            if (nums[mid] > nums[right]) {
                left = mid + 1
            } else {
                right = mid
            }
        }

        const pivot = left
        if (target >= nums[pivot] && target <= nums[nums.length - 1]) {
            left = pivot
            right = nums.length - 1
        } else {
            left = 0
            right = pivot
        }

        while (left <= right) {
            let mid = Math.floor((left + right) / 2)

            if (nums[mid] == target){
                return mid

            } else if (nums[mid] > target) {
                right = mid - 1
            } else {
                left = mid + 1
            }
        }

        return -1


    }
}
