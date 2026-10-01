# Reading list

Every source the survey cites, grouped by system and topic, with a line on why it matters. The
BibTeX is in [papers.bib](papers.bib). `scripts/fetch_papers.py` downloads the arXiv ones into
`papers/` and prints each one's licence.

## QubiC

Lawrence Berkeley National Laboratory. Profile: [docs/systems/qubic.md](../docs/systems/qubic.md).

- Xu et al., *QubiC 2.0: An Extensible Open-Source Qubit Control System Capable of Mid-Circuit Measurement and Feed-Forward*, arXiv preprint (2023). [arXiv:2309.10333](https://arxiv.org/abs/2309.10333)  
  The QubiC 2.0 paper: ZCU216, gateware, distributed processor, multi-board sync, mid-circuit measurement.
- Fruitwala et al., *Distributed Architecture for FPGA-based Superconducting Qubit Control*, arXiv preprint (2024). [arXiv:2404.15260](https://arxiv.org/abs/2404.15260)  
  The processor in depth: instruction set, FPROC, QubiC-IR and compiler, resources per core, teleportation.
- Xu et al., *Multi-FPGA Synchronization and Data Communication for Quantum Control and Measurement*, IEEE 33rd Annual International Symposium on Field-Programmable Custom Computing Machines (FCCM) (2025). [arXiv:2506.09856](https://arxiv.org/abs/2506.09856) [doi](https://doi.org/10.1109/FCCM62733.2025.00075)  
  Multi-board operation: ring time protocol on GPIO, Aurora links, three boards.
- Vora et al., *ML-Powered FPGA-based Real-Time Quantum State Discrimination Enabling Mid-circuit Measurements*, arXiv preprint (2024). [arXiv:2406.18807](https://arxiv.org/abs/2406.18807)  
  Neural-network state discrimination in fabric, for qubits and qutrits.
- Fruitwala et al., *Hardware-Efficient Randomized Compiling*, arXiv preprint (2024). [arXiv:2406.13967](https://arxiv.org/abs/2406.13967)  
  Randomized compiling done by the hardware.
- Rajagopala et al., *Hardware-Assisted Parameterized Circuit Execution*, arXiv preprint (2024). [arXiv:2409.03725](https://arxiv.org/abs/2409.03725)  
  Parameterized circuits executed by the hardware.
- Guang et al., *Breaking Memory Bottlenecks in Quantum Control Systems for More Precise Experiments and Higher Throughput Computing*, arXiv preprint (2026). [arXiv:2608.06318](https://arxiv.org/abs/2608.06318)  
  A memory hierarchy for envelopes and programs, said to be headed for QubiC 3.0; states QubiC 2.0's memory limits.
- Huszabianlou et al., *Error-Bounded Fixed-Point Design of Super-Sample-Rate IIR Filters for Real-Time Superconducting Qubit Flux Predistortion*, arXiv preprint (2026). [arXiv:2609.16488](https://arxiv.org/abs/2609.16488)  
  Flux predistortion filters on QubiC's flux lines.
- Brahmbhatt et al., *An open-source data storage and visualization platform for collaborative qubit control*, Scientific Reports 14 (2024). [arXiv:2403.14672](https://arxiv.org/abs/2403.14672) [doi](https://doi.org/10.1038/s41598-024-72584-9)  
  QubiCSV: calibration and data storage around QubiC.
- Xu et al., *QubiC: An Open-Source FPGA-Based Control and Measurement System for Superconducting Quantum Information Processors*, IEEE Transactions on Quantum Engineering 2 (2021). [arXiv:2101.00071](https://arxiv.org/abs/2101.00071) [doi](https://doi.org/10.1109/TQE.2021.3116540)  
  QubiC 1.0, before the RFSoC: VC707, IQ mixers, the 128-bit command format.
- Xu et al., *Radio frequency mixing modules for superconducting qubit room temperature control systems*, Review of Scientific Instruments 92 (2021). [arXiv:2101.00066](https://arxiv.org/abs/2101.00066) [doi](https://doi.org/10.1063/5.0055906)  
  QubiC 1.0's analog up- and down-converters.
- Xu et al., *Automatic Qubit Characterization and Gate Optimization with QubiC*, ACM Transactions on Quantum Computing 4 (2023). [arXiv:2104.10866](https://arxiv.org/abs/2104.10866) [doi](https://doi.org/10.1145/3529397)  
  QubiC 1.0's automatic calibration.
- Fruitwala et al., *Distributed Processor for FPGA-based Superconducting Qubit Control*, IEEE International Conference on Quantum Computing and Engineering (QCE) (2022). [doi](https://doi.org/10.1109/QCE53715.2022.00109)  
  First description of the distributed processor (two-page poster).
- Huang et al., *QubiC 2.0: A Flexible Advanced Full Stack Quantum Bit Control System*, IEEE International Conference on Quantum Computing and Engineering (QCE) (2023). [doi](https://doi.org/10.1109/QCE57702.2023.10227)  
  QubiC 2.0 at IEEE QCE 2023 (two-page abstract).
- Huang et al., *Updated QubiC: Improved Scalability, Performance, and QPU Support*, IEEE International Conference on Quantum Computing and Engineering (QCE) (2024). [doi](https://doi.org/10.1109/QCE60285.2024.10430)  
  QubiC updates at IEEE QCE 2024: front-end boards, multi-board software (two-page abstract).
- Hashim et al., *Quasiprobabilistic Readout Correction of Midcircuit Measurements for Adaptive Feedback via Measurement Randomized Compiling*, PRX Quantum 6 (2025). [arXiv:2312.14139](https://arxiv.org/abs/2312.14139) [doi](https://doi.org/10.1103/PRXQuantum.6.010307)  
  Mid-circuit measurement on QubiC; Appendix C gives the 150 ns feedback figure.
- Hashim et al., *Efficient generation of multi-partite entanglement between non-local superconducting qubits using classical feedback*, APL Quantum 2 (2025). [arXiv:2403.18768](https://arxiv.org/abs/2403.18768) [doi](https://doi.org/10.1063/5.0291637)  
  GHZ states between non-adjacent qubits by feedback; Appendix D builds lookup tables from branches.
- Francis et al., *Efficient Classical Processing of Constant-Depth Time Evolution Circuits in Control Hardware*, IEEE International Conference on Quantum Computing and Engineering (QCE) (2025). [arXiv:2507.12765](https://arxiv.org/abs/2507.12765) [doi](https://doi.org/10.1109/QCE65121.2025.00203)  
  Constant-depth time evolution using QubiC's parameterized execution.
- Balewski et al., *First-principle crosstalk dynamics and Hamiltonian learning via Rabi experiments*, arXiv preprint (2025). [arXiv:2502.05362](https://arxiv.org/abs/2502.05362)  
  Crosstalk learned from Rabi experiments run on QubiC.
- Chen et al., *Scalable and Site-Specific Frequency Tuning of Two-Level System Defects in Superconducting Qubit Arrays*, arXiv preprint (2025). [arXiv:2503.04702](https://arxiv.org/abs/2503.04702)  
  TLS defect tuning; drive and readout synthesized directly by QubiC.
- Goss et al., *A Qutrit Time Crystal Stabilized with Native Chiral Interactions*, arXiv preprint (2026). [arXiv:2605.14293](https://arxiv.org/abs/2605.14293)  
  A 20-qubit flux-tunable processor driven by QubiC.
- Cao et al., *Superconducting qubit readout enhanced by path signature*, arXiv preprint (2024). [arXiv:2402.09532](https://arxiv.org/abs/2402.09532)  
  Oxford: readout data taken on QubiC 2.0.
- Cao et al., *Automating quantum computing laboratory experiments with an agent-based AI framework*, Patterns 6 (2025). [arXiv:2412.07978](https://arxiv.org/abs/2412.07978) [doi](https://doi.org/10.1016/j.patter.2025.101372)  
  Oxford: lab agents on a QubiC-driven setup.
- Alghadeer et al., *Low Crosstalk in a Scalable Superconducting Quantum Lattice*, arXiv preprint (2025). [arXiv:2505.22276](https://arxiv.org/abs/2505.22276)  
  Oxford: pulses synthesized by QubiC, readout down-converted in analog.
- Giortamis et al., *MCMit: Hardware-Software Co-Design for Mid-Circuit Measurement Error Mitigation*, arXiv preprint (2026). [arXiv:2604.25863](https://arxiv.org/abs/2604.25863)  
  Third-party: QubiC branch and feedback latency against the number of inputs (Table II).
- Giortamis et al., *Oraqle: An Empirical Analysis of Qubit Readout and Discriminators in Quantum Error Correction*, arXiv preprint (2026). [arXiv:2608.01939](https://arxiv.org/abs/2608.01939)  
  Third-party: discriminator costs on QubiC's ZCU216 design.

## QICK

Fermilab. Profile: [docs/systems/qick.md](../docs/systems/qick.md).

- Stefanazzi et al., *The QICK (Quantum Instrumentation Control Kit): Readout and control for qubits and detectors*, Review of Scientific Instruments 93 (2022). [arXiv:2110.00557](https://arxiv.org/abs/2110.00557) [doi](https://doi.org/10.1063/5.0076249)  
  The founding paper: ZCU111, tProcessor v1, RF board, the only published QICK feedback-latency breakdown.
- Ding et al., *Experimental advances with the QICK (Quantum Instrumentation Control Kit) for superconducting quantum hardware*, Physical Review Research 6 (2024). [arXiv:2311.17171](https://arxiv.org/abs/2311.17171) [doi](https://doi.org/10.1103/PhysRevResearch.6.013305)  
  QICK on the ZCU216: mixer-free control to 10 GHz, multiplexed generators and readout, phase stability.
- Martin et al., *XCOM: Full Mesh Network Synchronization and Low-Latency Communication for QICK (Quantum Instrumentation Control Kit)*, arXiv preprint (2026). [arXiv:2603.18977](https://arxiv.org/abs/2603.18977)  
  XCOM: QICK's own full-mesh multi-board synchronization and messaging.
- Carobene et al., *Qibosoq: an open-source framework for quantum circuit RFSoC programming*, Quantum Science and Technology 10 (2025). [arXiv:2310.05851](https://arxiv.org/abs/2310.05851) [doi](https://doi.org/10.1088/2058-9565/adcd97)  
  Qibosoq: the server that connects QICK to Qibo.
- Efthymiou et al., *Qibolab: an open-source hybrid quantum operating system*, Quantum 8 (2024). [arXiv:2308.06313](https://arxiv.org/abs/2308.06313) [doi](https://doi.org/10.22331/q-2024-02-12-1247)  
  Qibolab: drives QICK through Qibosoq and benchmarks it against commercial controllers.
- Silva and Orgaz-Fuertes, *Manarat: A scalable QICK-based control system for superconducting quantum processors supporting synchronized control of 10 flux-tunable qubits*, Review of Scientific Instruments 97 (2026). [arXiv:2507.10676](https://arxiv.org/abs/2507.10676) [doi](https://doi.org/10.1063/5.0301360)  
  Manarat, from TII: QICK extended to two synchronized ZCU216s and 10 qubits.
- Guglielmo et al., *End-to-End Workflow for Machine-Learning-Based Qubit Readout With QICK and hls4ml*, IEEE Transactions on Quantum Engineering 6 (2025). [arXiv:2501.14663](https://arxiv.org/abs/2501.14663) [doi](https://doi.org/10.1109/TQE.2025.3604712)  
  A neural-network readout discriminator for QICK, built with hls4ml.
- Gaytan-Villarreal et al., *Real-Time Detection of Charge Jumps in Superconducting Qubits with a Convolutional Neural Network*, arXiv preprint (2026). [arXiv:2607.14293](https://arxiv.org/abs/2607.14293)  
  A neural network on a QICK ZCU216 flagging charge jumps for the tProcessor.
- Johnson et al., *Exploration of Optimizing FPGA-based Qubit Controller for Experiments on Superconducting Quantum Computing Hardware*, IEEE International Conference on Electro Information Technology (eIT) (2023). [arXiv:2305.06976](https://arxiv.org/abs/2305.06976) [doi](https://doi.org/10.1109/eIT57321.2023.10187252)  
  Ways to optimize QICK, surveyed.
- Johnson et al., *Demonstrating the Potential of Adaptive LMS Filtering on FPGA-Based Qubit Control Platforms for Improved Qubit Readout in 2D and 3D Quantum Processing Units*, IEEE International Conference on Quantum Computing and Engineering (QCE) (2024). [arXiv:2408.00904](https://arxiv.org/abs/2408.00904) [doi](https://doi.org/10.1109/QCE60285.2024.00156)  
  Adaptive LMS filtering as a QICK IP block.
- Riendeau et al., *Quantum Instrumentation Control Kit: Defect Arbitrary Waveform Generator (QICK-DAWG): A Quantum Sensing Control Framework for Quantum Defects*, arXiv preprint (2023). [arXiv:2311.18253](https://arxiv.org/abs/2311.18253)  
  QICK-DAWG: QICK extended for NV-centre sensing.
- Zhang et al., *Tunable Inductive Coupler for High-Fidelity Gates Between Fluxonium Qubits*, PRX Quantum 5 (2024). [arXiv:2309.05720](https://arxiv.org/abs/2309.05720) [doi](https://doi.org/10.1103/PRXQuantum.5.020326)  
  Fluxonium gates; QICK feedback used for active reset (App. G).
- Bland et al., *Millisecond lifetimes and coherence times in 2D transmon qubits*, Nature 647 (2025). [arXiv:2503.14798](https://arxiv.org/abs/2503.14798) [doi](https://doi.org/10.1038/s41586-025-09687-4)  
  Millisecond transmons, measured with a QICK-controlled ZCU216 alongside a commercial controller.
- Anferov et al., *Superconducting Qubits above 20 GHz Operating over 200 mK*, PRX Quantum 5 (2024). [arXiv:2402.03031](https://arxiv.org/abs/2402.03031) [doi](https://doi.org/10.1103/PRXQuantum.5.030347)  
  Qubits above 20 GHz, on a QICK ZCU111.
- Martinez et al., *Flat-band localization and interaction-induced delocalization of photons*, Science Advances 9 (2023). [arXiv:2303.02170](https://arxiv.org/abs/2303.02170) [doi](https://doi.org/10.1126/sciadv.adj7195)  
  Flat-band photonics experiment on a QICK ZCU216.
- Xia et al., *Fast superconducting qubit control with subharmonic drives*, Nature Communications 17 (2025). [arXiv:2306.10162](https://arxiv.org/abs/2306.10162) [doi](https://doi.org/10.1038/s41467-025-67766-6)  
  Subharmonic qubit drives with QICK.

## FIREQ

Politecnico di Torino. Profile: [docs/systems/fireq.md](../docs/systems/fireq.md).

- Capra et al., *FIREQ: FPGA Instrumentation for Readout and Qubit control*, arXiv preprint (2026). [arXiv:2608.29399](https://arxiv.org/abs/2608.29399)  
  The FIREQ paper. Also compares eight frameworks (Table I) and reports FPGA resources for QICK, QubiC, RISC-Q and FIREQ on one board (Tables II and III).

## RISC-Q

University of Maryland. Profile: [docs/systems/risc-q.md](../docs/systems/risc-q.md).

- Liu et al., *RISC-Q: A Generator for Real-Time Quantum Control System-on-Chips Compatible with RISC-V*, arXiv preprint (2025). [arXiv:2505.14902](https://arxiv.org/abs/2505.14902)  
  The RISC-Q generator; compares lines of HDL and resources with QICK and QubiC (Sec. V, Table I).
- Liu et al., *A Scalable Open-Source QEC System with Sub-Microsecond Decoding-Feedback Latency*, arXiv preprint (2026). [arXiv:2603.16203](https://arxiv.org/abs/2603.16203)  
  A three-board error-correction system on RISC-Q, in QubiC chassis, with a staged latency breakdown.

## SQ-CARS

IISc Bangalore. Profile: [docs/systems/sq-cars.md](../docs/systems/sq-cars.md).

- Singhal et al., *SQ-CARS: A Scalable Quantum Control and Readout System*, IEEE Transactions on Instrumentation and Measurement 72 (2023). [arXiv:2203.01523](https://arxiv.org/abs/2203.01523) [doi](https://doi.org/10.1109/TIM.2023.3305656)  
  The SQ-CARS paper; its Table I compares QubiC 1.0, QICK, ICARUS-Q, Presto and others as of 2022.
- Gautam et al., *Quantized NN Workflow for Low-Latency Multi-Qubit State Discrimination on FPGA*, 16th International Symposium on Highly Efficient Accelerators and Reconfigurable Technologies (2026). [arXiv:2407.03852](https://arxiv.org/abs/2407.03852) [doi](https://doi.org/10.1145/3814576.3814580)  
  The same group's neural-network readout for five qubits on the ZCU111.

## QiController

Karlsruhe Institute of Technology. Profile: [docs/systems/qicontroller.md](../docs/systems/qicontroller.md).

- Gebauer et al., *QiCells: A Modular RFSoC-based Approach to Interface Superconducting Quantum Bits*, ACM Transactions on Reconfigurable Technology and Systems 16 (2023). [doi](https://doi.org/10.1145/3571820)  
  QiCells: the most detailed description of the QiController's gateware.
- Gebauer et al., *A modular RFSoC-based approach to interface superconducting quantum bits*, International Conference on Field-Programmable Technology (ICFPT) (2021). [doi](https://doi.org/10.1109/ICFPT52863.2021.9609909)  
  The conference precursor of QiCells.
- Gebauer et al., *State preparation of a fluxonium qubit with feedback from a custom FPGA-based platform*, AIP Conference Proceedings (2020). [arXiv:1912.06814](https://arxiv.org/abs/1912.06814) [doi](https://doi.org/10.1063/5.0011721)  
  Fluxonium active reset; the 428 ns feedback figure.
- Ardila-Perez et al., *The Quantum Interface Controller: A Full-Stack, Modular, and Scalable System for Qubit Readout and Manipulation*, IEEE International Conference on Quantum Computing and Engineering (QCE) (2024). [doi](https://doi.org/10.1109/QCE60285.2024.10358)  
  The QiController as a multi-RFSoC ATCA system (two-page abstract).

## Related systems not in the comparison

See the README for why each is left out.

- Park et al., *ICARUS-Q: Integrated control and readout unit for scalable quantum processors*, Review of Scientific Instruments 93 (2022). [arXiv:2112.02933](https://arxiv.org/abs/2112.02933) [doi](https://doi.org/10.1063/5.0081232)  
  ICARUS-Q: a 16-channel RFSoC system, published without code.
- Liang et al., *HI-HCQC: A Tightly-Coupled Hardware Interface with High-Efficiency Communication for Hybrid Classical-Quantum Computing*, arXiv preprint (2026). [arXiv:2606.18642](https://arxiv.org/abs/2606.18642)  
  HI-HCQC: a PCIe-attached RFSoC controller, published without code.
- Tholén et al., *Measurement and control of a superconducting quantum processor with a fully integrated radio-frequency system on a chip*, Review of Scientific Instruments 93 (2022). [arXiv:2205.15253](https://arxiv.org/abs/2205.15253) [doi](https://doi.org/10.1063/5.0101398)  
  Presto: a commercial RFSoC controller with a well-documented feedback engine.
- Guo et al., *Vectorizing Quantum Control: A RISC-V Vector Extension Architecture for Scalable Qubit Systems*, arXiv preprint (2026). [arXiv:2607.07372](https://arxiv.org/abs/2607.07372)  
  HiSEP-Q 2.0: an open RISC-V vector processor for qubit control, without an RF chain yet.
- Zhao et al., *Distributed-HISQ: A Distributed Quantum Control Architecture*, 58th IEEE/ACM International Symposium on Microarchitecture (2025). [arXiv:2509.04798](https://arxiv.org/abs/2509.04798) [doi](https://doi.org/10.1145/3725843.3756048)  
  Distributed-HISQ: a distributed control architecture; discusses QubiC's sync instruction.
- She et al., *QuCtrl-BELL: A Compiler-Driven Sub-Microsecond Feedback Control Stack for Scalable Trapped-Ion Quantum Experiments*, arXiv preprint (2026). [arXiv:2605.22433](https://arxiv.org/abs/2605.22433)  
  QuCtrl-BELL, for trapped ions; its Table I compares ARTIQ, QubiC and QICK as programming models.
- Yang et al., *FPGA-based electronic system for the control and readout of superconducting quantum processors*, Review of Scientific Instruments 93 (2022). [arXiv:2110.07965](https://arxiv.org/abs/2110.07965) [doi](https://doi.org/10.1063/5.0085467)  
  An FPGA controller on discrete AD9739 DACs, often used as a comparison point.
- Kalfus et al., *High-Fidelity Control of Superconducting Qubits Using Direct Microwave Synthesis in Higher Nyquist Zones*, IEEE Transactions on Quantum Engineering 1 (2020). [arXiv:2008.02873](https://arxiv.org/abs/2008.02873) [doi](https://doi.org/10.1109/TQE.2020.3042895)  
  Direct synthesis in higher Nyquist zones on discrete DACs; the case the RFSoC designs rely on.
- Raftery et al., *Direct digital synthesis of microwave waveforms for quantum computing*, arXiv preprint (2017). [arXiv:1703.00942](https://arxiv.org/abs/1703.00942)  
  Direct digital synthesis of qubit waveforms, an early case for skipping the mixer.

## Surveys and comparisons

The closest prior work; see the README.

- Rizvi et al., *A Survey of Microwave-Implemented Superconducting Qubit Control and Readout Circuits*, IEEE Transactions on Quantum Engineering 7 (2026). [doi](https://doi.org/10.1109/TQE.2026.3659400)  
  A broad survey of control and readout, with a paragraph or two on each RFSoC system.
- Le et al., *Computing Systems for Superconducting Qubits: Challenges and Opportunities*, 23rd Annual International Conference on Mobile Systems, Applications and Services (2025). [doi](https://doi.org/10.1145/3711875.3737657)  
  A four-page overview of control systems, mostly by QubiC authors.
- Nikbakhtnasrabadi and Weides, *Quantum Control Architecture and Circuit Blocks for Solid-State Microwave Qubits*, TechRxiv preprint (2025). [doi](https://doi.org/10.36227/techrxiv.173933155.57992122/v1)  
  A review of FPGA control platforms, open and commercial. Full text not retrieved for this survey.
- Shammah et al., *Open hardware solutions in quantum technology*, APL Quantum 1 (2024). [arXiv:2309.17233](https://arxiv.org/abs/2309.17233) [doi](https://doi.org/10.1063/5.0180987)  
  Open quantum hardware, broadly; one paragraph each on QubiC and QICK.
- Brennan et al., *Classical interfaces for controlling cryogenic quantum computing technologies*, APL Quantum 2 (2025). [arXiv:2504.18527](https://arxiv.org/abs/2504.18527) [doi](https://doi.org/10.1063/5.0273490)  
  Classical interfaces for cryogenic quantum computers; scaling context.
- Malarchick, *Measuring Control-Plane Openness in Near-Term Quantum Computing: A Rubric, Its Validation, and an Application to Thirteen Vendor Stacks*, arXiv preprint (2026). [arXiv:2605.15233](https://arxiv.org/abs/2605.15233)  
  A rubric for scoring how open a control plane is, applied to commercial stacks.

## The RFSoC itself

- AMD, *Zynq UltraScale+ RFSoC RF Data Converter LogiCORE IP Product Guide (PG269), v2.6*,  (2025). [link](https://docs.amd.com/r/en-US/pg269-rf-data-converter)  
  The RF data converter: tiles, NCOs, Nyquist zones, multi-tile sync.
- AMD, *Zynq UltraScale+ RFSoC Data Sheet: Overview (DS889), v1.14*,  (2023). [link](https://docs.amd.com/v/u/en-US/ds889-zynq-usp-rfsoc-overview)  
  Device generations and converter counts.
- Farley et al., *An All-Programmable 16-nm RFSoC for Digital-RF Communications*, IEEE Micro 38 (2018). [doi](https://doi.org/10.1109/MM.2018.022071136)  
  The RFSoC's architecture, peer reviewed.
- Liu et al., *Characterizing the performance of high-speed data converters for RFSoC-based radio astronomy receivers*, Monthly Notices of the Royal Astronomical Society 501 (2021). [arXiv:2011.05691](https://arxiv.org/abs/2011.05691) [doi](https://doi.org/10.1093/mnras/staa3895)  
  Independent measurements of RFSoC converters, from radio astronomy.

## Control, readout and feedback

Background for the comparison's dimensions.

- Krantz et al., *A quantum engineer's guide to superconducting qubits*, Applied Physics Reviews 6 (2019). [arXiv:1904.06560](https://arxiv.org/abs/1904.06560) [doi](https://doi.org/10.1063/1.5089550)  
  The standard reference for drive and readout signal chains.
- Blais et al., *Circuit quantum electrodynamics*, Reviews of Modern Physics 93 (2021). [arXiv:2005.12667](https://arxiv.org/abs/2005.12667) [doi](https://doi.org/10.1103/RevModPhys.93.025005)  
  The physics of dispersive readout.
- Bardin et al., *Microwaves in Quantum Computing*, IEEE Journal of Microwaves 1 (2021). [arXiv:2011.01480](https://arxiv.org/abs/2011.01480) [doi](https://doi.org/10.1109/JMW.2020.3034071)  
  Control electronics requirements, from an engineering view.
- Salath\'e et al., *Low-Latency Digital Signal Processing for Feedback and Feedforward in Quantum Computing and Communication*, Physical Review Applied 9 (2018). [arXiv:1709.01030](https://arxiv.org/abs/1709.01030) [doi](https://doi.org/10.1103/PhysRevApplied.9.034011)  
  Defines feedback latency (Eq. 1) and budgets it.
- Ryan et al., *Hardware for dynamic quantum computing*, Review of Scientific Instruments 88 (2017). [arXiv:1704.08314](https://arxiv.org/abs/1704.08314) [doi](https://doi.org/10.1063/1.5006525)  
  A pre-RFSoC architecture for dynamic circuits, with a latency budget by stage.
- Ella et al., *Quantum-classical processing and benchmarking at the pulse-level*, arXiv preprint (2023). [arXiv:2303.03816](https://arxiv.org/abs/2303.03816)  
  Timing categories for quantum-classical processing, and a latency definition at the converters.
- Kurman et al., *Benchmarking the Ability of a Controller to Execute Quantum Error Corrected Non-Clifford Circuits*, IEEE Transactions on Quantum Engineering 6 (2025). [arXiv:2311.07121](https://arxiv.org/abs/2311.07121) [doi](https://doi.org/10.1109/TQE.2025.3608053)  
  Benchmarking a controller on error-corrected non-Clifford circuits.
- Rist\`e et al., *Feedback Control of a Solid-State Qubit Using High-Fidelity Projective Measurement*, Physical Review Letters 109 (2012). [arXiv:1207.2944](https://arxiv.org/abs/1207.2944) [doi](https://doi.org/10.1103/PhysRevLett.109.240502)  
  Feedback reset of a superconducting qubit.
- Corcoles et al., *Exploiting Dynamic Quantum Circuits in a Quantum Algorithm with Superconducting Qubits*, Physical Review Letters 127 (2021). [arXiv:2102.01682](https://arxiv.org/abs/2102.01682) [doi](https://doi.org/10.1103/PhysRevLett.127.100501)  
  Dynamic circuits in an algorithm.
- Caune et al., *Demonstrating real-time and low-latency quantum error correction with superconducting qubits*, Nature Communications 17 (2026). [arXiv:2410.05202](https://arxiv.org/abs/2410.05202) [doi](https://doi.org/10.1038/s41467-026-73331-6)  
  Real-time decoding inside a control stack, with the response time defined.

## Pulse-level languages

- Cross et al., *OpenQASM 3: A Broader and Deeper Quantum Assembly Language*, ACM Transactions on Quantum Computing 3 (2022). [arXiv:2104.14722](https://arxiv.org/abs/2104.14722) [doi](https://doi.org/10.1145/3505636)  
  OpenQASM 3; QubiC has a front end for it.
- McKay et al., *Qiskit Backend Specifications for OpenQASM and OpenPulse Experiments*, arXiv preprint (2018). [arXiv:1809.03452](https://arxiv.org/abs/1809.03452)  
  OpenPulse, the pulse-level model behind OpenQASM 3's frames.
