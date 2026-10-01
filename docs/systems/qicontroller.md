# QiController

The Quantum Interface Controller from KIT's Institute for Data Processing and Electronics. Each
qubit gets a "cell" with its own RISC-V sequencer, generators and recorder; a cell coordinator
synchronizes the cells and passes measurement results between them. Only the client software is
public.

| | |
|---|---|
| Group | KIT, Institute for Data Processing and Electronics (O. Sander's group); FZ Jülich on later papers |
| Boards | ZCU111 in the QiCells paper; the client also recognizes ZCU216, ZCU208 and others |
| Code | [qiclib](https://github.com/quantuminterface/qiclib), [cirque](https://github.com/quantuminterface/cirque), [crudo](https://github.com/quantuminterface/crudo) |
| Licence | GPL-3.0, client software only |
| Latest release | `qiclib` 3.0.0 on PyPI (2026-09-04) |

## Hardware and converters

In the QiCells paper, 8 DACs and 8 ADCs at 4 GS/s carry complex baseband, decimated or
interpolated to 1 GS/s in the fabric, with external IQ mixers and local oscillators. Up to 10
cells fit an XCZU28DR ([Gebauer 2023](https://doi.org/10.1145/3571820), Sec. 4, Table 1). Later
work describes mixerless and superheterodyne front ends and a multi-RFSoC ATCA system
([Ardila-Perez 2024](https://doi.org/10.1109/QCE60285.2024.10358)).

## Real-time control

One custom RISC-V sequencer per cell: 36 instructions, 32 registers, 4 ns steps in a single
250 MHz clock domain, 1024 instructions in block RAM. The cell coordinator provides barrier
synchronization. QiCode, a Python DSL, compiles to the sequencers
([Gebauer 2023](https://doi.org/10.1145/3571820), Secs. 4 to 7, Figs. 8, 9 and 12).

## Signal generation and readout

Per cell, two generators (control and readout), each with 4096 envelope samples, an NCO and a
complex multiplier; a pulse player for flux; a signal router for frequency multiplexing. The
recorder down-converts, integrates over a boxcar window, thresholds the state and returns it to
the sequencer through the coordinator ([Gebauer 2023](https://doi.org/10.1145/3571820), Secs. 5
and 6, Figs. 4, 5 and 11).

## Feedback

428 ns on the ZCU111 (125 MHz firmware, 500 MS/s), defined from the last readout sample entering
to the first sample of the conditioned pulse leaving, excluding cables and the readout itself; the
measurement method is not stated. Used for active reset of a fluxonium qubit to 99.4%
([Gebauer 2020](https://doi.org/10.1063/5.0011721)). The QiCells paper gives no new number.

## Multi-board

Future work in [Gebauer 2023](https://doi.org/10.1145/3571820); firmware for multi-board sync in
an ATCA system is described in [Ardila-Perez 2024](https://doi.org/10.1109/QCE60285.2024.10358),
without numbers in the abstract.

## Software

Yocto Linux on the ARM cores, a gRPC service hub, and a task runner on the real-time cores;
`qiclib` and QiCode on the host, with Qkit and Qiskit examples
([Gebauer 2023](https://doi.org/10.1145/3571820), Sec. 4; `qiclib/examples`).

## Demonstrated with qubits

Five transmons measured simultaneously: resonator spectroscopy and Ramsey
([Gebauer 2023](https://doi.org/10.1145/3571820), Figs. 13 to 15); fluxonium active reset
([Gebauer 2020](https://doi.org/10.1063/5.0011721)).

## Openness, in detail

The gateware is VHDL and closed ([Gebauer 2023](https://doi.org/10.1145/3571820), Sec. 4); the
`qiclib` README says development happens on an internal KIT GitLab. It is in this survey because
its client, its programming model and its architecture are public.
