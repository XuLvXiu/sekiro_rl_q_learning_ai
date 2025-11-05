#encoding=utf8

import cv2
import numpy as np

class Posture(): 
    def __init__(self, blood_gray_min=100, blood_gray_max=140): 
        self.blood_gray_min = blood_gray_min
        self.blood_gray_max = blood_gray_max

        gray = cv2.imread('./self.gray.player posture window.png', cv2.IMREAD_GRAYSCALE)
        if True: 

            # posture bar is symmetrical, we only use the first half, but the reserved one.
            middle_row = np.flip(gray[gray.shape[0] // 2, 0:gray.shape[1] // 2])
            print('middle_row: ', middle_row)
            self.full_count = len(middle_row)
            first_pixel = middle_row[0]
            # how to check if there is a posture bar?
            # print(self.debug_name)
            arr_index = np.where(middle_row < self.blood_gray_min)[0]
            if arr_index.size == 0: 
                arr_index = np.where(middle_row > self.blood_gray_max)[0]
                if arr_index.size > 15: 
                    self.hp_count = 0
                    self.status = 0
                    return

                self.hp_count = self.full_count
                self.status = 100
                return

            self.hp_count = arr_index[0]
            self.status = (self.hp_count / self.full_count) * 100
p = Posture()
print(p.status)
