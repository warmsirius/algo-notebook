# 最大值减去最小值小于或等于num的子数量数目

## 题目

给定数组 arr 和整数 num，共返回有多少个子数组满足如下情况:

```
max([arr[i...j]]) - min([arr[i...j]]) <= num
```

* max([arr[i...j]]): 表示子数组 arr[i...j]中的最大值
* min([arr[i...j]]): 表示子数组 arr[i...j]中的最小值

## 要求

如果数组长度为 N，请实现 时间复杂度为 O(N)的解法。

## 解题思路
生成2个双端队列 `qmax` 和 `qmin`。

当子数组为 arr[i...j] 时:
`qmax` 维护窗口子数组 arr[i...j]的最大值更新的结构
`qmin` 维护窗口子数组 arr[i...j]的最小值更新的结构

* 当子数组 arr[i...j]向右扩一个位置变成 arr[i...j+1]时，`qmax` 和 `qmin` 结构更新代价的平均时间复杂度为O(1)，并且可以再O(1)的时间内得到 arr[i...j+1]的最大值和最小值。
* 当子数组 arr[i...j]向左缩一个位置变成 arr[i+1...j]时，`qmax` 和 `qmin` 结构更新代价的平均时间复杂度为O(1)，并且可以再O(1)的时间内得到 arr[i+1...j]的最大值和最小值。

### 结论
* 如果子数组 arr[i...j] 满足条件，即 max(arr[i...j]) - min(arr[i...j]) <= num，那么arr[i...j] 中每一个子数组 arr[k...l] (i<=k<=l<=j)都满足条件。
* 如果子数组 arr[i...j] 不满足条件，即 max(arr[i...j]) - min(arr[i...j]) > num，那么arr[i...j] 中每一个子数组 arr[k...l] (i<=k<=l<=j)都不满足条件


## 设计思路
* 1.生成2个双端队列 qmax 和 qmin，生成2个整型变量 i 和 j，表示子数组范围，生成整型变量 res 表示所有满足条件的子数组数量

* 2.j不断向右移动(j++)，表示 arr[i...j]一直享有扩大，并不断更新 qmax 和 qmin结构，保证 qmax 和 qmin 始终维持动态窗口最大值和最小值的更新结构。
> 一旦出现 arr[i...j]不满足条件的情况，j向右扩的过程停止，此时 arr[i...j-2], arr[i...j-3]...arr[i,i]一定都是满足条件的。
> 
> 即，所有必须以 arr[i] 作为第一个元素的子数组，满足条件为 j - i 个，令 res += j-i

* 3.进行完步骤2后，令 i 向右移动1个位置，并对 qmax 和 qmin 做出相应更新。qmax 和 qmin从原来的 arr[i...j] 变成 arr[i+1...j]窗口的最大值和最小值的更新结构。 重复步骤2
> 也就是求所有必须以 arr[i+1] 作为第1个元素的子数组中，满足条件的数量有多少个。
    
* 4.根据步骤2和步骤3，依次求出:
  * 必须以 arr[0]开头的子数组，满足条件的数量有多少个
  * 必须以 arr[1]开头的子数组，满足条件的数量有多少个
  * 必须以 arr[2]开头的子数组，满足条件的数量有多少个
  * ...
    

上述过程中，所有的下标值最多进 `qmax` 和 `qmin` 一次，出 `qmax` 和 `qmin` 一次。 i 和 j 的值也不断增加，并且从来不减小，所以整个过程的时间复杂度为 O(N)。
