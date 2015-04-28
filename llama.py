"""
LLAMA version 0.3  -unofficial, unreleased version-

Program employs the matplotlib module of Python to plot potential energy surfaces
and output publishable quality plots.

Authors:
    [a] Andrew Launder and Kevin Moore
        Center for Computational Quantum Chemistry (CCQC)
        Dept. of Chemistry, Univ. of Georgia, Athens, GA, United States
    [b] Victoria Lim
        Dept. of Chemistry, Belmont University, Nashville, TN, United States
"""

import plotfxn as plot
import input_proc as in_proc

# Call the series of functions which read the command line input and

in_proc.input_processor()
in_proc.section_finder()

# Call functions to run matplotlib and create pdf of potential energy surface plot.

plot.format_axes()
plot.generate_xcoords()
plot.plt_spec_lines()
plot.plt_connecting_lines()
plot.create_pdf()
#plot.print_outgoing_msg()



