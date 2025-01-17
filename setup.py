import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PySideExtn", # Replace with your own username
    version="1.1.0",
    author="ANJAL.P",
    author_email="opensource.anj.official@gmail.com",
    description="PySideExtn is an Open Source Python Programming language extension for PySide, which greatly enhances the capability of the PySide library with extra widgets and more.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anjalp/PySide2extn",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    extras_require={
        "pyside6": ["PySide6>=6.1"],
        "pyside2": ["PySide2>=5.15"],
    },
)