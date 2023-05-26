import rospy
from home_robot.ros.grasp_helper import GraspClient
from data import load_available_input_data

rospy.init_node('test_grasping')
#p = "stretch_2022_09_14-12_51_59.npy"
#p = "stretch_2022_09_18-16_21_37.npy"
p = "stretch_2022_09_19-09_11_47.npy"
segmap, rgb, depth, cam_K, pc_full, pc_colors = load_available_input_data(p, K=None)

# TODO remove debug code
# print(segmap)
# print(pc_full)
# print(pc_colors)

client = GraspClient()
client.request(pc_full, pc_colors, segmap, frame="camera_color_optical_frame")
