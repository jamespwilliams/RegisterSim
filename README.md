# RegisterSim
Register machine simulator for CO240-style register machine programs

Usage: `python RegisterSim program_name state`

* `program_name`:
   
    Name of a register instruction program file.
    The passed program file must be of the correct format, with
    each line of the file being a valid register instruction. Valid
    instruction types are as follows:
    
           Rn+ -> Li
           Rn- -> Li, Lj
           HALT
         
    Separate instructions must be placed on new lines. Note that line 
    numbers are not necessary and should be omitted. Example files can
    be found in tests/test_programs/
        
* `state`:
    
    A list of integers [l0,x0,x1, ..., xn], such that the RM will be started at L0 with registers
    set to R0 = x0, R1 = x1, ..., Rn = xn on program start.
