import java.util.*;

class Graph {
    private Map<Integer, List<Integer>> graph;

    public Graph() {
        this.graph = new HashMap<>();
    }

    public void addEdge(int u, int v) {
        graph.computeIfAbsent(u, k -> new ArrayList<>()).add(v);
    }

    public void dfs(int start, boolean[] visited, boolean leftToRight) {
        visited[start] = true;
        System.out.print(start + " ");

        List<Integer> neighbors = new ArrayList<>(graph.getOrDefault(start, Collections.emptyList()));
        neighbors.sort(leftToRight ? Comparator.naturalOrder() : Comparator.reverseOrder());

        for (int neighbor : neighbors) {
            if (!visited[neighbor]) {
                dfs(neighbor, visited, leftToRight);
            }
        }
    }

    public void bfs(int start, boolean leftToRight) {
        boolean[] visited = new boolean[graph.size() + 1];
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(start);
        visited[start] = true;

        while (!queue.isEmpty()) {
            int current = queue.poll();
            System.out.print(current + " ");

            List<Integer> neighbors = new ArrayList<>(graph.getOrDefault(current, Collections.emptyList()));
            neighbors.sort(leftToRight ? Comparator.naturalOrder() : Comparator.reverseOrder());

            for (int neighbor : neighbors) {
                if (!visited[neighbor]) {
                    queue.offer(neighbor);
                    visited[neighbor] = true;
                }
            }
        }
    }

    public boolean isBipartite(int start) {
        int[] colors = new int[graph.size() + 1];
        Arrays.fill(colors, -1);
        colors[start] = 0;

        Queue<Integer> queue = new LinkedList<>();
        queue.offer(start);

        while (!queue.isEmpty()) {
            int current = queue.poll();

            List<Integer> neighbors = new ArrayList<>(graph.getOrDefault(current, Collections.emptyList()));

            for (int neighbor : neighbors) {
                if (colors[neighbor] == -1) {
                    colors[neighbor] = 1 - colors[current];
                    queue.offer(neighbor);
                } else if (colors[neighbor] == colors[current]) {
                    System.out.println("Cycle discovered while checking bipartiteness: " + current + " - " + neighbor);
                    return false; // Not bipartite
                }
            }
        }

        return true; // Bipartite
    }
    public static void main(String[] args) {
        Graph graph = new Graph();
        int[][] edges = {{1, 3}, {1, 4}, {2, 1}, {2, 3}, {3, 4}, {4, 1}, {4, 2}};

        for (int[] edge : edges) {
            graph.addEdge(edge[0], edge[1]);
        }

        System.out.println("DFS Left to Right:");
        graph.dfs(1, new boolean[graph.graph.size() + 1], true);
        System.out.println();

        System.out.println("DFS Right to Left:");
        graph.dfs(1, new boolean[graph.graph.size() + 1], false);
        System.out.println();

        System.out.println("BFS Left to Right:");
        graph.bfs(1, true);
        System.out.println();

        System.out.println("BFS Right to Left:");
        graph.bfs(1, false);
        System.out.println();

        if (graph.isBipartite(1)) {
            System.out.println("The graph is bipartite.");
        } else {
            System.out.println("The graph is not bipartite.");
        }
    }
}
