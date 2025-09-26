#PERSONAL COMMENT
#THE COMMENTS MUST BE UPDATED
# AND BE WELL COMMENTED OUT

#INPUT MATRIX FOR THE SUBSQUARE PRINTING OUT FUNCTION
bi_matrix = [   [1,2,3,4,5,6,7,8], 
                [2,3,3,4,5,6,7,8],
                [1,2,5,4,5,6,7,8],
                [1,2,21,4,5,6,7,8], 
                [1,2,3,77,5,6,7,8],
                [1,2,3,77,5,6,7,8],
                [1,2,3,77,5,6,7,8],
                [1,2,3,77,5,6,7,8],
                ]
            
#THE INITAL LENGTH OF THE SQUARE MATRIX
bi_matrix_length = len(bi_matrix[0])

#VERTIXES ARRAY NEEDED TO DEFINE THE VERTEXES OF THE SUBSQUARE TO CALCULATE
# AND INITIALLY USED FOR THE FULL SQUARE MATRIX
vertexes = [[0,0],[0, bi_matrix_length-1],[bi_matrix_length-1, bi_matrix_length-1], [bi_matrix_length-1, 0]]

#ROUND UPDATED LENGTH OF THE CALCULED MATRIX
actual_length = bi_matrix_length

#LOOP TO DEFINE THE OPERATIONS EVERY TWO STEPS FOR EVERY TWO NUMBERS OF THE SQUARE SUBMATRIX
for loop in range(0, (int(actual_length/2) + actual_length % 2)):
    print(f"Number of the main loop: {loop+1}")
    #FOR LOOP FOT THE 4 EDGES OF THE SQUARE MATRIX
    for i in range(0,4):
        #FOR EVERY NUMBER OF AN EDGE
        for j in range(0, actual_length):
            if i == 0:
                print(bi_matrix[vertexes[0][0]][vertexes[0][1]])
                vertexes[0][1] = vertexes[0][1] + 1
            elif i == 1:
                print(bi_matrix[vertexes[1][0]][vertexes[1][1]])
                vertexes[1][0] = vertexes[1][0] + 1
            elif i == 2:
                print(bi_matrix[vertexes[2][0]][vertexes[2][1]])
                vertexes[2][1] = vertexes[2][1] - 1
            elif i == 3:
                print(bi_matrix[vertexes[3][0]][vertexes[3][1]])
                vertexes[3][0] = vertexes[3][0] - 1
    #UPDATE THE POSITION OF THE VERTEXES FOR THE NEXT MAIN LOOP 
    vertexes[0][0] = vertexes[0][0] + 1
    vertexes[0][1] = vertexes[0][1] - actual_length + 1
    vertexes[1][0] = vertexes[1][0] - actual_length + 1
    vertexes[1][1] = vertexes[1][1] - 1
    vertexes[2][0] = vertexes[2][0] - 1
    vertexes[2][1] = vertexes[2][1] + actual_length - 1
    vertexes[3][0] = vertexes[3][0] + actual_length - 1
    vertexes[3][1] = vertexes[3][1] + 1
    #UPDATE THE ACTUAL LENGTH OF THE SQUARE SUBMATRIX
    actual_length = actual_length - 2
    