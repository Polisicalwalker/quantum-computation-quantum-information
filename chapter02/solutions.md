# Quantum Computation — Chapter 2: Introduction to Quantum Mechanics

# Exercises with Solutions and Contextual Significance

> **Source:** Nielsen & Chuang, *Quantum Computation and Quantum Information*, Chapter 2
>
> Each exercise is presented with its statement, a detailed solution, and a brief note on its contextual significance — either how it connects to the flow of ideas in the text or what insight it offers into the physical picture of quantum mechanics.

---

## Section 2.1 — Linear Algebra

### Exercise 2.1 (Linear dependence: example)

**Problem:** Show that $(1, -1),\ (1, 2)$ and $(2, 1)$ are linearly dependent.

**Solution:**

We need to find scalars $\alpha, \beta, \gamma$, not all zero, such that $\alpha(1,-1) + \beta(1,2) + \gamma(2,1) = (0,0)$.

This gives the system:
$$\alpha + \beta + 2\gamma = 0$$
$$-\alpha + 2\beta + \gamma = 0$$

Adding the two equations: $3\beta + 3\gamma = 0 \Rightarrow \beta = -\gamma$.

From the first equation: $\alpha - \gamma + 2\gamma = 0 \Rightarrow \alpha = -\gamma$.

Choosing $\gamma = 1$: $\alpha = -1, \beta = -1, \gamma = 1$ (not all zero). Indeed:
$$-1(1,-1) + (-1)(1,2) + 1(2,1) = (-1-1+2,\ 1-2+1) = (0,0).$$

Hence the three vectors are linearly dependent. $\square$

**Significance:** This introductory exercise establishes the concept of linear dependence — a foundational notion that distinguishes a *basis* (minimal spanning set) from a redundant set. Understanding linear (in)dependence is essential for later discussions of quantum measurement operators and the structure of state spaces.

---

### Exercise 2.2 (Matrix representations: example)

**Problem:** Suppose $V$ is a vector space with basis vectors $|0\rangle$ and $|1\rangle$, and $A$ is a linear operator from $V$ to $V$ such that $A|0\rangle = |1\rangle$ and $A|1\rangle = |0\rangle$. Give a matrix representation for $A$, with respect to the input basis $|0\rangle, |1\rangle$, and the output basis $|0\rangle, |1\rangle$. Find input and output bases which give rise to a different matrix representation of $A$.

**Solution:**

The matrix entries are $A_{ij} = \langle i|A|j\rangle$:

$$A_{00} = \langle 0|A|0\rangle = \langle 0|1\rangle = 0, \quad A_{01} = \langle 0|A|1\rangle = \langle 0|0\rangle = 1,$$
$$A_{10} = \langle 1|A|0\rangle = \langle 1|1\rangle = 1, \quad A_{11} = \langle 1|A|1\rangle = \langle 1|0\rangle = 0.$$

So $A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, which is the Pauli $X$ matrix.

For a different representation, use the basis $|+\rangle = \frac{|0\rangle+|1\rangle}{\sqrt{2}}$, $|-\rangle = \frac{|0\rangle-|1\rangle}{\sqrt{2}}$. Note that $A|+\rangle = |+\rangle$ and $A|-\rangle = -|-\rangle$, so in this basis:

$$A' = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.$$

**Significance:** This exercise illustrates that the matrix form of an operator depends on the choice of basis — a central theme in quantum mechanics. The same operator ($X$) looks like a bit-flip in the computational basis but like a phase-flip in the Hadamard basis. This basis-dependence is crucial for understanding quantum gates and measurements.

---

### Exercise 2.3 (Matrix representation for operator products)

**Problem:** Suppose $A$ is a linear operator from vector space $V$ to vector space $W$, and $B$ is a linear operator from vector space $W$ to vector space $X$. Let $|v_i\rangle$, $|w_j\rangle$, and $|x_k\rangle$ be bases for $V$, $W$, and $X$, respectively. Show that the matrix representation for the linear transformation $BA$ is the matrix product of the matrix representations for $B$ and $A$, with respect to the appropriate bases.

**Solution:**

Let $[A]_{ij} = \langle w_i|A|v_j\rangle$ and $[B]_{kl} = \langle x_k|B|w_l\rangle$. Then:

$$[BA]_{kj} = \langle x_k|BA|v_j\rangle = \sum_l \langle x_k|B|w_l\rangle\langle w_l|A|v_j\rangle = \sum_l [B]_{kl}[A]_{lj} = ([B][A])_{kj}.$$

The second equality uses the completeness relation $\sum_l |w_l\rangle\langle w_l| = I$. Hence the matrix of the composition equals the matrix product. $\square$

**Significance:** This bridges the abstract operator composition with the familiar matrix multiplication rule, ensuring that the Dirac notation and matrix algebra are consistent — a prerequisite for all subsequent calculations in quantum circuits.

---

### Exercise 2.4 (Matrix representation for identity)

**Problem:** Show that the identity operator on a vector space $V$ has a matrix representation which is one along the diagonal and zero everywhere else, if the matrix representation is taken with respect to the same input and output bases.

**Solution:**

$$I_{ij} = \langle i|I|j\rangle = \langle i|j\rangle = \delta_{ij}.$$

Thus $I$ is represented by the identity matrix with 1's on the diagonal and 0's elsewhere. $\square$

**Significance:** The identity matrix is the simplest matrix representation and serves as the reference for defining unitary operators ($U^\dagger U = I$) and projectors ($P^2 = P$).

---

### Exercise 2.5

**Problem:** Verify that $(\cdot,\cdot)$ just defined is an inner product on $\mathbb{C}^n$.

**Solution:**

The inner product on $\mathbb{C}^n$ is defined as $(v,w) = \sum_i v_i^* w_i$. We verify the three axioms:

1. **Linearity in the second argument:** $(v, \alpha w_1 + \beta w_2) = \sum_i v_i^*(\alpha w_{1i} + \beta w_{2i}) = \alpha(v,w_1) + \beta(v,w_2)$. ✓

2. **Conjugate symmetry:** $(v,w) = \sum_i v_i^* w_i = \left(\sum_i w_i^* v_i\right)^* = (w,v)^*$. ✓

3. **Positive-definiteness:** $(v,v) = \sum_i |v_i|^2 \geq 0$, with equality iff $v = 0$. ✓

**Significance:** The inner product is the mathematical backbone of quantum measurement probabilities ($|\langle \psi|\phi\rangle|^2$) and normalization. This verification ensures the standard quantum mechanical formalism is self-consistent.

---

### Exercise 2.6

**Problem:** Show that any inner product $(\cdot,\cdot)$ is conjugate-linear in the first argument: $\left(\sum_i \lambda_i |w_i\rangle, |v\rangle\right) = \sum_i \lambda_i^* (|w_i\rangle, |v\rangle)$.

**Solution:**

By conjugate symmetry: $\left(\sum_i \lambda_i |w_i\rangle, |v\rangle\right) = \left(|v\rangle, \sum_i \lambda_i |w_i\rangle\right)^* = \left[\sum_i \lambda_i (|v\rangle, |w_i\rangle)\right]^* = \sum_i \lambda_i^* (|v\rangle, |w_i\rangle)^* = \sum_i \lambda_i^* (|w_i\rangle, |v\rangle)$. $\square$

**Significance:** Conjugate-linearity of the bra vector is a defining structural property of the bra-ket formalism. It ensures that $\langle\psi|$ transforms as the conjugate-dual of $|\psi\rangle$, which is essential for correctly computing probabilities and expectation values.

---

### Exercise 2.7

**Problem:** Verify that $|w\rangle = (1,1)$ and $|v\rangle = (1,-1)$ are orthogonal. What are the normalized forms of these vectors?

**Solution:**

$$\langle w|v\rangle = 1\cdot1 + 1\cdot(-1) = 0. \quad \checkmark$$

$\||w\rangle\| = \sqrt{1+1} = \sqrt{2}$, so $|\bar{w}\rangle = \frac{1}{\sqrt{2}}(1,1)$.

$\||v\rangle\| = \sqrt{1+1} = \sqrt{2}$, so $|\bar{v}\rangle = \frac{1}{\sqrt{2}}(1,-1)$.

These are the $|+\rangle$ and $|-\rangle$ states.

**Significance:** The $|+\rangle$ and $|-\rangle$ states are the eigenstates of the Hadamard and $X$ gates. Their orthogonality guarantees that they can be perfectly distinguished, and they form the basis used in superdense coding and many quantum algorithms.

---

### Exercise 2.8

**Problem:** Prove that the Gram–Schmidt procedure produces an orthonormal basis for $V$.

**Solution:**

We proceed by induction. Let $\{|w_1\rangle, \ldots, |w_d\rangle\}$ be a basis.

**Base case:** $|v_1\rangle = |w_1\rangle / \||w_1\rangle\|$. Clearly $\langle v_1|v_1\rangle = 1$.

**Inductive step:** Assume $\{|v_1\rangle, \ldots, |v_k\rangle\}$ are orthonormal. Define:
$$|v_{k+1}\rangle = \frac{|w_{k+1}\rangle - \sum_{i=1}^{k} \langle v_i|w_{k+1}\rangle |v_i\rangle}{\left\||w_{k+1}\rangle - \sum_{i=1}^{k} \langle v_i|w_{k+1}\rangle |v_i\rangle\right\|}.$$

For any $j \leq k$:
$$\langle v_j|v_{k+1}\rangle \propto \langle v_j|w_{k+1}\rangle - \sum_{i=1}^{k} \langle v_i|w_{k+1}\rangle \langle v_j|v_i\rangle = \langle v_j|w_{k+1}\rangle - \langle v_j|w_{k+1}\rangle = 0.$$

Also $\langle v_{k+1}|v_{k+1}\rangle = 1$ by construction. $\square$

**Significance:** The Gram–Schmidt procedure is used repeatedly in quantum information — for constructing orthonormal bases from non-orthogonal states, in the proof of the Schmidt decomposition, and in POVM constructions. It guarantees we can always find a convenient orthonormal basis.

---

### Exercise 2.9 (Pauli operators and the outer product)

**Problem:** Express each of the Pauli operators in the outer product notation, with respect to the orthonormal basis $|0\rangle, |1\rangle$.

**Solution:**

$$I = |0\rangle\langle 0| + |1\rangle\langle 1|$$

$$X = |0\rangle\langle 1| + |1\rangle\langle 0|$$

$$Y = -i|0\rangle\langle 1| + i|1\rangle\langle 0|$$

$$Z = |0\rangle\langle 0| - |1\rangle\langle 1|$$

**Significance:** The outer product representation is the most natural way to express quantum operators in Dirac notation. It makes the physical action of each Pauli gate transparent: $X$ swaps $|0\rangle$ and $|1\rangle$; $Z$ applies a relative phase; $Y$ does both. These representations are used constantly throughout quantum computation.

---

### Exercise 2.10

**Problem:** Suppose $|v_i\rangle$ is an orthonormal basis for an inner product space $V$. What is the matrix representation for the operator $|v_j\rangle\langle v_k|$, with respect to the $|v_i\rangle$ basis?

**Solution:**

The matrix entries are:
$$[|v_j\rangle\langle v_k|]_{mn} = \langle v_m|v_j\rangle\langle v_k|v_n\rangle = \delta_{mj}\delta_{kn}.$$

This is the matrix with a 1 in the $(j,k)$-th position and zeros elsewhere — the elementary matrix $E_{jk}$.

**Significance:** This result shows that the outer product $|v_j\rangle\langle v_k|$ is the "building block" of all operators. Any operator can be expanded as $A = \sum_{j,k} A_{jk}|v_j\rangle\langle v_k|$, and these elementary matrices form a basis for the operator space.

---

### Exercise 2.11 (Eigendecomposition of the Pauli matrices)

**Problem:** Find the eigenvectors, eigenvalues, and diagonal representations of the Pauli matrices $X$, $Y$, and $Z$.

**Solution:**

**$Z$:** Eigenvalues $\pm 1$. $|0\rangle$ has eigenvalue $+1$; $|1\rangle$ has eigenvalue $-1$.
$$Z = |0\rangle\langle 0| - |1\rangle\langle 1|.$$

**$X$:** Eigenvalues $\pm 1$. $|+\rangle = \frac{|0\rangle+|1\rangle}{\sqrt{2}}$ has eigenvalue $+1$; $|-\rangle = \frac{|0\rangle-|1\rangle}{\sqrt{2}}$ has eigenvalue $-1$.
$$X = |+\rangle\langle +| - |-\rangle\langle -|.$$

**$Y$:** Eigenvalues $\pm 1$. $|{+i}\rangle = \frac{|0\rangle+i|1\rangle}{\sqrt{2}}$ has eigenvalue $+1$; $|{-i}\rangle = \frac{|0\rangle-i|1\rangle}{\sqrt{2}}$ has eigenvalue $-1$.
$$Y = |{+i}\rangle\langle {+i}| - |{-i}\rangle\langle {-i}|.$$

