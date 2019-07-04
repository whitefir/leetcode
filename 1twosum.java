int�ǻ����������ͣ� Integer�������������ͣ�
Integer��int�İ�װ�࣬int�ĳ�ֵΪ0��Integer�ĳ�ֵΪnull;


class Solution{
    public int[] twoSum(int nums, int target)
    {
        Map<Integer, Integer> map= new HashMap<>();
        for (int i=0; i<nums.length; i++)
        {
            int comp=target-nums[i];
            if(map.containsKey(comp))
            {
                return new int[] {i, map.get(comp)}
            }
            map.put(nums[i],i);//map[value]=seq
        }
        throw new IllegalArgumentException("no solution");
    }
}