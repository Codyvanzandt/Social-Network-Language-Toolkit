import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

requirements = ["lark-parser", "networkx"]

setuptools.setup(
    name="snltoolkit", # Replace with your own username
    version="0.0.1",
    author="Cody VanZandt",
    author_email="cody.a.vanzandt@gmail.com",
    description="A toolkit for working with Social Network Language documents.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Codyvanzandt/Social-Network-Language-Toolkit/tree/dev",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)