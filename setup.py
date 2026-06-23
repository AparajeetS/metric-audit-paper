from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# We only include the core evaluation dependencies.
# We don't want to force torch/torchvision on users who just want to run the pingouin math,
# unless they specifically want to use the PyTorch examples. But since the utils uses torch,
# we should include it. Or better, let's include the basics.
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = [line.strip() for line in f if line.strip()]

setup(
    name="mbe-eval",
    version="0.1.0",
    author="Aparajeet Shadangi",
    author_email="author@example.com",
    description="Marginal Baseline Eval (MBE): A framework for rigorously auditing representation metrics in deep neural networks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AparajeetS/metric-audit-paper-code",
    packages=find_packages(exclude=["experiments", "examples", "docs"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
)
