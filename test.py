import sys
import os
import numpy as np
#import open3d as o3d

def generate_dummy_point_cloud(output_path):
    # Create random 3D points
    points = np.random.rand(1000, 3)

    # Create Open3D point cloud
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)

    # Save as PLY file
    o3d.io.write_point_cloud(output_path, pcd)
    print("Point cloud saved at:", output_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No image path provided.")
        sys.exit(1)

    image_path = sys.argv[1]

    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "static", "output")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, "generated.ply")

    generate_dummy_point_cloud(output_path)

    sys.exit(0)