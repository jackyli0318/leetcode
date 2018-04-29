class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        last_index = len(nums)-1
        if last_index == 0:
            return 0
        # if len(set(nums[:-1]))==1 and nums[0]==1:
            # return last_index
        if nums[0] >= last_index:
            return 1
        
        f = [last_index]
        
        max_steps = 0
        
        
        cur_len = len(f)
#        print(len(nums))
#        print(last_index)
        
        # [1,3,3,2,1,4] pop4 3,2,1   len=1   pop1  2,3,3  len=2   pop2  3,3 len=2   pop3   3,2  len=2   2,3,3
        #  0 1 2 3 4 5
        '''
        {
            "len1": 4,3,2
            "len2": 3,2,1, 2,1, 1
            "len3": 0
        }
        
        '''
        
        
        index = 0
        if nums[index] == 1:
            while(nums[index]==1):
                print(index)
                index += nums[index]
                max_steps += 1
                print(index)
                if index >= last_index:
                    return max_steps
        else:
            index += nums[index]
            max_steps += 1
            
        while(len(f)>0):
            # 总能到终点
            max_steps += 1
            
            while(cur_len>0):
                cur_len -= 1
                
                print(f)
                target=f.pop(0)

                for i in range(target-1, -1, -1):
                    jump_dis = nums[i]
                    if i+jump_dis>=target:
                        if i not in f:
                            f.append(i)
                        if i == 0:
                            return max_steps
                        if i <= index:
                            return max_steps
                        # if i <= nums[0]:
                            # return max_steps + 1

            
            cur_len = len(f)
                    
        return max_steps
s = Solution()
a = [2,2,3,1,5]

print(s.jump(a))