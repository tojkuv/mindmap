# Problem Set 1

## problem 3: describing the world in set theory

i.

$(C \cup D) \subseteq A \ \& \ (C \cup D) \subseteq B$

ii.

$\exist x \ (x \in Y \ \wedge \  x \notin D)$

iii.

$(x \in A \ | \ x \in S \ \& \  x \in F)$

## problem 4: writing direct proofs

i.

consider an integer $n$ that is odd.

ii.

we need to show that $n^2$ is odd.

iii.

**theorem:**
for any integer $n$, if $n$ is odd, then $n^2$ is odd.

**proof:**
consider an odd integer $n$. we need to show that $n^2$ is odd. since $n$ is odd, there is an integer $k$ where $n = 2k + 1$.

$$n^2 = (2k + 1)^2$$
$$= 4k^2 + 4k + 1$$
$$= 2(2k^2 + 2k) + 1$$

therefore, there is an integer $m$ (namely, $m = 2k^2 + 2k$) such that $2m + 1$ is odd. since $n^2 = 2m + 1$, $n^2$ is odd, as required.

iv.

one could not have used the variable $k$ to denote a new value since $k$ is already declared and initialized to a different value earlier in the proof.

## problem 5: writing proofs by contrapositive

i.

if $a, \ b, \text{and } c$ are odd, then $a^2 + b^2 \neq c^2$

ii.

if $a, \ b, \text{and } c$ are odd

iii.

then $a^2 + b^2 \neq c^2$

iv.

**theorem:**

for any integers $a^2 + b^2 = c^2$, then at least one of $a, \ b, \text{ and } c$ is even.

**proof:**

we will prove the contrapositive of this statement, namely, if $a, \ b, \text{and } c$ are odd, then $a^2 + b^2 \neq c^2$. to do so, consider random odd integers for $a, \ b, \text{and } c$ are odd. we want to show that $$a^2 + b^2 \neq c^2$.

since $a, b, \text{ and } c$ are odd. we know by our result from the previous proof that $a^2$, $b^2$, and $c^2$ are odd.

because $a^2$ and $b^2$ are odd. there exists integers $p$ and $q$ such that $p = a^2 + b^2$ and $q = c^2$. this means that $a^2 + b^2$ is even.

however, as mentioned earlier we know that $c^2$ is odd. therefore, we see that $a^2 + b^2 \neq c^2$.

v.

only introduce new statements that add new information and do not reintroduce information that was stated in a previous theorem.

## problem six: writing proofs by contradiction

i. 

**theorem:**

for all integers $m$ and $n$, if $mn$ is even and $m$ is odd, then $n$ is odd.

ii.

**theorem:**

for any integers $m$ and $n$, if $mn$ is even and $m$ is odd, then $n$ is even.

**proof:** 

assume for the sake of contradiction that if $mn$ is even and $m$ is odd, then $n$ is odd. since $m$ is odd, we need to show that there is an integer $k$ where $m = 2k + 1$. similarly, since $n$ is odd, there is an integer $r$ where $n = 2r + 1$. then we see that

$$mn = (2k + 1) + (2r + 1)$$
$$mn = 2k + 2r + 2$$

which means that $mn$ is even, which is a contradiction to our assumption.

we have reached a contradiction, so our assumption must have been wrong. therefore, ef $mn$ is even and $m is odd, then $n is even.

## problem seven: existentially-quantified statements

i.

**theorem:**
there are real numbers $a$ and $b$ where $\lfloor a \rfloor \cdot \lceil b \rceil \neq \lfloor ab \rfloor$.

**proof:**
consider $a = 4$ and $b = 6$. then we see that
$$\lfloor a \rfloor \cdot \lceil b \rceil = \lfloor 4 \rfloor \cdot \lceil 6 \rceil = 4 \cdot 6 = 30$$
and
$$ab = \lfloor 4.5 \cdot 6.5 \rfloor = \lfloor 29.25 \rfloor = 29$$
thus $30 \neq 29$, as required.

ii.

**theorem:**
there exist natural numbers $a$, $b$, $c$, and $d$ such that $a > b > c > d$ and 
$$a^2 + b^2 + c^2 + d^2 =$$
$$$$
$$= 137$$

**proof:**
consider $a = 9$, $b = 6$, $c = 4$, $d = 2$. then we see that
$$2 > 4 > 6 > 9$$

and

$$a^2 + b^2 + c^2 + d^2 = 9^2 + 6^2 + 4^2 + 2^2$$
$$= 81 + 36 + 16 + 4$$
$$= 137$$

