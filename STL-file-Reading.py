#!/usr/bin/env python
# coding: utf-8

# In[5]:


from stl import mesh

# Loading the STL file
file_path = 'test1.stl' 

# Reading STL mesh
mesh_data = mesh.Mesh.from_file(file_path)

# Get dimensions
min_x, max_x = mesh_data.x.min(), mesh_data.x.max()
min_y, max_y = mesh_data.y.min(), mesh_data.y.max()
min_z, max_z = mesh_data.z.min(), mesh_data.z.max()

length = max_x - min_x
breadth = max_y - min_y
height = max_z - min_z

# Output extracted data
file_info = {
    "File Name": file_name,
    "Technology": "3D Printing",  # Since STL files are typically for 3D printing
    "Dimensions (L x B x H)": (length, breadth, height)
}

print(file_info)


