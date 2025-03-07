import zarr
import numpy as np
import visualizer
# 假设save_dir是Zarr存储的目录路径
save_dir = 'C:\\Users\\zxc26\\Downloads\\dp3_real_robot_demo\\real_robot_demo\\dumpling_new_40demo_1024.zarr'

# 打开Zarr存储
zarr_root = zarr.open_group(save_dir, mode='r')

# 访问数据组和元数据组
zarr_data = zarr_root['data']
zarr_meta = zarr_root['meta']

# 读取数据
img_arrays = zarr_data['img'][:]
state_arrays = zarr_data['state'][:]
point_cloud_arrays = zarr_data['point_cloud'][:]
depth_arrays = zarr_data['depth'][:]
action_arrays = zarr_data['action'][:]
episode_ends_arrays = zarr_meta['episode_ends'][:]

#转换成np
# my_array = np.array(img_arrays)
# 现在你可以使用这些数组进行进一步的处理或分析
# 例如，打印第一个图像数组的形状
print(type(img_arrays))
print(type(state_arrays))
print(type(point_cloud_arrays))
print(type(depth_arrays))
print(type(action_arrays))
print(episode_ends_arrays)
print(img_arrays.shape)
print(state_arrays.shape)
print(point_cloud_arrays.shape)
print(depth_arrays.shape)
print(action_arrays.shape)
print(episode_ends_arrays.shape)
# 或者访问特定的数据片段
# 例如，获取第一个图像
# first_img = img_arrays[0]

#点云可视化
# pointexample=point_cloud_arrays[50]
# visualizer.visualize_pointcloud(pointexample)