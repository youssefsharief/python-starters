* pdb
    * Characteristics
        * In standard library
        * not good at debugging multithreaded programs
        * can not attach to an already running process
    * Commands
        * `python -m pdb buggy.py`
        * `python -m pdb -c continue buggy.py`
            * Waits till there is an exception, then pdb could enter
        * `python -m pdb -c continue buggy.py`
        * pdb.pm()
            * Restart the program. Postmortem mode
        * pdb.run()
        * pdb.set_trace() (Besr mode)
    * PDB Command Prompt
        * Characteristics
            * You could evaluate python expressions
        * Commands
            * List
                * `l`
            * Print
                * `pp request`
            * `h p`
            * Where 
                * `w`
            * Evalue the value for a variable
                * `p`
                    * Example: `p word`
                * `pp` for pretty print
            * Execution control
                * Step into code
                    * `s` or `step`
                * Next (Step over function)
                    * `n` or `next`
                * Return (opposite of step)
                    * `r`
                * Ignores looping in a for loop and just jump
                    * `until`
            * Navigate through frames
                * `d`
                * `s`
            * Create testing scenraios
                * Example
                    * make a list empty to check what would happen
                        * `!cloud = []`
            * Break points
                * List
                    * `b`
                * Set breakpoint
                    * by line
                        * `b 17`
                    * by function name
                        * `b transform`
                * Clear breakpoint
                    * Al breakpoints
                        *  `cl`
                    * One breakpoint
                        * `cl 109`
                * Continue to next breakpoint
                    * `c`
    * Modes
        * Strict
        * Trace
        * Run
        * 
    * Execute the next statement… with “n” (next)
    * `Products.PDBDebugMode` makes you enter a pdb automatically when there is an exception.


