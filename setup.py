from setuptools import setup

with open("Readme.md","r",encoding="utf-8") as fh:
    long_description =fh.read()

Author_name='Ambati Shivani'
Src_repo='src'
LIST_OF_REQUIREMENTS=['streamlit']

setup(
    name=Src_repo,
    version='0.0.1',
    author=Author_name,
    author_email='ambatishivani24@gmail.com',
    description='A simple python package for Movies Recommendation',
    long_description='Recommendation systems are becoming increasingly important in todays extremely busy world. People are always short on time with the myriad tasks they need to accomplish in the limited 24 hours. Therefore, the recommendation systems are important as they help them make the right choices, without having to expend their cognitive resources. The purpose of a recommendation system basically is to search for content that would be interesting to an individual.',
    long_description_content_type='text/markdown',
    package=[Src_repo],
    python_requires='>=3.7',
    install_requires=LIST_OF_REQUIREMENTS,

)