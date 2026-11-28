class Solution {
    /**
     * @param {character[][]} grid
     * @return {number}
     */
    numIslands(grid) {


        const visited = new Set()
        let num_islands = 0

        const ROWS = grid.length
        const COLS = grid[0].length
        const dirs = [[0,1], [1,0], [-1,0], [0,-1]]

        function dfs(r,c) {
            if (r >= ROWS || r < 0 || c >= COLS || c < 0) {
                return
            }

            if (visited.has(`${r},${c}`)) {
                return
            }

            if (grid[r][c] !== "1") {
                return
            }

            visited.add(`${r},${c}`)

            for (const [dr, dc] of dirs) {
                const nr = dr + r
                const nc = dc + c
                if (nr >= ROWS || nr < 0 || nc >= COLS || nc < 0) {
                    continue
                }

                dfs(nr, nc)

            }

        }


        for (let r = 0; r < ROWS; r++) {
            for (let c = 0; c < COLS; c++) {
                if (grid[r][c] === "1" && visited.has(`${r},${c}`) === false) {
                    dfs(r,c)
                    num_islands += 1
                }
                
            }
        }

        return num_islands

    }
}