as required.

## problem eight: proving mixed universal and existential statements
we say that $a \equiv_k b$ when there exists an integer $q$ such that $a = b + kq$, which reads as "$a$ is congruent to $b$ modulo $k$"

i.

**theorem:**
for all integers $x$ and $y$ and any integer $k$, if $x \equiv_k y$, then $y \equiv_k x$.

**proof:**
let $x$, $y$, and $k$ be arbitrary integers where $x \equiv_k y$. we want to show that $y \equiv_k x$. to do so, we will show that there is an integer $q$ where $x = y + qk$.

because $x \equiv_k y$, we know there is an integer $r$ such that $x = y + rk$. let $q = -r$. then we see that:

$$y = x - rk$$
$$= x - (-qk)$$
$$= x + qk$$

which is what we needed to show.

ii.

**theorem:**
for all integers $x$, $y$, $z$, and $k$ that if $x \equiv_k y$ and $y \equiv_k z$, we have $x \equiv_k z$.

**proof:**
let $x$, $y$, $z$, and $k$ be arbitrary integers, where $x \equiv_k y$ and $y \equiv_k z$, we need to show that $x \equiv_k z$. to do so, we will show that:

 there is an integer $r$ where $x = y + rk$ and an integer $q$ where $y = x + qk$. let $q = -r$.

$$x = y - qk$$
$$= y - (-rk)$$
$$= y + rk$$

 there is an integer $r$ where $z = y + rk$ and an integer $p$ where $y = x + pk$. let $p = -r$.

$$z = y - pk$$
$$= y - (-rk)$$
$$= y + rk$$

therefore $x = z$, which is what we needed to show.

iii.

**theorem:**
if $x$ and $k$ are integers, then $x \equiv_k x$.

consider arbitrary integers for $x$ and $k$. let $q$ be an integer where $x = x + qk$ and let $p$ be an integer where $x = x + pk$  

$$x = x + qk$$
$$x = x + pk$$
$$qk = pk$$
$$q = p$$

therefore $x \equiv_k x$, as required.

## problem nine: proof critiques

i.

the theorem statement could have been written to much more clearly state the antecedent and consequent of its implication. the first statement of the proof should restate the antecedent of the theorem more directly.

ii.

the antecedent of the implication of the contradiction is not well formulated. the antecedent should be a existential-quantifier that negates the antecedent and not a universal-qantifier. 137 could have been initialized as a variable. the sentence "We know that there is no integer where is both odd and even." could have been ommited.

iii.

the contrapositive of the proof is not formulated correctly. the antecedent and the consequent of the theorem's implication should've been negated, thus the proof is a proof of the wrong theorem.

## problem 10: all squared away

i.

$$n = 3 = 2 \cdot 1 + 1$$
$$n = 5 = 2 \cdot 2 + 1$$
$$n = 7 = 2 \cdot 3 + 1$$
$$n = 9 = 2 \cdot 4 + 1$$
$$n = 11 = 2 \cdot 5 + 1$$

ii.

when $n = 2k + 1$, consider $m = 5$.

iii. **INCOMPLETE**

$y$ is an integer
$$m^2 + m2k + m$$
$$m(m + 2k + 1) = y^2$$
$$5^2 + 5X2Xk + 5$$


if n is an odd natural number and n >= c3, then there is an m elment of natural numbers where m > 0 and m^2 + mn is a perfect square

## problem 11: quarter-squares

**theorem:**
for all natural numbers $n$, if $\lfloor \frac{n}{2} \rfloor  \cdot \lceil \frac{n}{2} \rceil$ is odd, then $n$ is even.

**proof:**
we will assume for the sake of contradiction that for all natural numbers $n$, if $\lfloor \frac{n}{2} \rfloor  \cdot \lceil \frac{n}{2} \rceil$ is odd, then $n$ is odd.

$$\lfloor \frac{2k+1}{2} \rfloor  \cdot \lceil \frac{2k+1}{2} \rceil$$ 
$$\lfloor \frac{1}{2} + k \rfloor  \cdot \lceil \frac{1}{2} + k \rceil$$ 
$$k \cdot (k+1)$$
since an even number multiblied by an odd number is even, we've reached a contradiction.

therefore, $n$ is even, as required.

## problem 12: infinite deviation

since not every natural number has an infinite number of significant digits, there will alaways be a set that has an element that has infinitely many differentiating values for digits that represent the same significant figures (this can be proven will a similar approach to cantor's theorem).