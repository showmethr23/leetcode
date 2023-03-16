class Solution {
    public int lengthOfLongestSubstring(String s) {
        // Solution 1
        //Using ArrayList

        List<Character> sub = new ArrayList<>();
        int res = 0;
        if (s.length() == 0){
            return 0;
        }
        if (s.length() == 1){
            return 1;
        }

        for(int right = 0; right < s.length(); right++) {
            if(sub.contains(s.charAt(right))) { 
                // get the index of the char
                int index = sub.indexOf(s.charAt(right));
                sub.remove(index);
                if(index > 0)
                    sub.subList(0, index).clear();
            }
            sub.add(s.charAt(right));
            res = Math.max(res, sub.size());
        }
        return res;

        
        // Solution 2
        // Using Hashset

        Set<Character> set = new HashSet<>();
        int res = 0;
        int l = 0;
        int n = s.length();

        // base case
        if (n == 0){
            return 0;
        }

        if (n == 1){
            return 1;
        }

        for (int r = 0; r < n; r++){

            if (!set.contains(s.charAt(r))){
                set.add(s.charAt(r));
                res = Math.max(res, r - l + 1);
            }
            else{
                while (s.charAt(l)!=s.charAt(r)){
                    set.remove(s.charAt(l));
                    l++;
                }
                set.remove(s.charAt(l));
                l++;
                set.add(s.charAt(r));
            }
        }
        return res;
    }
}