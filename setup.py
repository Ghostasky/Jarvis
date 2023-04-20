from setuptools import setup

setup(
    name="Jarvis-gpt",
    version="0.3",
    packages=["Jarvis"],
    author="Ghostasky",
    author_email="ghostasky@foxmail.com",
    platforms='python3',  # 项目支持的平台
    description='这是一个命令行的gpt',
    entry_points={
        "console_scripts": [
            "Jarvis = Jarvis.jarvis:main",
        ]
    },
    include_package_data=True,
)

