class Solution{
    public int[] getConcatenation(int[] nums){

        // Solution 1
        // Using Modulo
        
        int n = nums.length;
        int[] ans = new int[n*2];

        // base case
        if ( n == 0){
            return ans;
        }

        for (int i = 0; i < n*2; i++){
            ans[i] = nums[i%n];
        }

        return ans
    }
}
