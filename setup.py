import setuptools

with open("README.md", "r") as f:
    long_description = f.read()
    
__version__ = "0.0.0"

REPO_NAME = "ML_002"
SRC_REPO = "ml_002-wine_pred"
AUTHOR_USER_NAME = "rayxxxeee"
AUTHOR_EMAIL = "rexxxstock@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version= __version__,
    author=AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description="ML project template package",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir={"": "src"},
    packages= setuptools.find_packages(where="src")
    )

