from setuptools import setup, find_packages

with open("README.md","r") as infile:
    README = infile.read()

# This call to setup() does all the work
setup(
    name="dsc-mailer",
    version="1.0.1",
    description="A simple mailing library for python powered applications using Sendgrid.",
    packages=find_packages(),
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jkuatdsc/dsc-mailer",
    download_url='https://github.com/jkuatdsc/dsc-mailer.git',
    author="Victor Waichigo",
    author_email="waichigovick@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    include_package_data=True,
    install_requires=["sendgrid", "python-decouple"],
)
