<h2>I. Intuition</h2>
In this code, we apply the concept of digital roots. 
A digital root is the single-digit number obtained by repeatedly summing the digits of a given number until a single digit is obtained.
<br>
<br>
<b>Eg. -</b> Digital root of the number 567 is 5+6+7 = 11+7 = 18 -> 1+8 = 9 
<br>
<br>
Our aim is to to compute the digital root of a given number, denoted as 'num' in the problem statement.
<hr>
<h2>II. Approach</h2>
We use a mathematical formula in our code to directly compute the digital root of 'num' - this allows us to find its digital root without iterating over its digits, which might lead to the formation of a loop(something which we're avoiding to establish through this solution).
The formula is given below - 
<br>
<br> 

| FORMULA  |
|---|
|(num-1)%9+1 |

Note -
<ul>
  <li>This formula is used as we observe that the digital root of any number is equal to the remainder when the number 'num' is divided by 9.</li>
  <li>In case the number is divisible by 9 and remainder = 0, then the root of that number is 9.</li>
  <li>However, 'num' is a single digit number, which is why we use the given formula to compute its root directly w/o iterations.</li>
</ul>
<hr>
<h2>III. Solution</h2>

```py
class Solution:
    def addDigits(self, num: int) -> int:
        # If the input number is 0, return 0
        if num == 0:
            return 0
        # Compute the digital root of the input number using the formula (num-1)%9+1
        else:
            return (num-1)%9+1
```
<ul>
  <li>'addDigits' function takes integer 'num' as input and returns an integer as an output.</li>
  <li>If num = 0, then function returns 0 as output.</li>
  <li>Else, the function computes the digital root of 'num' using the formula - (num-1)%9+1</li>
</ul>  
<hr>
<h2>IV. Time and Space Complexity</h2>
<b>Time Complexity -</b> O(1)
<br>
<b>What does it mean?</b>
<ul>
  <li>the amount of time the code takes to run is constant.</li>
  <li>code does not depend on the input size</li>
  <li><b>REASON -</b> the code performs a simple arithmetic computation to directly compute the digital root of num, without iterating over its digits.</li>
  <li>Hence, code runs in constant time.</li>
</ul>
<br>
<b>Space Complexity -</b> O(1)
<br>
<b>What does it mean?</b>
<ul>
  <li>amount of memory used - constant.</li>
  <li>does not depend on input size.</li>
  <li><b>REASON -</b> as the code does not implement any data structures that grow with input size and only stores a constant number of variable in memory.</li>
</ul>
