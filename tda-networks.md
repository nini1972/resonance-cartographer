---
layout: default
title: TDA & Cosmic Networks
description: Topological Data Analysis of persistent homology in neural vs. cosmic networks.
---

## Topological Data Analysis & Cosmic Networks

# Research Report: Topological Data Analysis of Persistent Homology in the
Morphological Evolution of Neural Networks vs. Cosmic Filamentary Networks

## Status Classification

**[THEORETICAL]**

The use of **Topological Data Analysis**, especially **persistent
homology**, is empirically and mathematically well established for
analyzing both **neuronal morphology/connectomes** and **cosmic web
structure** separately. However, the broader concept that neural-network
morphological evolution and cosmic filamentary-network evolution share a
deeper common organizing principle remains **theoretical and analogical**,
not experimentally verified. The strongest current interpretation is that
both systems can be studied with similar **Morse-theoretic,
filtration-based, and persistence-based tools**, but their physical
mechanisms are very different.

---

## 1. Core Concept

**Topological Data Analysis**, or **TDA**, studies the shape of data by
converting datasets into simplicial complexes and measuring features such
as connected components, loops, and voids across scales. The main
invariant used here is **persistent homology**, which tracks when
topological features are born, how long they persist, and when they die as
a scale parameter changes.

The comparison between **neural networks** and **cosmic filamentary
networks** is attractive because both display branching, hierarchical,
multiscale structures:

- In **biological neural systems**, dendrites, axons, synapses, and
connectomic pathways form branching and recurrent networks shaped by
development, activity-dependent plasticity, pruning, metabolic
constraints, and learning.
- In **artificial neural networks**, hidden-layer activations, decision
boundaries, and loss landscapes can be analyzed as evolving
geometric/topological objects during training.
- In the **cosmic web**, dark matter, gas, galaxies, clusters, filaments,
sheets, and voids form a large-scale network shaped by gravitational
instability, cosmic expansion, dark matter clustering, and baryonic
feedback.

The shared mathematical question is:

\[
\textHow does the topology of a complex network change as a function of
scale, time, or threshold?
\]

Persistent homology provides a way to answer this by producing
**barcodes**, **persistence diagrams**, **Betti curves**, and related
topological summaries.

---

## 2. Evidence Base

Key scientific sources supporting the separate domains include:

1. **Wasserman, L. (2018).** “Topological Data Analysis.” *Annual Review
of Statistics and Its Application*, 5, 501–532. DOI:
10.1146/annurev-statistics-031017-100045.
A foundational review of TDA, persistence diagrams, stability, and
statistical applications.

2. **Chazal, F., & Michel, B. (2021).** “An Introduction to Topological
Data Analysis: Fundamental and Practical Aspects for Data Scientists.”
*Frontiers in Artificial Intelligence*, 4, 667963. DOI:
10.3389/frai.2021.667963.
Explains filtrations, persistence modules, bottleneck distance,
Wasserstein distance, and practical limitations.

3. **Li, Y., Wang, D., Ascoli, G. A., Mitra, P., & Wang, Y. (2017).**
“Metrics for comparing neuronal tree shapes based on persistent homology.”
*PLOS ONE*, 12(8), e0182184. DOI: 10.1371/journal.pone.0182184.
Applies persistent homology to neuronal morphology and compares tree
shapes.

4. **Kanari, L., Dłotko, P., Scolamiero, M., Levi, R., Shillcock, J.,
Hess, K., & Markram, H. (2018).** “A Topological Representation of
Branching Neuronal Morphologies.” *Neuroinformatics*, 16, 341–362. DOI:
10.1007/s12021-017-9341-1.
Introduces topological descriptors, especially Tree-Mapping Dynamics,
for neuronal branching morphology.

5. **Giusti, C., Ghrist, R., & Bassett, D. S. (2017).** “Two’s company,
three or more is a simplex: Algebraic-topological tools for understanding
higher-order structure in neural data.” *Journal of Computational
Neuroscience*, 42, 1–14. DOI: 10.1007/s10827-016-0608-6.
Explains simplicial complexes and higher-order neural connectivity.

