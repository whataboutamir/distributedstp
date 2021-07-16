# Topology without a loop, already a spanning tree!
# 1 --- 2 --- 3 --- 4
# |           |     
# |           |     
# 5     6 --- 7 --- 8
# |     |           |
# |     |           |
# 9     10 -- 11    12
#       |     
#       |        
#       13

topo = { 1 : [2, 5], 
         2 : [1, 3],
         3 : [2, 7, 4], 
         4 : [3],
         5 : [1, 9], 
         6 : [7, 10],
         7 : [3, 6, 8],
         8 : [7, 12], 
         9 : [5],
         10: [6, 11, 13],
         11: [10],
         12: [8],
         13: [10] }