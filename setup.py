from distutils.core import setup

setup(
    name="panoply_dynamodb",
    version="1.0.0",
    description="Panoply Data Source for DynamoDB",
    author="Adam T",
    author_email="adam.anh.ta@gmail.com",
    url="http://panoply.io",
    install_requires=[
        "panoply-python-sdk==1.3.4",
        "boto3==1.4.91",
    ],
    extras_require={
        "test": [
            "pep8==1.7.0",
            "coverage==4.3.4",
            "requests_mock==1.1.0"
        ]
    },

    # place this package within the panoply package namespace
    package_dir={"panoply": ""},
    packages=["panoply.dynamodb"]
)
