import setuptools
# f = open("./requirements.txt", "r")
# def process(txt):
#     return txt.replace("\n", "")
# requirements = list(map(process, f.readlines()))
requirements = ["geopandas",\
"shapely",\
"requests",\
"beautifulsoup4"]
setuptools.setup(
    name="ll2location",
    version="0.0.1",
    author="Trương Xuân Linh",
    author_email="truonglinh1342001@gmail.com",
    description="ll2location",
    long_description="ll2location",
    long_description_content_type="text/markdown",
    url="https://github.com/truong-xuan-linh/mVQA-webapp",
    package_data={'': ['*.json', '*.yml']},
    install_requires= requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)