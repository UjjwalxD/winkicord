from setuptools import setup, find_packages

with open('README.md', 'r') as file:
    long_description = file.read()
setup(
    name='winkicord',
    version='1.0.0',
    author="Ujjwal Srivastava",
    author_email="ujjwal.winklebot@proton.me",
    description="Effortlessly create a fully functional Discord music bot with just one line of Python code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/UjjwalxD/winkicord/",
    project_urls={
        "Homepage": "https://github.com/UjjwalxD/winkicord/",
        "Issues" : "https://github.com/UjjwalxD/winkicord/issues"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.10",
    license="MIT",

)