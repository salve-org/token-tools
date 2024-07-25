# pip install -U -r requirements-dev.txt --break-system-packages; pip uninstall salve -y --break-system-packages; pip install . --break-system-packages --no-build-isolation; python3 -m pytest .
from setuptools import setup

with open("README.md", "r") as file:
    long_description = file.read()


setup(
    name="token_tools",
    version="0.1.0",
    description="Token Tools provides, well, tools for Token's!",
    author="Moosems",
    author_email="moosems.j@gmail.com",
    url="https://github.com/salve-org/token-tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=open("requirements.txt", "r+")
    .read()
    .splitlines(keepends=False),
    python_requires=">=3.11",
    license="MIT license",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",  # I believe it can be classified as such, cannot test Windows
        "Programming Language :: Python :: Implementation",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Typing :: Typed",
    ],
    packages=["token_tools"],
)
