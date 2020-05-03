import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="coloredlog",
    version="0.2.1",
    author="CangYin",
    author_email="excangyin@gmail.com",
    description="Colorize your console output.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cangyin/coloredlog",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)