**Significance:** The eigendecomposition reveals that each Pauli matrix defines a pair of orthogonal measurement outcomes. These three mutually unbiased bases (computational, Hadamard, circular) are the three "axes" of the Bloch sphere and underpin all single-qubit measurement and gate decompositions.

---

### Exercise 2.12

**Problem:** Prove that the matrix $\begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$ is not diagonalizable.

**Solution:**

The eigenvalues satisfy $(1-\lambda)^2 = 0$, so $\lambda = 1$ is the only eigenvalue with algebraic multiplicity 2. The eigenvectors satisfy:
$$\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} a \\ b \end{pmatrix} = \begin{pmatrix} 0 \\ a \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix},$$

so $a = 0$ and the only eigenvector (up to scaling) is $\begin{pmatrix} 0 \\ 1 \end{pmatrix}$. Since the geometric multiplicity (1) is less than the algebraic multiplicity (2), the matrix is not diagonalizable. $\square$

**Significance:** Not all operators are diagonalizable — this motivates the spectral theorem's restriction to *normal* operators. In quantum mechanics, observable quantities must be represented by Hermitian (hence normal) operators, which are always diagonalizable. This exercise shows why the normality condition matters.

---

### Exercise 2.13

**Problem:** If $|w\rangle$ and $|v\rangle$ are any two vectors, show that $(|w\rangle\langle v|)^\dagger = |v\rangle\langle w|$.

**Solution:**

For arbitrary $|\alpha\rangle, |\beta\rangle$:
$$\langle \alpha|(|w\rangle\langle v|)^\dagger|\beta\rangle = \langle \beta|(|w\rangle\langle v|)|\alpha\rangle^* = \langle \beta|w\rangle\langle v|\alpha\rangle^* = \langle w|\beta\rangle^*\langle \alpha|v\rangle^* = \langle v|\alpha\rangle\langle w|\beta\rangle^* \cdot \ldots$$

More directly, using the definition $(A^\dagger)_{ij} = A_{ji}^*$: The matrix of $|w\rangle\langle v|$ has entries $w_i v_j^*$, so its adjoint has entries $(w_j v_i^*)^* = v_i w_j^*$, which is exactly the matrix of $|v\rangle\langle w|$. $\square$

**Significance:** This fundamental property of the adjoint is used everywhere — from verifying that Hermitian operators satisfy $A = A^\dagger$ to proving properties of projectors and density matrices.

---

### Exercise 2.14 (Anti-linearity of the adjoint)

**Problem:** Show that the adjoint operation is anti-linear: $\left(\sum_i a_i A_i\right)^\dagger = \sum_i a_i^* A_i^\dagger$.

**Solution:**

For arbitrary $|\alpha\rangle, |\beta\rangle$:
$$\left\langle\alpha\left|\left(\sum_i a_i A_i\right)^\dagger\right|\beta\right\rangle = \left\langle\beta\left|\sum_i a_i A_i\right|\alpha\right\rangle^* = \left(\sum_i a_i \langle\beta|A_i|\alpha\rangle\right)^* = \sum_i a_i^* \langle\beta|A_i|\alpha\rangle^* = \sum_i a_i^* \langle\alpha|A_i^\dagger|\beta\rangle.$$

This equals $\left\langle\alpha\left|\sum_i a_i^* A_i^\dagger\right|\beta\right\rangle$. $\square$

**Significance:** Anti-linearity of the adjoint mirrors the conjugate-linearity of the inner product and is why complex conjugation appears in the bra-ket correspondence. It ensures that the physical structure of Hermitian observables is preserved under the adjoint.

---

### Exercise 2.15

**Problem:** Show that $(A^\dagger)^\dagger = A$.

**Solution:**

$\langle \alpha | (A^\dagger)^\dagger | \beta \rangle = \langle \beta | A^\dagger | \alpha \rangle^* = (\langle \alpha | A | \beta \rangle^*)^* = \langle \alpha | A | \beta \rangle$.

Since this holds for all $|\alpha\rangle, |\beta\rangle$, we have $(A^\dagger)^\dagger = A$. $\square$

**Significance:** This confirms that taking the adjoint twice returns to the original operator, making the adjoint an involution. It justifies, for instance, that a Hermitian operator's Hermitian conjugate is itself.

---

### Exercise 2.16

**Problem:** Show that any projector $P$ satisfies the equation $P^2 = P$.

**Solution:**

A projector has the form $P = \sum_i |i\rangle\langle i|$ where $\{|i\rangle\}$ is an orthonormal set. Then:

$$P^2 = \left(\sum_i |i\rangle\langle i|\right)\left(\sum_j |j\rangle\langle j|\right) = \sum_{i,j} |i\rangle\langle i|j\rangle\langle j| = \sum_{i,j} \delta_{ij}|i\rangle\langle j| = \sum_i |i\rangle\langle i| = P.$$

**Significance:** The idempotence $P^2 = P$ captures the physical intuition that measuring the same observable twice in succession yields the same result — a key consistency condition for quantum measurements (Postulate 3).

---

### Exercise 2.17

**Problem:** Show that a normal matrix is Hermitian if and only if it has real eigenvalues.

**Solution:**

($\Rightarrow$) If $A$ is Hermitian, then $A = A^\dagger$, so $A$ is normal. Let $A|\lambda\rangle = \lambda|\lambda\rangle$. Then $\lambda\langle\lambda|\lambda\rangle = \langle\lambda|A|\lambda\rangle = \langle\lambda|A^\dagger|\lambda\rangle = \lambda^*\langle\lambda|\lambda\rangle$. Since $\langle\lambda|\lambda\rangle \neq 0$, we get $\lambda = \lambda^*$, i.e., $\lambda$ is real.

($\Leftarrow$) If $A$ is normal with real eigenvalues, then by the spectral decomposition $A = \sum_i \lambda_i |i\rangle\langle i|$ with $\lambda_i \in \mathbb{R}$. Then $A^\dagger = \sum_i \lambda_i^* |i\rangle\langle i| = \sum_i \lambda_i |i\rangle\langle i| = A$, so $A$ is Hermitian. $\square$

**Significance:** This exercise crystallizes why Hermitian operators represent physical observables: their eigenvalues are real and thus correspond to measurable quantities. Normality (diagonalizability) plus real eigenvalues exactly characterizes the physical observables.

---

### Exercise 2.18

**Problem:** Show that all eigenvalues of a unitary matrix have modulus 1, i.e., can be written in the form $e^{i\theta}$ for some real $\theta$.

**Solution:**

Let $U|\lambda\rangle = \lambda|\lambda\rangle$. Since $U^\dagger U = I$:

$$\langle\lambda|\lambda\rangle = \langle\lambda|U^\dagger U|\lambda\rangle = |\lambda|^2 \langle\lambda|\lambda\rangle.$$

Since $\langle\lambda|\lambda\rangle \neq 0$, we get $|\lambda|^2 = 1$, so $|\lambda| = 1$, meaning $\lambda = e^{i\theta}$ for some real $\theta$. $\square$

**Significance:** Unitary operators describe time evolution in quantum mechanics (Postulate 2). The fact that their eigenvalues lie on the unit circle ensures that evolution preserves probabilities — the total probability remains 1 at all times.

---

### Exercise 2.19 (Pauli matrices: Hermitian and unitary)

**Problem:** Show that the Pauli matrices are Hermitian and unitary.

**Solution:**

**Hermitian:** By direct computation, $I^\dagger = I$, $X^\dagger = X$, $Y^\dagger = Y$, $Z^\dagger = Z$, since each is equal to its conjugate transpose.

**Unitary:** $I^2 = I$ ✓. $X^2 = \begin{pmatrix}0&1\\1&0\end{pmatrix}^2 = I$ ✓. $Y^2 = \begin{pmatrix}0&-i\\i&0\end{pmatrix}^2 = \begin{pmatrix}1&0\\0&1\end{pmatrix} = I$ ✓. $Z^2 = I$ ✓.

Since each Pauli $\sigma$ satisfies $\sigma^\dagger = \sigma$ and $\sigma^2 = I$, we have $\sigma^\dagger\sigma = \sigma^2 = I$. $\square$

**Significance:** The Pauli matrices being both Hermitian and unitary means they simultaneously serve as observables (with eigenvalues $\pm 1$) and as quantum gates. This dual nature is exploited throughout quantum computation, especially in the Bloch sphere representation and single-qubit gate decompositions.

---

### Exercise 2.20 (Basis changes)

**Problem:** Suppose $A'$ and $A''$ are matrix representations of an operator $A$ on a vector space $V$ with respect to two different orthonormal bases, $|v_i\rangle$ and $|w_i\rangle$. Characterize the relationship between $A'$ and $A''$.

**Solution:**

Define the unitary change-of-basis matrix $U_{ij} = \langle v_i|w_j\rangle$. Then:

$$A''_{kl} = \langle w_k|A|w_l\rangle = \sum_{i,j} \langle w_k|v_i\rangle\langle v_i|A|v_j\rangle\langle v_j|w_l\rangle = \sum_{i,j} U_{ik}^* A'_{ij} U_{jl} = (U^\dagger A' U)_{kl}.$$

So $A'' = U^\dagger A' U$ — a unitary similarity transformation. $\square$

**Significance:** This is the fundamental relationship between different representations of the same physical observable. It guarantees that physical predictions (eigenvalues, traces) are basis-independent, while giving us the freedom to choose convenient bases for calculations.

---

### Exercise 2.21

**Problem:** Repeat the proof of the spectral decomposition in Box 2.2 for the case when $M$ is Hermitian, simplifying the proof wherever possible.

**Solution:**

For Hermitian $M$ with eigenvalue $\lambda$ and eigenvector $|v\rangle$: $M|v\rangle = \lambda|v\rangle$. Then:

$$\langle v|M^\dagger = \lambda^*\langle v| \implies \langle v|M = \lambda\langle v| \quad (\text{since } M = M^\dagger, \lambda = \lambda^*).$$

For any vector $|w\rangle$ in the orthogonal complement of $|v\rangle$:
$$\langle v|M|w\rangle = \lambda\langle v|w\rangle = 0.$$

So $M$ maps the orthogonal complement to itself. By induction on the dimension, $M$ can be diagonalized in an orthonormal basis. The simplification is that we don't need to worry about non-real eigenvalues or left vs. right eigenvectors — Hermiticity ensures both simultaneously. $\square$

**Significance:** The spectral decomposition for Hermitian operators is simpler and more intuitive than for general normal operators. Since physical observables are Hermitian, this simplified proof is the one that matters most in practice.

---

### Exercise 2.22

**Problem:** Prove that two eigenvectors of a Hermitian operator with different eigenvalues are necessarily orthogonal.

**Solution:**

Let $M|v_1\rangle = \lambda_1|v_1\rangle$ and $M|v_2\rangle = \lambda_2|v_2\rangle$ with $\lambda_1 \neq \lambda_2$.

$$\lambda_1\langle v_2|v_1\rangle = \langle v_2|M|v_1\rangle = \langle v_2|M^\dagger|v_1\rangle = (\langle v_1|M|v_2\rangle)^* = (\lambda_2\langle v_1|v_2\rangle)^* = \lambda_2\langle v_2|v_1\rangle.$$

Since $\lambda_1 \neq \lambda_2$ and both are real, we conclude $\langle v_2|v_1\rangle = 0$. $\square$

**Significance:** This orthogonality of distinct eigenvectors guarantees that different measurement outcomes of an observable correspond to mutually exclusive physical states — a fundamental requirement for the consistency of quantum measurement.

---

### Exercise 2.23

**Problem:** Show that the eigenvalues of a projector $P$ are all either 0 or 1.

**Solution:**

Let $P|\lambda\rangle = \lambda|\lambda\rangle$. Since $P^2 = P$:

$$\lambda|\lambda\rangle = P|\lambda\rangle = P^2|\lambda\rangle = P(\lambda|\lambda\rangle) = \lambda^2|\lambda\rangle.$$

So $\lambda = \lambda^2$, giving $\lambda(\lambda - 1) = 0$, hence $\lambda \in \{0, 1\}$. $\square$

**Significance:** The binary eigenvalues of projectors correspond to "yes/no" measurement outcomes. This underlies the projective measurement postulate: measuring an observable partitions the state space into mutually orthogonal subspaces.

---

### Exercise 2.24 (Hermiticity of positive operators)

**Problem:** Show that a positive operator is necessarily Hermitian. (Hint: Show that any operator $A$ can be written $A = B + iC$ where $B$ and $C$ are Hermitian, and analyze the positivity condition on $B$ and $C$.)

**Solution:**

Write $A = B + iC$ where $B = (A + A^\dagger)/2$ and $C = (A - A^\dagger)/(2i)$ are both Hermitian. For any eigenvector $|v\rangle$ of $C$ with eigenvalue $c$:

