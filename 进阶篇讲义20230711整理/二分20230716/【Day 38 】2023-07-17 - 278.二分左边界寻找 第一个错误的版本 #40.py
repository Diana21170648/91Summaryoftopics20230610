【Day 38 】2023-07-17 - 278. 第一个错误的版本 #40
Open
azl397985856 opened this issue 11 hours ago · 5 comments
Comments
@azl397985856
azl397985856 commented 11 hours ago
278. 第一个错误的版本
入选理由
暂无

题目地址
https://leetcode-cn.com/problems/first-bad-version

前置知识
二分法
题目描述
你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

示例:

给定 n = 5，并且 version = 4 是第一个错误的版本。

调用 isBadVersion(3) -> false
调用 isBadVersion(5) -> true
调用 isBadVersion(4) -> true

所以，4 是第一个错误的版本。

@Diana21170648
Diana21170648 commented now
思路
二分找左边界

代码
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r=1,n
        while l<=r:
            mid=(l+r)//2
            if isBadVersion(mid):
                r=mid-1
            else:
                l=mid+1
        return l

复杂度分析

时间复杂度：O(logN)，其中 N 为数组长度。
空间复杂度：O(1)

@azl397985856 azl397985856 added 二分 38 labels 11 hours ago
@freesan44
freesan44 commented 3 hours ago
/**
 * The knows API is defined in the parent class VersionControl.
 *     func isBadVersion(_ version: Int) -> Bool{}
 */

class Solution : VersionControl {
    func firstBadVersion(_ n: Int) -> Int {
        var l = 1
    var r = n
    
    while l <= r {
        let mid = (l + r) / 2
        
        if isBadVersion(mid) {
            // 收缩
            r = mid - 1
        } else {
            l = mid + 1
        }
    }
    
    return l
    }
}
@Master-guang
Master-guang commented 1 hour ago
var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    return function(n) {
        let left = 1, right = n;
        while(left <= right) {
            let mid = Math.floor(left + (right - left) / 2);
            if(isBadVersion(mid)) {
                right = mid - 1
            } else {
                left = mid + 1
            }
        }
        return left
    };
};
@mo660
mo660 commented 1 hour ago
class Solution {
public:
    int firstBadVersion(int n) {
        int l = 1;
        int r = n;
        while(l < r){
            int mid = l + (r - l)/2;
            if (isBadVersion(mid)){
                r = mid;
            }else {
                l = mid + 1;
            }
        }
        return l ;
    }
};
@GuitarYs
GuitarYs commented 1 hour ago
class Solution:
    def __init__(self):
        self.bad_version = 0

    def isBadVersion(self, version):
        # 调用API接口，判断版本是否出错
        pass

    def firstBadVersion(self, n):
        left = 1
        right = n

        while left < right:
            mid = left + (right - left) // 2
            if self.isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left
