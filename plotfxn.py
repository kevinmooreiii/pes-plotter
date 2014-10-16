from __future__ import division
import numpy as np
from matplotlib import pyplot as plt
import pyparsing

def format_axes(y_top, y_bot, x_rgt, y_axis_label):
    """ Format the x- and y-axes. Default scaling factors defined in llama.py are used, unless user specifies a value in the input file. """
    print 'Formmatting the axes of the plot...\n\n'
    plt.axes(frameon=False)
    plt.axvline(0, y_bot, y_top, color='k')
    plt.tick_params(which='both', bottom='off', top='off', right='off', labelbottom='off')
    plt.xlim(0, x_rgt)
    plt.ylim(y_bot, y_top)
    plt.ylabel(y_axis_label)


def generate_xcoords(gr_count, sp_lin_len, sp_lin_spc, ex_rel):
    """ Generates a list of the coordinates for the left and right endpoints of each of the horizontal lines corresponding to a molecular species. """
    lft_endpt = []
    rgt_endpt = []
    for i in range(0, gr_count):
        lft_endpt.append(sp_lin_spc * i + 0.25)
        rgt_endpt.append(sp_lin_spc * i + 0.25 + sp_lin_len)

    for i in range(0, len(ex_rel)):
        lft_endpt.append(lft_endpt[ex_rel[i] - 1])
        rgt_endpt.append(rgt_endpt[ex_rel[i] - 1])

    return (lft_endpt, rgt_endpt)


def plt_spec_lines(spc_count, lft_connect, rgt_connect, lft_endpt, rgt_endpt, energy, sp_lin_clr, sp_lin_wid, en_shift, en_fsize, nm_shift, name, nm_fsize):
    """ Plot the lines that correspond to the molecular species. """
    print 'Plotting ground state species lines for surface...\n\n'
    for i in range(0, spc_count):
        plt.plot([lft_endpt[i], rgt_endpt[i]], [energy[i], energy[i]], color=sp_lin_clr, lw=sp_lin_wid, linestyle='-')
        plt.text((rgt_endpt[i] + lft_endpt[i]) / 2, energy[i] - en_shift, energy[i], horizontalalignment='center', fontsize=en_fsize)
        plt.text((rgt_endpt[i] + lft_endpt[i]) / 2, energy[i] + nm_shift, name[i], weight='bold', horizontalalignment='center', fontsize=nm_fsize)


def plt_connecting_lines(con_cnt, lft_connect, rgt_connect, lft_endpt, rgt_endpt, energy, cn_lin_clr, cn_lin_wid):
    """ Plot the lines that connect the species lines showing establishing a relationship of two molecular species in a reaction mechanism. """
    print 'Plotting connecting lines for surface...\n\n'
    for i in range(0, con_cnt):
        plt.plot([rgt_endpt[lft_connect[i] - 1], lft_endpt[rgt_connect[i] - 1]], [energy[lft_connect[i] - 1], energy[rgt_connect[i] - 1]], color=cn_lin_clr, lw=cn_lin_wid, linestyle='--')


def create_pdf(pdf_width, pdf_height, pdf_name, pdf_dpi):
    print 'Creating pdf of potential energy surface plot...\n\n'
    fig = plt.gcf()
    fig.set_size_inches(pdf_width, pdf_height)
    fig.savefig(pdf_name, dpi=pdf_dpi)

