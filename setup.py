import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cytogis",
    version="1.0.0",
    author="Sprum",
    author_email="sprum@hotmail.de",
    description="cyto to gis is a small package to convert .cyjs files from Cytoscape to .geojson Objects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sprum/cytogis",
    project_urls={
        "Bug Tracker": "https://github.com/Sprum/cytogis/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.11"
)
