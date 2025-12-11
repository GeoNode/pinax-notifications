from setuptools import find_packages, setup
setup(
    author="Pinax Team",
    author_email="team@pinaxproject.com",
    name="geonode-pinax-notifications",
    version="6.0.0.3",
    description="User notification management for the Django web framework",
    long_description="README.md",
    long_description_content_type="text/markdown",
    url="http://github.com/pinax/pinax-notifications/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "pinax.notifications": [
            "locale/**/**/*",
            "templates/pinax/notifications/*"
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.2',
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        "django>=4.2,<5.3",
        "django-appconf>=1.0.1",
    ],
    tests_require=[
        "pinax-templates>=1.0.0",
    ],
    test_suite="runtests.runtests",
    zip_safe=False
)
