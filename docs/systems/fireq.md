# FIREQ

FPGA Instrumentation for Readout and Qubit control, from Politecnico di Torino with INFN and
Milano-Bicocca. The newest system here (August 2026). It has no processor in the timing path: a
trigger table fires the generators.

| | |
|---|---|
| Group | Politecnico di Torino (VLSI nanocomputing), INFN, U. Milano-Bicocca |
| Board | ZCU216 (the docs also list the RFSoC 4x2; only a ZCU216 overlay is published) |
| Code | [FIREQ-Client](https://github.com/vlsi-nanocomputing/FIREQ-Client), [FIREQ-Server](https://github.com/vlsi-nanocomputing/FIREQ-Server) |
| Licence | AGPL-3.0 (client and server) |
| Docs | [fireq-docs.polito.it](https://fireq-docs.polito.it) |
| Latest release | 0.1.0, archived on Zenodo |

## Hardware and converters

DACs at 9.34 GS/s and ADCs at 2.33 GS/s with no interpolation or decimation; direct synthesis of
pulses up to 9.3 GHz, through AMD's XM655 balun card. The published build has two generation and
acquisition sets, enough for two qubits ([La Capra 2026](https://arxiv.org/abs/2608.29399),
abstract and firmware section).

## Real-time control

A trigger generator with up to 15 parallel triggers per event and 8096 entries, longest delay about
7.35 s. Events fall on a 1.7 ns grid; pulse durations resolve to 107 ps. 128-bit wave-definition
words, indexed through a queue, describe each pulse
([La Capra 2026](https://arxiv.org/abs/2608.29399), "Timing engine", Fig. 4).

## Signal generation and readout

An envelope table, linearly interpolated on the fly, times a DDS carrier; 16k IQ samples per
generator; virtual-Z phase updates; a crossbar routes pulses to DACs. Readout tones are summed for
frequency multiplexing. The acquisition block demodulates and returns either the raw stream or a
decimated, accumulated one ([La Capra 2026](https://arxiv.org/abs/2608.29399), Fig. 5 and
"Signal Acquisition").

## Feedback and multi-board

No conditional execution is described and no feedback latency reported. Multi-board operation is
listed as planned. On one board, multi-tile sync gives channel-to-channel skew of 1.8 ps mean,
0.84 ps standard deviation ([La Capra 2026](https://arxiv.org/abs/2608.29399), Table I, Fig. 8,
Sec. VI).

## Software

A PYNQ server on the ARM cores and a Python client talking MessagePack over TCP, with a tree-shaped
configuration. Software overhead falls from 26% of run time on the shortest sequences to about 1%
on long ones ([La Capra 2026](https://arxiv.org/abs/2608.29399), Fig. 3, Table VIII).

## Demonstrated with qubits

One superconducting qubit at Milano-Bicocca: resonator spectroscopy, punch-out, qubit
spectroscopy, Rabi, T1 = 6.94 µs, T2* = 13.50 µs
([La Capra 2026](https://arxiv.org/abs/2608.29399), Fig. 9, Table VII).

## Openness, in detail

Only the bitstream and its hardware handoff file are published (`FIREQ-Server/overlays/zcu216`).
The release file and the docs name a firmware repository, `vlsi-nanocomputing/FIREQ`, which
returned 404 on 2026-10-01.

## Worth knowing

The FIREQ paper itself compares eight frameworks (Table I) and reports post-route FPGA resources for
QICK, QubiC, RISC-Q and FIREQ built from their public repositories on the ZCU216 (Tables II and
III), the only such side-by-side measurement found.
