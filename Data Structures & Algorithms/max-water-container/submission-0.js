class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {

        let left = 0
        let right = heights.length - 1
        let max_area = 0

        while (left < right) {
            const length = right - left
            const height = Math.min(heights[left], heights[right])

            const area = height * length
            max_area  = Math.max(max_area, area)

            if (heights[left] < heights[right]) {
                left += 1
            } else {
                right -= 1
            }

        }

        return max_area



    }
}
