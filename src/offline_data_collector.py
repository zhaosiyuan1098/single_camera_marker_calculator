from transform_matrix_calculator import TransformMatrixCalculator
import cv2.aruco as aruco
import numpy as np
import time
import sys

CAMERA_RESOLUTION_X = 1280
CAMERA_RESOLUTION_Y = 720
CAMERA_FRAME_RATE=30
RANGE=1000

def main():

    aruco_dict_5 = aruco.getPredefinedDictionary(aruco.DICT_5X5_50)
    transform_matrix_calculator = TransformMatrixCalculator()

    transform_matrix_array = np.zeros((RANGE,4,4))
    start_timne_array=np.zeros((RANGE,1))
    end_time_array=np.zeros((RANGE,1))

    for i in range(RANGE):
        start_timne_array[i]=time.time()
        transform_matrix_array[i] = transform_matrix_calculator.calculate_transform_matrix(aruco_dict_5, CAMERA_RESOLUTION_X, CAMERA_RESOLUTION_Y, CAMERA_FRAME_RATE)
        end_time_array[i]=time.time()
        
    save_path='../data/transform_matrix_'+str(sys.argv[1])+'.npy'
    np.save(save_path, transform_matrix_array)
    save_path='../data/start_time_'+str(sys.argv[1])+'.npy'
    np.save(save_path, start_timne_array)
    save_path='../data/end_time_'+str(sys.argv[1])+'.npy'
    np.save(save_path, end_time_array)
    
def test():
    transform_matrix_array = np.zeros((RANGE,4,4))
    start_timne_array=np.zeros((RANGE,1))
    end_time_array=np.zeros((RANGE,1))
    
    transform_matrix_array[1]=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[0,0,0,1]])
    print(transform_matrix_array[1])
    
    
test()
    


