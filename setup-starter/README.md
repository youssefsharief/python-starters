## Setup

* Add requirements. Either:-
    * Manually add packages to requirements.txt
    * Throught pipreqs library
        * `pip install pipreqs`
        * `pipreqs .`
* Add setup.py
    * Make sure you have a remote origin for the repo since a url is needed in this file
    * Now you are able to install your library and use it anywhere in your local PC using
        * `pip install .`
        * `pip install -e .`
            * This command is preferred since changes to the source files will be immediately available to other users of the package on our system
            * Add "*.egg-info" to your .gitignore file
* Publish on PyPi
    * Add a license file
    * Travis
        * Make sure ruby is installed on your PC then `gem install travis`
        * Encrypt the password to be used in the travis.yml file
            * `travis encrypt --add deploy.password`
            * Now you should find the encrypted password in your ".travis.yml" file
    * Manually
        * Generate distribution archives
            * `python setup.py sdist bdist_wheel`
                * Make sure you add build and dist folders in .gitignore 
        * Upload the distribution archives to test/pypi
            * Install twine
                * `pip install twine` or `conda install twine`
            * Make sure to update version number
            * `twine upload --repository-url https://test.pypi.org/legacy/ dist/*` to upload to the test PyPi. My username is "youssef"
            * `twine upload dist/*` to upload to the real PyPi. My username is "youssef_sherif"
                * You would need to verify your email 
                * Now you could find your package in this url https://pypi.org/project/sample-lib/
    * Install our newly uploaded package from PyPi
        * `pip install --index-url https://test.pypi.org/simple/ sample-lib`
            * If you already installed using the `pip install .` command, you might receive a message that the requirement is already installed therefore you could uninstall it first for testing using the `pip uninstall sample_lib`
    