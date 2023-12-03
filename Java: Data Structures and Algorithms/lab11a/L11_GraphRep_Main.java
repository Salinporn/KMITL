import java.util.Arrays;

public class L11_GraphRep_Main {
    final static int inf = Integer.MAX_VALUE;
    // A B C D E F
    static int[][] distanceBetween = {
            { 0, 4, 5, inf, inf, inf },
            { 4, 0, 11, 9, 7, inf },
            { 5, 11, 0, inf, 3, inf },
            { inf, 9, inf, 0, 13, 2 },
            { inf, 7, 3, 13, 0, 6 },
            { inf, inf, inf, 2, 6, 0 }
    };

    public static void main(String[] args) {
        q3();
    }

    static void q3() {
        int A, B, C, D, E, F;
        A = 0;
        B = 1;
        C = 2;
        D = 3;
        E = 4;
        F = 5;
        System.out.println("dijkstra from A");
        dijkstra(distanceBetween, A);
    }

    // static void dijkstra(int[][] graph, int source) {
    //     int[] distance = initialize_distance_from_source(graph.length, source);
    //     boolean[] visited = new boolean[graph.length];
    //     while (moreCityToExplore(visited)) {
    //         int exploring = nextExplore(visited, distance);
    //         // dijkstra details
    //         visited[exploring] = true;
    //         System.out.println("exploring " + exploring + " " + Arrays.toString(distance));
    //     } // while
    // }

    private static int[] initialize_distance_from_source(int numCities, int source) {
        int[] distance = new int[numCities];
        for (int i = 0; i < numCities; i++)
            distance[i] = Integer.MAX_VALUE;
        /* your code 2 */ distance[source] = 0; // start from source!!
        return distance;
    }

    private static boolean moreCityToExplore(boolean[] visited) {
        for (int i = 0; i < visited.length; i++)
            if (!visited[i])
                return /* your code 3 */ true;
        return /* your code 4 */ false;
    }

    // private static int nextExplore(boolean[] visited, int[] dist) {
    //     int city_index = -1;
    //     int random_index = -1;
    //     while (city_index < 0) {
    //         random_index = (int) (Math.random() * 100) % visited.length;
    //         if (!visited[random_index])
    //             city_index = random_index;
    //     }
    //     /* your code 5 */
    //     return city_index;
    // }

    private static int nextExplore(boolean[] visited, int[] dist) {
        int min_val = Integer.MAX_VALUE;
        int i = 0;
        for (int x = 0; x < dist.length; x++) {
            if (visited[x] == false && dist[x] < min_val) {
                i = x;
                min_val = dist[x];
            }
        }
        /* your code 5 */
        // System.out.println(i);
        return (i);
    }

    static void dijkstra(int[][] graph, int source) {
        int[] distance = initialize_distance_from_source(graph.length, source);
        int[] prev = new int[distance.length];
        boolean[] visited = new boolean[graph.length];
        while (moreCityToExplore(visited)) {
            int exploring = nextExplore(visited, distance);
            boolean neighbor_of_exploring = false;
            for (int x = 0; x < distance.length; x++) {
                neighbor_of_exploring = 0 < distanceBetween[exploring][x] && distanceBetween[exploring][x] < inf;
                if (neighbor_of_exploring) { // x is neighbor
                    if (distance[x] /* your code 6 */ > distance[exploring] + distanceBetween[exploring][x]) {
                        distance[x] /* your code 7 */ = distance[exploring] + distanceBetween[exploring][x];
                        prev[x] = exploring;
                    }
                }
            }
            visited[exploring] = true;
            System.out.println("exploring " + exploring + " " + Arrays.toString(distance));
        } // while
        System.out.println("prev " + Arrays.toString(prev));
    }
}