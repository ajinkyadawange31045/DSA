class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        # for i in range(len(image)):
        #     image[i].reverse()
        # print(image)
        # for i in range(len(image)):
        #     for j in range(len(image[0])):
        #         if image[i][j] == 1:
        #             image[i][j] = 0
        #         else:
        #             image[i][j] = 1
        # return image



        # return [[0 if x==1 else 1 for x in x][::-1] for x in image] 


        
        for i in range(len(image)):
            image[i] = image[i][::-1]
            image[i] = [1 if x ==0 else 0 for x in image[i]]
        return image
            