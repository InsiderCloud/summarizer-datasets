import os
from typing import Any
from pathlib import Path
import yaml
from ensure import ensure_annotations
from box import Box, ConfigBox
from box.exceptions import BoxValueError
from Cogniezer.logging import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> Box:
    """
    Reads a YAML file and returns its content as a Box object.

    Args:
        path_to_yaml (Path): The path to the YAML file.

    Returns:
        Box: A Box object containing the content of the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: If any other error occurs while reading the YAML file.
    """
    try:
        with open(path_to_yaml, encoding="utf-8") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info("yaml file %s loaded successfully", path_to_yaml)
            return Box(content)
    except BoxValueError as exc:
        raise ValueError("yaml file is empty") from exc
    except Exception as exc:
        raise exc

@ensure_annotations
def create_directories(path_to_directories:list,verbose = True):
    """
    Creates directories at the specified paths if they don't already exist.

    Args:
    path_to_directories (list): A list of paths where directories need to be created.
    verbose (bool): If True, logs the path of the created directory.

    Returns:
    None
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info("Created directory at: %s",path)

@ensure_annotations
def get_size(path:Path) -> str:
    """
    Returns the size of the file at the given path in kilobytes (KB).
    
    Args:
    path (Path): The path to the file whose size is to be determined.
    
    Returns:
    str: A string representing the size of the file in KB.
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return ("~ %d KB",size_in_kb)

