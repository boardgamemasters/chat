# Import necessary libraries
import setuptools

# Read the contents of the README.md file into a variable
with open('README.md') as readme_file:
    readme = readme_file.read()

# Set up the package metadata and dependencies using setuptools.setup()
setuptools.setup(
    name="streamlit-chat",  # Name of the package
    version="0.1.1",  # Version number of the package
    author="Yash Pravin Pawar, Yash Vardhan Kapil",  # Authors of the package
    author_email="yashpawarp@gmail.com",  # Contact email address of the authors
    description="A streamlit component, to make chatbots",  # Short description of the package
    long_description=readme,  # Detailed description of the package (read from README.md)
    long_description_content_type="text/markdown",  # Specify that the long description is in Markdown format
    url="https://github.com/AI-Yash/st-chat",  # URL to the package's GitHub repository
    packages=setuptools.find_packages(),  # List of Python packages to be included in the distribution
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in in the distribution
    classifiers=[  # List of classifiers to categorize the package on PyPI
        "Programming Language :: Python :: 3",  # Python version compatibility
        "Operating System :: OS Independent",  # Compatible operating systems
    ],
    keywords="chat streamlit streamlit-component",  # Keywords/tags for the package
    python_requires=">=3.6",  # Minimum Python version required for the package
    install_requires=[  # List of Python packages required for the package to work
        "streamlit >= 0.63",  # Streamlit version dependency
    ],
)
