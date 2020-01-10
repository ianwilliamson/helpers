from string import ascii_lowercase, ascii_uppercase

import matplotlib.pyplot as plt
from matplotlib import rcParams

label_str = {'lower': ascii_lowercase, 
             'upper': ascii_uppercase}

def apply_panel_labels(axs,
                       xy=[(-50, 0)], 
                       size='medium', 
                       weight='bold', 
                       case='lower',
                       ha='right', 
                       va='top', 
                       prefix='', 
                       postfix='', 
                       color=['k'], 
                       color_bg=None):
    """Applies panel labels (e.g. a, b, c, ... ) to matplotlib axes objects in order
    
    Most of the function arguments should be self-explanatory. Some are described in
    more detail below:
    axs               - List of the axis objects to label.
    xy                - Specifies the offset, in points, between the top left corner
                        of the axis and the label.
                        If len(xy) == 1, then the same offset is used for all panels.
                        Alternatively, len(xy) == len(axs), for control over the 
                        offset for each individual panel.
    ha, va            - Horizontal / vertical alignment of the label.
    prefix, postfix   - Text to include before / after the label, e.g. prefix='('
                        and postifx=')'.
    color             - Color of the label text. Same len characteristics as xy.
    """

    assert len(xy) == len(axs) or len(xy) == 1, "Either the lengths of `axs` and `xy` must match or `xy` must be of length 1"
    assert len(color) == len(axs) or len(color) == 1, "Either the lengths of `axs` and `color` must match or `color` must be of length 1"
    assert case in ['lower', 'upper'], "Case must be either 'lower' or 'upper'"

    if color_bg is not None:
        bbox_props = dict(boxstyle="round,pad=0.1", fc=color_bg, ec="none", alpha=0.9)
    else:
        bbox_props = None
    
    # If using latex we need to manually insert the \textbf command
    if rcParams['text.usetex'] and weight == 'bold':
        prefix  = '\\textbf{' + prefix
        postfix = postfix + '}'
    
    for n, ax in enumerate(axs):
        this_xy = xy[n] if len(xy) == len(axs) else xy[0]
        this_color = color[n] if len(color) == len(axs) else color[0]
        
        ax.annotate(prefix + label_str[case][n] + postfix,
                    xy=(0, 1),
                    xytext=this_xy,
                    xycoords='axes fraction',
                    textcoords='offset points',
                    size=size,
                    color=this_color,
                    weight=weight,
                    horizontalalignment=ha,
                    verticalalignment=va,
                    bbox=bbox_props)


def mpl_set_latex():
    """Turns on tex processing for matplotlib and sets a decent preamble.
    """
    rcParams['text.usetex'] = True
    rcParams['text.latex.preamble'] = [
        r"\usepackage{tgheros}",
        r"\usepackage{bm}", 
        r"\usepackage{sansmath}",
        r"\sansmath",
        r"\usepackage{siunitx}",
        r"\sisetup{detect-all}",
        r"\usepackage{amsmath}",
        r"\usepackage{amsfonts}",
        r"\usepackage{amssymb}",
        r"\usepackage{braket}",
        r"\renewcommand{\rmdefault}{\sfdefault}"
    ]


def mpl_unset_latex():
    """Turns off tex processing for matplotlib
    """
    rcParams['text.usetex'] = False
