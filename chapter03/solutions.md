# Nielsen & Chuang — Chapter 3 Solutions

> Auto-generated solutions for exercises and problems from Chapter 3 (Introduction to Computer Science).

---

### Exercise 3.1 (Non-computable processes in Nature)

**Problem:**
How might we recognize that a process in Nature computes a function not computable by a Turing machine?

**Solution:**
To recognize that a natural process computes a function not computable by a Turing machine, we must bridge the gap between physical phenomena and mathematical computability theory. This requires a rigorous synthesis of physical modeling and mathematical proof. The recognition would likely proceed through the following logical steps:

1. **Mathematical Formalization of the Process:** We must first define the physical process as a mathematical function $f: \mathcal{X} \to \mathcal{Y}$, where $\mathcal{X}$ represents the set of possible initial physical configurations (inputs) and $\mathcal{Y}$ represents the set of possible final configurations (outputs). To connect this to standard computability theory, we must establish a reliable, finite encoding map $E: \Sigma^* \to \mathcal{X}$ and a decoding map $D: \mathcal{Y} \to \Sigma^*$, allowing us to translate discrete inputs $x \in \Sigma^*$ into physical states and physical states back into discrete outputs.

2. **Proof of Non-Computability:** We must mathematically prove that the composite function $g(x) = D \circ f \circ E(x)$ is not computable by any Turing machine. This is typically achieved by demonstrating a reduction from a known undecidable problem. For instance, if we can show that $g(x)$ computes the Halting function—i.e., $g(\langle M, w \rangle) = 1$ if and only if Turing machine $M$ halts on input $w$, and $g(\langle M, w \rangle) = 0$ otherwise—then $g$ is provably non-computable by Turing's Halting theorem.

3. **Physical Theory and Empirical Verification:** We must formulate a well-defined physical theory that predicts the natural process evaluates the function $f$. Because we cannot empirically test the infinite set of all possible inputs, we must verify the theory's predictions on a sufficiently large and diverse finite subset of inputs. If the empirical results perfectly match the theoretical predictions, and the theory itself is mathematically isomorphic to the non-computable function $g$, we gain confidence that the process computes a non-computable function.

4. **Finiteness of the Process:** Crucially, the physical process must yield the output in a finite amount of time and with finite physical resources (energy, space, etc.) for any given valid input $x$. If the process requires infinite time, infinite precision, or infinite energy to yield the correct output, it does not constitute a valid computation in the algorithmic sense, as it fails to provide a result within the finite bounds required by the definition of an effective procedure.

In summary, recognizing such a process requires identifying a physical system whose dynamics, according to a well-verified physical theory, map finite inputs to finite outputs in a way that is mathematically equivalent to solving a known undecidable problem. $\square$

> **Significance:**
> This exercise probes the foundations of the Church–Turing thesis, specifically its physical instantiation (the Physical Church–Turing thesis), which posits that any function computable by a physical process is computable by a Turing machine. Recognizing a non-computable process in Nature would falsify this thesis, demonstrating that the universe possesses intrinsic hypercomputational capabilities. Such a discovery would profoundly revolutionize both physics and computer science, necessitating an expansion of the theoretical framework of computation beyond the classical Turing model and potentially allowing us to harness Nature to solve currently undecidable problems.

---

### Exercise 3.2 (Turing numbers)

**Problem:**
Show that single-tape Turing machines can each be given a number from the list $1, 2, 3, \ldots$ in such a way that the number uniquely specifies the corresponding machine. We call this number the Turing number of the corresponding Turing machine. (Hint: Every positive integer has a unique prime factorization $p_1^{a_1} p_2^{a_2} \ldots p_k^{a_k}$, where $p_i$ are distinct prime numbers, and $a_1, \ldots, a_k$ are non-negative integers.)

**Solution:**
To show that each single-tape Turing machine can be uniquely numbered, we construct an injective mapping from the set of all valid Turing machines to the set of positive integers $\mathbb{Z}^+$. This process is a variant of Gödel numbering.

**Step 1: Formalize the components of a Turing Machine.**
A single-tape Turing machine is completely specified by a finite set of internal states $Q$, a finite tape alphabet $\Gamma$, and a finite set of program lines (transition rules). Without loss of generality, we can represent the states as integers $Q = \{1, 2, \dots, m\}$ and the symbols in the tape alphabet as integers $\Gamma = \{1, 2, \dots, n\}$. The tape head movement directions can also be represented by positive integers, e.g., $\{1, 2, 3\}$ for left, stay, and right, respectively. This ensures all components of a rule are positive integers.

**Step 2: Encode a single program line.**
A program line is a 5-tuple $\langle q, x, q', x', s \rangle$, where $q$ is the current state, $x$ is the symbol read, $q'$ is the next state, $x'$ is the symbol to write, and $s$ is the head movement direction. We can uniquely encode this 5-tuple into a single positive integer $c$ using the first five prime numbers:
$$ c = 2^q \cdot 3^x \cdot 5^{q'} \cdot 7^{x'} \cdot 11^s $$
By the Fundamental Theorem of Arithmetic, every distinct 5-tuple yields a distinct positive integer $c$, and given $c$, we can uniquely recover the 5-tuple by factoring it.

**Step 3: Encode the entire Turing Machine.**
A Turing machine consists of a finite sequence of $k$ program lines. Let the integer encodings of these lines, derived from Step 2, be $c_1, c_2, \dots, c_k$. We can encode the entire sequence of program lines into a single positive integer $N$ (the Turing number) using the sequence of prime numbers:
$$ N = p_1^{c_1} \cdot p_2^{c_2} \cdot p_3^{c_3} \dots p_k^{c_k} $$
where $p_i$ denotes the $i$-th prime number (i.e., $p_1=2, p_2=3, p_3=5, \dots$).

**Step 4: Verify uniqueness.**
According to the hint and the Fundamental Theorem of Arithmetic, the prime factorization of $N$ is strictly unique. Therefore, from $N$, we can uniquely recover the sequence of exponents $c_1, c_2, \dots, c_k$. Since each $c_i$ also possesses a unique prime factorization, we can uniquely recover each program line $\langle q, x, q', x', s \rangle$. Thus, the integer $N$ uniquely specifies the Turing machine. 

Since every Turing machine can be mapped to a unique positive integer $N \in \{1, 2, 3, \dots\}$, the set of all single-tape Turing machines is countable, and each can be assigned a unique Turing number. $\square$

> **Significance:**
> This result demonstrates that the set of all possible Turing machines is countable, which is a foundational concept in computability theory. The existence of a unique Turing number (or Gödel number) for each machine allows machines to be enumerated and systematically treated as inputs to other machines. This encoding is the essential prerequisite for the construction of a Universal Turing Machine and for formulating diagonalization arguments, such as the proof of the Halting problem, which establishes that there exist well-defined functions that are not computable by any Turing machine.

---

### Exercise 3.3 (Turing machine to reverse a bit string)

**Problem:**
Describe a Turing machine which takes a binary number $x$ as input, and outputs the bits of $x$ in reverse order. (Hint: In this exercise and the next it may help to use a multi-tape Turing machine and/or symbols other than $\triangleright$, $0$, $1$ and the blank.)

**Solution:**
Following the hint, we construct a 2-tape Turing machine. Tape 1 will hold the input string, and Tape 2 will be used to build the output string. Let the tape alphabet be $\Gamma = \{\triangleright, 0, 1, \sqcup\}$, where $\sqcup$ denotes the blank symbol. The set of states is $Q = \{q_{\text{seek}}, q_{\text{copy}}, q_{\text{halt}}\}$, with $q_{\text{seek}}$ as the initial state.

The machine operates in two main phases:
1. **Seek the end:** In state $q_{\text{seek}}$, the head on Tape 1 moves right until it encounters the first blank symbol, positioning itself over the last bit of the input string $x$. The head on Tape 2 remains stationary at the starting position.
2. **Copy in reverse:** In state $q_{\text{copy}}$, the head on Tape 1 reads the current bit and moves left, while the head on Tape 2 writes that same bit and moves right. This continues until the left-end marker $\triangleright$ is reached on Tape 1.

Formally, the transition function $\delta: Q \times \Gamma^2 \to Q \times \Gamma^2 \times \{L, R, S\}^2$ is defined as follows, where the tuples represent $( \text{Tape 1 symbol}, \text{Tape 2 symbol} )$ and the directions represent $( \text{Tape 1 head}, \text{Tape 2 head} )$:

**Phase 1: Seeking the end of the input**
- $\delta(q_{\text{seek}}, (\triangleright, \sqcup)) = (q_{\text{seek}}, (\triangleright, \sqcup), (R, S))$
- $\delta(q_{\text{seek}}, (0, \sqcup)) = (q_{\text{seek}}, (0, \sqcup), (R, S))$
- $\delta(q_{\text{seek}}, (1, \sqcup)) = (q_{\text{seek}}, (1, \sqcup), (R, S))$
- $\delta(q_{\text{seek}}, (\sqcup, \sqcup)) = (q_{\text{copy}}, (\sqcup, \sqcup), (L, S))$

**Phase 2: Copying the bits in reverse order**
- $\delta(q_{\text{copy}}, (0, \sqcup)) = (q_{\text{copy}}, (0, 0), (L, R))$
- $\delta(q_{\text{copy}}, (1, \sqcup)) = (q_{\text{copy}}, (1, 1), (L, R))$
- $\delta(q_{\text{copy}}, (\triangleright, \sqcup)) = (q_{\text{halt}}, (\triangleright, \sqcup), (S, S))$

When the machine enters $q_{\text{halt}}$, Tape 2 will contain the bits of $x$ in reverse order, preceded by the $\triangleright$ marker. $\square$

> **Significance:**
> This exercise demonstrates the utility of multi-tape Turing machines in simplifying algorithm design, particularly for string manipulation tasks like reversal. While a single-tape Turing machine could accomplish this (by repeatedly swapping the outermost unmatched bits, shifting the string, or using marker symbols), the multi-tape paradigm provides a more intuitive and efficient $O(n)$ solution. It reinforces the concept that augmenting the Turing machine with additional tapes does not change its fundamental computational power (what functions it can compute), but significantly affects its algorithmic efficiency and the complexity of its state transition descriptions.

---



---

### Exercise 3.5 (Halting problem with no inputs)

**Problem:**
Show that given a Turing machine $M$ there is no algorithm to determine whether $M$ halts when the input to the machine is a blank tape.

**Solution:**
We prove this by reduction from the standard Halting Problem. The standard Halting Problem asks whether a given Turing machine $M$ halts on a specific input $x$. It is a well-known result in computability theory that the standard Halting Problem is undecidable; that is, there exists no algorithm that can solve it for all possible pairs $(M, x)$.

Assume, for the sake of contradiction, that there exists an algorithm $A$ which solves the blank tape halting problem. That is, given any Turing machine $M'$, $A(M')$ outputs "yes" if $M'$ halts when started on a blank tape, and "no" otherwise.

Now, suppose we are given an arbitrary Turing machine $M$ and an arbitrary input string $x$. We construct a new Turing machine $M_x$ that depends on $x$ but ignores its own input tape. The machine $M_x$ is designed to perform the following steps upon being started:
1. Erase the input tape entirely, leaving it blank.
2. Write the string $x$ onto the blank tape.
3. Simulate the execution of $M$ on input $x$.

Let us analyze the behavior of $M_x$ when it is provided with a blank tape as its initial input:
- Step 1 does nothing, as the tape is already blank.
- Step 2 writes the string $x$ onto the tape.
- Step 3 simulates $M$ on $x$.

Therefore, $M_x$ halts on a blank tape if and only if $M$ halts on input $x$. 

If algorithm $A$ existed, we could use it to solve the standard Halting Problem for any pair $(M, x)$ by simply constructing the corresponding machine $M_x$ and evaluating $A(M_x)$. If $A(M_x)$ outputs "yes", then $M$ halts on $x$; if $A(M_x)$ outputs "no", then $M$ does not halt on $x$. 

