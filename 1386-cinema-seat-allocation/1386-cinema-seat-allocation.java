import java.util.*;

class Solution {
    public int maxNumberOfFamilies(int n, int[][] reservedSeats) {

        Map<Integer, List<Integer>> map = new TreeMap<>();

        for(int[] i: reservedSeats){
            if(!map.containsKey(i[0]) && i[1] != 1 && i[1] != 10){
                map.put(i[0], new ArrayList<>());
            }

            if(map.containsKey(i[0]) && i[1] != 1 && i[1] != 10){
                map.get(i[0]).add(i[1]);
                Collections.sort(map.get(i[0]));
            }
        }

        int answer = (n - map.keySet().size()) * 2;
        
        for(int row : map.keySet()){
            int index = 2;
            int count = 0;
            for(int j = index; j <= 9; j++){
                List<Integer> col = map.getOrDefault(row, null);

                if(col != null && !col.isEmpty() && col.get(0) == j){
                    count = 0;
                    col.remove(0);

                    if(j <= 3){
                        j = 3;
                        col.removeIf(a -> a < 4);
                    } else if(j > 3 && j <= 5){
                        j = 5;
                        col.removeIf(a -> a < 6);
                    } else {
                        j = 7;
                        col.removeIf(a -> a < 8);
                    }

                    continue;
                }

                count++;

                if(count >= 4){
                    answer++;
                    count = 0;            
                }
            }
        }
        return answer;
    }
}