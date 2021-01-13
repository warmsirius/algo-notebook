# 1. 设计1个getMin功能的栈

## 题目
实现1个特殊的栈，实现基本功能的基础上再实现返回栈中最小元素的操作

## 难度
1颗星

## 要求
1.`pop`、`push`、`getMin`操作的时间复杂度都是 O(1)
2.设计的栈类型可以使用现成的栈结构


## 思路
维护2个栈: `stackData`、`stackMin`
* `stackData`: 保存原始栈列数值
* `stackMin`: 保存最小栈列数值

### 思路1
* 每次 `push` newNum 到 `stackData`，获取 minNum = Min(newNum, 当前最小值)，minNum入栈
* 每次 `pop`，`stackData` 和 `stackMin` 分别弹出元素 

### 思路2
* 每次 `push` 数字 newNum 到 `stackData`:
    * 如果 newNum <= 当前的最小值，则newNum入栈
    * 否则不处理
* 每次 `pop`，`stackData` 弹出元素 num，获取stackMin的 peek位置元素 minNum，Compare(num, minNum)
    * 如果 num == minNum，则 num，minNum 均出栈
    * 否则，num出栈