This implies that the standard Halting Problem is decidable, which directly contradicts the established fact that it is undecidable. Thus, our initial assumption must be false. We conclude that there is no algorithm to determine whether an arbitrary Turing machine halts on a blank tape. $\square$

> **Significance:**
> This exercise demonstrates that the undecidability of the Halting Problem is not dependent on the complexity or specificity of the input provided to the machine. Even for the simplest possible input—a completely blank tape—determining whether a Turing machine will eventually halt remains an undecidable problem. This reinforces the fundamental limits of computation and algorithmic predictability established by Turing.

---

### Exercise 3.6 (Probabilistic halting problem)

**Problem:**
Suppose we number the probabilistic Turing machines using a scheme similar to that found in Exercise 3.2 and define the probabilistic halting function $h_p(x)$ to be 1 if machine $x$ halts on input of $x$ with probability at least $1/2$ and 0 if machine $x$ halts on input of $x$ with probability less than $1/2$. Show that there is no probabilistic Turing machine which can output $h_p(x)$ with probability of correctness strictly greater than $1/2$ for all $x$.

**Solution:**
We proceed by contradiction. Suppose there exists a probabilistic Turing machine $H$ that computes the probabilistic halting function $h_p(x)$ with a probability of correctness strictly greater than $1/2$ for all $x$. 

Let $M_x$ denote the probabilistic Turing machine indexed by $x$, and let $p_x$ be the true probability that $M_x$ halts on input $x$. By definition, the probabilistic halting function is:
$$ h_p(x) = \begin{cases} 1 & \text{if } p_x \ge 1/2 \\ 0 & \text{if } p_x < 1/2 \end{cases} $$

Since $H$ correctly outputs $h_p(x)$ with probability strictly greater than $1/2$, there exists some $\epsilon > 0$ such that for any input $x$:
$$ P(H(x) = h_p(x)) = \frac{1}{2} + \epsilon $$

Using $H$ as a subroutine, we can construct a new probabilistic Turing machine $D$ (the diagonalization machine) that takes an input $x$ and operates as follows:
1. Run $H(x)$.
2. If $H(x)$ outputs $1$, enter an infinite loop (i.e., halt with probability $0$).
3. If $H(x)$ outputs $0$, halt immediately (i.e., halt with probability $1$).

Because the probabilistic Turing machines are enumerated, $D$ must have an index in this enumeration; let this index be $d$. Thus, $M_d = D$. We now evaluate the behavior of $D$ on its own index $d$.

Let $p_d$ be the true probability that $D$ halts on input $d$. Based on the construction of $D$, its probability of halting is exactly the probability that $H(d)$ outputs $0$:
$$ p_d = P(D \text{ halts on } d) = P(H(d) = 0) $$

We now consider the two possible cases for $h_p(d)$:

**Case 1: $h_p(d) = 1$.**
This implies that the true halting probability $p_d \ge 1/2$. 
However, if $h_p(d) = 1$, the probability that $H(d)$ outputs the correct value is $P(H(d) = 1) = 1/2 + \epsilon$. 
Consequently, the probability that $H(d)$ outputs $0$ is $P(H(d) = 0) = 1 - (1/2 + \epsilon) = 1/2 - \epsilon$.
By the definition of $D$, this means $p_d = 1/2 - \epsilon < 1/2$, which contradicts the premise that $p_d \ge 1/2$.

**Case 2: $h_p(d) = 0$.**
This implies that the true halting probability $p_d < 1/2$. 
However, if $h_p(d) = 0$, the probability that $H(d)$ outputs the correct value is $P(H(d) = 0) = 1/2 + \epsilon$. 
By the definition of $D$, this means $p_d = 1/2 + \epsilon > 1/2$, which contradicts the premise that $p_d < 1/2$.

In both cases, we arrive at a contradiction. Therefore, our initial assumption must be false. There is no probabilistic Turing machine capable of computing $h_p(x)$ with a probability of correctness strictly greater than $1/2$ for all $x$. $\square$

> **Significance:**
> This problem demonstrates that the undecidability of the Halting problem extends to probabilistic models of computation. Even when relaxing the requirement of absolute certainty to a probabilistic advantage (strictly better than a random coin flip), the fundamental limits imposed by self-reference and diagonalization persist. This establishes a crucial boundary in computation theory: randomness and probability alone cannot circumvent the deepest structural limitations of computability, a principle that remains relevant even in the foundational limits of quantum computation.

---

### Exercise 3.7 (Halting oracle)

**Problem:**
Suppose a black box is made available to us which takes a non-negative integer $x$ as input, and then outputs the value of $h(x)$, where $h(\cdot)$ is the halting function defined in Box 3.2 on page 130. This type of black box is sometimes known as an oracle for the halting problem. Suppose we have a regular Turing machine which is augmented by the power to call the oracle. One way of accomplishing this is to use a two-tape Turing machine, and add an extra program instruction to the Turing machine which results in the oracle being called, and the value of $h(x)$ being printed on the second tape, where $x$ is the current contents of the second tape. It is clear that this model for computation is more powerful than the conventional Turing machine model, since it can be used to compute the halting function. Is the halting problem for this model of computation undecidable? That is, can a Turing machine aided by an oracle for the halting problem decide whether a program for the Turing machine with oracle will halt on a particular input?

**Solution:**
Yes, the halting problem for this model of computation is undecidable. A Turing machine aided by an oracle for the standard halting problem cannot decide whether a program for the Turing machine with the same oracle will halt on a particular input. 

To prove this, we use a diagonalization argument analogous to the one used for the standard halting problem (Box 3.2). 

Let $O$ denote the oracle for the standard halting function $h(x)$. An oracle Turing machine is a Turing machine that can query $O$ at any point during its computation. Since the set of all oracle Turing machines is countable, we can enumerate them, assigning each a unique index $x$. Let $M^O_x$ denote the oracle Turing machine with index $x$.

Define the *relativized halting function* $h^O(x)$ for this class of oracle Turing machines as:
$$
h^O(x) = \begin{cases} 
1 & \text{if } M^O_x \text{ halts upon input of } x \\
0 & \text{if } M^O_x \text{ does not halt upon input of } x 
\end{cases}
$$

Assume, for the sake of contradiction, that there exists an oracle Turing machine $HALT^O$ that can compute $h^O(x)$. That is, $HALT^O$ is an oracle Turing machine that takes an input $x$, queries the oracle $O$ as needed, and correctly outputs $h^O(x)$.

Using $HALT^O$ as a subroutine, we can construct a new oracle Turing machine $TURING^O(x)$ with the following pseudocode:

```
TURING^O(x)
  y = HALT^O(x)
  if y = 0 then
    halt
  else
    loop forever
  end if
```

Since $HALT^O$ is a valid oracle Turing machine, $TURING^O$ is also a valid oracle Turing machine. Therefore, $TURING^O$ must appear in our enumeration of oracle Turing machines, meaning it has some index $t$ such that $M^O_t = TURING^O$.

By the definition of the relativized halting function, $h^O(t) = 1$ if and only if $TURING^O$ halts on input $t$. 

However, by inspecting the program for $TURING^O$, we see that $TURING^O$ halts on input $t$ if and only if $HALT^O(t) = 0$, which occurs if and only if $h^O(t) = 0$. 

This yields a contradiction: $h^O(t) = 1$ if and only if $h^O(t) = 0$. Therefore, our initial assumption that the algorithm $HALT^O$ exists must be false. We conclude that there is no oracle Turing machine with oracle $O$ that can solve the halting problem for oracle Turing machines. $\square$

> **Significance:**
> This problem illustrates the concept of the **Turing jump** and the **arithmetic hierarchy**. It demonstrates that undecidability is not merely a barrier for standard Turing machines, but a structural feature of computation that persists even when the machine's capabilities are augmented. Providing an oracle for the halting problem solves the original halting problem but simultaneously introduces a new, higher-order halting problem that is similarly undecidable. This reveals an infinite hierarchy of increasingly undecidable problems, showing that there is no "ultimate" oracle that can solve all halting problems.

---

### Exercise 3.8 (Universality of NAND)

**Problem:**
Show that the NAND gate can be used to simulate the NOT, AND, and OR gates, provided wires, ancilla bits and FANOUT are available.

**Solution:**
Let the NAND gate be defined as a boolean function acting on two inputs $x$ and $y$, such that $\text{NAND}(x, y) = \neg(x \land y)$. To prove the universality of the NAND gate, we must demonstrate that the fundamental gates NOT, AND, and OR can be constructed using only NAND gates, wires, ancilla bits, and FANOUT. The FANOUT operation allows us to duplicate a bit (e.g., route a single input $x$ to two separate gates), which is essential for gates that require the same input twice.

**1. Simulating the NOT gate**
To construct a NOT gate, we require an output of $\neg x$ given an input $x$. Using FANOUT, we can feed the input $x$ into both inputs of a NAND gate:
$$ \text{NOT}(x) = \text{NAND}(x, x) = \neg(x \land x) = \neg x $$
Alternatively, using an ancilla bit constantly set to $1$, we can simulate the NOT gate as $\text{NAND}(x, 1) = \neg(x \land 1) = \neg x$.

**2. Simulating the AND gate**
To construct an AND gate, we require an output of $x \land y$ given inputs $x$ and $y$. We can achieve this by applying a NAND gate to the inputs, and then negating the result using our simulated NOT gate. This requires FANOUT to duplicate the output of the first NAND gate to feed both inputs of the second:
$$ \text{AND}(x, y) = \text{NOT}(\text{NAND}(x, y)) = \text{NAND}(\text{NAND}(x, y), \text{NAND}(x, y)) $$
Expanding the boolean logic:
$$ \text{NAND}(\text{NAND}(x, y), \text{NAND}(x, y)) = \neg(\neg(x \land y) \land \neg(x \land y)) = \neg(\neg(x \land y)) = x \land y $$

**3. Simulating the OR gate**
To construct an OR gate, we require an output of $x \lor y$ given inputs $x$ and $y$. By De Morgan's laws, we know that $x \lor y = \neg(\neg x \land \neg y)$. Thus, we can simulate an OR gate by negating both inputs individually (using the simulated NOT gate) and then passing the results through a NAND gate. This requires FANOUT to duplicate $x$ and $y$ for the NOT gates:
$$ \text{OR}(x, y) = \text{NAND}(\text{NOT}(x), \text{NOT}(y)) = \text{NAND}(\text{NAND}(x, x), \text{NAND}(y, y)) $$
Expanding the boolean logic:
$$ \text{NAND}(\neg x, \neg y) = \neg(\neg x \land \neg y) = x \lor y $$

Since NAND can be used to simulate NOT, AND, and OR, it forms a universal set of logic gates. $\square$

> **Significance:**
> The universality of the NAND gate is a foundational result in classical digital logic, demonstrating that any boolean function, no matter how complex, can be computed using just a single type of logic gate. This principle allows for the mass production of identical logic components, significantly simplifying the physical design and fabrication of classical microprocessors. In the context of quantum computing, this classical universality highlights a stark contrast: quantum gates must be reversible and unitary, meaning non-invertible classical gates like NAND and AND cannot be directly translated into quantum operations without the introduction of ancilla qubits to preserve information and ensure reversibility.

---

### Exercise 3.9

**Problem:**
Prove that $f(n)$ is $O(g(n))$ if and only if $g(n)$ is $\Omega(f(n))$. Deduce that $f(n)$ is $\Theta(g(n))$ if and only if $g(n)$ is $\Theta(f(n))$.

**Solution:**
We begin by recalling the standard definitions of the asymptotic notations for positive real-valued functions:
- $f(n) \in O(g(n))$ if and only if there exist positive constants $c$ and $n_0$ such that $0 \leq f(n) \leq c \cdot g(n)$ for all $n \geq n_0$.
- $g(n) \in \Omega(f(n))$ if and only if there exist positive constants $c'$ and $n_0'$ such that $0 \leq c' \cdot f(n) \leq g(n)$ for all $n \geq n_0'$.
- $f(n) \in \Theta(g(n))$ if and only if $f(n) \in O(g(n))$ and $f(n) \in \Omega(g(n))$.

