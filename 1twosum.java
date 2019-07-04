int是基本数据类型， Integer是引用数据类型；
Integer是int的包装类，int的初值为0，Integer的初值为null;


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