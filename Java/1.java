class Solution:{
    public int[] twoSum(int[] nums, int target){
        /*
         * 1. create a hashmap to store numbers in nums
         * 2. using for loop to compare the difference between target and difference of two numbers
         * 3. if matches then return indices of them
         */

        
        HashMap<Integer, Integer> hash = new HashMap<Integer,Integer>();

        for (int i = 0, i < nums.length; i++){
            int diff = target - nums[i];

            if (hash.containsKey(diff)){
                return new int[] {hash.get(diff)};
            }

            hash.put(nums[i], i);
        }
        return new int[] {};

    }
}