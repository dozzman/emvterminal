import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="emvterminal",
    version="0.0.1",
    author="Dorian Peake",
    author_email="dorian@vereia.com",
    description="EMV POS Terminal Implemenatation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dozzman/emvterminal",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'emvframework @ git+https://github.com/dozzman/emv-framework@master'
    ],
    python_requires='>=3.6',
)


