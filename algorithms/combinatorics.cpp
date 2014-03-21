#include <iostream>






/* Combinations:
   Gosper's hack allows us to find the next number (lexicography) that has the
   same number of bits set.  This allows us to enumberate combinations of k
   out of n elements.

   Procedure:
   1.  obtain least significant 1 bit of x.
   2.  add that bit to x
   3.  ???
   4.  Profit!

   See here for more details: 
   http://read.seas.harvard.edu/cs207/2012/

 */

unsigned long long next_combination(unsigned long long x) 
{
  auto a = x & -x; 
  auto b = a + x; 
  return b + (((b ^ x) / a) >> 2); 
}
