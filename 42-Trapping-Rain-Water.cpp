#include <vector>

class Solution {
public:
    int trap(std::vector<int>& height) {
      int totalVol = 0;
      int rightMax = -1, leftMax = -1;
      int left = 0, right = height.size() - 1;
      while (left <= right) {
          if (height[left] < height[right]) {
              if (height[left] > leftMax) {
                  leftMax = height[left];
              } else {
                  totalVol += leftMax - height[left];
              }
              left++;
          } else {
              if (height[right] > rightMax) {
                  rightMax = height[right];
              } else {
                  totalVol += rightMax - height[right];
              }
              right--;
          }
      }
      return totalVol;
    }
};