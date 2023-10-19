import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="TMS Plan Project",
    version="1.0.0",
    author="Trường Nguyễn",
    author_email="nguyenkhoatruong231199@gmail.com",
    description="TMS Plan Use Machine Learning",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/NguyenKhoaTruong/tms",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.11.2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent :: Window",
    ],
    install_requires=requirements,
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "myawesomecommand=myawesomeproject.cli:main",
        ],
    },
    project_urls={
        "Bug Tracker": "https://github.com/NguyenKhoaTruong/tms",
        "Documentation": "https://github.com/NguyenKhoaTruong/tms",
    },
    license="MIT",
)
