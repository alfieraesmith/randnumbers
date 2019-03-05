 
 ## Package Details
   * Version: 0.1 
   * Author: Alfie Smith
   * Owner: Mango Solutions 
   * Usage: Anyone! (Non-copyrighted material) 
    
 ## Package Summary 
    This package is for generating an numpy array of numbers that
    have been randomly selected from a user-specified probability
    distribution. 
    
    You can generate a list of random numbers by calling 
    the get_random_numbers function, found in functions.py. 
    Alternatively, there is a class for each supported distribution,
    found in Classes.py, where each class has a .draw method
    that generates an array of random numbers. 
    
    Note: This package only supports the Normal,
    Binomial and Poisson distributions at this time. 
    
    This package also has a test unit (UnitTest) 
    that can be executed by running either "nosetests" or 
    "python -m unittests" from the command line after installation.  
 
 ## Deployment 
  1. Create a virtual environment (virtualenv is recommended)
  2. Install package - pip install randomnumbers.tar.gz
 
 ## Requirements 
    Please see requirements.txt for all dependencies required to deploy
    this package.
 
 ## Examples
    Please see examples/functions.py for how to generate numbers
    using the get_random_numbers method and 
    examples/classes.py to see examples of how to generate
    numbers using the distribution classes. 
 ### Test Notes
  ###### No Tests for Distribution.summarise()
    * Issue 1: cannot test print output - 
             method could tested if we saved summary values (mean/max/min)
             to instance. This would make the class messier so I've opted to present class in best state and note this issue.
    * Issue 2: We may be only able to test mean and sd as min/max are any value between value +-inf
   
  ###### No Tests for Binomial and Poisson distribution config
  
    Binomial distribution and Poisson distributions 
    generator function/classes take (p, n) 
    and (lambda) respectively as inputs. 
    Neither test consistently returned expected
    results in sample,  even at sample size > 10 million. 
    I've added this issue to further development. 
    
## Further Development 
   1. Research repeatable moments for Binomial and Poisson distributions
    and set up tests to check that moments match expected moments
    given config. 
   2. Add Bimodal and Gaussian distributions 
   3. Add better package logging 