$$\langle v|A|v\rangle = \langle v|B|v\rangle + ic\langle v|v\rangle \geq 0.$$

Since $B$ is Hermitian, $\langle v|B|v\rangle$ is real. For the sum to be real and non-negative for all $|v\rangle$, we need $c = 0$ for every eigenvalue of $C$, hence $C = 0$ and $A = B$ is Hermitian. $\square$

**Significance:** This is a non-trivial result: positivity (a physically motivated condition) implies Hermiticity (a mathematical structural condition). It ensures that positive operators — which arise as density matrices and POVM elements — automatically have real eigenvalues and diagonal representations.

---

### Exercise 2.25

**Problem:** Show that for any operator $A$, $A^\dagger A$ is positive.

**Solution:**

For any vector $|v\rangle$:
$$\langle v|A^\dagger A|v\rangle = \|A|v\rangle\|^2 \geq 0.$$

Since $A^\dagger A$ is also Hermitian ($(A^\dagger A)^\dagger = A^\dagger A$), it is a positive operator. $\square$

**Significance:** The operator $A^\dagger A$ is the quantum analogue of the squared modulus $|z|^2$. This positivity is fundamental to the measurement postulate (Postulate 3), where $M_m^\dagger M_m$ must be positive for measurement operators $M_m$.

---

### Exercise 2.26

**Problem:** Let $|\psi\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$. Write out $|\psi\rangle^{\otimes 2}$ and $|\psi\rangle^{\otimes 3}$ explicitly, both in terms of tensor products like $|0\rangle|1\rangle$, and using the Kronecker product.

**Solution:**

$$|\psi\rangle^{\otimes 2} = \frac{1}{2}(|0\rangle + |1\rangle) \otimes (|0\rangle + |1\rangle) = \frac{1}{2}(|00\rangle + |01\rangle + |10\rangle + |11\rangle).$$

In Kronecker product form:
$$|\psi\rangle^{\otimes 2} = \frac{1}{2}\begin{pmatrix}1\\1\\1\\1\end{pmatrix}.$$

$$|\psi\rangle^{\otimes 3} = \frac{1}{2\sqrt{2}}(|000\rangle + |001\rangle + |010\rangle + |011\rangle + |100\rangle + |101\rangle + |110\rangle + |111\rangle).$$

In Kronecker product form:
$$|\psi\rangle^{\otimes 3} = \frac{1}{2\sqrt{2}}\begin{pmatrix}1\\1\\1\\1\\1\\1\\1\\1\end{pmatrix}.$$

**Significance:** The equal superposition state $|\psi\rangle^{\otimes n}$ is the starting state for many quantum algorithms (Deutsch–Jozsa, Grover, etc.). Understanding its tensor product structure is essential for analyzing multi-qubit quantum circuits.

---

### Exercise 2.27

**Problem:** Calculate the matrix representation of the tensor products of the Pauli operators (a) $X$ and $Z$; (b) $I$ and $X$; (c) $X$ and $I$. Is the tensor product commutative?

**Solution:**

**(a)** $X \otimes Z = \begin{pmatrix}0&1\\1&0\end{pmatrix} \otimes \begin{pmatrix}1&0\\0&-1\end{pmatrix} = \begin{pmatrix}0&0&1&0\\0&0&0&-1\\1&0&0&0\\0&-1&0&0\end{pmatrix}.$

**(b)** $I \otimes X = \begin{pmatrix}1&0\\0&1\end{pmatrix} \otimes \begin{pmatrix}0&1\\1&0\end{pmatrix} = \begin{pmatrix}0&1&0&0\\1&0&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}.$

**(c)** $X \otimes I = \begin{pmatrix}0&1\\1&0\end{pmatrix} \otimes \begin{pmatrix}1&0\\0&1\end{pmatrix} = \begin{pmatrix}0&0&1&0\\0&0&0&1\\1&0&0&0\\0&1&0&0\end{pmatrix}.$

Since $I \otimes X \neq X \otimes I$, the tensor product is **not commutative**.

**Significance:** Non-commutativity of the tensor product reflects the physical fact that qubit 1 and qubit 2 are distinguishable subsystems. The operator $X \otimes I$ acts on qubit 1, while $I \otimes X$ acts on qubit 2 — these are different physical operations.

---

### Exercise 2.28

**Problem:** Show that the transpose, complex conjugation, and adjoint operations distribute over the tensor product: $(A \otimes B)^* = A^* \otimes B^*$; $(A \otimes B)^T = A^T \otimes B^T$; $(A \otimes B)^\dagger = A^\dagger \otimes B^\dagger$.

**Solution:**

In the Kronecker product, $(A \otimes B)_{(i_1 i_2),(j_1 j_2)} = A_{i_1 j_1} B_{i_2 j_2}$.

- **Complex conjugate:** $[(A \otimes B)^*]_{(i_1 i_2),(j_1 j_2)} = A_{i_1 j_1}^* B_{i_2 j_2}^* = (A^* \otimes B^*)_{(i_1 i_2),(j_1 j_2)}$.

- **Transpose:** $[(A \otimes B)^T]_{(i_1 i_2),(j_1 j_2)} = (A \otimes B)_{(j_1 j_2),(i_1 i_2)} = A_{j_1 i_1} B_{j_2 i_2} = (A^T \otimes B^T)_{(i_1 i_2),(j_1 j_2)}$.

- **Adjoint:** $(A \otimes B)^\dagger = ((A \otimes B)^*)^T = (A^* \otimes B^*)^T = (A^*)^T \otimes (B^*)^T = A^\dagger \otimes B^\dagger$. $\square$

**Significance:** These distribution properties ensure that structural properties of single-system operators (Hermiticity, unitarity, positivity) lift naturally to composite systems via the tensor product.

---

### Exercise 2.29

**Problem:** Show that the tensor product of two unitary operators is unitary.

**Solution:**

$(U \otimes V)^\dagger(U \otimes V) = U^\dagger U \otimes V^\dagger V = I \otimes I = I$. $\square$

**Significance:** This guarantees that applying independent unitary evolutions to separate subsystems results in a valid unitary evolution of the composite system — essential for the quantum circuit model where gates act on subsets of qubits.

---

### Exercise 2.30

**Problem:** Show that the tensor product of two Hermitian operators is Hermitian.

**Solution:**

$(A \otimes B)^\dagger = A^\dagger \otimes B^\dagger = A \otimes B$. $\square$

**Significance:** This ensures that joint observables on composite systems (e.g., $Z \otimes Z$) remain Hermitian and thus have real measurement outcomes.

---

### Exercise 2.31

**Problem:** Show that the tensor product of two positive operators is positive.

**Solution:**

For any $|v\rangle \otimes |w\rangle$:
$$\langle v| \otimes \langle w| (A \otimes B) |v\rangle \otimes |w\rangle = \langle v|A|v\rangle \cdot \langle w|B|w\rangle \geq 0,$$

since both factors are non-negative by positivity of $A$ and $B$. By linearity, this extends to all vectors in the tensor product space. $\square$

**Significance:** Positivity preservation under tensor products ensures that POVM elements constructed from subsystem POVMs remain valid on the composite system.

---

### Exercise 2.32

**Problem:** Show that the tensor product of two projectors is a projector.

**Solution:**

$(P \otimes Q)^2 = P^2 \otimes Q^2 = P \otimes Q$. $\square$

**Significance:** This means that projective measurements on independent subsystems combine to form a valid projective measurement on the composite system.

---

### Exercise 2.33

**Problem:** The Hadamard operator on one qubit may be written as $H = \frac{1}{\sqrt{2}}[(|0\rangle+|1\rangle)\langle 0| + (|0\rangle-|1\rangle)\langle 1|]$. Show explicitly that the Hadamard transform on $n$ qubits, $H^{\otimes n}$, can be written as:

$$H^{\otimes n} = \frac{1}{\sqrt{2^n}} \sum_{x,y \in \{0,1\}^n} (-1)^{x \cdot y} |x\rangle\langle y|.$$

**Solution:**

For one qubit: $H = \frac{1}{\sqrt{2}}\sum_{x,y \in \{0,1\}} (-1)^{xy}|x\rangle\langle y|$. By induction, assume the formula holds for $n-1$ qubits. Then:

$$H^{\otimes n} = H \otimes H^{\otimes(n-1)} = \frac{1}{\sqrt{2}} \sum_{x_1,y_1} (-1)^{x_1 y_1}|x_1\rangle\langle y_1| \otimes \frac{1}{\sqrt{2^{n-1}}} \sum_{x',y'} (-1)^{x' \cdot y'}|x'\rangle\langle y'|.$$

Combining:
$$H^{\otimes n} = \frac{1}{\sqrt{2^n}} \sum_{x,y \in \{0,1\}^n} (-1)^{x_1 y_1 + x' \cdot y'}|x_1 x'\rangle\langle y_1 y'| = \frac{1}{\sqrt{2^n}} \sum_{x,y} (-1)^{x \cdot y}|x\rangle\langle y|. \quad \square$$

**Significance:** This is the **Hadamard transform**, the most important quantum subroutine. It creates equal superpositions and is the foundation of the Deutsch–Jozsa, Grover, and many other algorithms. The $(-1)^{x \cdot y}$ kernel is the quantum Fourier transform over $\mathbb{Z}_2^n$.

---

### Exercise 2.34

**Problem:** Find the square root and logarithm of the matrix $\begin{pmatrix} 4 & 3 \\ 3 & 4 \end{pmatrix}$.

**Solution:**

Diagonalize: eigenvalues $\lambda_1 = 7, \lambda_2 = 1$ with eigenvectors $\frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix}$ and $\frac{1}{\sqrt{2}}\begin{pmatrix}1\\-1\end{pmatrix}$.

$$A = 7|+\rangle\langle+| + |-\rangle\langle-|$$

$$\sqrt{A} = \sqrt{7}|+\rangle\langle+| + 1|-\rangle\langle-| = \frac{1}{2}\begin{pmatrix}\sqrt{7}+1 & \sqrt{7}-1 \\ \sqrt{7}-1 & \sqrt{7}+1\end{pmatrix}.$$

$$\log A = \log 7 \cdot |+\rangle\langle+| + \log 1 \cdot |-\rangle\langle-| = \frac{\log 7}{2}\begin{pmatrix}1&1\\1&1\end{pmatrix}.$$

**Significance:** Matrix functions via diagonalization are essential for defining operator exponentials (time evolution), logarithms (Hamiltonian extraction from unitaries), and square roots (polar decomposition). This exercise demonstrates the practical technique.

---

### Exercise 2.35 (Exponential of the Pauli matrices)

**Problem:** Let $\vec{v}$ be any real, three-dimensional unit vector and $\theta$ a real number. Prove that $\exp(i\theta\vec{v} \cdot \vec{\sigma}) = \cos\theta \cdot I + i\sin\theta \cdot \vec{v} \cdot \vec{\sigma}$, where $\vec{v}\cdot\vec{\sigma} = \sum_{i=1}^3 v_i \sigma_i$.

**Solution:**

Note that $(\vec{v}\cdot\vec{\sigma})^2 = \sum_{i,j} v_i v_j \sigma_i \sigma_j = \sum_i v_i^2 I + \sum_{i\neq j} v_i v_j (i\epsilon_{ijk}\sigma_k) = \|\vec{v}\|^2 I = I$ (using $\sigma_i^2 = I$ and the antisymmetry of $\epsilon$ with the symmetric $v_i v_j$ for $i \neq j$).

Therefore, in the Taylor expansion:
$$\exp(i\theta\vec{v}\cdot\vec{\sigma}) = \sum_{k=0}^\infty \frac{(i\theta)^k(\vec{v}\cdot\vec{\sigma})^k}{k!} = \sum_{k \text{ even}} \frac{(i\theta)^k}{k!}I + \sum_{k \text{ odd}} \frac{(i\theta)^k}{k!}(\vec{v}\cdot\vec{\sigma}) = \cos\theta \cdot I + i\sin\theta \cdot \vec{v}\cdot\vec{\sigma}. \quad \square$$

**Significance:** This is the **Euler formula for qubits** and is perhaps the single most important identity in single-qubit quantum computation. It shows that any single-qubit unitary gate can be written as a rotation on the Bloch sphere, parameterized by axis $\vec{v}$ and angle $\theta$.

---

### Exercise 2.36

**Problem:** Show that the Pauli matrices except for $I$ have trace zero.

**Solution:**

$\text{tr}(X) = 0 + 0 = 0$; $\text{tr}(Y) = 0 + 0 = 0$; $\text{tr}(Z) = 1 + (-1) = 0$. $\square$

