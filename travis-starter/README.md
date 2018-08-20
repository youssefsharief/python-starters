## Python Travis Starter

* Add your lib files in sample_lib
* Add your tests in tests folder
* Travis
    * Add a ".travis.yml" file
        * You should either have requirements.txt file or add requirments in travis
            * In travis the "install" field automatically have a value of "pip install -r requirements.txt"
        * Add "python -m pytest" to run tests for each build
        * Add to travis file a cache field with "pip" if needed
    * Go to "https://travis-ci.org/profile/{github_username}" and enable your project
    


* Check the template below (would appear only in md) to show in the readme the build status


#### Master branch build status: 
![](https://travis-ci.org/youssefsharief/python-travis-starter.svg?branch=master)

* No need to use tox to test different environments as long as travis is used
