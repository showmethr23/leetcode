class Solution{
    public int longestConsecutive(int[] nums){

        // base case
        if (nums.length == 0){
            return 0;
        }

        if (nums.length == 1){
            return 1;
        }

        Arrays.sort(nums);
        int curr = 1;
        int longest = 1;

        for (int i = 1; i < nums.length; i++){
            if (nums[i] != nums[i-1]){

                if(nums[i] == nums[i-1] + 1){
                    curr++;
                }
                else{
                    longest = Math.max(curr, longest);
                    curr = 1;
                }

            }
        }
        return Math.max(longest, curr);

    }
}