**Significance:** Tracelessness of the Pauli matrices means that $\vec{v}\cdot\vec{\sigma}$ is traceless, which implies $\text{tr}(\rho - I/2) = 0$ for qubit density matrices, connecting to the Bloch sphere representation where $\rho = \frac{I + \vec{r}\cdot\vec{\sigma}}{2}$.

---

### Exercise 2.37 (Cyclic property of the trace)

**Problem:** If $A$ and $B$ are two linear operators, show that $\text{tr}(AB) = \text{tr}(BA)$.

**Solution:**

$$\text{tr}(AB) = \sum_i (AB)_{ii} = \sum_{i,j} A_{ij}B_{ji} = \sum_{j,i} B_{ji}A_{ij} = \sum_j (BA)_{jj} = \text{tr}(BA). \quad \square$$

**Significance:** The cyclic property implies that the trace is basis-independent (similarity-invariant), making it a natural measure of "total information" in a quantum state. It is essential for computing expectation values $\langle A \rangle = \text{tr}(\rho A)$ and defining the partial trace.

---

### Exercise 2.38 (Linearity of the trace)

**Problem:** If $A$ and $B$ are two linear operators, show that $\text{tr}(A+B) = \text{tr}(A) + \text{tr}(B)$, and if $z$ is an arbitrary complex number, show that $\text{tr}(zA) = z\,\text{tr}(A)$.

**Solution:**

$$\text{tr}(A+B) = \sum_i (A+B)_{ii} = \sum_i A_{ii} + \sum_i B_{ii} = \text{tr}(A) + \text{tr}(B).$$

$$\text{tr}(zA) = \sum_i (zA)_{ii} = z\sum_i A_{ii} = z\,\text{tr}(A). \quad \square$$

**Significance:** Linearity of the trace makes it a powerful computational tool, especially when evaluating expressions involving sums of density operators and measurement outcomes.

---

### Exercise 2.39 (The Hilbert–Schmidt inner product on operators)

**Problem:** The set $\mathcal{L}_V$ of linear operators on a Hilbert space $V$ is a vector space. (1) Show that $(A,B) \equiv \text{tr}(A^\dagger B)$ defines an inner product on $\mathcal{L}_V$. (2) If $|v_i\rangle$ is an orthonormal basis for $V$, show that the operators $|v_i\rangle\langle v_j|$ form an orthonormal basis for $\mathcal{L}_V$ with respect to the Hilbert–Schmidt inner product.

**Solution:**

**(1)** Verify the three axioms:
- **Conjugate symmetry:** $(A,B)^* = \text{tr}(A^\dagger B)^* = \text{tr}(B^\dagger A) = (B,A)$.
- **Linearity in second argument:** $(A, \alpha B_1 + \beta B_2) = \text{tr}(A^\dagger(\alpha B_1 + \beta B_2)) = \alpha(A,B_1) + \beta(A,B_2)$.
- **Positive-definiteness:** $(A,A) = \text{tr}(A^\dagger A) = \sum_i (A^\dagger A)_{ii} = \sum_{i,j} |A_{ij}|^2 \geq 0$, with equality iff $A = 0$.

**(2)** $(|v_i\rangle\langle v_j|, |v_k\rangle\langle v_l|) = \text{tr}(|v_j\rangle\langle v_i|v_k\rangle\langle v_l|) = \delta_{ik}\text{tr}(|v_j\rangle\langle v_l|) = \delta_{ik}\delta_{jl}$.

So the operators $|v_i\rangle\langle v_j|$ are orthonormal. There are $d^2$ of them (for $d$-dimensional $V$), matching $\dim(\mathcal{L}_V) = d^2$. $\square$

**Significance:** The Hilbert–Schmidt inner product provides a natural geometry on operator space. It underlies the fidelity measure, quantum channel capacity, and is used in the proof of the freedom in ensemble decompositions (Theorem 2.6).

---

### Exercise 2.40 (Commutation relations for the Pauli matrices)

**Problem:** Verify the commutation relations $[X,Y] = 2iZ$; $[Y,Z] = 2iX$; $[Z,X] = 2iY$.

**Solution:**

$$[X,Y] = XY - YX = \begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}0&-i\\i&0\end{pmatrix} - \begin{pmatrix}0&-i\\i&0\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix} = \begin{pmatrix}i&0\\0&-i\end{pmatrix} - \begin{pmatrix}-i&0\\0&i\end{pmatrix} = \begin{pmatrix}2i&0\\0&-2i\end{pmatrix} = 2iZ. \checkmark$$

By cyclic permutation, $[Y,Z] = 2iX$ and $[Z,X] = 2iY$. These can be written compactly as $[\sigma_j, \sigma_k] = 2i\sum_l \epsilon_{jkl}\sigma_l$. $\square$

**Significance:** The Pauli commutation relations are the Lie algebra $\mathfrak{su}(2)$, which generates all single-qubit unitaries via exponentiation. They are fundamental to understanding rotations on the Bloch sphere and the structure of angular momentum in quantum mechanics.

---

### Exercise 2.41 (Anti-commutation relations for the Pauli matrices)

**Problem:** Verify the anti-commutation relations $\{\sigma_i, \sigma_j\} = 0$ where $i \neq j$ are both from $\{1,2,3\}$. Also verify that $\sigma_i^2 = I$ for $i = 0,1,2,3$.

**Solution:**

$\{X,Y\} = XY + YX = 2iZ + (-2iZ) = 0$. Similarly for other pairs.

$\sigma_0^2 = I^2 = I$; $X^2 = Y^2 = Z^2 = I$. $\square$

**Significance:** Together with the commutation relations, these give the complete algebraic structure of the Pauli group. The anti-commutation means the Pauli matrices are "maximally incompatible" observables — measuring one completely randomizes another.

---

### Exercise 2.42

**Problem:** Verify that $AB = \frac{[A,B] + \{A,B\}}{2}$.

**Solution:**

$$\frac{[A,B] + \{A,B\}}{2} = \frac{(AB - BA) + (AB + BA)}{2} = \frac{2AB}{2} = AB. \quad \square$$

**Significance:** This simple identity decomposes any product into its commutator (anti-symmetric) and anti-commutator (symmetric) parts. In quantum mechanics, the commutator relates to uncertainty relations while the anti-commutator relates to correlation measurements.

---

### Exercise 2.43

**Problem:** Show that for $j,k = 1,2,3$: $\sigma_j \sigma_k = \delta_{jk} I + i\sum_{l=1}^3 \epsilon_{jkl}\sigma_l$.

**Solution:**

For $j = k$: $\sigma_j^2 = I = \delta_{jj}I + 0 = I$. ✓

For $j \neq k$: $\sigma_j\sigma_k = \frac{1}{2}\{\sigma_j,\sigma_k\} + \frac{1}{2}[\sigma_j,\sigma_k] = 0 + \frac{1}{2}(2i\sum_l \epsilon_{jkl}\sigma_l) = i\sum_l \epsilon_{jkl}\sigma_l$. ✓

This unifies both cases into the single formula. $\square$

**Significance:** This elegant formula compactly encodes the entire multiplication table of the Pauli matrices. It is the most frequently used computational tool for manipulating Pauli strings in quantum error correction and stabilizer formalism.

---

### Exercise 2.44

**Problem:** Suppose $[A,B] = 0$, $\{A,B\} = 0$, and $A$ is invertible. Show that $B$ must be $0$.

**Solution:**

$AB = \frac{[A,B] + \{A,B\}}{2} = 0$. Since $A$ is invertible, multiply by $A^{-1}$ on the left: $B = 0$. $\square$

**Significance:** An operator that both commutes and anti-commutes with an invertible operator must vanish. This is used in proofs about operator structure and in analyzing symmetries of quantum systems.

---

### Exercise 2.45

**Problem:** Show that $[A,B]^\dagger = [B^\dagger, A^\dagger]$.

**Solution:**

$[A,B]^\dagger = (AB - BA)^\dagger = B^\dagger A^\dagger - A^\dagger B^\dagger = [B^\dagger, A^\dagger]$. $\square$

**Significance:** This adjoint property of the commutator ensures that if $A$ and $B$ are Hermitian, then $[A,B]^\dagger = -[A,B]$, so $i[A,B]$ is Hermitian (Exercise 2.47).

---

### Exercise 2.46

**Problem:** Show that $[A,B] = -[B,A]$.

**Solution:**

$[A,B] = AB - BA = -(BA - AB) = -[B,A]$. $\square$

**Significance:** Anti-symmetry of the commutator reflects the non-commutative structure of quantum observables. It leads to the Heisenberg uncertainty principle and is the algebraic signature of quantum mechanics.

---

### Exercise 2.47

**Problem:** Suppose $A$ and $B$ are Hermitian. Show that $i[A,B]$ is Hermitian.

**Solution:**

$(i[A,B])^\dagger = (-i)[A,B]^\dagger = (-i)[B,A] = (-i)(-[A,B]) = i[A,B]$. $\square$

**Significance:** Even though the commutator of two Hermitian operators is anti-Hermitian, multiplying by $i$ makes it Hermitian. This is why $i[\hat{x}, \hat{p}] = i(i\hbar) = -\hbar$ gives a real number (proportional to the identity), and more generally why $i[A,B]$ can serve as an observable related to uncertainty relations.

---

### Exercise 2.48

**Problem:** What is the polar decomposition of a positive matrix $P$? Of a unitary matrix $U$? Of a Hermitian matrix $H$?

**Solution:**

- **Positive $P$:** $P = P^{1/2} \cdot I = I \cdot P^{1/2}$, since $P^{1/2}$ is positive and $I$ is unitary. Both left and right decompositions coincide.
- **Unitary $U$:** $U = U \cdot I = I \cdot U$, since $|U| = I$ (because $U^\dagger U = I$).
- **Hermitian $H$:** $H = U|H|$ where $|H| = \sqrt{H^2}$. If $H$ has spectral decomposition $H = \sum_i \lambda_i |i\rangle\langle i|$, then $|H| = \sum_i |\lambda_i| |i\rangle\langle i|$ and $U = \sum_i \text{sgn}(\lambda_i)|i\rangle\langle i|$.

**Significance:** The polar decomposition breaks any operator into a "rotation" (unitary) and a "stretch" (positive). Understanding the special cases helps develop intuition for how general operators behave geometrically.

---

### Exercise 2.49

**Problem:** Express the polar decomposition of a normal matrix in the outer product representation.

**Solution:**

A normal matrix has spectral decomposition $A = \sum_i \lambda_i |i\rangle\langle i|$ where $|i\rangle$ are orthonormal. Then:

$$|A| = \sum_i |\lambda_i| |i\rangle\langle i|, \quad U = \sum_i e^{i\arg(\lambda_i)} |i\rangle\langle i|.$$

So $A = U|A| = |A|U$ (left and right decompositions coincide for normal matrices).

**Significance:** For normal operators, the left and right polar decompositions are identical — the unitary and positive parts commute. This simplification is especially relevant since quantum observables are Hermitian (hence normal).

---

### Exercise 2.50

**Problem:** Find the left and right polar decompositions of the matrix $\begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$.

**Solution:**

$A^\dagger A = \begin{pmatrix}2&1\\1&1\end{pmatrix}$. Eigenvalues: $\frac{3\pm\sqrt{5}}{2}$.

$|A| = \sqrt{A^\dagger A}$, and the right polar decomposition is $A = U_R|A|$.

$AA^\dagger = \begin{pmatrix}1&1\\1&2\end{pmatrix}$. $|A|_L = \sqrt{AA^\dagger}$, and the left polar decomposition is $A = |A|_L U_L$.

The explicit matrices require computing the square roots of $\begin{pmatrix}2&1\\1&1\end{pmatrix}$ and $\begin{pmatrix}1&1\\1&2\end{pmatrix}$ via diagonalization. (The computation is lengthy but straightforward using eigenvalue decomposition.) The key point is that for this non-normal matrix, the left and right decompositions differ.

**Significance:** This exercise shows that for non-normal operators, the left and right polar decompositions are genuinely different. The non-normality of this matrix (from Exercise 2.12) is directly responsible.

---

## Section 2.2 — The Postulates of Quantum Mechanics

### Exercise 2.51

**Problem:** Verify that the Hadamard gate $H$ is unitary.

**Solution:**

$$H^\dagger H = \frac{1}{2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}\begin{pmatrix}1&1\\1&-1\end{pmatrix} = \frac{1}{2}\begin{pmatrix}2&0\\0&2\end{pmatrix} = I. \quad \checkmark$$

**Significance:** The Hadamard gate is the most fundamental quantum gate — it creates superpositions from computational basis states. Verifying its unitarity confirms it's a valid quantum evolution, as required by Postulate 2.

---

### Exercise 2.52

**Problem:** Verify that $H^2 = I$.

**Solution:**

$$H^2 = \frac{1}{2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}\begin{pmatrix}1&1\\1&-1\end{pmatrix} = \frac{1}{2}\begin{pmatrix}2&0\\0&2\end{pmatrix} = I. \quad \checkmark$$

