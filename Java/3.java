class Solution {
    public int lengthOfLongestSubstring(String s) {
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
    }
}