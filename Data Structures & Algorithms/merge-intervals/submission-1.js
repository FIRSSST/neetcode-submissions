class Solution {
    /**
     * @param {number[][]} intervals
     * @return {number[][]}
     */
    merge(intervals) {


        intervals.sort((itm1, itm2) => itm1[0] - itm2[0])
        console.log(intervals)

        const new_intervals = []
        
        new_intervals.push(intervals[0])
        
        for (let i = 1; i < intervals.length; i++) {
            const [curr_start, curr_end] = new_intervals.at(-1)
            let [start, end] = intervals[i]
            if (start <= curr_end) {
                let new_end = Math.max(curr_end, end)
                new_intervals[new_intervals.length - 1] = [curr_start, new_end]
            } else {
                new_intervals.push([start, end])
            }
        }

        return new_intervals


    }
}