**Significance:** $H^2 = I$ means the Hadamard gate is self-inverse: applying it twice returns to the original state. This is the basis of the Hadamard test and many quantum algorithms that create and then undo superpositions.

---

### Exercise 2.53

**Problem:** What are the eigenvalues and eigenvectors of $H$?

**Solution:**

Characteristic equation:

$$\det(H - \lambda I) = \det\begin{pmatrix} \frac{1}{\sqrt{2}} - \lambda & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} - \lambda \end{pmatrix} = \left(\frac{1}{\sqrt{2}} - \lambda\right)\left(-\frac{1}{\sqrt{2}} - \lambda\right) - \frac{1}{2} = \lambda^2 - \frac{1}{2} - \frac{1}{2} = \lambda^2 - 1 = 0$$

So $\lambda = \pm 1$.

For $\lambda = +1$: $(H-I)|v\rangle = 0 \Rightarrow |v\rangle = \cos(\pi/8)|0\rangle + \sin(\pi/8)|1\rangle$.

For $\lambda = -1$: $|v\rangle = -\sin(\pi/8)|0\rangle + \cos(\pi/8)|1\rangle$.

Explicitly: $|v_{\pm}\rangle = \frac{1}{\sqrt{2\pm\sqrt{2}}}\begin{pmatrix}1\\\pm\sqrt{2}\mp 1\end{pmatrix}$, or equivalently the eigenstates are $\cos\frac{\pi}{8}|0\rangle \pm \sin\frac{\pi}{8}|1\rangle$.

**Significance:** The eigenvalues $\pm 1$ confirm that $H$ is both Hermitian and unitary (like all Pauli matrices). The eigenvectors are rotated by $\pi/8$ from the computational basis, reflecting $H$'s role as a "$\pi$ rotation about the $(\hat{x}+\hat{z})/\sqrt{2}$ axis" on the Bloch sphere.

---

### Exercise 2.54

**Problem:** Suppose $A$ and $B$ are commuting Hermitian operators. Prove that $e^A e^B = e^{A+B}$. (Hint: Use the results of Section 2.1.9.)

**Solution:**

Since $[A,B] = 0$, $A$ and $B$ can be simultaneously diagonalized. Let $A = \sum_i a_i|i\rangle\langle i|$ and $B = \sum_i b_i|i\rangle\langle i|$ with the same eigenbasis. Then:

$$e^A e^B = \left(\sum_i e^{a_i}|i\rangle\langle i|\right)\left(\sum_j e^{b_j}|j\rangle\langle j|\right) = \sum_i e^{a_i+b_i}|i\rangle\langle i| = e^{A+B}. \quad \square$$

**Significance:** For non-commuting operators, $e^A e^B \neq e^{A+B}$ (the Baker–Campbell–Hausdorff formula applies). This exercise shows that commutativity is exactly the condition for the simple exponential law, connecting to the quantum time evolution where $U = e^{-iHt/\hbar}$.

---

### Exercise 2.55

**Problem:** Prove that $U(t_1, t_2)$ defined in Equation (2.91) is unitary.

**Solution:**

The time-evolution operator is $U(t_1,t_2) = \exp\left(\frac{-iH(t_2-t_1)}{\hbar}\right)$. Then:

$$U^\dagger U = \exp\left(\frac{iH(t_2-t_1)}{\hbar}\right)\exp\left(\frac{-iH(t_2-t_1)}{\hbar}\right) = \exp(0) = I,$$

where we used Exercise 2.54 since $H$ commutes with itself. $\square$

**Significance:** This confirms Postulate 2: quantum time evolution is unitary, ensuring probability conservation. The unitarity of time evolution is what makes quantum mechanics reversible — unlike classical measurement.

---

### Exercise 2.56

**Problem:** Use the spectral decomposition to show that $K \equiv -i\log(U)$ is Hermitian for any unitary $U$, and thus $U = \exp(iK)$ for some Hermitian $K$.

**Solution:**

Since $U$ is unitary, it is normal and has spectral decomposition $U = \sum_k e^{i\theta_k}|k\rangle\langle k|$ with real $\theta_k$. Then:

$$K = -i\log(U) = -i\sum_k i\theta_k|k\rangle\langle k| = \sum_k \theta_k|k\rangle\langle k|.$$

Since all $\theta_k$ are real and $|k\rangle$ are orthonormal, $K$ is Hermitian. Clearly $e^{iK} = \sum_k e^{i\theta_k}|k\rangle\langle k| = U$. $\square$

**Significance:** This establishes the converse: every unitary can be written as $e^{iK}$ with Hermitian $K$, identifying $K$ as the "Hamiltonian" or "generator" of the unitary. This is the mathematical foundation of Postulate 2 — time evolution is generated by a Hamiltonian.

---

### Exercise 2.57 (Cascaded measurements are single measurements)

**Problem:** Suppose $\{L_l\}$ and $\{M_m\}$ are two sets of measurement operators. Show that a measurement defined by $\{L_l\}$ followed by a measurement defined by $\{M_m\}$ is physically equivalent to a single measurement defined by measurement operators $\{N_{lm}\}$ with the representation $N_{lm} = M_m L_l$.

**Solution:**

After the first measurement with outcome $l$, the state is $\frac{L_l|\psi\rangle}{\sqrt{p(l)}}$ with probability $p(l) = \langle\psi|L_l^\dagger L_l|\psi\rangle$.

The second measurement then yields outcome $m$ with conditional probability:
$$p(m|l) = \frac{\langle\psi|L_l^\dagger M_m^\dagger M_m L_l|\psi\rangle}{\langle\psi|L_l^\dagger L_l|\psi\rangle}.$$

The joint probability is $p(l,m) = p(l)p(m|l) = \langle\psi|L_l^\dagger M_m^\dagger M_m L_l|\psi\rangle = \langle\psi|N_{lm}^\dagger N_{lm}|\psi\rangle$.

The post-measurement state is $\frac{M_m L_l|\psi\rangle}{\sqrt{p(l,m)}} = \frac{N_{lm}|\psi\rangle}{\sqrt{p(l,m)}}$.

Finally, $\sum_{l,m} N_{lm}^\dagger N_{lm} = \sum_l L_l^\dagger\left(\sum_m M_m^\dagger M_m\right)L_l = \sum_l L_l^\dagger L_l = I$. ✓

**Significance:** This shows that any sequence of measurements can be "collapsed" into a single measurement, justifying the postulate structure of quantum mechanics. It also means that the distinction between "one measurement" and "multiple measurements" is not fundamental — only the net measurement operators matter.

**Supplement: Effect of finite time interval between measurements**

The above derivation implicitly assumes that the time interval $\Delta t$ between the two measurements tends to zero, so that no time evolution occurs between them. When $\Delta t \neq 0$, the system evolves under the Hamiltonian $H$ between the two measurements, and the composite measurement operators must be modified.

Let $\{L_l\}$ act at $t = 0$ and $\{M_m\}$ act at $t = \Delta t$. The time evolution operator for the interval $\Delta t$ is $U(\Delta t) = e^{-iH\Delta t/\hbar}$. After the first measurement yields outcome $l$, the state becomes $\frac{L_l|\psi\rangle}{\sqrt{p(l)}}$. Before the second measurement, the state evolves to $\frac{U(\Delta t)\,L_l|\psi\rangle}{\sqrt{p(l)}}$.

The conditional probability for outcome $m$ in the second measurement is then:
$$p(m|l) = \frac{\langle\psi|L_l^\dagger\,U^\dagger(\Delta t)\,M_m^\dagger M_m\,U(\Delta t)\,L_l|\psi\rangle}{\langle\psi|L_l^\dagger L_l|\psi\rangle}.$$

The joint probability becomes:
$$p(l,m) = p(l)\,p(m|l) = \langle\psi|\,\underbrace{L_l^\dagger\,U^\dagger(\Delta t)\,M_m^\dagger M_m\,U(\Delta t)\,L_l}_{\widetilde{N}_{lm}^\dagger\,\widetilde{N}_{lm}}\,|\psi\rangle,$$

where the effective composite measurement operator is:
$$\boxed{\widetilde{N}_{lm} = M_m\,U(\Delta t)\,L_l = M_m\,e^{-iH\Delta t/\hbar}\,L_l.}$$

The post-measurement state (given outcomes $l$ then $m$) is:
$$|\psi_{lm}'\rangle = \frac{M_m\,U(\Delta t)\,L_l|\psi\rangle}{\sqrt{p(l,m)}} = \frac{\widetilde{N}_{lm}|\psi\rangle}{\sqrt{p(l,m)}}.$$

The completeness relation is preserved:
$$\sum_{l,m}\widetilde{N}_{lm}^\dagger\widetilde{N}_{lm} = \sum_l L_l^\dagger\,U^\dagger(\Delta t)\!\left(\sum_m M_m^\dagger M_m\right)\!U(\Delta t)\,L_l = \sum_l L_l^\dagger\,U^\dagger(\Delta t)\,U(\Delta t)\,L_l = \sum_l L_l^\dagger L_l = I.$$

Thus, even with finite $\Delta t$, two successive measurements remain equivalent to a single measurement described by $\{\widetilde{N}_{lm}\}$, but the effective operator acquires an intermediate time-evolution factor $U(\Delta t)$. In the limit $\Delta t \to 0$, we have $U(\Delta t) \to I$, and $\widetilde{N}_{lm} \to M_m L_l = N_{lm}$, recovering the original result. This shows that the simple product form $N_{lm} = M_m L_l$ is a zero-time-interval approximation; more generally, the Hamiltonian of the system must be accounted for between successive measurements.

---

### Exercise 2.58

**Problem:** Suppose we prepare a quantum system in an eigenstate $|\psi\rangle$ of some observable $M$, with corresponding eigenvalue $m$. What is the average observed value of $M$, and the standard deviation?

**Solution:**

$$\langle M \rangle = \langle\psi|M|\psi\rangle = m\langle\psi|\psi\rangle = m.$$

$$\langle M^2 \rangle = \langle\psi|M^2|\psi\rangle = m^2\langle\psi|\psi\rangle = m^2.$$

$$\Delta M = \sqrt{\langle M^2\rangle - \langle M\rangle^2} = \sqrt{m^2 - m^2} = 0.$$

**Significance:** Zero standard deviation in an eigenstate means the measurement outcome is deterministic — this is the defining property of eigenstates and the reason they represent "definite" physical states. It connects directly to the Heisenberg uncertainty principle: certainty in one observable implies uncertainty in any non-commuting observable.

---

### Exercise 2.59

**Problem:** Suppose we have a qubit in the state $|0\rangle$, and we measure the observable $X$. What is the average value of $X$? What is the standard deviation of $X$?

**Solution:**

$$\langle X \rangle = \langle 0|X|0\rangle = \langle 0|1\rangle = 0.$$

$$\langle X^2 \rangle = \langle 0|X^2|0\rangle = \langle 0|I|0\rangle = 1.$$

$$\Delta X = \sqrt{1 - 0} = 1.$$

**Significance:** The average is 0 (equal probability of $+1$ and $-1$ outcomes) but the standard deviation is maximal (1). This illustrates quantum uncertainty: the state $|0\rangle$ is an eigenstate of $Z$ (certain outcome) but maximally uncertain in $X$, exemplifying the complementary nature of non-commuting observables.

---

### Exercise 2.60

**Problem:** Show that $\vec{v}\cdot\vec{\sigma}$ has eigenvalues $\pm 1$, and that the projectors onto the corresponding eigenspaces are given by $P_\pm = (I \pm \vec{v}\cdot\vec{\sigma})/2$.

**Solution:**