**Part 1: Prove $f(n) \in O(g(n)) \iff g(n) \in \Omega(f(n))$**

*Forward direction ($\implies$):*
Assume $f(n) \in O(g(n))$. By definition, there exist positive constants $c$ and $n_0$ such that:
$$0 \leq f(n) \leq c \cdot g(n) \quad \text{for all } n \geq n_0$$
Since $c > 0$, we can divide the inequality by $c$ to obtain:
$$0 \leq \frac{1}{c} f(n) \leq g(n) \quad \text{for all } n \geq n_0$$
Let $c' = \frac{1}{c} > 0$ and $n_0' = n_0$. Then we have:
$$0 \leq c' \cdot f(n) \leq g(n) \quad \text{for all } n \geq n_0'$$
This is precisely the definition of $g(n) \in \Omega(f(n))$.

*Backward direction ($\impliedby$):*
Assume $g(n) \in \Omega(f(n))$. By definition, there exist positive constants $c'$ and $n_0'$ such that:
$$0 \leq c' \cdot f(n) \leq g(n) \quad \text{for all } n \geq n_0'$$
Since $c' > 0$, we can divide the inequality by $c'$ to obtain:
$$0 \leq f(n) \leq \frac{1}{c'} \cdot g(n) \quad \text{for all } n \geq n_0'$$
Let $c = \frac{1}{c'} > 0$ and $n_0 = n_0'$. Then we have:
$$0 \leq f(n) \leq c \cdot g(n) \quad \text{for all } n \geq n_0$$
This is precisely the definition of $f(n) \in O(g(n))$. 

Thus, $f(n) \in O(g(n))$ if and only if $g(n) \in \Omega(f(n))$. $\square$

**Part 2: Deduce $f(n) \in \Theta(g(n)) \iff g(n) \in \Theta(f(n))$**

Assume $f(n) \in \Theta(g(n))$. By definition, this means:
$$f(n) \in O(g(n)) \quad \text{and} \quad f(n) \in \Omega(g(n))$$

From the first part, we know that $f(n) \in O(g(n)) \iff g(n) \in \Omega(f(n))$. 
Similarly, by swapping the roles of $f$ and $g$ in the first part, we have $f(n) \in \Omega(g(n)) \iff g(n) \in O(f(n))$.

Substituting these equivalent statements, we find that $f(n) \in \Theta(g(n))$ implies:
$$g(n) \in \Omega(f(n)) \quad \text{and} \quad g(n) \in O(f(n))$$
By the definition of Big-Theta, this means $g(n) \in \Theta(f(n))$. 

The converse follows identically by symmetry (swapping $f$ and $g$ in the argument). Therefore, $f(n) \in \Theta(g(n))$ if and only if $g(n) \in \Theta(f(n))$. $\square$

> **Significance:**
> This exercise establishes the formal duality between upper bounds ($O$) and lower bounds ($\Omega$), and proves that the $\Theta$ notation defines an equivalence relation on the asymptotic growth rates of functions. In computation theory, this symmetry is crucial; it means stating that an algorithm's runtime is $\Theta(n^2)$ is completely unambiguous, as it guarantees the algorithm is bounded above and below by $n^2$ asymptotically, regardless of the direction of the comparison.

---

### Exercise 3.10 (Asymptotic Notation for Polynomials)

**Problem:**
Suppose $g(n)$ is a polynomial of degree $k$. Show that $g(n)$ is $O(n^l)$ for any $l \ge k$.

**Solution:**
Let $g(n)$ be a polynomial of degree $k$. We can express $g(n)$ explicitly as:
$$ g(n) = \sum_{i=0}^k a_i n^i $$
where $a_i$ are constant coefficients and the leading coefficient $a_k \neq 0$.

By the definition of Big-$O$ notation, $g(n) \in O(n^l)$ if there exist positive constants $c$ and $n_0$ such that $0 \le |g(n)| \le c n^l$ for all $n \ge n_0$.

Let us define the constant $A$ as the sum of the absolute values of the coefficients:
$$ A = \sum_{i=0}^k |a_i| $$
Since $a_k \neq 0$, it follows that $A > 0$.

For any $n \ge 1$, we have $n^i \le n^k$ for all integers $0 \le i \le k$. We can therefore bound the absolute value of $g(n)$ for $n \ge 1$ as follows:
$$ |g(n)| = \left| \sum_{i=0}^k a_i n^i \right| \le \sum_{i=0}^k |a_i| n^i \le \sum_{i=0}^k |a_i| n^k = A n^k $$

We are given that $l \ge k$. For all $n \ge 1$, it follows that $n^k \le n^l$. Substituting this into our inequality, we obtain:
$$ |g(n)| \le A n^k \le A n^l $$

By choosing the constants $c = A$ and $n_0 = 1$, we have demonstrated that:
$$ |g(n)| \le c n^l \quad \text{for all } n \ge n_0 $$
Thus, by the definition of Big-$O$ notation, $g(n)$ is $O(n^l)$ for any $l \ge k$. $\square$

> **Significance:**
> This exercise establishes a fundamental property of polynomial functions in computational complexity: any polynomial of degree $k$ is asymptotically bounded above by $n^l$ for any $l \ge k$. In the analysis of algorithms, particularly in defining complexity classes such as P (polynomial time) and BQP (bounded-error quantum polynomial time), this property justifies the focus on the highest-degree term and the abstraction of lower-order terms. It demonstrates that the specific degree of a polynomial is often secondary to the fact that it is bounded by some polynomial, allowing for broad categorization of algorithmic efficiency.

---

### Exercise 3.11

**Problem:**
Show that $\log n$ is $O(n^k)$ for any $k > 0$.

**Solution:**
By definition, a function $f(n)$ is $O(g(n))$ if there exist positive constants $c$ and $n_0$ such that $0 \le f(n) \le c g(n)$ for all $n \ge n_0$. 

To show that $\log n$ is $O(n^k)$ for any $k > 0$, we evaluate the limit of the ratio of the two functions as $n \to \infty$:
$$ \lim_{n \to \infty} \frac{\log n}{n^k} $$

Since the base of the logarithm does not affect the asymptotic behavior (as $\log_b n = \frac{\ln n}{\ln b}$ and $\ln b$ is merely a constant), we can use the natural logarithm $\ln n$ without loss of generality:
$$ \lim_{n \to \infty} \frac{\ln n}{n^k} $$

As $n \to \infty$, both $\ln n$ and $n^k$ tend to infinity, resulting in an indeterminate form of type $\infty / \infty$. We can therefore apply L'Hôpital's Rule by differentiating the numerator and the denominator with respect to $n$:
$$ \lim_{n \to \infty} \frac{\frac{d}{dn} \ln n}{\frac{d}{dn} n^k} = \lim_{n \to \infty} \frac{1/n}{k n^{k-1}} = \lim_{n \to \infty} \frac{1}{k n^k} $$

Since $k > 0$, $n^k \to \infty$ as $n \to \infty$. Thus, the limit evaluates to:
$$ \lim_{n \to \infty} \frac{1}{k n^k} = 0 $$

Because the limit of $\frac{\log n}{n^k}$ is $0$ as $n \to \infty$, it follows that for any chosen constant $c > 0$, there must exist a threshold $n_0$ such that $\frac{\log n}{n^k} \le c$ for all $n \ge n_0$. Multiplying both sides by $n^k$ yields $\log n \le c n^k$ for all $n \ge n_0$.

By the definition of Big-O notation, this proves that $\log n$ is $O(n^k)$ for any $k > 0$. $\square$

> **Significance:**
> This result formally establishes that any logarithmic function grows asymptotically slower than any polynomial function with a positive degree. In the context of algorithm analysis and computational complexity, it guarantees that an algorithm running in logarithmic time is strictly more efficient than any algorithm running in polynomial time, regardless of how small the polynomial exponent $k$ is.

---

### Exercise 3.12 ($n^{\log n}$ is super-polynomial)

**Problem:**
Show that $n^k$ is $O(n^{\log n})$ for any $k$, but that $n^{\log n}$ is never $O(n^k)$.

**Solution:**
Recall the definition of Big-O notation: $f(n) \in O(g(n))$ if and only if there exist constants $c > 0$ and $n_0 > 0$ such that $0 \le f(n) \le c g(n)$ for all $n \ge n_0$.

**Part 1: Show that $n^k \in O(n^{\log n})$ for any $k$.**

We want to show that there exist constants $c > 0$ and $n_0 > 0$ such that $n^k \le c n^{\log n}$ for all $n \ge n_0$. 

Consider the ratio of the two functions:
$$ \frac{n^k}{n^{\log n}} = n^{k - \log n} $$

For any fixed constant $k$, we can choose $n_0$ such that $\log n_0 > k$ (for instance, $n_0 = 2^{k+1}$). Then, for all $n \ge n_0$, we have $\log n \ge \log n_0 > k$, which implies that the exponent $k - \log n < 0$. 

Since $n \ge n_0 > 1$ and the exponent is negative, it follows that:
$$ n^{k - \log n} < 1 \implies n^k < n^{\log n} $$

Thus, choosing $c = 1$ and $n_0 = 2^{k+1}$, we have $n^k \le c n^{\log n}$ for all $n \ge n_0$. Therefore, $n^k \in O(n^{\log n})$. $\square$

**Part 2: Show that $n^{\log n} \notin O(n^k)$ for any $k$.**

We will proceed by contradiction. Assume that $n^{\log n} \in O(n^k)$ for some fixed $k$. By the definition of Big-O notation, there must exist constants $c > 0$ and $n_0 > 0$ such that:
$$ n^{\log n} \le c n^k \quad \text{for all } n \ge n_0 $$

Dividing both sides by $n^k$ (which is positive for $n \ge 1$), we obtain:
$$ n^{\log n - k} \le c $$

Taking the natural logarithm of both sides yields:
$$ (\log n - k) \ln n \le \ln c $$

However, as $n \to \infty$, $\log n \to \infty$ and $\ln n \to \infty$. Consequently, the product $(\log n - k) \ln n \to \infty$ as $n \to \infty$. This means that for any constant $\ln c$, there exists an $n' \ge n_0$ such that $(\log n' - k) \ln n' > \ln c$, which contradicts the inequality derived above.

Therefore, our initial assumption must be false, and $n^{\log n} \notin O(n^k)$ for any $k$. $\square$

> **Significance:**
> This exercise rigorously demonstrates that the function $n^{\log n}$ grows faster than any polynomial function $n^k$. Functions of this growth rate are termed "super-polynomial" (yet sub-exponential, as they grow slower than $2^{\epsilon n}$ for any $\epsilon > 0$). In computational complexity theory, this distinction is fundamental. For instance, the best known classical algorithm for integer factorization, the General Number Field Sieve, runs in super-polynomial time $O(n^{\log n})$, whereas Shor's quantum algorithm factors integers in polynomial time $O(n^3)$. This very separation in asymptotic growth constitutes the exponential speedup and computational advantage offered by quantum computing for certain problems.

---

### Exercise 3.13 ($n^{\log n}$ is sub-exponential)

**Problem:**
Show that $c^n$ is $\Omega(n^{\log n})$ for any $c > 1$, but that $n^{\log n}$ is never $\Omega(c^n)$.

**Solution:**
Recall the definition of the asymptotic lower bound: $f(n) = \Omega(g(n))$ if and only if there exist positive constants $c_0$ and $n_0$ such that $f(n) \ge c_0 g(n)$ for all $n \ge n_0$. A sufficient condition for $f(n) = \Omega(g(n))$ is that $\lim_{n \to \infty} \frac{f(n)}{g(n)} = \infty$.

**Part 1: Prove $c^n = \Omega(n^{\log n})$ for any $c > 1$.**

Consider the limit of the ratio of the two functions:
$$ \lim_{n \to \infty} \frac{c^n}{n^{\log n}} $$
To evaluate this limit, we take the natural logarithm of the ratio:
$$ \ln\left( \frac{c^n}{n^{\log n}} \right) = n \ln c - \log n \cdot \ln n = n \ln c - (\ln n)^2 $$
Since $c > 1$, we have $\ln c > 0$. The term $n \ln c$ grows linearly with $n$, whereas the term $(\ln n)^2$ grows polylogarithmically. Because linear growth strictly dominates polylogarithmic growth, it follows that:
$$ \lim_{n \to \infty} \left( n \ln c - (\ln n)^2 \right) = \infty $$
Consequently, the original limit diverges to infinity:
$$ \lim_{n \to \infty} \frac{c^n}{n^{\log n}} = \infty $$
Since the ratio grows without bound, for any constant $c_0 > 0$, there exists an $n_0$ such that $c^n \ge c_0 n^{\log n}$ for all $n \ge n_0$. Thus, by definition, $c^n = \Omega(n^{\log n})$.

**Part 2: Prove $n^{\log n} \neq \Omega(c^n)$ for any $c > 1$.**

If $n^{\log n}$ were $\Omega(c^n)$, there would exist positive constants $c_0$ and $n_0$ such that $n^{\log n} \ge c_0 c^n$ for all $n \ge n_0$. This would require the limit of their ratio to be bounded away from zero. However, from Part 1, we established that:
$$ \lim_{n \to \infty} \frac{n^{\log n}}{c^n} = \lim_{n \to \infty} \left( \frac{c^n}{n^{\log n}} \right)^{-1} = \frac{1}{\infty} = 0 $$
Because the ratio $\frac{n^{\log n}}{c^n}$ vanishes as $n \to \infty$, no positive constant $c_0$ can satisfy $n^{\log n} \ge c_0 c^n$ for all sufficiently large $n$. Therefore, $n^{\log n}$ is never $\Omega(c^n)$. $\square$

> **Significance:**
> This exercise rigorously establishes that the function $n^{\log n}$ grows faster than any polynomial (as shown in Exercise 3.12) but slower than any exponential function $c^n$ (where $c>1$). In computational complexity theory, this classifies $n^{\log n}$ as a sub-exponential function. This boundary is critical in algorithm analysis; for instance, the best-known classical algorithms for integer factorization run in sub-exponential time, distinguishing them from NP-hard problems that are widely believed to require exponential time.

---

### Exercise 3.14

**Problem:**
Suppose $e(n)$ is $O(f(n))$ and $g(n)$ is $O(h(n))$. Show that $e(n)g(n)$ is $O(f(n)h(n))$.

**Solution:**
By the definition of Big-O notation, $e(n)$ is $O(f(n))$ if and only if there exist positive constants $c_1$ and $n_1$ such that for all $n \geq n_1$,
$$0 \leq e(n) \leq c_1 f(n)$$

Similarly, $g(n)$ is $O(h(n))$ if and only if there exist positive constants $c_2$ and $n_2$ such that for all $n \geq n_2$,
$$0 \leq g(n) \leq c_2 h(n)$$

To show that $e(n)g(n)$ is $O(f(n)h(n))$, we must find a positive constant $c$ and an integer $n_0$ such that for all $n \geq n_0$,
$$0 \leq e(n)g(n) \leq c f(n)h(n)$$

Let $n_0 = \max(n_1, n_2)$ and $c = c_1 c_2$. Since $c_1 > 0$ and $c_2 > 0$, it follows that $c > 0$. For all $n \geq n_0$, both of the initial inequalities hold, and since all terms are non-negative, we can multiply the two inequalities together:
$$e(n)g(n) \leq (c_1 f(n))(c_2 h(n))$$
$$e(n)g(n) \leq (c_1 c_2) f(n)h(n)$$
$$e(n)g(n) \leq c f(n)h(n)$$

Thus, by definition, $e(n)g(n)$ is $O(f(n)h(n))$. $\square$

> **Significance:**
> This exercise demonstrates the multiplicative property of Big-O notation, which is a fundamental tool for analyzing the time and space complexity of algorithms. When an algorithm consists of nested operations—such as the nested loops in the compare-and-swap sorting algorithm provided in the text—this property allows us to rigorously combine the complexities of the individual components to determine the overall asymptotic complexity of the system.

---

### Exercise 3.15 (Lower bound for compare-and-swap based sorts)

**Problem:**
Suppose an $n$ element list is sorted by applying some sequence of compare-and-swap operations to the list. There are $n!$ possible initial orderings of the list. Show that after $k$ of the compare-and-swap operations have been applied, at most $2^k$ of the possible initial orderings will have been sorted into the correct order. Conclude that $\Omega(n \log n)$ compare-and-swap operations are required to sort all possible initial orderings into the correct order.

**Solution:**
Consider the execution of a compare-and-swap operation on a list. A compare-and-swap operation on two elements at positions $i$ and $j$ compares their values. If the element at $i$ is greater than the element at $j$, they are swapped; otherwise, the list remains unchanged. Thus, each compare-and-swap operation has exactly two possible outcomes based on the comparison: either a swap occurs, or it does not.

We can model the sequence of compare-and-swap operations as a binary decision tree. Each node in the tree represents a compare-and-swap operation, and the two outgoing edges represent the two possible outcomes (swap or no swap). An execution path from the root to a leaf corresponds to a specific sequence of outcomes for the $k$ operations. Since there are $k$ operations and each operation has 2 possible outcomes, there are at most $2^k$ distinct execution paths.

Given a specific sequence of outcomes (a fixed execution path), the overall transformation applied to the list is a fixed permutation (a composition of transpositions and identity operations). Because a permutation is a bijection, there is at most one initial ordering that can be mapped to the correctly sorted order under this specific sequence of outcomes. Since there are at most $2^k$ distinct execution paths, there can be at most $2^k$ initial orderings sorted into the correct order after $k$ operations.

To sort *all* $n!$ possible initial orderings of the list into the correct order, the number of distinct

---



---

### Exercise 3.17 (Factoring and P)

**Problem:**
Prove that a polynomial-time algorithm for finding the factors of a number $m$ exists if and only if the factoring decision problem is in P. 

*(Context: The factoring decision problem asks, given a composite integer $m$ and $l < m$, does $m$ have a non-trivial factor less than $l$?)*

**Solution:**
Let $n = \lceil \log_2 m \rceil$ be the size of the input $m$. We must prove that a polynomial-time algorithm for the factoring search problem exists if and only if the factoring decision problem is in P. We will prove both directions.

**($\implies$) Suppose there exists a polynomial-time algorithm $A_{\text{find}}$ that finds the factors of $m$.**
To solve the factoring decision problem for an input $(m, l)$, we can run $A_{\text{find}}$ on $m$. By assumption, $A_{\text{find}}$ outputs the non-trivial factors of $m$ in time $O(n^k)$ for some constant $k$. Once the factors are obtained, we simply check if any of the output factors is strictly less than $l$. Since the number of non-trivial factors of $m$ is bounded by $O(n)$, checking all of them against $l$ takes at most $O(n)$ time. The total running time is $O(n^k) + O(n) = O(n^k)$, which is polynomial in $n$. Thus, the factoring decision problem is in P.

**($\Longleftarrow$) Suppose the factoring decision problem is in P.**
This means there exists a polynomial-time algorithm $A_{\text{dec}}$ that, given $(m, l)$, outputs "yes" if $m$ has a non-trivial factor less than $l$, and "no" otherwise, in time $O(n^j)$ for some constant $j$. We can use $A_{\text{dec}}$ as an oracle to find the factors of $m$ in polynomial time using binary search and recursive division.

1.  **Finding the smallest factor:** Any non-trivial factor of $m$ must be less than or equal to $\sqrt{m}$. We perform a binary search on the interval $l \in \{2, 3, \dots, \lfloor\sqrt{m}\rfloor + 1\}$ to find the smallest $l^*$ such that $A_{\text{dec}}(m, l^*)$ returns "yes". 
    Because $A_{\text{dec}}(m, l)$ answers whether there is a factor *strictly less than* $l$, the transition from "no" to "yes" occurs exactly at $l^* = p_1 + 1$, where $p_1$ is the smallest non-trivial factor of $m$. Thus, $p_1 = l^* - 1$. 
    The range of the binary search is $\sqrt{m} \le 2^{n/2}$, so it requires $O(\log(\sqrt{m})) = O(n)$ queries to $A_{\text{dec}}$. Each query takes $O(n^j)$ time, so finding $p_1$ takes $O(n^{j+1})$ time.
2.  **Recursive factorization:** Once $p_1$ is found, we compute $m' = m / p_1$ using long division, which takes $O(n^2)$ time. We then recursively apply the same binary search procedure to $m'$ to find its smallest non-trivial factor.
3.  **Time complexity:** The number of recursive steps is bounded by the total number of prime factors of $m$ (counting multiplicity), which is at most $\log_2 m = O(n)$. Since each step takes $O(n^{j+1})$ time, the total time to find all factors is $O(n) \times O(n^{j+1}) = O(n^{j+2})$, which is polynomial in $n$.

Since both directions hold, a polynomial-time algorithm for finding the factors of $m$ exists if and only if the factoring decision problem is in P. $\square$

> **Significance:**
> This exercise demonstrates a fundamental concept in computational complexity: the equivalence between search problems and decision problems. It shows that for factoring, the ability to simply answer "yes" or "no" to whether a factor below a threshold exists is computationally just as powerful as the ability to explicitly produce the factors. This equivalence is crucial for defining complexity classes like NP based on decision problems without loss of generality,

---

### Exercise 3.18

**Problem:**
Prove that if $\text{coNP} \neq \text{NP}$ then $\text{P} \neq \text{NP}$.

**Solution:**
We will prove this statement by contraposition. That is, we will show that if $\text{P} = \text{NP}$, then it necessarily follows that $\text{coNP} = \text{NP}$. 

Assume that $\text{P} = \text{NP}$. 

First, recall that the complexity class $\text{P}$ is closed under complement. This means that for any language $L \in \text{P}$, its complement $\bar{L}$ is also in $\text{P}$. This follows because a deterministic Turing machine that decides $L$ in polynomial time can be converted into a machine that decides $\bar{L}$ in polynomial time simply by swapping the accept and reject states. Consequently, the class of complements of languages in $\text{P}$, denoted $\text{coP}$, is exactly equal to $\text{P}$:
$$ \text{coP} = \text{P} $$

Now, take the complement of both sides of our initial assumption $\text{P} = \text{NP}$. The complement of the class $\text{NP}$ is by definition $\text{coNP}$, and the complement of $\text{P}$ is $\text{coP}$. Thus, we have:
$$ \text{coP} = \text{coNP} $$

Substituting $\text{P}$ for $\text{coP}$ in the equation above yields:
$$ \text{P} = \text{coNP} $$

Since we assumed $\text{P} = \text{NP}$, we can substitute $\text{NP}$ for $\text{P}$ to obtain:
$$ \text{NP} = \text{coNP} $$

We have shown that $\text{P} = \text{NP}$ implies $\text{NP} = \text{coNP}$. By the law of contraposition, the negation of the conclusion implies the negation of the hypothesis. Therefore, if $\text{coNP} \neq \text{NP}$, then $\text{P} \neq \text{NP}$. $\square$

> **Significance:**
> This exercise establishes a fundamental relationship between the $\text{P}$ vs $\text{NP}$ and $\text{NP}$ vs $\text{coNP}$ conjectures. It demonstrates that proving $\text{coNP} \neq \text{NP}$ is at least as hard as proving the famous $\text{P} \neq \text{NP}$ conjecture, as the former directly implies the latter. In complexity theory, this means that the $\text{NP}$ vs $\text{coNP}$ question is a stronger (and arguably more difficult) open problem; resolving it would automatically resolve $\text{P}$ vs $\text{NP}$.

---

### Exercise 3.20 (Euler's Theorem)

**Problem:**
Prove Theorem 3.1 (Euler's theorem): A connected graph contains an Euler cycle if and only if every vertex has an even number of edges incident upon it.

**Solution:**
We prove the two directions of the "if and only if" statement separately.

**($\Rightarrow$)** Suppose a connected graph $G$ contains an Euler cycle. An Euler cycle is a closed walk that traverses every edge of the graph exactly once. Let $v_0$ be the starting and ending vertex of the cycle. For any vertex $v \neq v_0$, every time the cycle enters $v$ via an edge, it must subsequently leave $v$ via a different edge. Thus, the edges incident to $v$ are traversed in pairs. Since the cycle traverses all edges incident to $v$, the total number of edges incident upon $v$ (its degree) must be even. For the starting vertex $v_0$, the cycle leaves $v_0$ at the first step and returns to $v_0$ at the last step. Any intermediate visits to $v_0$ also consist of an entry followed by an exit. Therefore, the edges incident to $v_0$ are also traversed in pairs, meaning its degree is even as well. Hence, every vertex in $G$ has an even number of edges incident upon it.

**($\Leftarrow$)** Suppose $G$ is a connected graph in which every vertex has an even number of edges incident upon it. We can construct an Euler cycle algorithmically as follows:
1. Start at any vertex $v_0$ and arbitrarily follow a trail of unused edges. Because every vertex has an even degree, any time we enter a vertex other than $v_0$, there must be at least one unused edge available to leave. Thus, the trail can only terminate at the starting vertex $v_0$, forming a cycle $C_1$.
2. If $C_1$ traverses every edge in $G$, then it is an Euler cycle, and we are done.
3. If $C_1$ does not traverse every edge, remove the edges of $C_1$ from $G$ to form a new subgraph $G'$. Because $C_1$ enters and leaves each vertex an equal number of times, it uses an even number of edges incident to each vertex. Since all vertices in $G$ had even degrees, all vertices in $G'$ must also have even degrees.
4. Because $G$ is connected, there must be at least one vertex $v_1$ in $C_1$ that is incident to an edge in $G'$. Start a new trail from $v_1$ using only edges in $G'$. By the same logic, this trail must eventually return to $v_1$, forming a cycle $C_2$.
5. We can splice $C_2$ into $C_1$ at $v_1$ to form a larger cycle: traverse $C_1$ from $v_0$ to $v_1$, traverse $C_2$ completely, and then continue traversing $C_1$ from $v_1$ back to $v_0$.
6. Repeat this splicing process until all edges are included in the cycle. The resulting cycle is an Euler cycle for $G$.

Therefore, a connected graph contains an Euler cycle if and only if every vertex has an even number of edges incident upon it. $\square$

> **Significance:**
> Euler's theorem is historically the first theorem in graph theory, originating from Leonhard Euler's solution to the Königsberg bridge problem. In the context of computation theory, it provides a profound example of how a seemingly complex combinatorial search problem (finding a path visiting every edge) can be reduced to verifying a simple local parity condition. This reduction allows the Euler cycle decision problem to be solved in polynomial time (specifically, $O(n^3)$ or $O(E)$), placing it in the complexity class P. This stands in stark contrast to the Hamiltonian cycle problem (visiting every vertex), which is NP-complete, illustrating how subtle differences in problem constraints can lead to vastly different computational complexities.

---



---

### Exercise 3.21 (Transitive property of reduction)

**Problem:**
Show that if a language $L_1$ is reducible to the language $L_2$ and the language $L_2$ is reducible to $L_3$ then the language $L_1$ is reducible to the language $L_3$.

**Solution:**
By the definition of reduction provided in the text, a language $L_A$ is reducible to a language $L_B$ if there exists a polynomial-time Turing machine $R$ that maps an input $x$ to an output $R(x)$ such that $x \in L_A$ if and only if $R(x) \in L_B$.

Given that $L_1$ is reducible to $L_2$, there exists a polynomial-time Turing machine $R_{12}$ such that for any string $x$:
$$x \in L_1 \iff R_{12}(x) \in L_2$$

Given that $L_2$ is reducible to $L_3$, there exists a polynomial-time Turing machine $R_{23}$ such that for any string $y$:
$$y \in L_2 \iff R_{23}(y) \in L_3$$

To show that $L_1$ is reducible to $L_3$, we must construct a polynomial-time Turing machine $R_{13}$ such that for any string $x$:
$$x \in L_1 \iff R_{13}(x) \in L_3$$

Define the Turing machine $R_{13}$ as the composition of $R_{23}$ and $R_{12}$:
$$R_{13}(x) = R_{23}(R_{12}(x))$$

We first verify the logical equivalence. For any string $x$:
$$x \in L_1 \iff R_{12}(x) \in L_2$$
Let $y = R_{12}(x)$. Substituting $y$ into the second equivalence yields:
$$R_{12}(x) \in L_2 \iff R_{23}(R_{12}(x)) \in L_3$$
By chaining the equivalences, we obtain:
$$x \in L_1 \iff R_{13}(x) \in L_3$$
This satisfies the logical condition for reduction.

Next, we verify that $R_{13}$ operates in polynomial time. Suppose $R_{12}$ computes its output in time bounded by the polynomial $p_1(|x|)$, where $|x|$ is the length of the input string. The length of the output string $|R_{12}(x)|$ is bounded by the number of steps taken by the Turing machine, so $|R_{12}(x)| \le p_1(|x|)$. 

Suppose $R_{23}$ computes its output in time bounded by the polynomial $p_2(|y|)$. The time taken for $R_{23}$ to compute on input $R_{12}(x)$ is therefore bounded by $p_2(|R_{12}(x)|) \le p_2(p_1(|x|))$.

The total time for $R_{13}$ to compute $R_{23}(R_{12}(x))$ is the sum of the time taken by $R_{12}$ and the time taken by $R_{23}$:
$$T(|x|) \le p_1(|x|) + p_2(p_1(|x|))$$
Since the sum and composition of polynomials yield a polynomial, $T(|x|)$ is bounded by a polynomial in $|x|$. Thus, $R_{13}$ operates in polynomial time.

Since $R_{13}$ is a polynomial-time Turing machine satisfying $x \in L_1 \iff R_{13}(x) \in L_3$, the language $L_1$ is reducible to the language $L_3$. $\square$

> **Significance:**
> The transitive property of reduction is foundational in computational complexity theory. It guarantees that the relation "is reducible to" forms a preorder over formal languages. This transitivity is essential for defining completeness within complexity classes (such as NP-complete or PSPACE-complete); it ensures that if a newly discovered problem can be reduced to a known complete problem, and that complete problem reduces to all others in the class, the new problem is no harder than the complete problem, and conversely, reducing a known complete problem to a new problem immediately establishes the new problem's completeness.

---

### Exercise 3.22 (Completeness of Reduced Languages)

**Problem:**
Suppose $L$ is complete for a complexity class, and $L'$ is another language in the complexity class such that $L$ reduces to $L'$. Show that $L'$ is complete for the complexity class.

**Solution:**
Let $C$ be the complexity class in question. By definition, a language $L$ is complete for $C$ if and only if:
1. $L \in C$.
2. For every language $A \in C$, $A$ reduces to $L$ (denoted $A \le L$).

We are given that $L$ is complete for $C$, that $L' \in C$, and that $L \le L'$. We must show that $L'$ is complete for $C$, which requires verifying the two conditions above for $L'$.

**Condition 1:** We are explicitly given that $L' \in C$, so the first condition is immediately satisfied.

**Condition 2:** Let $A$ be an arbitrary language in $C$. Since $L$ is complete for $C$, it follows that $A \le L$. By the definition of a reduction (such as a polynomial-time Karp reduction), this means there exists a polynomial-time computable function $R_1$ such that for any input $x$:
$$ x \in A \iff R_1(x) \in L $$

We are also given that $L \le L'$. This means there exists a polynomial-time computable function $R_2$ such that for any input $y$:
$$ y \in L \iff R_2(y) \in L' $$

Consider the composition of these reduction functions, $R(x) = R_2(R_1(x))$. Since $R_1$ and $R_2$ are both polynomial-time computable, their composition $R$ is also polynomial-time computable. Furthermore, for any input $x$, we can chain the equivalences:
$$ x \in A \iff R_1(x) \in L \iff R_2(R_1(x)) \in L' \iff R(x) \in L' $$
This demonstrates that $A \le L'$.

Since $A$ was an arbitrary language in $C$, we conclude that every language in $C$ reduces to $L'$. Combined with the fact that $L' \in C$, this proves that $L'$ is complete for the complexity class $C$. $\square$

> **Significance:**
> This exercise establishes a fundamental transitive property of complete problems: if a known complete problem can be reduced to another problem in the same class, the latter must also be complete. This is the cornerstone of proving complexity results like NP-completeness. Instead of directly showing that every problem in a class reduces to a new problem (a daunting task), one only needs to show that the new problem is in the class and that a single known complete problem reduces to it. For instance, this is exactly the mechanism used to prove that the Boolean Satisfiability Problem (SAT) is NP-complete by reducing the Circuit Satisfiability Problem (CIRCUIT-SAT) to it, as outlined in the surrounding text of Nielsen & Chuang.

---

### Exercise 3.23 (SAT is NP-complete)

**Problem:**
Show that SAT is NP-complete by first showing that SAT is in NP, and then showing that CIRCUIT-SAT reduces to SAT. (Hint: for the reduction it may help to represent each distinct wire in an instance of CIRCUIT-SAT by different variables in a Boolean formula.)

**Solution:**
To prove that the satisfiability problem (SAT) is NP-complete, we must demonstrate two properties: (1) SAT is in the complexity class NP, and (2) SAT is NP-hard. Since CIRCUIT-SAT is known to be NP-complete, proving that CIRCUIT-SAT reduces to SAT in polynomial time will establish that SAT is NP-hard.

**Part 1: SAT is in NP**
A problem is in NP if a proposed solution (a "certificate") can be verified in polynomial time. For an instance of SAT, the input is a Boolean formula $\phi$. A certificate is an assignment of truth values to the variables $x_1, x_2, \ldots, x_n$. Given this assignment, we can evaluate the Boolean formula by substituting the values and applying the Boolean connectives ($\land, \lor, \neg$). The evaluation of each connective takes constant time, and the number of connectives is at most the length of the formula. Therefore, the formula can be evaluated in time polynomial in the size of the input, verifying whether the assignment satisfies $\phi$. Thus, SAT $\in$ NP.

**Part 2: CIRCUIT-SAT $\le_p$ SAT**
We must show that any instance of CIRCUIT-SAT can be reduced to an instance of SAT in polynomial time. Let $C$ be a Boolean circuit composed of AND, OR, and NOT gates, with input variables $x_1, \ldots, x_n$ and a designated output wire. We will construct a Boolean formula $\phi$ that is satisfiable if and only if the circuit $C$ is satisfiable.

Following the hint, we introduce a Boolean variable for each distinct wire in the circuit $C$. Let $y_i$ denote the variable corresponding to the $i$-th internal wire, and let $y_{out}$ denote the variable for the output wire. The input wires simply correspond to the input variables $x_1, \ldots, x_n$.

For each logic gate in $C$, we write a set of clauses that logically enforce the correct relationship between the input wires and the output wire of the gate:
1. **NOT gate** (input $a$, output $b$): The constraint is $b \iff \neg a$, which is equivalent to the CNF clause $(a \lor b) \land (\neg a \lor \neg b)$.
2. **AND gate** (inputs $a, b$, output $c$): The constraint is $c \iff (a \land b)$, which is equivalent to the CNF clauses $(\neg a \lor \neg b \lor c) \land (a \lor \neg c) \land (b \lor \neg c)$.
3. **OR gate** (inputs $a, b$, output $c$): The constraint is $c \iff (a \lor b)$, which is equivalent to the CNF clauses $(a \lor b \lor \neg c) \land (\neg a \lor c) \land (\neg b \lor c)$.

The formula $\phi$ is constructed as the conjunction (AND) of all the clauses from all the gates in the circuit, along with the unit clause $(y_{out})$ which enforces that the output of the circuit is 1 (true).

*Polynomial Time Construction:* The number of wires and gates in $C$ is bounded by the size of the circuit. Each gate contributes at most 3 clauses, each of constant size. Thus, $\phi$ can be constructed in time polynomial in the size of $C$.

*Equivalence of Satisfiability:*
- If $C$ is satisfiable, there exists an assignment to the input variables $x_1, \ldots, x_n$ that makes the output wire 1. Propagating these values through the circuit yields valid truth values for all internal wires. Assigning the corresponding variables $y_i$ and $y_{out}$ these exact values will satisfy all the gate constraints and the output constraint, meaning $\phi$ is satisfiable.
- If $\phi$ is satisfiable, there exists an assignment to all variables (including $x_i, y_i, y_{out}$) that satisfies all clauses. The gate constraints guarantee that the values of the internal wire variables $y_i$ are precisely the logical outputs of the gates given their input wire variables. Since $(y_{out})$ is satisfied, the output of the circuit is 1. Thus, the assignment restricted to the input variables $x_1, \ldots, x_n$ satisfies the circuit $C$.

Since CIRCUIT-SAT $\le_p$ SAT and CIRCUIT-SAT is NP-complete, SAT is NP-hard. Combined with Part 1, SAT is NP-complete. $\square$

> **Significance:**
> This exercise outlines the foundational step of the Cook-Levin theorem, which establishes SAT as the first known NP-complete problem. By reducing CIRCUIT-SAT to SAT, we transition from a topological, hardware-oriented model of computation (circuits) to a purely logical, software-oriented model (Boolean formulae). This is profoundly significant because it allows all subsequent NP-completeness proofs to be constructed via logical reductions from SAT (or its variant 3-SAT), forming the bedrock of computational complexity theory and the formal understanding of the P vs NP problem.

---



---

### Exercise 3.25 (PSPACE $\subseteq$ EXP)

**Problem:**
The complexity class EXP (for exponential time) contains all decision problems which may be decided by a Turing machine running in exponential time, that is time $O(2^{n^k})$, where $k$ is any constant. Prove that PSPACE $\subseteq$ EXP. (Hint: If a Turing machine has $l$ internal states, an $m$ letter alphabet, and uses space $p(n)$, argue that the machine can exist in one of at most $l \cdot m^{p(n)}$ different states, and that if the Turing machine is to avoid infinite loops then it must halt before revisiting a state.)

**Solution:**
Let $L$ be a language in PSPACE. By definition, there exists a deterministic Turing machine (DTM) $M$ that decides $L$ using a polynomial amount of space. Let $p(n)$ be the polynomial bounding the space used by $M$ on an input of length $n$. 

Assume $M$ has $l$ internal states and a tape alphabet of size $m$. At any point during its computation, the complete configuration (or "state" as referred to in the hint) of $M$ is uniquely determined by:
1. The current internal state of the machine (at most $l$ possibilities).
2. The contents of the work tape (at most $m^{p(n)}$ possibilities, since there are $p(n)$ tape cells and each can hold one of $m$ symbols).
3. The position of the head on the work tape (at most $p(n)$ possibilities).
4. The position of the head on the read-only input tape (at most $n+1$ possibilities).

Therefore, the total number of distinct configurations $N$ that $M$ can possibly enter is bounded by:
$$N \le l \cdot m^{p(n)} \cdot p(n) \cdot (n+1)$$

Because $M$ is a deterministic Turing machine, its transition function uniquely determines the next configuration from the current one. If $M$ ever revisits a configuration, it will repeat the exact same sequence of transitions indefinitely, entering an infinite loop. Since $M$ is a decider for $L$, it must halt on all inputs and therefore cannot enter an infinite loop. Consequently, $M$ must halt before revisiting any configuration. 

This implies that the maximum number of steps (time) $M$ can take before halting is strictly less than the total number of possible configurations $N$. We can bound this time $T(n)$ as follows:
$$T(n) \le l \cdot m^{p(n)} \cdot p(n) \cdot (n+1)$$

Since $p(n)$ is a polynomial, there exists a constant $c$ such that $p(n) = O(n^c)$ for large $n$. We can rewrite the bound on $T(n)$ by expressing $m^{p(n)}$ with a base of 2:
$$m^{p(n)} = 2^{p(n) \log_2 m}$$

Substituting this into our time bound yields:
$$T(n) \le l \cdot 2^{p(n) \log_2 m} \cdot p(n) \cdot (n+1)$$

Because $p(n) = O(n^c)$ and $\log_2 m$ is a constant, the dominant term in the exponent is $O(n^c)$. The polynomial factors $p(n)$ and $(n+1)$ grow much slower than exponential functions. Specifically, for a sufficiently large constant $k$ (e.g., $k = c+1$), it is guaranteed that:
$$l \cdot 2^{p(n) \log_2 m} \cdot p(n) \cdot (n+1) = O(2^{n^k})$$

Thus, the time taken by $M$ is bounded by an exponential function of the input size. By definition, this means $L \in \text{EXP}$. Since $L$ was an arbitrary language in PSPACE, we conclude that:
$$\text{PSPACE} \subseteq \text{EXP} \quad \square$$

> **Significance:**
> This result establishes a fundamental hierarchy in computational complexity theory, demonstrating that space is a more powerful resource than time in the worst case. Specifically, any problem solvable with a polynomial amount of memory can be solved in an exponential amount of time. This makes intuitive sense: a machine with limited memory can only be in a finite number of configurations, so if it runs longer than that finite number without halting, it must be stuck in an infinite loop. This proof provides a baseline relationship between space and time complexity classes, showing that PSPACE is strictly bounded above by EXP, though whether this inclusion is strict (PSPACE $\neq$ EXP) remains a major open problem.

---

### Exercise 3.26 (L ⊆P)

**Problem:**
The complexity class L (for logarithmic space) contains all decision problems which may be decided by a Turing machine running in logarithmic space, that is, in space $O(\log n)$. More precisely, the class L is defined using a two-tape Turing machine. The first tape contains the problem instance, of size $n$, and is a read-only tape, in the sense that only program lines which don't change the contents of the first tape are allowed. The second tape is a working tape which initially contains only blanks. The logarithmic space requirement is imposed on the second, working tape only. Show that $L \subseteq P$.

**Solution:**
To show that $L \subseteq P$, we must prove that any decision problem solvable in logarithmic space is also solvable in polynomial time. 

Let $M$ be a two-tape Turing machine that decides a language in $L$. By the definition of $L$, on an input of size $n$, the work tape of $M$ uses at most $O(\log n)$ space. Specifically, let the space used on the work tape be bounded by $c \log n$ for some constant $c > 0$.

A configuration of $M$ is completely determined by the following information:
1. The state of the Turing machine (there are $l$ possible states, where $l$ is a constant).
2. The contents of the work tape.
3. The position of the head on the work tape.
4. The position of the head on the read-only input tape.

We can count the maximum number of distinct configurations of $M$:
- The Turing machine can be in one of $l$ internal states.
- The work tape has an alphabet of size $m$ (a constant) and uses at most $c \log n$ cells. The number of possible strings on the work tape is $m^{c \log n}$.
- The work tape head can be in one of at most $c \log n + 1$ positions.
- The input tape head can be in one of $n$ positions (or $n+1$ if we include the blank at the end, but $O(n)$ suffices).

Thus, the total number of possible configurations is bounded by:
$$ N \le l \cdot m^{c \log n} \cdot (c \log n + 1) \cdot n $$

We can simplify $m^{c \log n}$ as follows:
$$ m^{c \log n} = (2^{\log m})^{c \log n} = 2^{c \log m \log n} = n^{c \log m} $$
Let $k = c \log m$. Since $c$ and $m$ are constants, $k$ is also a constant. Therefore, $m^{c \log n} = n^k$.

Substituting this back into the bound for $N$:
$$ N \le l \cdot n^k \cdot (c \log n + 1) \cdot n = O(n^{k+1} \log n) = O(n^{k+2}) $$
Since $k+2$ is a constant, the total number of possible configurations $N$ is polynomial in $n$.

If $M$ runs for more than $N$ steps, by the pigeonhole principle, it must revisit a configuration. Because the transition function of a deterministic Turing machine is well-defined, revisiting a configuration implies that $M$ has entered an infinite loop and will never halt. However, since $M$ is a decider for a language in $L$, it must halt on all inputs. Therefore, $M$ cannot run for more than $N$ steps.

Because the maximum number of steps $M$ can take is bounded by a polynomial in $n$, the running time of $M$ is $O(n^{k+2})$, which is polynomial time. Thus, any problem in $L$ can be decided in polynomial time, proving that $L \subseteq P$. $\square$

> **Significance:**
> This result establishes a fundamental relationship between space-bounded and time-bounded computation, specifically showing that logarithmic space is a more restrictive resource than polynomial time. It is a key part of the standard complexity class inclusions $L \subseteq P \subseteq NP \subseteq PSPACE \subseteq EXP$, demonstrating that spatial efficiency inherently imposes a strict limit on the temporal requirements of a deterministic computation.

---

### Exercise 3.27 (Approximation algorithm for VERTEX COVER)

**Problem:**
Let $G = (V, E)$ be an undirected graph. Prove that the following algorithm finds a vertex cover for $G$ that is within a factor two of being a minimal vertex cover:
$$ VC = \emptyset $$
$$ E' = E $$
do until $E' = \emptyset$
$\quad$ let $(\alpha, \beta)$ be any edge of $E'$
$\quad$ $VC = VC \cup \{\alpha, \beta\}$
$\quad$ remove from $E'$ every edge incident on $\alpha$ or $\beta$
return $VC$.

**Solution:**
To prove that the algorithm yields a vertex cover within a factor of two of the optimal (minimal) vertex cover, we must establish two facts: first, that the algorithm returns a valid vertex cover, and second, that the size of this cover is at most twice the size of the minimal vertex cover.

**1. The algorithm returns a valid vertex cover.**
During each iteration of the loop, an edge $(\alpha, \beta)$ is selected from $E'$, and both of its endpoints, $\alpha$ and $\beta$, are added to the set $VC$. Subsequently, all edges incident to either $\alpha$ or $\beta$ are removed from $E'$. Because any edge removed from $E'$ must be incident to at least one vertex in $VC$, every removed edge is covered by $VC$. The loop terminates only when $E' = \emptyset$, which implies that every edge in the original graph $G$ has been removed from $E'$ and is therefore incident to at least one vertex in $VC$. Thus, $VC$ is a valid vertex cover for $G$.

**2. The size of $VC$ is at most twice the size of the minimal vertex cover.**
Let $M$ be the set of all edges selected by the algorithm across all iterations. By the construction of the algorithm, when an edge $(\alpha, \beta)$ is selected, all edges incident to $\alpha$ or $\beta$ are removed from $E'$. This guarantees that no two edges in $M$ share a common vertex. A set of edges with no common vertices is known as a *matching*. 

In each iteration, exactly the two endpoints of the selected edge are added to $VC$. Therefore, the total number of vertices in $VC$ is exactly twice the number of edges in $M$:
$$ |VC| = 2|M| $$

Now, let $VC^*$ denote a minimal vertex cover for $G$. Because $VC^*$ must cover every edge in the graph, it must cover every edge in the matching $M$. Since the edges in $M$ are disjoint (they share no vertices), covering each edge in $M$ requires a distinct vertex in $VC^*$. Consequently, the size of any vertex cover must be at least the size of the matching $M$:
$$ |VC^*| \ge |M| $$

Combining the two equations, we find the relationship between the size of the algorithm's vertex cover and the minimal vertex cover:
$$ |VC| = 2|M| \le 2|VC^*| $$

This demonstrates that the algorithm finds a vertex cover whose size is at most twice the size of the minimal vertex cover, meaning it is guaranteed to be within a factor of two of the optimum. $\square$

> **Significance:**
> This problem illustrates a fundamental concept in computational complexity: while all NP-complete problems are equivalently hard with respect to finding exact solutions, their approximability can vary drastically. Vertex cover admits a constant-factor (2) polynomial-time approximation, whereas other NP-complete problems (such as the general Traveling Salesman Problem) do not admit any constant-factor approximation unless P = NP. This reveals that standard polynomial-time reductions do not necessarily preserve the structure required for good approximations, leading to a rich, finer-grained complexity theory of approximation algorithms (such as the class MAXSNP) that extends beyond the exact P vs NP dichotomy.

---

### Exercise 3.28 (Arbitrariness of the constant in the definition of BPP)

**Problem:**
Suppose $k$ is a fixed constant, $1/2 < k \le 1$. Suppose $L$ is a language such that there exists a Turing machine $M$ with the property that whenever $x \in L$, $M$ accepts $x$ with probability at least $k$, and whenever $x \notin L$, $M$ rejects $x$ with probability at least $k$. Show that $L \in \text{BPP}$.

**Solution:**
To show that $L \in \text{BPP}$, we must construct a probabilistic Turing machine $M'$ that decides $L$ with a success probability of at least $3/4$ for all inputs. We will achieve this by using probability amplification through repetition and applying the Chernoff bound.

Let $x$ be an input string. We run the original Turing machine $M$ on $x$ a total of $n$ times, where $n$ is an odd integer to avoid ties in the majority vote. Let $X_i$ be an indicator random variable for the $i$-th run of $M$ producing the correct answer. That is, $X_i = 1$ if $M$ correctly accepts (when $x \in L$) or correctly rejects (when $x \notin L$), and $X_i = 0$ otherwise.

By the problem statement, the probability of a correct outcome in a single run is at least $k$. Since $k > 1/2$, we can define $\epsilon = k - 1/2$, which implies $\epsilon > 0$. Thus, the probability of success for each independent run is:
$$P(X_i = 1) \ge \frac{1}{2} + \epsilon$$
and the probability of error is:
$$P(X_i = 0) \le \frac{1}{2} - \epsilon$$

The new Turing machine $M'$ will output the majority vote of these $n$ trials. $M'$ will make an error if and only if the sum of the correct outcomes is at most $n/2$. Using the Chernoff bound (Theorem 3.4 in the text), the probability of $M'$ making an error is bounded by:
$$P\left(\sum_{i=1}^n X_i \le \frac{n}{2}\right) \le e^{-2\epsilon^2 n}$$

For $L$ to be in $\text{BPP}$, the probability of error must be at most $1/4$, meaning the probability of success must be at least $3/4$. We therefore require:
$$e^{-2\epsilon^2 n} \le \frac{1}{4}$$

Taking the natural logarithm of both sides, we get:
$$-2\epsilon^2 n \le \ln\left(\frac{1}{4}\right) = -\ln 4$$
$$2\epsilon^2 n \ge \ln 4$$
$$n \ge \frac{\ln 4}{2\epsilon^2}$$

Since $k$ is a fixed constant strictly greater than $1/2$, $\epsilon = k - 1/2$ is a fixed positive constant. Therefore, $\frac{\ln 4}{2\epsilon^2}$ is merely a fixed constant. We can choose $n$ to be any odd integer greater than or equal to this constant. 

By running $M$ exactly $n$ times and taking the majority vote, the newly constructed Turing machine $M'$ accepts $x \in L$ with probability at least $3/4$ and rejects $x \notin L$ with probability at least $3/4$. By definition, this implies $L \in \text{BPP}$. $\square$

> **Significance:**
> This exercise demonstrates the robustness of the complexity class BPP. It proves that the choice of the $3/4$ threshold in the definition of BPP is essentially arbitrary; any constant probability strictly greater than $1/2$ defines the exact same class of languages. This is because probabilistic algorithms can be efficiently amplified—requiring only a polynomial (in fact, constant with respect to input size, logarithmic with respect to desired confidence) number of repetitions to exponentially suppress the error rate. Consequently, BPP is firmly established as the standard theoretical class for efficiently solvable decision problems on a classical probabilistic computer.

---

### Exercise 3.29 (Fredkin gate is self-inverse)

**Problem:**
Show that applying two consecutive Fredkin gates gives the same outputs as inputs. The Fredkin gate is a reversible logic gate with three input bits and three output bits, denoted as $a, b, c$ and $a', b', c'$, respectively. The bit $c$ is a control bit, which remains unchanged by the gate, so $c' = c$. The control bit dictates the operation on the other two bits: if $c = 0$, then $a$ and $b$ are left alone, meaning $a' = a$ and $b' = b$; if $c = 1$, then $a$ and $b$ are swapped, meaning $a' = b$ and $b' = a$.

**Solution:**
Let the initial inputs to the first Fredkin gate be $a, b, c$, and the outputs be $a', b', c'$. By the definition of the Fredkin gate, we have:
$$ c' = c $$
and the transformation of $a$ and $b$ is conditional on $c$:
- If $c = 0$, then $a' = a$ and $b' = b$.
- If $c = 1$, then $a' = b$ and $b' = a$.

Now, let us apply a second consecutive Fredkin gate to the outputs of the first gate. Let the inputs to the second gate be $a', b', c'$, and the final outputs be $a'', b'', c''$. By the definition of the Fredkin gate applied to these new inputs, we have:
$$ c'' = c' $$
Substituting $c' = c$, we immediately get:
$$ c'' = c $$

Next, we evaluate the transformation of $a'$ and $b'$ into $a''$ and $b''$, which is conditional on the control bit $c'$. Since $c' = c$, we can analyze the two possible cases for $c$:

**Case 1: $c = 0$**
Since $c = 0$, we have $c' = 0$. The first gate leaves $a$ and $b$ unchanged, so $a' = a$ and $b' = b$. 
Because $c' = 0$, the second gate also leaves its inputs unchanged, yielding:
$$ a'' = a' = a $$
$$ b'' = b' = b $$

**Case 2: $c = 1$**
Since $c = 1$, we have $c' = 1$. The first gate swaps $a$ and $b$, so $a' = b$ and $b' = a$.
Because $c' = 1$, the second gate swaps its inputs, yielding:
$$ a'' = b' = a $$
$$ b'' = a' = b $$

In both cases, the final outputs of the two consecutive Fredkin gates are exactly the original inputs:
$$ a'' = a, \quad b'' = b, \quad c'' = c $$
Thus, applying two consecutive Fredkin gates is equivalent to the identity operation, proving that the Fredkin gate is self-inverse. $\square$

> **Significance:**
> The self-inverse property of the Fredkin gate is fundamental to reversible computing. A self-inverse gate guarantees that any operation can be systematically undone by simply applying the same gate again, ensuring that no information is lost during the computation. This reversibility is a necessary condition for quantum computation and is deeply connected to Landauer's principle, which states that irreversible computations must dissipate energy. The Fredkin gate, alongside the Toffoli gate, serves as a universal primitive for constructing logically reversible circuits.

---



---



---



---

### Exercise 3.1 (Minsky machines)

**Problem:**
A Minsky machine consists of a finite set of registers, $r_1, r_2, \ldots, r_k$, each capable of holding an arbitrary non-negative integer, and a program, made up of orders of one of two types. The first type has the form:
$$ m: (r_j^+, n) $$
The interpretation is that at point $m$ in the program, register $r_j$ is incremented by one, and execution proceeds to point $n$ in the program. The second type of order has the form:
$$ m: (r_j^-, n, p) $$
The interpretation is that at point $m$ in the program, register $r_j$ is decremented if it contains a positive integer, and execution proceeds to point $n$ in the program. If register $r_j$ is zero then execution simply proceeds to point $p$ in the program. The program for the Minsky machine consists of a collection of such orders, of a form like:
$$ 1: (r_1^-, 2, 0) $$
$$ 2: (r_2^+, 1) $$
The starting and all possible halting points for the program are conventionally labeled zero. This program takes the contents of register $r_1$ and adds them to register $r_2$, while decrementing $r_1$ to zero.

(1) Prove that all (Turing) computable functions can be computed on a Minsky machine, in the sense that given a computable function $f(\cdot)$ there is a Minsky machine program that when the registers start in the state $(n, 0, \ldots, 0)$ gives as output $(f(n), 0, \ldots, 0)$.

(2) Sketch a proof that any function which can be computed on a Minsky machine, in the sense just defined, can also be computed on a Turing machine.

**Solution:**

**(1) Turing computable $\implies$ Minsky computable**

To prove this, we show that a Minsky machine can simulate a Turing machine. A Turing machine consists of an infinite tape, a finite alphabet $\Sigma = \{0, 1, \dots, B-1\}$, a finite state control $Q$, and a read/write head. We can simulate this using a Minsky machine with a sufficient number of registers.

We represent the Turing machine's tape using two registers, $L$ and $R$, which store the portions of the tape to the left and right of the head, respectively. We encode the tape contents as integers in base $B$. Let the tape symbols to the left of the head be $s_{-1}, s_{-2}, \dots$ and to the right (including the current cell) be $s_0, s_1, s_2, \dots$. We set:
$$ L = \sum_{i=1}^{\infty} s_{-i} B^{i-1} $$
$$ R = \sum_{i=0}^{\infty} s_i B^i $$
The current symbol under the head is simply $R \bmod B$. The Minsky machine uses its instruction labels to track the finite state control $Q$ of the Turing machine.

We must show that the Minsky machine can perform the basic Turing machine operations:
- **Read:** The current symbol is $R \bmod B$. A Minsky machine can compute the modulo of a constant $B$ by repeatedly decrementing $R$ and incrementing a temporary register $R'$ until $R$ reaches zero. During this process, a counter register $c$ is incremented. Whenever $c$ reaches $B$, it is reset to $0$ and a quotient register $q$ is incremented. When $R=0$, $c$ holds $R \bmod B$ and $q$ holds $\lfloor R/B \rfloor$. The original $R$ can be restored by multiplying $q$ by $B$ and adding $c$. The value of $c$ determines the Turing machine's transition.
- **Write:** To change the current symbol from $s_{old}$ to $s_{new}$, we compute $R \leftarrow R - s_{old} + s_{new}$. Subtraction of a constant is achieved by decrementing the register a fixed number of times.
- **Move Head Right:** Moving the head right corresponds to removing the least significant digit of $R$ and appending it to $L$. This is achieved by the assignments:
  $$ L \leftarrow L \cdot B + (R \bmod B) $$
  $$ R \leftarrow \lfloor R/B \rfloor $$
  Multiplication by a constant $B$ is performed by a loop that decrements $L$ by 1 and increments a temporary register by $B$, then transferring the temporary register back to $L$. Division by $B$ (with remainder) is performed as described in the read step.
- **Move Head Left:** Symmetrically, this is achieved by:
  $$ R \leftarrow R \cdot B + (L \bmod B) $$
  $$ L \leftarrow \lfloor L/B \rfloor $$

Since a Minsky machine can simulate the tape contents and the finite state control of a Turing machine, and can execute the read, write, and move operations required by the Turing machine's transition function, any Turing-computable function is Minsky-computable. $\square$

**(2) Minsky computable $\implies$ Turing computable**

To prove

---



---



---

### Problem 3.4 (Undecidability of dynamical systems)

**Problem:**
A Fractran program is essentially just a very simple dynamical system taking positive integers to positive integers. Prove that there is no algorithm to decide whether such a dynamical system ever reaches 1.

**Solution:**
We prove this by reduction from the Halting Problem for Turing machines.

Suppose, for the sake of contradiction, that there exists an algorithm $A$ which, given any Fractran program $P$ and an initial positive integer $m$, decides whether the dynamical system defined by $P$ ever reaches the state $1$.

Recall the undecidability of the Halting Problem: given an arbitrary Turing machine $M$ and an input $n$, there is no algorithm to decide whether $M$ halts on $n$. We can encode the input $n$ as the integer $2^n$.

Define a partial computable function $f$ such that:
$$ f(n) = \begin{cases} 0 & \text{if } M \text{ halts on input } n \\ \text{undefined} & \text{if } M \text{ does not halt on input } n \end{cases} $$

By the result of Problem 3.3, for any (partial) computable function $f(\cdot)$, there exists a Fractran program $P_f$ which, when started with the integer $2^n$, reaches $2^{f(n)}$ without going through any intermediate powers of $2$.

Consider the Fractran program $P_f$ corresponding to our defined function $f$. We run $P_f$ starting with the integer $2^n$:
1. If $M$ halts on input $n$, then $f(n) = 0$. The program $P_f$ will eventually reach $2^{f(n)} = 2^0 = 1$.
2. If $M$ does not halt on input $n$, then $f(n)$ is undefined. The program $P_f$ will never reach a power of $2$, and consequently, it will never reach $1$.

Therefore, the Fractran program $P_f$ started on $2^n$ reaches $1$ if and only if the Turing machine $M$ halts on input $n$.

If algorithm $A$ existed, we could decide whether $M$ halts on $n$ by simply constructing $P_f$ and running $A$ on the input $(P_f, 2^n)$. This would provide a decision procedure for the Halting Problem, which is a contradiction. 

Thus, there is no algorithm to decide whether a Fractran dynamical system ever reaches $1$. $\square$

> **Significance:**
> This problem demonstrates that even exceedingly simple dynamical systems, such as Fractran programs acting on integers, possess computational universality and are subject to the limits of computability. It illustrates that undecidability is not a property restricted to complex models like Turing machines, but naturally emerges in any system capable of universal computation, reinforcing the profound reach of Gödel's Incompleteness Theorems and the Halting Problem across computer science and dynamical systems theory.

---



---

### Problem 3.6 (Hardness of approximation of TSP)

**Problem:**
Let $r \geq 1$ and suppose that there is an approximation algorithm for TSP which is guaranteed to find the shortest tour among $n$ cities to within a factor $r$. Let $G = (V, E)$ be any graph on $n$ vertices. Define an instance of TSP by identifying cities with vertices in $V$, and defining the distance between cities $i$ and $j$ to be $1$ if $(i, j)$ is an edge of $G$, and to be $r|V| + 1$ otherwise. Show that if the approximation algorithm is applied to this instance of TSP then it returns a Hamiltonian cycle for $G$ if one exists, and otherwise returns a tour of length more than $r|V|$. From the NP-completeness of Hamiltonian cycle it follows that no such approximation algorithm can exist unless $P = NP$.

**Solution:**
Let $G = (V, E)$ be a graph with $|V| = n$. We construct an instance of the Traveling Salesman Problem (TSP) by defining a distance function $d$ on the set of cities $V$ such that:
$$
d(i, j) = \begin{cases} 
1 & \text{if } (i, j) \in E \\
r|V| + 1 & \text{if } (i, j) \notin E 
\end{cases}
$$
We are given an approximation algorithm for TSP that guarantees a solution within a factor $r$ of the optimal tour length. Let $L_{\text{opt}}$ be the length of the shortest possible tour, and $L_{\text{approx}}$ be the length of the tour returned by the approximation algorithm. The algorithm guarantees that $L_{\text{approx}} \leq r L_{\text{opt}}$.

We evaluate the two possible cases for the graph $G$:

**Case 1: $G$ has a Hamiltonian cycle.**
If $G$ contains a Hamiltonian cycle, there exists a tour that visits every vertex exactly once using only edges in $E$. The length of this tour is exactly $n = |V|$. Since all distances are positive, this must be the optimal tour, so $L_{\text{opt}} = |V|$. 
When the approximation algorithm is applied, it is guaranteed to return a tour of length:
$$L_{\text{approx}} \leq r L_{\text{opt}} = r|V|$$
Any tour that uses even a single edge not in $E$ will have a length of at least $(|V|-1) \cdot 1 + (r|V| + 1) = |V| - 1 + r|V| + 1 = (r+1)|V|$. Since $(r+1)|V| > r|V|$ for $r \geq 1$, a tour of length $\leq r|V|$ cannot contain any edges not in $E$. Therefore, the tour returned by the approximation algorithm must consist entirely of edges in $E$, meaning it corresponds exactly to a Hamiltonian cycle in $G$.

**Case 2: $G$ does not have a Hamiltonian cycle.**
If $G$ does not contain a Hamiltonian cycle, then any tour visiting all vertices must traverse at least one edge not in $E$. The length of such a tour is at least:
$$(|V|-1) \cdot 1 + (r|V| + 1) = (r+1)|V| > r|V|$$
Thus, any valid tour in this instance has a length strictly greater than $r|V|$. Consequently, the approximation algorithm must return a tour of length greater than $r|V|$.

**Conclusion:**
The above analysis shows that running the approximation algorithm on this constructed TSP instance solves the Hamiltonian cycle decision problem: if the algorithm returns a tour of length $\leq r|V|$, $G$ has a Hamiltonian cycle; if it returns a tour of length $> r|V|$, $G$ does not have a Hamiltonian cycle. 

Since the construction of the TSP instance from $G$ takes polynomial time, and the approximation algorithm runs in polynomial time by definition, this yields a polynomial-time algorithm for the Hamiltonian cycle problem. However, the Hamiltonian cycle problem is NP-complete. Therefore, such a polynomial-time approximation algorithm cannot exist unless $P = NP$. $\square$

> **Significance:**
> This problem demonstrates the inapproximability of the general Traveling Salesman Problem. While some constrained optimization problems admit efficient approximation algorithms (e.g., metric TSP), general TSP is provably hard to approximate within any constant factor unless $P = NP$. This establishes a fundamental limit in classical computation theory, highlighting the boundary between tractable approximation and computational intractability.

---

### Problem 3.7 (Reversible Turing machines)

**Problem:**
(1) Explain how to construct a reversible Turing machine that can compute the same class of functions as is computable on an ordinary Turing machine. (Hint: It may be helpful to use a multi-tape construction.)
(2) Give general space and time bounds for the operation of your reversible Turing machine, in terms of the time $t(x)$ and space $s(x)$ required on an ordinary single-tape Turing machine to compute a function $f(x)$.

**Solution:**

**(1) Construction of a Reversible Turing Machine**

An ordinary Turing machine (TM) is generally not reversible because its transition function may be non-injective; that is, multiple configurations can transition to the same subsequent configuration (e.g., erasing a symbol or merging state paths). To construct a reversible TM $R$ that computes the same class of functions as an ordinary TM $M$, we employ a 3-tape construction (originally due to Bennett):

- **Tape 1 (Input/Output Tape):** Initially contains the input $x$. It will also hold the final output.
- **Tape 2 (Work Tape):** Initially blank. This tape will simulate the tape of the ordinary TM $M$.
- **Tape 3 (History Tape):** Initially blank. This tape will record the sequence of states of $M$ to ensure the overall computation remains reversible.

The computation of $R$ proceeds in three phases:

**Phase 1: Forward Computation**
$R$ simulates the ordinary TM $M$ step-by-step. Tape 1 is treated as read-only, and Tape 2 is updated exactly as the tape of $M$ would be. At each step of the simulation, $R$ appends the current state of $M$ to Tape 3. Because the history tape records the exact sequence of states, the global configuration of $R$ at any time step is uniquely determined. This makes the transition function of $R$ injective, and thus the forward simulation is logically reversible. This phase continues until $M$ reaches its halting state.

**Phase 2: Copy Output**
When $M$ halts, Tape 2 contains the output $f(x)$. $R$ now copies the result $f(x)$ from Tape 2 to Tape 1. This copying process is performed reversibly (e.g., by appending $f(x)$ to Tape 1 without overwriting the original input $x$, mapping $(x, f(x), \text{blank}) \to (x \frown f(x), f(x), \text{blank})$).

**Phase 3: Reverse Computation**
To clean up the intermediate computational garbage, $R$ runs the simulation of $M$ in reverse. At each step, $R$ reads the last recorded state on Tape 3 to determine the previous state of $M$. Using this information, $R$ applies the inverse of $M$'s transition function on Tape 2 and erases the last symbol from Tape 3. This phase exactly undoes the work of Phase 1, restoring Tape 2 and Tape 3 to their initial blank states. The final configuration leaves Tape 1 containing the input $x$ alongside the output $f(x)$, with Tapes 2 and 3 blank.

Since any ordinary TM $M$ can be simulated by $R$ in this manner, $R$ can compute exactly the same class of functions as an ordinary TM, but does so reversibly.

**(2) Space and Time Bounds**

Let $t(x)$ and $s(x)$ be the time and space required by the ordinary single-tape TM $M$ to compute $f(x)$.

**Time Bounds:**
- Phase 1 (Forward computation) takes $O(t(x))$ time.
- Phase 2 (Copying the output) takes $O(s(x))$ time, since the output size cannot exceed the space used by $M$.
- Phase 3 (Reverse computation) takes $O(t(x))$ time.
The total time $T(x)$ required by the reversible TM $R$ is:
$$T(x) = O(t(x)) + O(s(x)) + O(t(x)) = O(t(x))$$

**Space Bounds:**
- Tape 1 holds the input $x$ and the output $f(x)$, requiring $O(|x| + s(x))$ space.
- Tape 2 simulates $M$ and thus requires $O(s(x))$ space.
- Tape 3 records the state of $M$ at each of the $t(x)$ steps, requiring $O(t(x))$ space.
The total space $S(x)$ required by the reversible TM $R$ is:
$$S(x) = O(|x| + s(x)) + O(s(x)) + O(t(x)) = O(t(x))$$

In summary, the reversible Turing machine operates with a time bound of $O(t(x))$ and a space bound of $O(t(x))$. $\square$

> **Significance:**
> This problem demonstrates Bennett's fundamental theorem of reversible computation

---

### Problem 3.7 (Reversible Turing machines)

**Problem:**
(1) Explain how to construct a reversible Turing machine that can compute the same class of functions as is computable on an ordinary Turing machine. (Hint: It may be helpful to use a multi-tape construction.)
(2) Give general space and time bounds for the operation of your reversible Turing machine, in terms of the time $t(x)$ and space $s(x)$ required on an ordinary single-tape Turing machine to compute a function $f(x)$.

**Solution:**
**(1)** To construct a reversible Turing machine (RTM) that computes the same class of functions as an ordinary (irreversible) Turing machine (TM), we employ Bennett's multi-tape construction. An ordinary TM may have transition functions that are not one-to-one (i.e., two distinct internal states and tape symbol configurations might transition to the same configuration), making it irreversible. To enforce reversibility, we must ensure that the entire computational history is uniquely determined by the final state.

We construct a 3-tape RTM $M_R$ to simulate an ordinary single-tape TM $M$ computing a function $f(x)$:
1.  **Input Tape:** Holds the input $x$ and remains read-only throughout the computation.
2.  **Work Tape:** Simulates the single tape of the ordinary TM $M$.
3.  **History Tape:** Records the sequence of internal states or transition indices of $M$ at each step.

The computation proceeds in three phases:
*   **Forward Computation:** $M_R$ simulates $M$ step-by-step. For each step of $M$, $M_R$ updates the Work Tape according to $M$'s transition function and appends the current internal state of $M$ (or the index of the transition applied) to the History Tape. Because the state of $M$ and the symbol under the head on the Work Tape uniquely determine the next step, appending this information makes the global transition function of $M_R$ injective, and thus reversible.
*   **Copying the Output:** Once $M$ reaches its halting state, the output $f(x)$ resides on the Work Tape. $M_R$ reversibly copies this output to a designated output section (e.g., a separate track on the Input Tape or a 4th tape). This copying operation is a permutation of symbols and is inherently reversible.
*   **Reversing the Computation:** To avoid leaving "garbage" information on the Work and History tapes (which would prevent the overall process from being reversible), $M_R$ reverses its forward computation. It reads the History Tape backwards to uniquely determine the reverse transitions, restoring the Work Tape to its initial blank state and erasing the History Tape. 

This process leaves only the input $x$ and the output $f(x)$, achieving a completely reversible computation of $f(x)$.

**(2)** Let $t(x)$ be the time and $s(x)$ be the space required by the ordinary TM $M$ to compute $f(x)$.
*   **Time Bounds:** The forward computation takes $t(x)$ steps. Copying the output takes $O(|x|)$ or $O(s(x))$ steps. The

---



---



---

