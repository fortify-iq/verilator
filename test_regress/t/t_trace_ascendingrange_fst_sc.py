#!/usr/bin/env python3
# DESCRIPTION: Verilator: Verilog Test driver/expect definition
#
# Copyright 2024 by Wilson Snyder. This program is free software; you can
# redistribute it and/or modify it under the terms of either the GNU
# Lesser General Public License Version 3 or the Perl Artistic License
# Version 2.0.
# SPDX-License-Identifier: LGPL-3.0-only OR Artistic-2.0

import vltest_bootstrap

test.scenarios('simulator')
test.top_filename = "t/t_trace_ascendingrange.v"

if not test.have_sc:
    test.skip("No SystemC installed")

# CI environment offers 2 VCPUs, 2 thread setting causes the following warning.
# %Warning-UNOPTTHREADS: Thread scheduler is unable to provide requested parallelism; consider asking for fewer threads.
# Strangely, asking for more threads makes it go away.
test.compile(verilator_flags2=['--sc --trace-fst --trace-params -Wno-ASCRANGE'],
             threads=(6 if test.vltmt else 1))

test.execute()

test.fst_identical(test.trace_filename, test.golden_filename)

test.passes()