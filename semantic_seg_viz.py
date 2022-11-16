import os
import open3d as o3d
import open3d.ml as _ml3d
import open3d.ml.torch as ml3d
from time import sleep

import numpy as np

import glob
	

def load_custom_dataset(dataset_path):
	print("Loading custom dataset")
	pcd_paths = glob.glob(dataset_path+"/*.pcd")
	pcds = []
	for pcd_path in pcd_paths:
		pcds.append(o3d.io.read_point_cloud(pcd_path))
	return pcds


def prepare_point_cloud_for_inference(pcd):
	# Remove NaNs and infinity values
	pcd.remove_non_finite_points()
	# Extract the xyz points
	xyz = np.asarray(pcd.points)
	# Set the points to the correct format for inference
	data = {"point":xyz, 'feat': None, 'label':np.zeros((len(xyz),), dtype=np.int32)}

	return data, pcd

def load_point_cloud_for_inference(file_path, dataset_path):
	pcd_path = dataset_path + "/" + file_path
	# Load the file
	pcd = o3d.io.read_point_cloud(pcd_path)
	# Remove NaNs and infinity values
	pcd.remove_non_finite_points()
	# Extract the xyz points
	xyz = np.asarray(pcd.points)
	# Set the points to the correct format for inference
	data = {"point":xyz, 'feat': None, 'label':np.zeros((len(xyz),), dtype=np.int32)}

	return data, pcd

# Class colors, RGB values as ints for easy reading
COLOR_MAP = {
    0: (0, 0, 0),
    1: (245, 150, 100),
    2: (245, 230, 100),
    3: (150, 60, 30),
    4: (180, 30, 80),
    5: (255, 0., 0),
    6: (30, 30, 255),
    7: (200, 40, 255),
    8: (90, 30, 150),
    9: (255, 0, 255),
    10: (255, 150, 255),
    11: (75, 0, 75),
    12: (75, 0., 175),
    13: (0, 200, 255),
    14: (50, 120, 255),
    15: (0, 175, 0),
    16: (0, 60, 135),
    17: (80, 240, 150),
    18: (150, 240, 255),
    19: (0, 0, 255),
}

# ------ for custom data -------
kitti_labels = {
    0: 'unlabeled',
    1: 'car',
    2: 'bicycle',
    3: 'motorcycle',
    4: 'truck',
    5: 'other-vehicle',
    6: 'person',
    7: 'bicyclist',
    8: 'motorcyclist',
    9: 'road',
    10: 'parking',
    11: 'sidewalk',
    12: 'other-ground',
    13: 'building',
    14: 'fence',
    15: 'vegetation',
    16: 'trunk',
    17: 'terrain',
    18: 'pole',
    19: 'traffic-sign'
}

# Convert class colors to doubles from 0 to 1, as expected by the visualizer
for label in COLOR_MAP:
	COLOR_MAP[label] = tuple(val/255 for val in COLOR_MAP[label])

# Load an ML configuration file
cfg_file = '/home/brian/miniconda3/envs/ml3d/lib/python3.10/site-packages/open3d/_ml3d/configs/randlanet_semantickitti.yml'
cfg = _ml3d.utils.Config.load_from_file(cfg_file)

# Load the RandLANet model
model = ml3d.models.RandLANet(**cfg.model)
# Add path to the SemanticKitti dataset and your own custom dataset
cfg.dataset['dataset_path'] = '/home/brian/Desktop/3d/SemanticKitti'
# cfg.dataset['custom_dataset_path'] = './pcds'

# Load the datasets
dataset = ml3d.datasets.SemanticKITTI(cfg.dataset.pop('dataset_path', None), **cfg.dataset)
# custom_dataset = load_custom_dataset(cfg.dataset.pop('custom_dataset_path', None))

# Create the ML pipeline
pipeline = ml3d.pipelines.SemanticSegmentation(model, dataset=dataset, device="gpu", **cfg.pipeline)

# Download the weights.
ckpt_folder = "./logs/"
os.makedirs(ckpt_folder, exist_ok=True)
ckpt_path = ckpt_folder + "randlanet_semantickitti_202201071330utc.pth"
randlanet_url = "https://storage.googleapis.com/open3d-releases/model-zoo/randlanet_semantickitti_202201071330utc.pth"
if not os.path.exists(ckpt_path):
    cmd = "wget {} -O {}".format(randlanet_url, ckpt_path)
    os.system(cmd)

# Load the parameters of the model.
pipeline.load_ckpt(ckpt_path=ckpt_path)

results = []
data_set = []

for i in range(0,20):
    test_split = dataset.get_split("test")
    data_sample = test_split.get_data(i)
    data_set.append(data_sample)
    results.append(pipeline.run_inference(data_sample))

vis = o3d.visualization.Visualizer()
vis.create_window()
vis.get_render_option().point_size = 2.0
vis.get_render_option().background_color = np.asarray([1.0, 1.0, 1.0])

pcd = o3d.geometry.PointCloud()
xyz = data_set[0]["point"] # Get the points
pcd.points = o3d.utility.Vector3dVector(xyz)
colors = [COLOR_MAP[clr] for clr in list(results[0]['predict_labels'])] # Get the color associated to each predicted label
pcd.colors = o3d.utility.Vector3dVector(colors) # Add color data to the point cloud

vis.add_geometry(pcd)
vis.poll_events()
vis.update_renderer()
sleep(1)
# Get one test point cloud from the SemanticKitti dataset
for data, result in zip(data_set, results):

    xyz = data["point"] # Get the points
    pcd.points = o3d.utility.Vector3dVector(xyz)
    colors = [COLOR_MAP[clr] for clr in list(result['predict_labels'])] # Get the color associated to each predicted label
    pcd.colors = o3d.utility.Vector3dVector(colors) # Add color data to the point cloud

    vis.update_geometry(pcd)
    vis.poll_events()
    vis.update_renderer()
    sleep(1)
# # Get one test point cloud from the custom dataset
# pc_idx = 5 # change the index to get a different point cloud
# data, pcd = prepare_point_cloud_for_inference(custom_dataset[pc_idx])


# # Run inference
# result = pipeline.run_inference(data)

# # Colorize the point cloud with predicted labels
# colors = [COLOR_MAP[clr] for clr in list(result['predict_labels'])]
# pcd.colors = o3d.utility.Vector3dVector(colors)

# # Create visualization
# custom_draw_geometry(pcd)

# # evaluate performance on the test set; this will write logs to './logs'.
# #pipeline.run_test()