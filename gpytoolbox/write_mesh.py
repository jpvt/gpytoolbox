import os
import numpy as np
import csv

def write_mesh(file,
    V,
    F,
    UV=None,
    Ft=None,
    N=None,
    Fn=None,
    fmt=None,
    return_UV=False,
    return_N=False,
    writer=None):
    # Writes a mesh to a file.
    #
    # If you have the approproate C++ extensions installed, this will use a fast
    # C++-based writer. If you do not, this will use a slow python writer.
    #
    # Currently only supports triangle meshes.
    # 
    # Input:
    #       file  the path to the mesh
    #       V  numpy array of mesh vertex positions
    #       F  numpy array of mesh face indices into V (0 indexing)
    #       Optional:
    #                UV  numpy array of texture coordinates
    #                Ft  numpy array of mesh face indices into UV 
    #                N  numpy array of normal coordinates
    #                Fn  numpy array of mesh face indices into N
    #                fmt  The file format of the mesh to open.
    #                     If None, try to guess the format from the file
    #                     extension.
    #                     Supported formats: obj
    #                writer  Which writer engine to use. None, 'C++' or 'Python'.
    #                        If None, will use C++ if available, and else Python.
    #

    # Detect format if it has not been specified
    if fmt is None:
        _, fmt = os.path.splitext(file)
    fmt = fmt[1:].lower()

    # Call appropriate helper function to read mesh
    if fmt=='obj':
        _write_obj(file,V,F,UV,Ft,N,Fn,writer)
    else:
        assert False, "Mesh format not supported."


try:
    # Import C++ reader
    from gpytoolbox_eigen_bindings import _write_obj_cpp_impl
    _CPP_WRITER_AVAILABLE = True
except Exception as e:
    _CPP_WRITER_AVAILABLE = False

def _write_obj(file,V,F,UV,Ft,N,Fn,writer):
    # Private helper function for writing an OBJ file.
    # Currently, only triangle meshes are supported.

    # Pick a reader default
    if writer is None:
        writer = "C++" if _CPP_WRITER_AVAILABLE else "Python"

    # Select appropriate writer
    if writer=="C++":
        if UV is None:
            UV = np.ndarray([], dtype=np.float64)
        if Ft is None:
            Ft = np.ndarray([], dtype=np.int32)
        if N is None:
            N = np.ndarray([], dtype=np.float64)
        if Fn is None:
            Fn = np.ndarray([], dtype=np.int32)
        err = _write_obj_cpp_impl(file,
            V.astype(np.float64),
            F.astype(np.int32),
            UV.astype(np.float64),
            Ft.astype(np.int32),
            N.astype(np.float64),
            Fn.astype(np.int32))
        if err != 0:
            raise Exception(f"Error {err} writing obj file.")
    elif writer=="Python":
        _write_obj_python(file,V,F,UV,Ft,N,Fn)
    else:
        assert False, "Invalid choice of writer."


def _write_obj_python(file,V,F,UV,Ft,N,Fn):
    # Private helper function for writing an OBJ file in pure Python.
    # Currently, only triangle meshes are supported.

    with open(file, 'w') as f:
        def write_row(identifier, x):
            f.write(identifier)
            f.write(' ')
            f.write(' '.join(x))
            f.write('\n')
        if V is not None:
            for r in range(V.shape[0]):
                write_row('v', V[r].astype(str))
        if UV is not None:
            for r in range(UV.shape[0]):
                write_row('vt', UV[r].astype(str))
        if N is not None:
            for r in range(N.shape[0]):
                write_row('vn', N[r].astype(str))
        assert F is not None
        if Ft is not None:
            assert Ft.shape[0] == F.shape[0]
        if Fn is not None:
            assert Fn.shape[0] == F.shape[0]
        for r in range(F.shape[0]):
            if Ft is not None and Fn is not None:
                fs = [f'{f+1}/{t+1}/{n+1}' for f,t,n in zip(F[r],Ft[r],Fn[r])]
            elif Ft is not None:
                fs = [f'{f+1}/{t+1}' for f,t in zip(F[r],Ft[r])]
            elif Fn is not None:
                fs = [f'{f+1}//{n+1}' for f,n in zip(F[r],Fn[r])]
            else:
                fs = [f'{f+1}' for f in F[r]]
            write_row('f', fs)

