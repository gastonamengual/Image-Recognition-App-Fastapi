from pathlib import Path

import dparse
from setuptools import setup

from gamr_backend_api_service import __version__

content = Path("Pipfile").read_text()
df = dparse.parse(content, file_type=dparse.filetypes.pipfile)
required = [
    dependency.line
    for dependency in df.dependencies
    if dependency.sections[0] == "packages"
]

setup(
    name="gamr_backend_api_service",
    version=__version__,
    description="An example Python package",
    url="https://github.com/example/example_package",
    author="Your Name",
    author_email="your.email@example.com",
    install_requires=[required],
    include_package_data=True,
)
