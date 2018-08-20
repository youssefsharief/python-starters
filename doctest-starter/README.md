## Doctest
* Add tests (for success and error scenarios) as shown in sample_lib/sum.py
* To run tests explicitly (not recommended)
    * Add the main function that calls doctest in sum.py
    * Now you could `python .\sample_lib\sum.py -v` to test directly
* To run tests implicitly (recommended)
    * You do not need to add the main function 
    * `python -m doctest -v .\sample_lib\sum.py`
