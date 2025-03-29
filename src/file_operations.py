import os, shutil
from pathlib import Path

def cpy_src_to_dst(src: os.PathLike, dst: os.PathLike):
    if not os.path.exists(src):
        raise ValueError(f"src path {src} does not exist")
    if os.path.exists(dst):
        shutil.rmtree(dst)

    os.mkdir(dst)

    dir_list = os.listdir(src)

    for item in dir_list:
        src_item = Path(os.path.join(src, item))
        dst_item = Path(os.path.join(dst, item))
        if os.path.isfile(src_item):
            print(f"copying file: {src_item} to {dst_item}")
            shutil.copy(src_item, dst_item)
        else:
            print(f"copying directory: {src_item} to {dst_item}")
            cpy_src_to_dst(src_item, dst_item)
