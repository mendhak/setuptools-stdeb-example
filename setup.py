import os
import shutil
import setuptools


if not os.path.exists("tmp"):
    os.makedirs("tmp")
shutil.copy('example_pkg/example_pkg.py', 'tmp/example_pkg')

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-mendhak", # Replace with your own username
    version="0.0.2",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Ubuntu 20.04",
    ],
    python_requires='>=3.6',
    install_requires=[],
    data_files=[
        ('/usr/sbin/', ['tmp/example_pkg'])
    ]
)
