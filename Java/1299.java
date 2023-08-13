class Solution{
    public int[] replaceElements(int[] arr) {
        
        // Solution 1

        // base case
        if (arr.length){
            return arr;
        }

        int rightmax = -1;

        for (int i = arr.length; i >= 0; i--){
            temp = Math.max(rightmax, arr[i]);
            arr[i] = rightmax;
            rightmax = temp
        }
        return arr;
    }
}
