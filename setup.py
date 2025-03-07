from setuptools import setup, find_packages

setup(
    name="mschema",
    version="1.0",
    url="https://github.com/P10-Software/mschema",
    packages=find_packages(),  # Automatically finds all sub-packages
    install_requires=[
        "llama-index",
        "numpy",
        "sqlalchemy",
    ],
    python_requires=">=3.7",
)
