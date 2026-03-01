from setuptools import setup

# Read the README.md file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mermaid-magic",
    version="0.1.4",
    description="IPython magic for rendering Mermaid diagrams",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Vijay Balasubramaniam",
    author_email="vbalasu@gmail.com",
    py_modules=["mermaid_magic"],
    install_requires=[
        "ipython",
    ],
    project_urls={
        "Source": "https://github.com/vbalasu/mermaid-magic",
        "Bug Reports": "https://github.com/vbalasu/mermaid-magic/issues",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
) 