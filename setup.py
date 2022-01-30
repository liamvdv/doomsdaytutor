# import re
# from typing import List
# from pathlib import Path
from setuptools import setup, find_packages


# def get_version(file: Path) -> str:
#     text = file.read_text()
#     r = re.search('^__version__\s*=\s*"(.*)"', text, re.M)
#     return r.group(1)


# HERE = Path(__file__).parent
# version = get_version(HERE / "doomsdaytutor" / "__init__.py")
# description = (HERE / "README.md").read_text()
# requirements = (HERE / "requirements.txt").read_text().splitlines()

setup(
    # name="doomsdaytutor",
    # packages=find_packages(),
    # version=version,
    # description="Doomsdaytutor - learn the doomsday algorithm fast",
    # long_description=description,
    # long_description_content_type="text/markdown",
    # install_requires=requirements,
    # include_package_data=True,  # needed for MANIFEST.in files to exist
    # python_requires=">=3.5",
    # classifiers=[
    #     "Development Status :: 3 - Alpha",
    #     "Topic :: Education",
    #     "License :: OSI Approved :: MIT License",
    #     "Programming Language :: Python :: 3",
    #     "Programming Language :: Python :: 3.5",
    # ],
    # entry_points={"console_scripts": ["doomsdaytutor = doomsdaytutor.cli:run"]},
    # license="MIT",
    # author="Liam van der Viven",
    # author_email="liam.vanderviven@gmx.de",
    # url="https://github.com/liamvdv/doomsdaytutor",
)
