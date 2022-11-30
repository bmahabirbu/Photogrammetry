# Photogrammetry
Using Open3D-ML/Pytorch to realize PointCloud Reconstruction, Segmentation and Object Detection, with Deep Learning Method and created our GUI.
# Team Members:
__By Group A2_09: Brian, Chris, and Risa__

## Introduction to our project
* Learn what is PointCloud and several formats of its dataset.
* Learn mainstream python algorithms to do computer vision tasks related to PointCloud, such as *__Tensorflow, Pytorch, Pytorch3D, Open3D__*.
* Compare different methods to create drone pcd files, in terms of speed, resolution, and point quality.(*__Open3D,PPKT real-time visualization__*)
* Set up complex environment with scc and wsl2(Ubuntu) and use OpenGL to rendering datasets.
* Test *__mesh-RCNN__* on scc.
* Build up pipeline, yaml, preprocess files, define different Class Method and use *__RandLa-Net model__* to realize Segmentation.
* Using *__Semantic3D and KITTI__* dataset to realize animation, segmentation and also object detection.
* Preprocess Optimizaition. 

## MVP
Create optimizaition algorithms in terms of data processing based on Open3D to help better performance(speed/quality) on all kinds of cv tasks.

## Create a PointCloud

<div align = center>
<img src = "https://user-images.githubusercontent.com/81452190/204732364-026b9699-fc2e-4b32-9022-524dab76d7a4.png" width = "600px"><br>
</div>

## Mesh-Net
<div align = center>
<img src = "https://user-images.githubusercontent.com/81452190/204731614-0b22b6b6-b8b1-4be5-9ab2-db11da942490.png" width = "800px"><br>
</div>

## Test trianing Rendering on scc with Mesh-RCNN
<div align = center>
<img src = "https://user-images.githubusercontent.com/81452190/204732818-6a78a2b2-1d24-4754-a171-c0e398af3b11.png" width = "600px"><br>
</div>

## Real-time PointCould Visualization - ppkt

## Open3D - Sparse and Denser PointCloud with drone las file
<div align = center>
<img src = "https://user-images.githubusercontent.com/81452190/204733255-244526cb-531f-4bee-9c67-6738fa5df070.png" width = "400px"><br>
</div>
<div align = center>
<img src = "https://user-images.githubusercontent.com/81452190/204733543-31ea36cd-6ec5-4fcf-9b71-f779f7f4240e.png" width = "400px"><br>
</div>


## Open3D vs PPKT

