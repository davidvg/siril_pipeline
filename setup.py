import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="siril_pipeline",
    version="0.1.0",
    author="David Vázquez García",
    author_email="davidvazquezgijon@gmail.com",
    description="A pipeline for automatic astrophotography processing using Siril",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    project_urls={
        # "Bug Tracker": "https://bugs.example.com/HelloWorld/",
        # "Documentation": "https://docs.example.com/HelloWorld/",
        "Source Code": "https://github.com/davidvg/siril_pipeline",
    },
    install_requires=[],
    packages=setuptools.find_packages(exclude=[]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)