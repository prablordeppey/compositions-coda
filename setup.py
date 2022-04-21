import setuptools

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="compositions-coda",
    version="1.0.0",
    author="Ablordeppey Prosper",
    author_email="prablordeppey@gmail.com",
    description="An extensive package for Compositional Data Analysis (CoDA)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prablordeppey/compositions",
    project_urls={
        "Bug Tracker": "https://github.com/prablordeppey/compositions/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=['numpy>=1.19.2'],
    license='MIT',
)