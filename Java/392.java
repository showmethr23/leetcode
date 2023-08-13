class Solution{
    public boolean isSubsequence(String s, String t){
    
        // Solution 1

        // base case
        if (s.length() <= 0){
            return true;
        }

        if (t.length() < s.length()){
            return false;
        }

        int subs = 0;

        for (int i = 0; i <= t.length()-1; i++){
            if (subs <= s.length()-1){
                if (s.charAt(subs) == t.charAt(i)){
                    subs++;
                }
            }
        }

        if (s.length() == subs){
            return true;
        }

        return false;

    }
}
