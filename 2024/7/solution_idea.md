**Idea for 7.1:**

First, start in reverse order and check whether the target number can be divided by the current number (without remainder), if it's true, 
than make new target by applying this division and check this for other nums the same way using recursion.

If target can't be divided by current num, then new target can be found by subtracting current num from the previous target. 
After that the process of checking above-mentioned options repeats for new target and new num through the recursion.

For each target and array of nums this process continues till the bool result not returned. 

**Idea for 7.2:**

The main idea here is that concatenation is possible only when current num is a part of the target. 
Therefore, if option with * operator is not working, it is necessary to check this condition and if it's true then new target can
be created by subtracting current num from the target. After that the process of checking repeats through recursion.
