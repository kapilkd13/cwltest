# Stubs for galaxy.tools.deps.mulled.util (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from collections import namedtuple

def quay_versions(namespace, pkg_name): ...
def mulled_tags_for(namespace, image, tag_prefix: Optional[Any] = ...): ...
def split_tag(tag): ...
def version_sorted(elements): ...

Target = namedtuple('Target', ['package_name', 'version', 'build'])

def build_target(package_name, version: Optional[Any] = ..., build: Optional[Any] = ..., tag: Optional[Any] = ...): ...
def conda_build_target_str(target): ...
def v1_image_name(targets, image_build: Optional[Any] = ..., name_override: Optional[Any] = ...): ...
def v2_image_name(targets, image_build: Optional[Any] = ..., name_override: Optional[Any] = ...): ...

image_name = ...  # type: Any

# Names in __all__ with no definition:
#   Target
