# 0 = intermediate
# 1 = specifically active
# 2 = specifically not active

OR_data = [
          # [1,0] = 1
           [[[1,0,0],
             [0,0,0],
             [0,0,0]],

            [[0,0,0],
             [0,0,1],
             [0,0,0]]],
            
          # [0,1] = 1
           [[[0,0,0],
             [0,0,0],
             [1,0,0]],

            [[0,0,0],
             [0,0,1],
             [0,0,0]]],
            
          # [1,1] = 1
           [[[1,0,0],
             [0,0,0],
             [1,0,0]],

            [[0,0,0],
             [0,0,1],
             [0,0,0]]]
             ]
AND_data = [
          # [1,0] = 0
           [[[1,0,0],
             [0,0,0],
             [0,0,0]],

            [[0,0,0],
             [0,0,2],
             [0,0,0]]],
            
          # [0,1] = 0
           [[[0,0,0],
             [0,0,0],
             [1,0,0]],

            [[0,0,0],
             [0,0,2],
             [0,0,0]]],
            
          # [1,1] = 1
           [[[1,0,0],
             [0,0,0],
             [1,0,0]],

            [[0,0,0],
             [0,0,1],
             [0,0,0]]]
             ]

XOR_data = [
          # [1,0] = 1
           [[[1,0,0],
             [0,0,0],
             [0,0,0]],

            [[0,0,0],
             [0,0,1],
             [0,0,0]]],
            
          # [0,1] = 1
           [[[0,0,0],
             [0,0,0],
             [1,0,0]],

            [[0,0,0],
             [0,0,1],
             [0,0,0]]],
            
          # [1,1] = 0
           [[[1,0,0],
             [0,0,0],
             [1,0,0]],

            [[0,0,0],
             [0,0,2],
             [0,0,0]]]
             ]