### Open3D method
![myFile11-30-2022_32011_AM](https://user-images.githubusercontent.com/81452190/204744241-73edbd27-f45f-405c-8f13-0676388c761b.gif)

### PPKT method
![myFile11-30-2022_31912_AM](https://user-images.githubusercontent.com/81452190/204744259-56f53dab-d316-42e7-96f2-dcac87d77c3f.gif)


## Open3D/Open3D-ml
Open3D is an open-source library that supports rapid development of software that deals with 3D data. The Open3D frontend exposes a set of carefully selected data structures and algorithms in both C++ and Python. The backend is highly optimized and is set up for parallelization. Open3D was developed from a clean slate with a small and carefully considered set of dependencies. It can be set up on different platforms and compiled from source with minimal effort. The code is clean, consistently styled, and maintained via a clear code review mechanism. Open3D has been used in a number of published research projects and is actively deployed in the cloud


## 3D-PointCould conversion

## Dataset 

### Ladar dataset
<div align = center>
<img src = "https://user-images.githubusercontent.com/81452190/204734244-d72ca38c-976f-4055-8e9c-679c5915792b.png" width = "400px"><br>
</div>

### SemanticKITTI dataset
<div align = center>
<img src = "https://user-images.githubusercontent.com/81452190/204734448-a57b9f9e-5030-4012-ac50-d2571e0e14f0.png" width = "400px"><br>
</div>

### Semantic3D dataset
<div align = center>
<img src = "https://user-images.githubusercontent.com/81452190/204735134-e4845810-92be-4981-9a0b-05e012947ff9.png" width = "400px"><br>
</div>

## preprocess

## Segmentation and GUI
<div align = center>
<img src = "https://user-images.githubusercontent.com/81452190/204744840-989cf101-87aa-4129-a556-d946f35964be.png" width = "400px"><br>
</div>

# Output

## Segmentation Semantic3D dataset
<div align = center>
<img src = "https://user-images.githubusercontent.com/81452190/204735570-dcbb869a-3dca-41ef-8a2b-6499db81c235.png" width = "400px"><br>
</div>

<div align = center>
<img src = "https://user-images.githubusercontent.com/81452190/204735635-468a7a73-1973-4764-aae7-d10e467c3c79.png" width = "400px"><br>
</div>

## Animation Visualizaiton of SemanticKITTI dataset

![myFile11-30-2022_30719_AM](https://user-images.githubusercontent.com/81452190/204741397-9a7dc3c8-86ae-4b0f-bf49-f765c1adcc96.gif)

# Reference
[1]https://hermary.com/learning/3d-vision-data-look-like/?gclid=EAIaIQobChMIwonapPaK-gIVAvjICh2yxAKfEAAYAiAAEgIbOPD_BwE<br><br>
[2]F. Chen, Y. Lu, B. Cai and X. Xie, "Multi-Drone Collaborative Trajectory Optimization for Large-Scale Aerial 3D Scanning," 2021 IEEE International Symposium on Mixed and Augmented Reality Adjunct (ISMAR-Adjunct), 2021, pp. 121-126, doi: 10.1109/ISMAR-Adjunct54149.2021.00034.<br><br>
[3]J. -W. Han, D. -J. Synn, T. -H. Kim, H. -C. Chung and J. -K. Kim, "Feature Based Sampling: A Fast and Robust Sampling Method for Tasks Using 3D Point Cloud," in IEEE Access, vol. 10, pp. 58062-58070, 2022, doi: 10.1109/ACCESS.2022.3178519.<br><br>
[4]X. Qu, J. Zhao, Y. Sun and L. Wang, "3D Reconstruction Method Based on Aerial Sequence of UAV," 2020 International Conference on Virtual Reality and Visualization (ICVRV), 2020, pp. 33-37, doi: 10.1109/ICVRV51359.2020.00017.<br><br>
[5]D. Marchisotti and E. Zappa, "Uncertainty mitigation in drone-based 3D scanning of defects in concrete structures," 2022 IEEE International Instrumentation and Measurement Technology Conference, doi: 10.1109/I2MTC48687.2022.9806652.
[6]Y. Chen, S. Liu, X. Shen, and J. Jia, ‘‘Fast point R-CNN,’’ in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), Oct. 2019, pp. 9775–9784.<br><br>
[7]R. Q. Charles, H. Su, M. Kaichun, and L. J. Guibas, ‘‘PointNet: Deep learning on point sets for 3D classification and segmentation,’’ in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), Jul. 2017, pp. 652–660.<br><br>
[8]X. Yan, C. Zheng, Z. Li, S. Wang, and S. Cui, ‘‘PointASNL: Robust point clouds processing using nonlocal neural networks with adaptive sampling,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR),Jun. 2020, pp. 5589–5598.<br><br>
[9]R. Huang, D. Zou, R. Vaughan, and P. Tan. Active image-based modeling with a toy drone. In 2018 IEEE International Conference on Robotics and Automation (ICRA), pp. 6124–6131. IEEE, 2018.<br><br>
[10]C. Szegedy, W. Liu, Y. Jia, P. Sermanet, S. Reed, D. Anguelov, D. Erhan,V. Vanhoucke, and A. Rabinovich, “Going deeper with convolutions,” in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun 2015,pp. 1–9.<br><br>
[11]R. Klokov and V. Lempitsky, “Escape from cells: Deep kd-networks for the recognition of 3d point cloud models,” in Proc. IEEE Int. Conf. Comput. Vis. (ICCV), Oct 2017, pp. 863–872.<br><br>
[12]Q. Xu, X. Sun, C.-Y. Wu, P. Wang, and U. Neumann, “Grid-GCN for fast and scalable point cloud learning,” in Proc. IEEE Conf. Comput.Vis. Pattern Recognit. (CVPR), Jun 2020, pp. 5661–5670.