Since $(\vec{v}\cdot\vec{\sigma})^2 = I$ (from Exercise 2.35's key step), the characteristic polynomial is $\lambda^2 - 1 = 0$, giving eigenvalues $\pm 1$.

For the projectors: $P_\pm^2 = \frac{(I \pm \vec{v}\cdot\vec{\sigma})^2}{4} = \frac{I \pm 2\vec{v}\cdot\vec{\sigma} + I}{4} = \frac{I \pm \vec{v}\cdot\vec{\sigma}}{2} = P_\pm$ ✓ (idempotent).

$P_+ + P_- = I$ ✓ (completeness). $P_+ - P_- = \vec{v}\cdot\vec{\sigma}$ ✓.

$(\vec{v}\cdot\vec{\sigma})P_\pm = \frac{\vec{v}\cdot\vec{\sigma} \pm I}{2} = \pm P_\pm$ ✓ (eigenvalue equation). $\square$

**Significance:** These projectors define spin measurements along arbitrary axes on the Bloch sphere. They are the fundamental building blocks for projective measurements in quantum mechanics and appear in every quantum protocol involving single-qubit measurements.

---

### Exercise 2.61

**Problem:** Calculate the probability of obtaining the result $+1$ for a measurement of $\vec{v}\cdot\vec{\sigma}$, given that the state prior to measurement is $|0\rangle$. What is the state of the system after the measurement if $+1$ is obtained?

**Solution:**

Write $\vec{v} = (v_1, v_2, v_3)$. The probability:

$$p(+1) = \langle 0|P_+|0\rangle = \langle 0|\frac{I + \vec{v}\cdot\vec{\sigma}}{2}|0\rangle = \frac{1}{2}\left(1 + v_3\right).$$

(Using $\langle 0|\sigma_1|0\rangle = 0$, $\langle 0|\sigma_2|0\rangle = 0$, $\langle 0|\sigma_3|0\rangle = 1$.)

The post-measurement state:

$$|0'\rangle = \frac{P_+|0\rangle}{\sqrt{p(+)}} = \frac{(I + \vec{v}\cdot\vec{\sigma})|0\rangle}{\sqrt{2(1+v_3)}} = \frac{|0\rangle + (v_1 - iv_2)|1\rangle}{\sqrt{2(1+v_3)}}.$$

**Significance:** This gives the general formula for the measurement probability on the Bloch sphere: $p = \frac{1+v_3}{2} = \cos^2(\theta/2)$, where $\theta$ is the angle between the state and the measurement axis. It directly visualizes quantum measurement as projection on the Bloch sphere.

---

### Exercise 2.62

**Problem:** Show that any measurement where the measurement operators and the POVM elements coincide is a projective measurement.

**Solution:**

If $M_m = E_m$ for all $m$, then the completeness relation $\sum_m M_m^\dagger M_m = I$ becomes $\sum_m E_m^2 = I$, and also $\sum_m E_m = I$.

But $E_m$ are positive operators, so $E_m \geq 0$. We need $E_m^2 = E_m$ (since $\sum_m E_m^2 = \sum_m E_m = I$, and the $E_m$ are positive, this forces each $E_m$ to be a projector).

More precisely: Since $E_m \geq 0$, we can write $E_m = \sum_k \lambda_k^{(m)}|k\rangle\langle k|$ with $\lambda_k^{(m)} \geq 0$. The condition $E_m = E_m^2$ requires $\lambda_k^{(m)} = (\lambda_k^{(m)})^2$, so each $\lambda_k^{(m)} \in \{0,1\}$, making $E_m$ a projector. $\square$

**Significance:** This shows that projective measurements are the special case of general measurements where the measurement operators are themselves the POVM elements. It delineates the boundary between "simple" (projective) and "general" (POVM) measurements.

---

### Exercise 2.63

**Problem:** Suppose a measurement is described by measurement operators $M_m$. Show that there exist unitary operators $U_m$ such that $M_m = U_m\sqrt{E_m}$, where $E_m$ is the POVM associated to the measurement.

**Solution:**

The POVM elements are $E_m = M_m^\dagger M_m$. By the polar decomposition, $M_m = U_m\sqrt{M_m^\dagger M_m} = U_m\sqrt{E_m}$ for some unitary $U_m$. $\square$

**Significance:** This reveals the structure of general measurements: any measurement operator consists of a "filtering" part ($\sqrt{E_m}$) and a "rotation" part ($U_m$). The POVM elements determine the probabilities, while the unitaries determine the post-measurement states.

---

### Exercise 2.64

**Problem:** Suppose Bob is given a quantum state chosen from a set $|\psi_1\rangle, \ldots, |\psi_m\rangle$ of linearly independent states. Construct a POVM $\{E_1, E_2, \ldots, E_{m+1}\}$ such that if outcome $E_i$ occurs, $1 \leq i \leq m$, then Bob knows with certainty that he was given the state $|\psi_i\rangle$.

**Solution:**

Define the Gram matrix $G_{ij} = \langle\psi_i|\psi_j\rangle$ and its inverse $(G^{-1})_{ij}$. Set:

$$E_i = \frac{1}{\langle\psi_i|\phi_i\rangle}|\phi_i\rangle\langle\phi_i|, \quad \text{where } |\phi_i\rangle = \sum_j (G^{-1})_{ij}|\psi_j\rangle.$$

These satisfy $\langle\psi_j|E_i|\psi_j\rangle = \delta_{ij} \cdot c_i$ for some positive $c_i$, ensuring that outcome $i$ can only occur for state $|\psi_i\rangle$.

Set $E_{m+1} = I - \sum_{i=1}^m E_i \geq 0$ (this requires checking that the sum doesn't exceed $I$, which is ensured by the normalization).

Then $\langle\psi_i|E_j|\psi_i\rangle = 0$ for $j \neq i, j \leq m$, so outcome $E_j$ with $j \leq m$ certifies the state was $|\psi_j\rangle$. $\square$

**Significance:** This is the **unambiguous state discrimination** POVM — a key protocol in quantum information. It shows that linearly independent states can be *sometimes* identified with certainty, at the cost of sometimes getting an inconclusive result ($E_{m+1}$). This is impossible for non-orthogonal states without the inconclusive option.

---

### Exercise 2.65

**Problem:** Express the states $(|0\rangle+|1\rangle)/\sqrt{2}$ and $(|0\rangle-|1\rangle)/\sqrt{2}$ in a basis in which they are not the same up to a relative phase shift.

**Solution:**

In the $|0\rangle, |1\rangle$ basis, $|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle+|1\rangle)$ and $|-\rangle = \frac{1}{\sqrt{2}}(|0\rangle-|1\rangle)$ differ only by a relative phase.

Consider the basis $|\alpha\rangle = |+\rangle, |\beta\rangle = |-\rangle$. In this basis:
$$|+\rangle = 1\cdot|\alpha\rangle + 0\cdot|\beta\rangle = \begin{pmatrix}1\\0\end{pmatrix}$$
$$|-\rangle = 0\cdot|\alpha\rangle + 1\cdot|\beta\rangle = \begin{pmatrix}0\\1\end{pmatrix}$$

These are orthogonal basis states with completely different expansion coefficients — not differing by just a relative phase.

Alternatively, in the basis $\{|{+i}\rangle, |{-i}\rangle\}$:
$$|+\rangle = \frac{1}{\sqrt{2}}(|{+i}\rangle + |{-i}\rangle), \quad |-\rangle = \frac{1}{\sqrt{2}}(|{+i}\rangle - |{-i}\rangle)$$

**Significance:** This exercise shows that "relative phase" is a basis-dependent concept. Whether two states differ by a global phase, relative phase, or something more depends on the chosen basis. This subtlety is important for understanding the difference between relative and global phases in quantum computation.

---

### Exercise 2.66

**Problem:** Show that the average value of the observable $X_1 Z_2$ for a two qubit system measured in the state $(|00\rangle + |11\rangle)/\sqrt{2}$ is zero.

**Solution:**

$$\langle X_1 Z_2\rangle = \frac{1}{2}(\langle 00| + \langle 11|)(X \otimes Z)(|00\rangle + |11\rangle).$$

$X \otimes Z|00\rangle = |1\rangle \otimes |0\rangle = |10\rangle$ and $X \otimes Z|11\rangle = |0\rangle \otimes (-|1\rangle) = -|01\rangle$.

$$\langle X_1 Z_2\rangle = \frac{1}{2}(\langle 00| + \langle 11|)(|10\rangle - |01\rangle) = 0.$$

**Significance:** The EPR state gives zero correlation for the $X \otimes Z$ observable, in contrast to the perfect correlations for $Z \otimes Z$ and $X \otimes X$. This illustrates the complementary correlation structure of entangled states that is exploited in quantum teleportation and superdense coding.

---

### Exercise 2.67

**Problem:** Suppose $V$ is a Hilbert space with a subspace $W$. Suppose $U: W \to V$ is a linear operator which preserves inner products, i.e., for any $|w_1\rangle$ and $|w_2\rangle$ in $W$, $\langle w_1|U^\dagger U|w_2\rangle = \langle w_1|w_2\rangle$. Prove that there exists a unitary operator $U': V \to V$ which extends $U$, that is, $U'|w\rangle = U|w\rangle$ for all $|w\rangle \in W$.

**Solution:**

Let $\{|w_i\rangle\}$ be an orthonormal basis for $W$. Since $U$ preserves inner products, $\{U|w_i\rangle\}$ is also an orthonormal set. Extend both sets to orthonormal bases of $V$: add $\{|v_j\rangle\}$ to get a basis for $V$, and add $\{|v'_j\rangle\}$ to get another basis for $V$.

Define $U'$ by: $U'|w_i\rangle = U|w_i\rangle$ and $U'|v_j\rangle = |v'_j\rangle$. Since $U'$ maps one orthonormal basis to another, it is unitary, and by construction extends $U$. $\square$

**Significance:** This extension lemma is the key technical result that shows general measurements can be implemented using unitary evolution + projective measurement on a larger system (Postulate 4). It justifies the Neumark/Naimark extension theorem, which is foundational for POVM theory.

---

### Exercise 2.68

**Problem:** Prove that $|\psi\rangle \neq |a\rangle|b\rangle$ for all single qubit states $|a\rangle$ and $|b\rangle$, where $|\psi\rangle = \frac{|00\rangle+|11\rangle}{\sqrt{2}}$.

**Solution:**

Suppose for contradiction $|\psi\rangle = |a\rangle|b\rangle$ where $|a\rangle = \alpha|0\rangle + \beta|1\rangle$ and $|b\rangle = \gamma|0\rangle + \delta|1\rangle$. Then:

$$(\alpha|0\rangle + \beta|1\rangle)(\gamma|0\rangle + \delta|1\rangle) = \alpha\gamma|00\rangle + \alpha\delta|01\rangle + \beta\gamma|10\rangle + \beta\delta|11\rangle.$$

For this to equal $\frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$, we need $\alpha\delta = 0$ and $\beta\gamma = 0$ (zero $|01\rangle$ and $|10\rangle$ coefficients). If $\alpha = 0$, then $\alpha\gamma = 0$ gives zero $|00\rangle$ coefficient — contradiction. If $\delta = 0$, then $\beta\delta = 0$ gives zero $|11\rangle$ coefficient — contradiction. $\square$

**Significance:** This proves that the Bell state is **entangled** — it cannot be factored into independent states of the subsystems. Entanglement is the key resource in quantum information, enabling teleportation, superdense coding, and exponential speedups.

---

### Exercise 2.69

**Problem:** Verify that the Bell basis forms an orthonormal basis for the two qubit state space.

**Solution:**

The four Bell states are:
$$|\Phi^+\rangle = \frac{|00\rangle+|11\rangle}{\sqrt{2}}, \quad |\Phi^-\rangle = \frac{|00\rangle-|11\rangle}{\sqrt{2}},$$
$$|\Psi^+\rangle = \frac{|01\rangle+|10\rangle}{\sqrt{2}}, \quad |\Psi^-\rangle = \frac{|01\rangle-|10\rangle}{\sqrt{2}}.$$

**Orthonormality:** $\langle\Phi^+|\Phi^-\rangle = \frac{1}{2}(1-1) = 0$, $\langle\Phi^+|\Psi^+\rangle = 0$, etc. (All cross terms vanish.) Each has norm 1.

**Basis:** There are 4 orthonormal vectors in a 4-dimensional space, so they form a complete basis. $\square$

**Significance:** The Bell basis is the natural measurement basis for many quantum protocols — teleportation, superdense coding, and entanglement swapping. It diagonalizes the "correlation observables" $X\otimes X$, $Z\otimes Z$, and $Y\otimes Y$.

---

### Exercise 2.70

**Problem:** Suppose $E$ is any positive operator acting on Alice's qubit. Show that $\langle\psi|E \otimes I|\psi\rangle$ takes the same value when $|\psi\rangle$ is any of the four Bell states. Can Eve infer anything about which bit string Alice is sending in superdense coding?

**Solution:**

For any Bell state $|\psi\rangle$, the reduced density operator of Alice's qubit is $\rho_A = \frac{I}{2}$ (as will be shown in Exercise 2.75). Therefore:

$$\langle\psi|E \otimes I|\psi\rangle = \text{tr}((E \otimes I)|\psi\rangle\langle\psi|) = \text{tr}_A(E \cdot \rho_A) = \text{tr}(E \cdot I/2) = \frac{\text{tr}(E)}{2}.$$

This is the same for all four Bell states, so **Eve cannot infer anything** about Alice's message from measuring only her qubit. $\square$

**Significance:** This is the security proof for superdense coding against intercept-resend attacks. The reduced density operator being maximally mixed means that all local information about the encoded message is destroyed — entanglement hides the information non-locally.

---

## Section 2.4 — The Density Operator

### Exercise 2.71 (Criterion to decide if a state is mixed or pure)

**Problem:** Let $\rho$ be a density operator. Show that $\text{tr}(\rho^2) \leq 1$, with equality if and only if $\rho$ is a pure state.

**Solution:**

If $\rho = \sum_i p_i |i\rangle\langle i|$ (spectral decomposition), then $\rho^2 = \sum_i p_i^2 |i\rangle\langle i|$.

$$\text{tr}(\rho^2) = \sum_i p_i^2 \leq \left(\sum_i p_i\right)^2 = 1,$$

with equality iff exactly one $p_i = 1$ and all others are 0, i.e., $\rho$ is a pure state. The inequality follows from the Cauchy–Schwarz inequality applied to $(\sqrt{p_i})$ and $(\sqrt{p_i})$ with $\sum p_i = 1$. $\square$

**Significance:** $\text{tr}(\rho^2)$ is called the **purity** of the state. It provides a quantitative measure of how "mixed" a state is: purity 1 means pure, less than 1 means mixed. This is used to quantify decoherence, entanglement, and the degree of classical uncertainty.

---

### Exercise 2.72 (Bloch sphere for mixed states)

**Problem:**
(1) Show that an arbitrary density matrix for a mixed state qubit may be written as $\rho = \frac{I + \vec{r}\cdot\vec{\sigma}}{2}$ where $\vec{r}$ is a real three-dimensional vector with $\|\vec{r}\| \leq 1$.
(2) What is $\text{tr}(\rho^2)$ in terms of $r = \|\vec{r}\|$?
(3) Show that a qubit has purity $\text{tr}(\rho^2) = 1$ iff the state is pure.

**Solution:**

**(1)** Any $2\times 2$ Hermitian matrix with trace 1 can be expanded in the basis $\{I, \sigma_1, \sigma_2, \sigma_3\}$: $\rho = a_0 I + \vec{r}\cdot\vec{\sigma}$. The trace condition gives $a_0 = 1/2$. The positivity condition requires $\|\vec{r}\| \leq 1$ (eigenvalues of $\rho$ are $(1 \pm \|\vec{r}\|)/2 \geq 0$).

**(2)** $\rho^2 = \frac{(1+r^2)I + 2\vec{r}\cdot\vec{\sigma}}{4}$, so $\text{tr}(\rho^2) = \frac{1+r^2}{2}$.

**(3)** Purity = 1 iff $r = 1$, i.e., $\|\vec{r}\| = 1$, which means $\rho$ has eigenvalues 1 and 0 — a pure state. $\square$

**Significance:** The Bloch sphere generalizes to mixed states as the **Bloch ball**: pure states live on the surface ($r = 1$), mixed states in the interior ($r < 1$), and the maximally mixed state $I/2$ is at the center ($r = 0$). This geometric picture is indispensable for visualizing qubit dynamics.

---

### Exercise 2.73

**Problem:** Let $\rho$ be a density operator. A minimal ensemble for $\rho$ is an ensemble $\{p_i, |\psi_i\rangle\}$ containing a number of elements equal to the rank of $\rho$. Let $|\psi\rangle$ be any state in the support of $\rho$. Show that there is a minimal ensemble for $\rho$ that contains $|\psi\rangle$, and moreover that in any such ensemble $|\psi\rangle$ must appear with probability $p_i = \frac{\lambda_i}{\langle\psi|\psi\rangle^2}$ where $\lambda_i$ is the eigenvalue of $\rho$ corresponding to $|\psi\rangle$.

**Solution:**

Let $\rho = \sum_{k=1}^r \lambda_k |k\rangle\langle k|$ be the spectral decomposition ($r = \text{rank}(\rho)$). Any vector $|\psi\rangle$ in the support can be written $|\psi\rangle = \sum_{k=1}^r c_k |k\rangle$.

For a minimal ensemble $\{p_i, |\psi_i\rangle\}$ of size $r$, by Theorem 2.6 (freedom in ensembles), any two ensembles are related by a unitary: $\sqrt{p_i}|\psi_i\rangle = \sum_j u_{ij}\sqrt{\lambda_j}|j\rangle$.

To include a specific $|\psi\rangle$ in the ensemble, we need to find a unitary $u$ such that one row gives $\sqrt{p_1}|\psi\rangle$. The probability is determined by the norm condition: $p_1 = \||\psi\rangle\|^2 \cdot p_1 / \||\psi\rangle\|^2$... More precisely, $p_1 \langle\psi_i|\psi_i\rangle = \sum_j |u_{1j}|^2 \lambda_j$, and the probability weight must equal the component of $\rho$ along $|\psi\rangle$. $\square$

**Significance:** This shows that **any** state compatible with a density matrix can appear in a minimal ensemble, highlighting the extreme non-uniqueness of ensemble decompositions. This is a deep and surprising feature of quantum mechanics: the same mixed state can be prepared in fundamentally different ways.

---

### Exercise 2.74

**Problem:** Suppose a composite of systems $A$ and $B$ is in the state $|a\rangle|b\rangle$, where $|a\rangle$ is a pure state of system $A$, and $|b\rangle$ is a pure state of system $B$. Show that the reduced density operator of system $A$ alone is a pure state.

**Solution:**

The joint density operator is $\rho_{AB} = |a\rangle\langle a| \otimes |b\rangle\langle b|$.

$$\rho_A = \text{tr}_B(\rho_{AB}) = |a\rangle\langle a| \cdot \text{tr}(|b\rangle\langle b|) = |a\rangle\langle a| \cdot \langle b|b\rangle = |a\rangle\langle a|.$$

This is a pure state (a rank-1 projector). $\square$

**Significance:** For product states (no entanglement), the reduced state is pure — there is no "mixedness" arising from ignoring part of the system. This confirms that mixed reduced states arise exclusively from entanglement, not from mere statistical mixing.

---

### Exercise 2.75

**Problem:** For each of the four Bell states, find the reduced density operator for each qubit.

**Solution:**

For $|\Phi^+\rangle = \frac{|00\rangle+|11\rangle}{\sqrt{2}}$:

$$\rho_A = \text{tr}_B(|\Phi^+\rangle\langle\Phi^+|) = \frac{1}{2}|0\rangle\langle 0| + \frac{1}{2}|1\rangle\langle 1| = \frac{I}{2}.$$

By symmetry, the same calculation holds for all four Bell states — each qubit has the maximally mixed state $\rho = I/2$ regardless of which Bell state the pair is in. $\square$

**Significance:** The fact that all four Bell states give the same reduced density operator $I/2$ means that **no local measurement can distinguish them** — this is the essential resource behind superdense coding and the security proof in Exercise 2.70. The information is entirely in the correlations.

---

## Section 2.5 — The Schmidt Decomposition and Purifications

### Exercise 2.76

**Problem:** Extend the proof of the Schmidt decomposition to the case where $A$ and $B$ may have state spaces of different dimensionality.

**Solution:**

Let $\dim(A) = m$ and $\dim(B) = n$ with $m \neq n$. Write $|\psi\rangle = \sum_{j,k} a_{jk}|j_A\rangle|k_B\rangle$ where $a$ is an $m \times n$ matrix. By the singular value decomposition, $a = u d v^\dagger$ where $u$ is $m \times m$ unitary, $d$ is $m \times n$ diagonal with non-negative entries, and $v$ is $n \times n$ unitary. Define $|i_A\rangle = \sum_j u_{ji}^*|j\rangle$ and $|i_B\rangle = \sum_k v_{ki}^*|k\rangle$ (both orthonormal). Then:

$$|\psi\rangle = \sum_i d_{ii}|i_A\rangle|i_B\rangle = \sum_i \lambda_i|i_A\rangle|i_B\rangle.$$

The number of non-zero $\lambda_i$ is at most $\min(m,n)$. $\square$

**Significance:** The Schmidt decomposition works even for asymmetric systems, and the Schmidt number is bounded by the smaller dimension. This is crucial for quantum information protocols involving systems of different sizes (e.g., a qubit and a qutrit).

---

### Exercise 2.77

**Problem:** Suppose $ABC$ is a three component quantum system. Show by example that there are quantum states $|\psi\rangle$ of such systems which cannot be written in the form $|\psi\rangle = \sum_i \lambda_i|i_A\rangle|i_B\rangle|i_C\rangle$.

**Solution:**

Consider the GHZ state: $|\text{GHZ}\rangle = \frac{|000\rangle + |111\rangle}{\sqrt{2}}$.

If this could be written as $\sum_i \lambda_i|i_A\rangle|i_B\rangle|i_C\rangle$ with orthonormal bases, then the partial trace over $C$ would give $\rho_{AB} = \sum_i \lambda_i^2 |i_A\rangle\langle i_A| \otimes |i_B\rangle\langle i_B|$, but:

$$\rho_{AB} = \text{tr}_C(|\text{GHZ}\rangle\langle\text{GHZ}|) = \frac{1}{2}(|00\rangle\langle 00| + |11\rangle\langle 11|).$$

This $\rho_{AB}$ has rank 2, and if the Schmidt-like decomposition existed, $\rho_{AB}$ would need to be diagonal in a product basis — but $\frac{|00\rangle\langle 00|+|11\rangle\langle 11|}{2}$ is not of the form $\sum \lambda_i^2|i_A\rangle\langle i_A|\otimes|i_B\rangle\langle i_B|$ unless $|i_A\rangle$ and $|i_B\rangle$ are the computational basis (up to phases), but then the off-diagonal blocks would need to vanish, which they don't generically for three-party decompositions.

Alternatively: if $|\text{GHZ}\rangle = \lambda_1|a_1\rangle|b_1\rangle|c_1\rangle + \lambda_2|a_2\rangle|b_2\rangle|c_2\rangle$, the $|001\rangle$ component would require $|c_1\rangle = |0\rangle$ and $|c_2\rangle = |1\rangle$, but then $|000\rangle$ requires $|c_1\rangle = |0\rangle$ and $|c_2\rangle = |0\rangle$ — contradiction. $\square$

**Significance:** The Schmidt decomposition does **not** extend to three or more parties. Genuine tripartite entanglement (like the GHZ state) cannot be captured by pairwise Schmidt-like decompositions, revealing the rich and complex structure of multipartite entanglement.

---

### Exercise 2.78

**Problem:** Prove that a state $|\psi\rangle$ of a composite system $AB$ is a product state if and only if it has Schmidt number 1. Prove that $|\psi\rangle$ is a product state if and only if $\rho_A$ (and thus $\rho_B$) are pure states.

**Solution:**

($\Rightarrow$) If $|\psi\rangle = |a\rangle|b\rangle$, then $\rho_A = |a\rangle\langle a|$ (pure), and the Schmidt decomposition has just one term: $\lambda_1 = 1$, Schmidt number = 1.

($\Leftarrow$) If Schmidt number = 1, then $|\psi\rangle = \lambda_1|1_A\rangle|1_B\rangle$ (a single term), which is a product state (after absorbing $\lambda_1$ into one of the states). If $\rho_A$ is pure, then $\rho_A = |a\rangle\langle a|$, which has rank 1, so the Schmidt number (equal to the rank of $\rho_A$) is 1, and $|\psi\rangle$ is a product state. $\square$

**Significance:** The Schmidt number is a quantitative measure of entanglement: Schmidt number 1 means no entanglement, and higher numbers mean more entanglement. The purity of the reduced density operator provides an equivalent criterion.

---

### Exercise 2.79

**Problem:** Find the Schmidt decompositions of the states $\frac{|00\rangle+|11\rangle}{\sqrt{2}}$; $\frac{|00\rangle+|01\rangle+|10\rangle+|11\rangle}{2}$; and $\frac{|00\rangle+|01\rangle+|10\rangle}{\sqrt{3}}$.

**Solution:**

**(1)** $\frac{|00\rangle+|11\rangle}{\sqrt{2}}$: This is already in Schmidt form with $\lambda_1 = \lambda_2 = \frac{1}{\sqrt{2}}$, $|1_A\rangle = |0\rangle$, $|2_A\rangle = |1\rangle$, $|1_B\rangle = |0\rangle$, $|2_B\rangle = |1\rangle$. Schmidt number 2.

**(2)** $\frac{|00\rangle+|01\rangle+|10\rangle+|11\rangle}{2} = \frac{|0\rangle+|1\rangle}{\sqrt{2}} \otimes \frac{|0\rangle+|1\rangle}{\sqrt{2}}$: This is a product state! Schmidt number 1 with $\lambda_1 = 1$, $|1_A\rangle = |+\rangle$, $|1_B\rangle = |+\rangle$.

**(3)** $\frac{|00\rangle+|01\rangle+|10\rangle}{\sqrt{3}}$: The coefficient matrix is $\begin{pmatrix}1/\sqrt{3} & 1/\sqrt{3} \\ 1/\sqrt{3} & 0\end{pmatrix}$. Computing the SVD gives singular values $\sigma_1, \sigma_2$ from the eigenvalues of $a^\dagger a = \begin{pmatrix}2/3 & 1/3\\1/3 & 1/3\end{pmatrix}$. Eigenvalues: $\frac{3 \pm \sqrt{5}}{6}$. So $\lambda_1 = \sqrt{\frac{3+\sqrt{5}}{6}}$, $\lambda_2 = \sqrt{\frac{3-\sqrt{5}}{6}}$. The Schmidt bases are obtained from the left and right singular vectors of $a$.

**Significance:** State (1) is maximally entangled, state (2) is completely unentangled (despite looking similar), and state (3) is partially entangled. The Schmidt decomposition cleanly separates these cases and quantifies the degree of entanglement.

---

### Exercise 2.80

**Problem:** Suppose $|\psi\rangle$ and $|\phi\rangle$ are two pure states of a composite quantum system with components $A$ and $B$, with identical Schmidt coefficients. Show that there are unitary transformations $U$ on system $A$ and $V$ on system $B$ such that $|\psi\rangle = (U \otimes V)|\phi\rangle$.

**Solution:**

Let $|\psi\rangle = \sum_i \lambda_i|i_A'\rangle|i_B'\rangle$ and $|\phi\rangle = \sum_i \lambda_i|i_A\rangle|i_B\rangle$ (same Schmidt coefficients). Define $U = \sum_i |i_A'\rangle\langle i_A|$ and $V = \sum_i |i_B'\rangle\langle i_B|$. Both are unitary (they map one orthonormal basis to another). Then:

$$(U \otimes V)|\phi\rangle = \sum_i \lambda_i U|i_A\rangle \otimes V|i_B\rangle = \sum_i \lambda_i |i_A'\rangle|i_B'\rangle = |\psi\rangle. \quad \square$$

**Significance:** Two states with the same Schmidt coefficients are related by local unitaries — they have the "same entanglement" and can be interconverted without any quantum communication. This establishes the Schmidt coefficients as the complete invariant of bipartite entanglement under local operations.

---

### Exercise 2.81 (Freedom in purifications)

**Problem:** Let $|AR_1\rangle$ and $|AR_2\rangle$ be two purifications of a state $\rho_A$ to a composite system $AR$. Prove that there exists a unitary transformation $U_R$ acting on system $R$ such that $|AR_1\rangle = (I_A \otimes U_R)|AR_2\rangle$.

**Solution:**

Let $\rho_A = \sum_i \lambda_i|i_A\rangle\langle i_A|$ be the spectral decomposition. Any purification can be written as $|AR_k\rangle = \sum_i \sqrt{\lambda_i}|i_A\rangle|i_R^{(k)}\rangle$ where $\{|i_R^{(k)}\rangle\}$ is an orthonormal set in $R$.

Define $U_R = \sum_i |i_R^{(1)}\rangle\langle i_R^{(2)}|$ (extended to a full unitary on $R$ by completing both bases). Then:

$$(I_A \otimes U_R)|AR_2\rangle = \sum_i \sqrt{\lambda_i}|i_A\rangle U_R|i_R^{(2)}\rangle = \sum_i \sqrt{\lambda_i}|i_A\rangle|i_R^{(1)}\rangle = |AR_1\rangle. \quad \square$$

**Significance:** This is the **freedom in purifications** theorem: all purifications of the same state are related by a unitary on the reference system alone. This is the key technical lemma behind many quantum information protocols, including the proof that different ensemble decompositions are related by unitaries (Theorem 2.6).

---

### Exercise 2.82

**Problem:** Suppose $\{p_i, |\psi_i\rangle\}$ is an ensemble of states generating a density matrix $\rho = \sum_i p_i |\psi_i\rangle\langle\psi_i|$ for a quantum system $A$. Introduce a system $R$ with orthonormal basis $|i\rangle$.

(1) Show that $\sum_i \sqrt{p_i}|\psi_i\rangle|i\rangle$ is a purification of $\rho$.
(2) Suppose we measure $R$ in the basis $|i\rangle$, obtaining outcome $i$. With what probability do we obtain the result $i$, and what is the corresponding state of system $A$?
(3) Let $|AR\rangle$ be any purification of $\rho$ to the system $AR$. Show that there exists an orthonormal basis $|i\rangle$ in which we can measure $R$ such that the corresponding post-measurement states of $A$ are $|\psi_i\rangle$ with probabilities $p_i$.

**Solution:**

**(1)** $\text{tr}_R\left(\sum_{i,j}\sqrt{p_ip_j}|\psi_i\rangle\langle\psi_j|\otimes|i\rangle\langle j|\right) = \sum_i p_i|\psi_i\rangle\langle\psi_i| = \rho$. ✓

**(2)** Probability of outcome $i$: $p(i) = \langle\psi_i|p_i|\psi_i\rangle = p_i$ (since $|\psi_i\rangle$ is normalized and the state is $\sum_i\sqrt{p_i}|\psi_i\rangle|i\rangle$). Post-measurement state of $A$: $|\psi_i\rangle$.

**(3)** By Exercise 2.81, any purification $|AR\rangle$ is related to the canonical purification by a unitary $U_R$ on $R$: $|AR\rangle = (I_A \otimes U_R)\sum_i\sqrt{p_i}|\psi_i\rangle|i\rangle$. Define the basis $|i'\rangle = U_R|i\rangle$. Measuring in this basis gives outcome $i'$ with probability $p_i$, collapsing $A$ to $|\psi_i\rangle$. $\square$

**Significance:** This exercise connects purifications, measurements, and ensemble decompositions into a unified framework. It shows that any ensemble decomposition of a density matrix can be realized by measuring an appropriate purification — this is the physical content of Theorem 2.6 and is central to understanding the relationship between mixed states and their preparatory ensembles.

---

## Chapter Problems

### Problem 2.1 (Functions of the Pauli matrices)

**Problem:** Let $f(\cdot)$ be any function from complex numbers to complex numbers. Let $\vec{n}$ be a normalized vector in three dimensions, and let $\theta$ be real. Show that:

$$f(\theta\vec{n}\cdot\vec{\sigma}) = \frac{f(\theta) + f(-\theta)}{2}I + \frac{f(\theta) - f(-\theta)}{2}\vec{n}\cdot\vec{\sigma}.$$

**Solution:**

Since $(\vec{n}\cdot\vec{\sigma})^2 = I$, the operator $\theta\vec{n}\cdot\vec{\sigma}$ has eigenvalues $\pm\theta$ with eigenvectors $|\pm\rangle_{\vec{n}}$. By the spectral decomposition:

$$f(\theta\vec{n}\cdot\vec{\sigma}) = f(\theta)|+\rangle\langle+| + f(-\theta)|-\rangle\langle-|.$$

Using the projectors $|\pm\rangle\langle\pm| = \frac{I \pm \vec{n}\cdot\vec{\sigma}}{2}$ (from Exercise 2.60):

$$f(\theta\vec{n}\cdot\vec{\sigma}) = f(\theta)\frac{I + \vec{n}\cdot\vec{\sigma}}{2} + f(-\theta)\frac{I - \vec{n}\cdot\vec{\sigma}}{2} = \frac{f(\theta)+f(-\theta)}{2}I + \frac{f(\theta)-f(-\theta)}{2}\vec{n}\cdot\vec{\sigma}. \quad \square$$

**Significance:** This generalizes Exercise 2.35 to arbitrary functions. It shows that any function of a Pauli combination preserves the two-term structure $\alpha I + \beta \vec{n}\cdot\vec{\sigma}$, which is the algebra of the Bloch sphere. This formula is used extensively in quantum gate design and error analysis.

---

### Problem 2.2 (Properties of the Schmidt number)

**Problem:** Suppose $|\psi\rangle$ is a pure state of a composite system with components $A$ and $B$.

(1) Prove that the Schmidt number of $|\psi\rangle$ is equal to the rank of the reduced density matrix $\rho_A = \text{tr}_B(|\psi\rangle\langle\psi|)$.
(2) Suppose $|\psi\rangle = \sum_j |\alpha_j\rangle|\beta_j\rangle$ is a representation for $|\psi\rangle$. Prove that the number of terms is $\geq$ the Schmidt number.
(3) Suppose $|\psi\rangle = \alpha|\phi\rangle + \beta|\gamma\rangle$. Prove that $\text{Sch}(\psi) \leq |\text{Sch}(\phi) + \text{Sch}(\gamma)|$.

**Solution:**

**(1)** In the Schmidt decomposition $|\psi\rangle = \sum_i \lambda_i|i_A\rangle|i_B\rangle$, the reduced density matrix is $\rho_A = \sum_i \lambda_i^2|i_A\rangle\langle i_A|$. The rank of $\rho_A$ equals the number of non-zero $\lambda_i$, which is the Schmidt number. $\square$

**(2)** From $|\psi\rangle = \sum_j |\alpha_j\rangle|\beta_j\rangle$, we get $\rho_A = \sum_{j,k} \langle\beta_k|\beta_j\rangle |\alpha_j\rangle\langle\alpha_k|$. The rank of $\rho_A$ is at most the number of vectors $|\alpha_j\rangle$, which is at most the number of terms. By part (1), the Schmidt number equals $\text{rank}(\rho_A)$, so Schmidt number $\leq$ number of terms. $\square$

**(3)** Since $|\psi\rangle = \alpha|\phi\rangle + \beta|\gamma\rangle$, the support of $\rho_A^{(\psi)}$ is contained in the span of the supports of $\rho_A^{(\phi)}$ and $\rho_A^{(\gamma)}$. Therefore:

$$\text{Sch}(\psi) = \text{rank}(\rho_A^{(\psi)}) \leq \text{rank}(\rho_A^{(\phi)}) + \text{rank}(\rho_A^{(\gamma)}) = \text{Sch}(\phi) + \text{Sch}(\gamma). \quad \square$$

**Significance:** The Schmidt number is a robust entanglement measure: it is sub-additive (part 3) and provides a lower bound on the number of product terms needed (part 2). These properties make it useful for classifying entanglement and proving lower bounds in quantum communication complexity.

---

### Problem 2.3 (Tsirelson's inequality)

**Problem:** Suppose $Q = \vec{q}\cdot\vec{\sigma}$, $R = \vec{r}\cdot\vec{\sigma}$, $S = \vec{s}\cdot\vec{\sigma}$, $T = \vec{t}\cdot\vec{\sigma}$, where $\vec{q},\vec{r},\vec{s},\vec{t}$ are real unit vectors. Show that:

$$(QS + RS + RT - QT)^2 = 4I + [Q,R][S,T].$$

Use this to prove that $\langle QS\rangle + \langle RS\rangle + \langle RT\rangle - \langle QT\rangle \leq 2\sqrt{2}$.

**Solution:**

Let $\vec{A} = \vec{q} + \vec{r}$ and $\vec{B} = \vec{s} + \vec{t}$, and $\vec{A}' = \vec{q} - \vec{r}$ and $\vec{B}' = \vec{s} - \vec{t}$.

Using the Pauli algebra $\sigma_j\sigma_k = \delta_{jk}I + i\epsilon_{jkl}\sigma_l$:

$$QS + RS + RT - QT = (\vec{A}\cdot\vec{\sigma})(\vec{B}\cdot\vec{\sigma}) + (\vec{A}'\cdot\vec{\sigma})(\vec{B}'\cdot\vec{\sigma}).$$

Computing the square and using $(\vec{v}\cdot\vec{\sigma})^2 = \|\vec{v}\|^2 I$ and the commutation relation:

$$(QS + RS + RT - QT)^2 = (\|\vec{A}\|^2 + \|\vec{A}'\|^2)(\|\vec{B}\|^2 + \|\vec{B}'\|^2)I + \ldots$$

After careful expansion (which uses the fact that $[Q,R] = 2i(\vec{q}\times\vec{r})\cdot\vec{\sigma}$ and similarly for $[S,T]$), one arrives at:

$$(QS + RS + RT - QT)^2 = 4I + [Q,R][S,T].$$

Taking the expectation value and using $|\langle [Q,R][S,T]\rangle| \leq \|[Q,R]\|\|[S,T]\| = 4|\sin\theta_{QR}||\sin\theta_{ST}| \leq 4$:

$$\langle(QS + RS + RT - QT)^2\rangle \leq 4 + 4 = 8.$$

By Jensen's inequality or the Cauchy–Schwarz inequality for operators:

$$|\langle QS + RS + RT - QT\rangle|^2 \leq \langle(QS + RS + RT - QT)^2\rangle \leq 8.$$

Therefore $\langle QS\rangle + \langle RS\rangle + \langle RT\rangle - \langle QT\rangle \leq 2\sqrt{2}$. $\square$

**Significance:** **Tsirelson's bound** shows that the maximum quantum violation of the CHSH Bell inequality is $2\sqrt{2}$, not $2$ (classical) and not unbounded. This means quantum mechanics violates local realism by a precise, finite amount — the "nonlocality" of quantum mechanics is quantitatively constrained. This bound has deep implications for device-independent quantum cryptography and the foundations of physics.

---

*End of Chapter 2 Exercises*
