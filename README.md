# Algo2. Home work 3
## "Graphs and Trees"

### Task 1. Application of Maximum Flow Algorithm for Goods Logistics

Develop a program for modeling a flow network for goods logistics from warehouses to stores using the maximum flow algorithm. Analyze the obtained results and compare them with theoretical knowledge.

#### Task Description

Build a graph model representing the flow network as shown in the following image:

Connections and capacities in the graph are as follows:

| From        | To          | Capacity (units) |
|-------------|-------------|------------------|
| Terminal 1  | Warehouse 1 | 25               |
| Terminal 1  | Warehouse 2 | 20               |
| Terminal 1  | Warehouse 3 | 15               |
| Terminal 2  | Warehouse 3 | 15               |
| Terminal 2  | Warehouse 4 | 30               |
| Terminal 2  | Warehouse 2 | 10               |
| Warehouse 1 | Store 1     | 15               |
| Warehouse 1 | Store 2     | 10               |
| Warehouse 1 | Store 3     | 20               |
| Warehouse 2 | Store 4     | 15               |
| Warehouse 2 | Store 5     | 10               |
| Warehouse 2 | Store 6     | 25               |
| Warehouse 3 | Store 7     | 20               |
| Warehouse 3 | Store 8     | 15               |
| Warehouse 3 | Store 9     | 10               |
| Warehouse 4 | Store 10    | 20               |
| Warehouse 4 | Store 11    | 10               |
| Warehouse 4 | Store 12    | 15               |
| Warehouse 4 | Store 13    | 5                |
| Warehouse 4 | Store 14    | 10               |

Apply the maximum flow algorithm to solve the problem. Write a program that implements the Edmonds-Karp algorithm, or use an already implemented version to find the maximum flow in the constructed graph. Analyze the obtained result. Has the optimal flow been achieved, and what does this mean for the considered network?

Prepare a report with calculations and explanations. Explain which vertices and edges were chosen, how they correspond to real elements of the logistics system. Show step-by-step calculation of the maximum flow and explain the logic of each step.

#### Technical Requirements

1. Use the Edmonds-Karp algorithm for implementing maximum flow.

2. Graph construction must match the given structure with 20 vertices and specified capacities.

#### Requirements

1. The program correctly performs the maximum flow calculation and returns accurate results.

2. Data is correctly added to the graph and matches the given logistics network structure.

3. Explanations and analysis are clear and clearly reflect the algorithm's logic.

4. The report includes analysis of the obtained results.

#### After obtaining the table, answer the following questions:

1. Which terminals provide the largest flow of goods to stores?

2. Which routes have the smallest capacity and how does this affect the total flow?

3. Which stores received the least goods and can their supply be increased by increasing the capacity of certain routes?

4. Are there bottlenecks that can be eliminated to improve the efficiency of the logistics network?

Solution is in file `task1.ipynb`

### Task 2. Comparison of `OOBTree` and Dictionary Efficiency for Range Queries

Develop a program to store a large dataset of products in two data structures — `OOBTree` and `dict` — and conduct a comparative analysis of their performance for executing range queries.

#### Task Description

1. Use the provided file generated_items_data.csv to load product information. Each product includes a unique identifier ID, name Name, category Category, and price Price.

2. Implement two structures for storing products. First — OOBTree from the BTrees library, where the key is ID and the value is a dictionary with product attributes. Second — dict (standard dictionary), where the key is also ID and the value is a similar dictionary with product attributes.

3. Create functions for adding products to both structures: add_item_to_tree and add_item_to_dict.

4. Create functions for executing a range query to find all products within a specified price range: range_query_tree and range_query_dict.

5. Measure the total execution time of the range query for each structure using timeit.

6. Execute the range query 100 times for each structure to calculate the average execution time.

7. Output the total execution time of the range query for each structure, specifically, how long it takes to execute 100 queries for OOBTree and dict.

#### Technical Requirements

1. Use only OOBTree and standard dict for comparison.

2. Implement separate functions for adding a product to the structure: add_item_to_tree, add_item_to_dict.

3. Implement separate functions for range query: range_query_tree, range_query_dict.

4. Use the timeit library for accurate performance measurement of each structure.

5. Time measurement must be performed for 100 range queries for each structure.

#### Acceptance Criteria

1. The program correctly executes the range query and returns accurate results for both structures: OOBTree and dict.

2. Data is correctly added to each structure.

3. OOBTree uses the items(min, max) method for fast access to range values.

4. Dictionary dict implements range query using linear search.

5. Comparative results of execution time for OOBTree and dict are correctly output.

6. OOBTree is expected to show better results for range queries due to its sorted data structure.

7. Output of results includes the total execution time of the range query for each structure with the format:

```
Total range_query time for OOBTree: X.XXXXXX seconds
Total range_query time for Dict: X.XXXXXX seconds
```