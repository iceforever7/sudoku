//解数独算法
var solveSudoku = function (board) {
    const rows = new Array(9)
    const cols = new Array(9)
    const blocks = new Array(9)
    const opitons = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for (let i = 0; i < 9; i++) { //初始化
        rows[i] = new Set(opitons)
        cols[i] = new Set(opitons)
        blocks[i] = new Set(opitons)
    }

    const getBlockIndex = (i, j) => { //获取坐标所在框的索引
        return parseInt(i / 3) * 3 + parseInt(j / 3)
        // return (i / 3 | 0) * 3 + (j / 3 | 0)gi
    }

    for (let i = 0; i < 9; i++) { //更新set,删除该选项
        for (let j = 0; j < 9; j++) {
            if (board[i][j] != "") {
                rows[i].delete(board[i][j])
                cols[j].delete(board[i][j])
                blocks[getBlockIndex(i, j)].delete(board[i][j])
            }
        }
    }
    //递归
    const fill = (i, j) => {
        if (j == 9) { //换行
            i++
            j = 0
            if (i == 9) {
                return true
            }
        }
        if (board[i][j] != '') {
            return fill(i, j + 1)
        }
        const blockIndex = getBlockIndex(i, j)

        for (let num = 1; num <= 9; num++) {
            const s = String(num)
            if (!rows[i].has(s) || !cols[j].has(s) || !blocks[blockIndex].has(s)) { //如果数组中没有,continue
                continue
            }
            board[i][j] = s
            rows[i].delete(board[i][j])
            cols[j].delete(board[i][j])
            blocks[blockIndex].delete(board[i][j])

            if (fill(i, j + 1)) {
                return true
            }
            board[i][j] = ""
            rows[i].add(s)
            cols[j].add(s)
            blocks[blockIndex].add(s)
        }
        return false
    }
    fill(0, 0)
    return board
}
//历遍容器
const containers = document.querySelectorAll('.content');
for (let i = 0; i < containers.length; i++) {
  const container = containers[i];
  const table = document.getElementById(container.id);
		const rows = table.querySelectorAll('tr');
		// 创建一个空数组来存储表格数据
		var data = [];
		// 循环遍历每一行
		rows.forEach(row => {
		  // 获取当前行中所有单元格元素
		  const cells = row.querySelectorAll('td');
		  // 创建一个空数组来存储当前行的数据
		  const rowData = [];
		  // 循环遍历当前行中的每个单元格
		  cells.forEach(cell => {
			// 将单元格的内容添加到当前行的数据数组中
			rowData.push(cell.textContent);
		  });
		  // 将当前行的数据数组添加到表格数据数组中
		  data.push(rowData);
		});
		// 输出表格数据数组data
		solveSudoku(data);
		console.log(data);
}