6. **Reimann, M. W., et al. (2017).** “Cliques of neurons bound into
cavities provide a missing link between structure and function.”
*Frontiers in Computational Neuroscience*, 11, 48. DOI:
10.3389/fncom.2017.00048.
Applies clique complexes and cavities to neural microcircuit structure.

7. **Curto, C., & Sanderson, N. (2024).** “Topological Neuroscience:
Linking Circuits to Function.” *Annual Review of Neuroscience*. DOI:
10.1146/annurev-neuro-112723-034315.
Reviews modern topological neuroscience, including persistent homology
and circuit-level topology.

8. **Pranav, P., et al. (2017).** “The topology of the cosmic web in terms
of persistent Betti numbers.” *Monthly Notices of the Royal Astronomical
Society*, 465(4), 4281–4310. DOI: 10.1093/mnras/stw2862.
Establishes persistent Betti numbers as descriptors of cosmic web
topology.

9. **Wilding, G., Nevenzeel, K., van de Weygaert, R., Pranav, P., et al.
(2021).** “Persistent homology of the cosmic web. I. Hierarchical topology
in ΛCDM cosmologies.” *Monthly Notices of the Royal Astronomical Society*,
507(2), 2968–2985. arXiv:2011.12851.
Applies persistent homology to ΛCDM simulations and studies
hierarchical cosmic topology.

10. **Sousbie, T. (2011).** “The persistent cosmic web and its filamentary
structure – I. Theory and implementation.” *Monthly Notices of the Royal
Astronomical Society*, 414, 350–383. DOI:
10.1111/j.1365-2966.2011.18365.x.
Introduces DisPerSE, a discrete Morse-theory method for identifying
filaments, walls, and voids in the cosmic web.

11. **Naitzat, G., Zhitnikov, A., & Lim, L.-H. (2020).** “Topology of Deep
Neural Networks.” *Journal of Machine Learning Research*, 21(196), 1–40.
arXiv:2004.06093.
Shows that deep neural networks transform the topology of data
representations through layers.

12. **Ramamurthy, K. N., et al. (2019).** “Topological Data Analysis of
Decision Boundaries with Application to Model Selection.” *Proceedings of
ICML*, PMLR 97, 5274–5283.
Applies TDA to decision boundaries of machine-learning classifiers.

---

## 3. Mathematical Framework

### 3.1 Filtration and Simplicial Complexes

Given a dataset, TDA builds a nested family of simplicial complexes:

\[
K_{a_1} \subseteq K_{a_2} \subseteq \cdots \subseteq K_{a_n}
\]

where \(a\) is a scale parameter, density threshold, distance threshold,
or filtration value.

For a point cloud \(P = \{x_1,\dots,x_N\}\), common complexes include:

- **Vietoris–Rips complex**:

\[
VR_\epsilon(P) = \{ \sigma \subseteq P : \|x_i - x_j\| \leq \epsilon \text{ for all } x_i, x_j \in \sigma \}.
\]

- **Čech complex**:

\[
C_\epsilon(P) = \{ \sigma \subseteq P : \bigcap_{x_i \in \sigma} B_\epsilon(x_i) \neq \emptyset \}.
\]

- **Alpha complex**, often used for Euclidean point clouds and
computationally efficient in low dimensions.

The homology groups \(H_k(K_a;\mathbb{F})\) capture:

\[
\beta_0 = \# \text{connected components},
\]

\[
\beta_1 = \# \text{loops/tunnels},
\]

\[
\beta_2 = \# \text{voids/cavities}.
\]

The full Betti curve is:

\[
\beta_k(a) = \dim H_k(K_a;\mathbb{F}).
\]

---

### 3.2 Persistent Homology

A topological feature is born at filtration value \(b\) and dies at value
\(d\). Its lifetime is:

\[
\ell = d-b.
\]

A persistence diagram is a multiset:

\[
D_k(f) = \{ (b_i, d_i) \}_i.
\]

A barcode represents each feature as an interval:

\[
I_i = [b_i,d_i).
\]

The persistent Betti number between two filtration values \(p \leq q\) is:

\[
\beta_k^p,q
=
\dim \operatornameim
\left[
H_k(K_p) \rightarrow H_k(K_q)
\right].
\]

This counts \(k\)-dimensional features born before or at \(p\) that
survive until \(q\).

---

### 3.3 Stability Theorem

A major reason TDA is useful is stability. If \(f\) and \(g\) are two
scalar fields or filtrations, then under standard conditions:

\[
d_B(D_k(f), D_k(g)) \leq \|f - g\|_\infty,
\]

where \(d_B\) is the bottleneck distance.

This means small perturbations in the data produce only small changes in
the persistence diagram. This is crucial for noisy biological imaging and
observational cosmology.

---

### 3.4 Distance Between Persistence Diagrams

A common metric is the \(p\)-Wasserstein distance:

\[
d_p(D,D')
=
\left[
\inf_{\gamma
\sum_{x \in D
\|x-\gamma(x)\|_\infty^p
\right]^1/p,
\]

where \(\gamma\) is a matching between points in the two diagrams.

This allows one to compare neural morphologies, activation manifolds, or
cosmic-web simulations quantitatively.

---

### 3.5 Persistence Entropy

A scalar summary of barcode complexity is persistence entropy:

\[
H_P
=
-\sum_i p_i \log p_i,
\]

where

\[
p_i =
\frac\ell_i\sum_j \ell_j,
\qquad
\ell_i = d_i-b_i.
\]

High persistence entropy indicates many comparably long-lived features;
low persistence entropy indicates dominance by a few robust features.

---

## 4. Neural Networks: Persistent Homology and Morphological Evolution

### 4.1 Biological Neuronal Morphology

A neuron is often represented as a rooted tree:

\[
T = (V,E),
\]

where \(V\) are branch points, terminals, and the soma, and \(E\) are
dendritic or axonal segments.

A scalar height function can be assigned:

\[
h: V \rightarrow \mathbbR}{\geq 0,
\]

where \(h(v)\) may represent radial distance from the soma, path length,
electrotonic distance, or another morphological coordinate.

The sublevel set of the tree is:

\[
T_{\leq t = \{v \in V : h(v) \leq t\{.
\]

As \(t\) increases, terminal branches appear and merge at branch points.
Each branch produces an \(H_0\) persistence interval:

\[
I_b = [h_{\texttip, h_{\textmerge].
\]

Its persistence is:

\[
\pi_b = h_{\textmerge - h_{\texttip.
\]

This is the basis of **Tree-Mapping Dynamics**, or TMD, used by Kanari et
al. to convert neuronal branching morphology into a barcode-like
representation.

Important point: a bare tree is contractible, so ordinary persistent
homology of the tree as a graph is topologically trivial:

\[
\beta_0 = 1, \qquad \beta_k = 0 \text{ for } k \geq 1.
\]

Therefore, neuronal TDA usually does not study the tree’s intrinsic
topology alone. It studies the tree with an added scalar function, such as
distance from the soma, branch order, or electrotonic length.

---

### 4.2 Biological Interpretation

Persistent homology of neuronal morphology can encode:

- dendritic branching complexity,
- axonal arborization,
- cell-type differences,
- developmental stage,
- pathology-related degeneration,
- effects of pruning or regeneration.

For example, short-lived intervals may correspond to fine local branching,
while long-lived intervals may correspond to major branches that persist
across larger spatial scales.

The proposed biological mechanisms include:

1. **Genetic developmental programs**
Neuronal morphology is constrained by cell type, transcription factors,
and molecular guidance cues.

2. **Activity-dependent plasticity**
Synaptic activity, calcium signaling, and Hebbian/STDP-like mechanisms
stabilize or eliminate branches.

3. **Metabolic and wiring-cost constraints**
Neurons balance coverage, signal propagation, and energy expenditure.

4. **Competition and pruning**
Branches compete for trophic support and synaptic reinforcement.

A schematic phenomenological branching rule could be written as:

\[
P_{\textbranch(s,t)
=
\sigma
\left(
\alpha h(s)
+
\beta C(s,t)
+
\gamma A(s,t)
-
\delta E(s,t)
+
\eta
\right),
\]

where \(h(s)\) is branch position, \(C\) is calcium activity, \(A\) is
synaptic activity, \(E\) is energetic or structural cost, and \(\eta\) is
stochasticity.

This is not a universal law, but it illustrates how morphological
evolution can be modeled as a stochastic process whose topology changes
through branching and pruning.

---

### 4.3 Neural Connectomes and Brain Networks

For connectomic or functional brain networks, one often starts with a
weighted adjacency matrix:

\[
W = (w_{ij).
\]

A threshold filtration can be defined by:

\[
G_\tau = (V, E_\tau),
\qquad
E_\tau = \{(i,j): w_{ij \geq \tau\{.
\]

Then one builds the clique complex:

\[
Cl(G_\tau).
\]

As \(\tau\) decreases, more edges and higher-order cliques appear.
Persistent homology tracks:

\[
\beta_0(\tau), \quad \beta_1(\tau), \quad \beta_2(\tau), \dots
\]

In neural systems, \(\beta_1\) may capture loops in connectivity, while
\(\beta_2\) may capture higher-order cavities formed by cliques. This has
been used in topological neuroscience to study integration, segregation,
and higher-order organization.

---

### 4.4 Artificial Neural Networks

For artificial neural networks, morphology can refer to the geometry of
hidden representations rather than physical branching.

A feedforward network can be written as:

\[
z_\ell(x)
=
\phi_\ell(W_\ell z_{\ell-1(x)+b_\ell),
\]

where \(z_\ell(x)\) is the activation vector at layer \(\ell\).

For a dataset \(\{x_i}{i=1^N\), one obtains a point cloud in activation
space:

\[
Z_\ell = \{z_\ell(x_i)}{i=1^N.
\]

Then persistent homology can be applied to:

\[
VR_\epsilon(Z_\ell),
\]

yielding:

\[
D_k^\ell = \operatornamePH}k(VR_\epsilon(Z_\ell)).
\]

This allows one to study how training changes the topology of
representations. Deep networks often transform tangled input manifolds
into more linearly separable representations.

For ReLU networks, the input space is partitioned into linear regions:

\[
\mathcalA = \{A_s}{s,
\]

where each \(A_s\) corresponds to a pattern of active and inactive ReLU
units. The number of linear regions grows combinatorially with depth and
width. Persistent homology can characterize the topology of these
polyhedral decompositions and decision boundaries.

---

## 5. Cosmic Filamentary Networks: Persistent Homology of the Cosmic Web

### 5.1 Cosmic Web Structure

The cosmic web consists of:

- dense clusters,
- filaments,
- sheets or walls,
- voids,
- galaxy groups.

In ΛCDM cosmology, structure forms through gravitational instability from
small primordial density fluctuations.

The matter density field is:

\[
\rho(\mathbfx,z) = \bar\rho(z)[1+\delta(\mathbfx,z)],
\]

where \(\delta\) is the density contrast.

In the linear regime, density perturbations grow approximately according
to:

\[
\ddot\delta
+
2H\dot\delta
-
4\pi G\bar\rho}m\delta
=
0.
\]

Here \(H\) is the Hubble parameter and \(\bar\rho}m\) is the mean matter
density.

---

### 5.2 Filament Formation in ΛCDM

A useful approximation is the Zel’dovich displacement:

\[
\mathbfx(\mathbfq,t)
=
\mathbfq
-
D(t)\nabla_{\mathbfq\Phi(\mathbfq),
\]

where \(\mathbfq\) is the Lagrangian coordinate, \(D(t)\) is the growth
factor, and \(\Phi\) is the gravitational potential.

Collapse occurs when:

\[
1 - D(t)\lambda_i = 0,
\]

where \(\lambda_i\) are eigenvalues of the deformation tensor.

Anisotropic collapse produces:

1. collapse along one axis → sheets,
2. collapse along two axes → filaments,
3. collapse along three axes → nodes/clusters.

This naturally produces the filamentary cosmic web.

---

### 5.3 Persistent Homology of the Cosmic Web

For the cosmic density field, one defines superlevel sets:

\[
K_\nu = \{\mathbfx : \rho(\mathbfx) \geq \nu\{.
\]

As \(\nu\) decreases, more regions are included.

The Betti numbers have physical interpretations:

\[
\beta_0(\nu) = \# \textisolated high-density components,
\]

\[
\beta_1(\nu) = \# \textloops/tunnels associated with filamentary
connectivity,
\]

\[
\beta_2(\nu) = \# \textvoid-like cavities enclosed by dense structures.
\]

The curves \(\beta_k(\nu)\) are called **Betti curves**. They encode how
cosmic structure appears hierarchically across density thresholds.

Persistent Betti numbers improve robustness:

\[
\beta_k^p,q
=
\dim \operatornameim
\left[
H_k(K_p) \rightarrow H_k(K_q)
\right].
\]

This allows one to distinguish real cosmic structures from noise or
numerical artifacts.

---

### 5.4 Discrete Morse Theory and DisPerSE

Sousbie’s DisPerSE method uses discrete Morse theory to identify critical
points of the density field and connect them into a Morse–Smale complex.
Filaments, walls, and void boundaries are identified as stable topological
structures above a persistence threshold.

The critical points include:

- minima: void centers,
- index-1 saddles: wall-like structures,
- index-2 saddles: filamentary structures,
- maxima: clusters or nodes.

Pairs of critical points with high persistence correspond to robust cosmic
features.

---

## 6. Proposed Common Mechanisms: What Is Shared?

The strongest shared mechanism is not a shared physical law, but a shared
mathematical structure: **Morse-theoretic hierarchical organization under
a scalar field**.

| Feature | Neural systems | Cosmic web |
|---|---|---|
| Object | Neuron, connectome, activation manifold | Density field, galaxy
distribution, dark matter distribution |
| Scalar field | Distance from soma, activation strength, connectivity
weight, loss value | Density \(\rho(\mathbfx,z)\), gravitational
potential |
| Filtration | Branch length, thresholded connectivity, activation
distance | Density threshold \(\nu\), redshift \(z\), smoothing scale |
| \(H_0\) | Components, branches, clusters of activations | Clusters,
proto-halos |
| \(H_1\) | Loops in connectomes or activation manifolds | Filament
loops/tunnels |
| \(H_2\) | Cavities in higher-order neural complexes | Voids |
| Evolution driver | Plasticity, growth, pruning, training | Gravity,
expansion, dark matter clustering, feedback |
| Main TDA output | Barcodes, persistence landscapes, Betti curves |
Persistent Betti numbers, filament catalogs, void topology |

The common mathematical pattern is:

\[
O_t
\longrightarrow
f_t
\longrightarrow
K_a(f_t)
\longrightarrow
H_k(K_a)
\longrightarrow
D_k(t),
\]

where \(O_t\) is the object at time \(t\), \(f_t\) is a scalar field or
filtration function, \(K_a\) is the filtered complex, and \(D_k(t)\) is
the persistence diagram.

However, this is a shared **data-analysis framework**, not evidence of a
shared physical mechanism.

---

## 7. Mainstream Model vs. Alternative Counter-Hypothesis: ΛCDM vs. MOND

### 7.1 Mainstream Model: ΛCDM and Dark Matter

The mainstream cosmological model is **ΛCDM**, where structure forms in a
universe dominated by:

- cold dark matter,
- dark energy,
- baryonic matter,
- primordial nearly Gaussian fluctuations.

The Friedmann equation is:

\[
H^2(a)
=
H_0^2
\left[
\Omega_r a^-4
+
\Omega_m a^-3
+
\Omega_k a^-2
+
\Omega_\Lambda
\right].
\]

In this model, cosmic filaments arise because dark matter collapses
gravitationally along anisotropic tidal fields. Persistent homology of
ΛCDM simulations has shown that Betti curves and persistence diagrams
encode information about:

- matter density \(\Omega_m\),
- dark energy,
- primordial fluctuation amplitude,
- neutrino mass,
- bias and smoothing scale,
- redshift evolution.

This is a mainstream, physically motivated use of TDA.

---

### 7.2 Alternative Counter-Hypothesis: MOND / Modified Gravity

An alternative is **MOND**, or Modified Newtonian Dynamics, which attempts
to explain galaxy rotation curves without particle dark matter.

The MOND relation is commonly written as:

\[
a\,\mu\left(\fracaa_0\right) = a_N,
\]

where:

\[
a_N = \fracGMr^2
\]

is the Newtonian acceleration, and:

\[
a_0 \approx 1.2 \times 10^-10\,\mathrmm/s^2.
\]

In the deep-MOND regime:

\[
a \ll a_0,
\]

one obtains:

\[
a \approx \sqrta_0 a_N.
\]

This successfully explains many galaxy-scale rotation curves, but it
struggles with:

- galaxy clusters,
- gravitational lensing,
- CMB acoustic peak structure,
- large-scale structure formation,
- cosmic web topology,
- relativistic consistency.

Relativistic MOND theories, such as TeVeS-like models, add extra fields,
but they have not replaced ΛCDM as a complete cosmological model.

---

### 7.3 Experimental and Observational Bounds

Current observations strongly constrain alternatives to ΛCDM:

1. **Cosmic microwave background**
Planck measurements require non-baryonic matter to reproduce the
observed acoustic peak structure.

2. **Baryon density constraint**
BBN and CMB give:

\[
\Omega_b \approx 0.049,
\qquad
\Omega_m \approx 0.315.
\]

Baryons alone cannot account for the total matter density.

3. **Neutrino mass bounds**
Cosmological constraints give approximately:

\[
\sum m_\nu \lesssim 0.12\,\mathrmeV,
\]

too small for neutrinos to serve as the dominant dark matter component.

4. **Cluster lensing and merging systems**
Systems such as the Bullet Cluster show lensing mass separated from hot
X-ray gas, favoring collisionless mass components or additional fields.

5. **Self-interacting dark matter bounds**
Cluster mergers typically constrain:

\[
\frac\sigmam
\lesssim
0.1-1\,\mathrmcm^2/g,
\]

depending on system and analysis.

Persistent homology could in principle help distinguish ΛCDM from
MOND-like models by comparing Betti curves and persistence diagrams of
simulated cosmic webs. However, current observational and simulation-based
evidence still favors ΛCDM for the full cosmic web.

---

## 8. Skepticism, Limitations, and Empirical Gaps

### 8.1 The Analogy Is Real but Easily Overinterpreted

The neural-cosmic comparison is mathematically legitimate but physically
limited. Neural systems are:

- adaptive,
- directed,
- plastic,
- metabolically active,
- information-processing systems.

Cosmic filaments are:

- gravitationally evolved,
- non-adaptive,
- nondirected,
- not computational in the biological sense.

Therefore, claims that the universe is “like a brain” are not supported by
TDA alone.

---

### 8.2 Neural Morphology Limitations

For biological neurons:

1. A tree has trivial ordinary topology:

\[
\beta_0=1,\qquad \beta_{k\geq1=0.
\]

2. TMD depends on the chosen height function, such as radial distance or
path length.

3. Different height functions can produce different barcodes.

4. Imaging artifacts can create false branches or remove real ones.

5. Most datasets are static snapshots, not true longitudinal developmental
trajectories.

6. Persistent homology summarizes morphology but does not by itself
identify causal developmental mechanisms.

---

### 8.3 Artificial Neural Network Limitations

For artificial neural networks:

1. Persistent homology depends on the chosen layer, activation space,
distance metric, and filtration.

2. Different architectures can produce similar topological summaries.

3. Topology does not uniquely determine function.

4. High-dimensional point clouds suffer from sparsity and metric
concentration.

5. Interpretation of \(H_1\) loops or \(H_2\) cavities in activation space
is not always biologically or computationally meaningful.

---

### 8.4 Cosmic Web Limitations

For cosmology:

1. Galaxy surveys have selection functions, masks, and redshift-space
distortions.

2. Observed galaxies are biased tracers of the underlying dark matter
field.

3. Simulation results depend on resolution, box size, smoothing scale, and
baryonic physics.

4. Persistent homology is sensitive to the chosen density estimator.

5. Gaussian random fields can reproduce some large-scale topological
features, so topology alone does not uniquely identify cosmology.

6. Observational persistent homology is still less mature than
simulation-based persistent homology.

---

### 8.5 Cross-Domain Limitations

The comparison between neural and cosmic networks faces additional
problems:

1. **Different causal physics**
Neurons are shaped by molecular and activity-dependent processes;
cosmic filaments are shaped by gravity and expansion.

2. **Different dimensionality and scale**
Neural morphology operates at micrometer-to-meter scales; cosmic
filaments operate at megaparsec scales.

3. **Different meaning of topology**
Neural loops may represent recurrent circuits; cosmic loops may
represent filamentary tunnels or survey artifacts.

4. **Equifinality**
Similar Betti curves can arise from different mechanisms.

5. **Lack of predictive cross-domain law**
No equation currently predicts both neuronal branching and cosmic
filamentation from the same parameters.

---

## 9. Current Understanding

The current scientific understanding can be summarized as follows:

1. **Persistent homology is mathematically robust** for extracting
multiscale topological features from noisy data.

2. **Neuronal morphology can be represented by persistence barcodes**,
especially when a meaningful height function is chosen.

3. **Brain connectomes and artificial neural networks can be studied
through clique complexes, activation manifolds, and decision-boundary
topology.**

4. **Cosmic web topology can be quantified using persistent Betti
numbers**, persistent diagrams, and discrete Morse theory.

5. **ΛCDM simulations produce characteristic Betti curves** associated
with hierarchical structure formation.

6. **The neural-cosmic analogy is best understood as a shared mathematical
framework**, not as evidence of shared physical causality.

---

## 10. Research Implications

A rigorous future research program would require:

1. Standardized filtrations for neuronal morphology.
2. Longitudinal neural development datasets.
3. Controlled artificial neural network training experiments.
4. Large ΛCDM and alternative-cosmology simulations.
5. Null models for both neural and cosmic networks.
6. Statistical tests using persistence landscapes, Betti curves, and
Wasserstein distances.
7. Direct comparison only after dimensionless normalization.

A possible comparative descriptor is:

\[
S(O_t)
=
\left[
\beta_0(t),
\beta_1(t),
\beta_2(t),
H_P(t),
d_W(D_t,D_{t+\Delta t)
\right],
\]

where \(O_t\) is either a neural object or cosmic object at time \(t\).

But at present, this remains a comparative analytic framework rather than
a verified unified theory.

---

## 11. Final Classification

**[THEORETICAL]**

The separate applications of persistent homology to neuronal morphology,
neural connectomes, artificial neural networks, and cosmic web structure
are scientifically credible and increasingly validated. However, the
broader concept of a shared morphological evolution between neural
networks and cosmic filamentary networks remains theoretical. The analogy
is mathematically meaningful but physically unproven.

The strongest justified statement is:

> Persistent homology provides a common language for describing
hierarchical branching, connectivity, and multiscale topology in both
neural and cosmic networks, but it does not establish a shared mechanism
or physical equivalence between them.

---

## 12. Visual Grounding

Create a two-panel scientific schematic diagram: on the left, show a
biological neuron with dendritic branches and an axon, overlaid with a
smaller artificial neural network whose hidden-layer activations appear as
colored point clouds; on the right, show a three-dimensional cosmic web
with luminous filaments, dense nodes, sheet-like walls, and dark voids. In
the center, place a TDA pipeline: “Data object → scalar field/filtration →
simplicial complex → persistent homology → barcode/Betti curves.” Use
arrows from the neuron to the pipeline labeled \(h(v)\), “branch length,”
and \(I_b=[b,d)\); arrows from the cosmic web labeled
\(\rho(\mathbfx,z)\), “density threshold,” and \(\beta_k(\nu)\). Below
the pipeline, show matching barcode plots and Betti curves for neural and
cosmic cases, with \(H_0\), \(H_1\), and \(H_2\) color-coded. Add a dashed
comparison arrow between the two panels labeled “shared mathematical
framework, not shared physics.” Include small insets for null models, a