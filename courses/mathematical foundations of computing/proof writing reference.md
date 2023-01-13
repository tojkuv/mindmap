# proof-writing reference

## general guidelines

- state the **antecedent** and **consequent** of the theorem implication
  - implication: \<antecedent\> \<conditional phrase (if, if and only if)> \<consequent\>
- variables must always be declared
- variables can be [or] uninitialized (left for [or] the reader, the theorem prover to initialize), initialized as a literal value, initialized as a composite of [and/or] literal values, other types
- type-check every statement that uses such variables 
- have each sentence introduce new information that helps complete [or] the proof, the disproof
  - set up a goal for each statement before introducing a new statement
  - introduce new variables if you need to proof an auxiliary statement
  - statements that do not introduce new variables should introduce logical steps to get closer to the completion of the proof, by taking some number of preceding statements and deriving a new statement in the form of an implication.
- variables are preferable over existentially quantified statements

## direct proofs: implications

an **implication** is a conditional statement in the form: 
$$ \text{if } P \text{ is true, then } Q \text{ is true.}  $$

- the **antecedent** is "$P \text{ is true}$".
- the **consequent** is "$Q \text{ is true}$".

direct proofs assume that the antecedent is true and proceed to proof the consequent

## direct proofs: universally-quantified statements

a **universally-quantified statement** has a placeholder variable and a claim that remains true regardless of the value assigned to the variable.

### template

**theorem:**
 \<universally-quantified statement> + \<antecedent of the implication> + \<consequent of the implication>

**proof:**
 \<request to consider a value for the universally-quantified statement that is bounded by the antecedent of the implication>. + *we need to show that* \<consequent of the implication>.

 (the actual logic of the proof)

*Therefore* \<consequent of the implication>, as required.

### examples

i.

**theorem:**
 For all languages $L$, if $L$ is regular, then $\bar{L}$ is regular.

**proof:**
consider a random regular language for $L$. we need to show that $\bar{L}$ is regular.

 (the actual logic of the proof)

Therefore $\bar{L}$ is regular, as required.

ii.

**theorem:**
 for any rectible integer $x$, if $x$ is Egan-prime, then $G[x,2]$ is unobserved.

**proof:**
 consider a random rectible integer $x$ that is Egan-prime, we need to show that $G[x,2]$ is unobserved.

(the actual logic of the proof)

Therefore, $G[x,2]$ is unobserved, as required.

iii.

**theorem:**
 for any integers $x$, $y$, and $z$, if $x^2 + y^2 = z^2$, then $(x + 1)^2 + (y + 1)^2 \neq (z + 1)^2$.

 **proof:**
  consider a random integers for $x$, $y$, and $z$ where $x^2 + y^2 = z^2$. we need to show that $(x + 1)^2 + (y + 1)^2 \neq (z + 1)^2$.

(the actual proof of the logic)

Therefore, $(x + 1)^2 + (y + 1)^2 \neq (z + 1)^2$, as required.

## direct proofs: existentially-quantified statements

an *existentially-quantified statement* has a placeholder variable and a claim that is true for at least one choice of the variable.

### template

**theorem:**
 \<existentially-quantified statement bounded by antecedent of the implication> such that \<consequent of the implication>

**proof:**
 \<initialize a value for the existentially-quantified statement that is bounded by antecedent of the implication>. + *we need to show that* \<consequent of the implication>.

 (the actual logic of the proof)

*Therefore* \<consequent of the implication>, as required.

## direct proofs: universally-quantified statement and existentially-quantified statements in the same theorem

### template

**theorem:**
 \<universally-quantified statement> +
 \<existentially-quantified statement bounded by antecedent of the implication> such that \<consequent of the implication>

**proof:**
 \<request to consider a value for the universally-quantified statement that is bounded by the antecedent of the implication> +
 \<initialize a value for the existentially-quantified statement that is bounded by the antecedent of the implication>. + *we need to show that* \<consequent of the implication>.

 (the actual logic of the proof)

*Therefore* \<consequent of the implication>, as required.

## direct proofs: biconditional statements

A *biconditional* is a statement of the form

$$P \text{ is true if and only if } Q \text{ is true}$$

the state of $P$ is completely derived from the state of $Q$ (where the state of $P$ is equivalent to the state of $Q$), thus they will always be the same value.

### template

**theorem:**
 \<antecedent of the implication> if an only if \<consequent of the implication>

**proof:**
 first, we need to proof the first implication (left to right).

 (the actual logic of the proof)

 next, we need to proof the second implication (left to right).

 (the actual logic of the proof)

*Therefore* \<biconditional statement>, as required.

## proof by contrapositive

### template

**proof:**
 we will proof \<the theorem>. to do so we will prove the contrapositive, \<the contrepositive of the theorem>

 (the actual logic of the proof)

 Therefore, \<the contrapositive of the theorem>, as required.

## proof by contracdiction

### template

**proof:**
 assume for the sake of contradiction \<the negation of the implication of the theorem>.

 (the actual logic that leads to the contradiction)

 We have reached a contradiction, therefore \<consequent of the implication of the theorem>, as required.

### logical table

| logical statement                          | negation of the logical statement                         |
| ------------------------------------------ | --------------------------------------------------------- |
| All $P$'s are $Q$'s                        | Some $P$ is not a $Q$                                     |
| No $P$'s are $Q$'s                         | Some $P$ is a $Q$                                         |
| Some $P$ is a $Q$                          | No $P$'s are $Q$'s                                        |
| Some $P$ is not a $Q$                      | All $P$'s are $Q$'s                                       |
| If $P$ is true, then $Q$ is true           | $P$ is true and $Q$ is false                              |
| $P$ is true and $Q$ is true                | $P$ is false, $Q$ is false, or both $P$ and $Q$ are false |
| $P$ is true, $Q$ is true, or both are true | both $P$ and $Q$ are false                                |