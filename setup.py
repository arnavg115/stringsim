import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="stringsim",
    version="0.0.2",
    author="Arnav G",
    author_email="soccercream20@gmail.com",
    description="A package that uses other algorithms for fuzzy matching",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arnavg115/stringsim",
    packages=['strsim'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)