__version__ = '0.1.0'

# This function depends on skimage 
from .png2poly import png2poly

# These functions depend ONLY on numpy, scipy and each other
from .linear_elasticity import linear_elasticity
from .linear_elasticity_stiffness import linear_elasticity_stiffness
from .edge_indices import edge_indices
from .regular_square_mesh import regular_square_mesh
from .regular_cube_mesh import regular_cube_mesh
from .regular_circle_polyline import regular_circle_polyline
from .signed_distance_polygon import signed_distance_polygon
from .metropolis_hastings import metropolis_hastings
from .ray_polyline_intersect import ray_polyline_intersect
from .poisson_surface_reconstruction import poisson_surface_reconstruction
from .fd_interpolate import fd_interpolate
from .fd_grad import fd_grad
from .fd_partial_derivative import fd_partial_derivative
from .normalize_points import normalize_points
from .initialize_quadtree import initialize_quadtree
from .initialize_aabbtree import initialize_aabbtree
from .traverse_aabbtree import traverse_aabbtree
from .squared_distance import squared_distance
from .squared_distance_to_element import squared_distance_to_element
from .subdivide_quad import subdivide_quad
from .in_quadtree import in_quadtree
from .quadtree_gradient import quadtree_gradient
from .quadtree_laplacian import quadtree_laplacian
from .quadtree_boundary import quadtree_boundary
from .quadtree_children import quadtree_children
from .grad import grad
from .doublearea import doublearea
from .doublearea_intrinsic import doublearea_intrinsic
from .volume import volume
from .marching_cubes import marching_cubes
from .massmatrix import massmatrix
from .massmatrix_intrinsic import massmatrix_intrinsic
from .halfedges import halfedges
from .edges import edges
from .boundary_loops import boundary_loops
from .boundary_edges import boundary_edges
from .boundary_vertices import boundary_vertices
from .halffaces import halffaces
from .faces import faces
from .boundary_faces import boundary_faces
from .min_quad_with_fixed import min_quad_with_fixed
from .min_quad_with_fixed import min_quad_with_fixed_precompute
from .fast_winding_number import fast_winding_number
from .fixed_dof_solve import fixed_dof_solve
from .fixed_dof_solve import fixed_dof_solve_precompute
from .halfedge_lengths import halfedge_lengths
from .halfedge_lengths_squared import halfedge_lengths_squared
from .cotangent_laplacian_intrinsic import cotangent_laplacian_intrinsic
from .tip_angles import tip_angles
from .tip_angles_intrinsic import tip_angles_intrinsic
from .cotangent_laplacian import cotangent_laplacian
from .cotangent_weights_intrinsic import cotangent_weights_intrinsic
from .cotangent_weights import cotangent_weights
from .remove_duplicate_vertices import remove_duplicate_vertices
from .bad_quad_mesh_from_quadtree import bad_quad_mesh_from_quadtree
from .per_face_normals import per_face_normals
from .per_vertex_normals import per_vertex_normals
from .triangle_triangle_adjacency import triangle_triangle_adjacency
from .halfedge_edge_map import halfedge_edge_map
from .array_correspondence import array_correspondence
from .signed_distance import signed_distance
from .subdivide import subdivide
from .read_mesh import read_mesh
from .write_mesh import write_mesh
from .decimate import decimate
from .in_element_aabb import in_element_aabb
from .ray_mesh_intersect import ray_mesh_intersect
from .remesh_botsch import remesh_botsch
from .upper_envelope import upper_envelope
from .colormap import colormap
from .apply_colormap import apply_colormap
from .offset_surface import offset_surface
from .barycentric_coordinates import barycentric_coordinates
from .ray_box_intersect import ray_box_intersect
from .ray_triangle_intersect import ray_triangle_intersect
from .catmull_rom_spline import catmull_rom_spline
from .random_points_on_mesh import random_points_on_mesh
from .compactly_supported_normal import compactly_supported_normal
from .matrix_from_function import matrix_from_function
from .angle_defect import angle_defect
from .angle_defect_intrinsic import angle_defect_intrinsic
from .grid_neighbors import grid_neighbors
from .grid_laplacian_eigenfunctions import grid_laplacian_eigenfunctions
from .squared_exponential_kernel import squared_exponential_kernel
from .gaussian_process import gaussian_process
from .gaussian_process import gaussian_process_precompute
from .remove_unreferenced import remove_unreferenced
from .compactly_supported_normal_kernel import compactly_supported_normal_kernel
from .remove_unreferenced import remove_unreferenced
from .edge_edge_distance import edge_edge_distance
from .triangle_triangle_distance import triangle_triangle_distance
from .minimum_distance import minimum_distance
from .approximate_hausdorff_distance import approximate_hausdorff_distance
from .icosphere import icosphere
from .cylinder import cylinder
from .cone import cone
from .torus import torus
from .adjacency_matrix import adjacency_matrix