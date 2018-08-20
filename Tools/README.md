Analysers
* Static
    * pylint
    * Macropy : Check folder
* Dynamic
    * CProfile
        * Commands
            * 
            * 
        * outputs
            * on command line
                * Command: `python -m cProfile "script"`
            * to external file file
                * Command: `python -m cProfile -o l.profile <myScript.py> arg1 arg2`
                * other tools could use this file like
                    * Snakeviz
                        * `snakeviz l.profile`
                    * Gprof and dot
                        * `gprof2dot -f pstats l.profile -o callingGraph.dot`
                        * `dot callingGraph.dot -Tpng -o image.png`
                            * Note that you need to install graphvis
    * VProf
        * Is directly used without explicitly calling CProfile
        * vprof -c mh ".\try.py" 