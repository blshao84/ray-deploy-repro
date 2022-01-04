from setuptools import find_packages, setup

ray_version = "1.9.0"
requires = [
    f'ray[default]=={ray_version}',
    f'ray[serve]=={ray_version}',
    "pytest>=4.3.0",
    "pytest-cov>=2.6.1"
]

setup(
    name="deploytest",
    version="0.0.1",
    description="risk analytics lib framework ",
    long_description="reproduce issues in ray serve deployment",
    long_description_content_type="text/markdown",
    author="Baolin Shao",
    author_email="b.l.shao84@gmail.com",
    install_requires=requires,
    classifiers=[
        "Programming Language :: Python :: 3.8",
    ],
    keywords="test",
    packages=find_packages(
        exclude=[
            "tests",
        ]
    ),
    include_package_data=True,
    zip_safe=False,
)
