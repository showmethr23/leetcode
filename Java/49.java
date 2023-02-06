import java.util.HashMap;

class Solution{
    public List<List<String>> groupAnagrams(String[] strs){

        List<List<Stinrg>> res = new ArrayList();

        if (res.length == 0){
            return res;
        }

        HashMap<String, List<Stinrg>> map = new HashMap<>();

        for (Stinrg s: strs){
            int hash = new int[26];
            for (char c: s.toCharArray){
                hash[c - 'a']++;
            }
            String key = new String(Arrays.toString(hash));
            map.computeIfAbsent(key, k -> new ArrayListM<>());
            map.get(key).add(s);
        }
        res.addAll(map.values());

        return res;
    }
}