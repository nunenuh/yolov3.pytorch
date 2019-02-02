from pathlib import Path
from collections import OrderedDict
import os

def config_parser(full_path):
    path = Path(full_path)
    if path.exists() and path.is_file():
        with open(str(path), 'r') as file:
            lines = file.read().split('\n')
            lines = [line for line in lines if line and not line.startswith('#')]
            lines = [line.rstrip().lstrip() for line in lines]
        mod_def = []
        for line in lines:
            if line.startswith('['):
                header_name = line[1:-1].strip()
                mod = OrderedDict({'header':header_name})
                mod_def.append(mod)
            else:
                key, val = line.split('=')
                key, val = key.strip(), val.strip()
                submod = {key:val}
                mod_def[-1].update(submod)

        return mod_def
    else:
        return None


if __name__ == '__main__':
    module = config_parser('../cfg/yolov3.cfg')
    print(module)


