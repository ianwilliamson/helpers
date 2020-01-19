from string import ascii_lowercase, ascii_uppercase

import matplotlib.pyplot as plt
from matplotlib import rcParams

label_str = {'lower': ascii_lowercase, 
             'upper': ascii_uppercase}

def apply_panel_labels(axs,
                       xy=(-25, 0), 
                       size='medium', 
                       weight='bold', 
                       case='lower',
                       ha='right', 
                       va='top', 
                       prefix='', 
                       postfix='', 
                       color='k', 
                       bg_color=None,
                       bg_alpha=0.5):
    """Apply axis labels to a list of matplotlib axes objects (e.g. a, b, c, ...)
    Parameters:
    axs      - The list of matplotlib axis objects to label. Axes are labeled in the order
               that they are supplied.
    xy       - Tuple specififying the offset points, (xpts, ypts) between the top left corner
               of the axis and the label. This can also be a list of tuples to specify the 
               offset for each axis individually, in which case len(xy) == len(axs)
    size     - Font size of the labels, e.g. 9, 10, 'small, 'medium', etc.
    weight   - Font weight of the labels, e.g. 'normal', 'bold'
    case     - Case of the label characters, either 'upper' or 'lower'
    ha       - Horizontal alignment of the labels, defaults to 'right'
    va       - Vertical alignment of the labels, defaults to 'top'
    prefix   - Text to include before each label, e.g. prefix='('
    postfix  - Text to include after each label, e.g. postfix=')'
    color    - Color of the label text, defaults to 'black'. This can also be a list to specify
               the label color each axis individually, in which case len(color) == len(axs)
    bg_color - If specificed, draw a background box for the label with this color
    bg_alpha - Alpha transparency paramater for the background box, default is 0.5
    """

    if type(xy) is not list: xy = [xy]
    if type(color) is not list: color = [color]

    assert len(xy) == len(axs) or len(xy) == 1, 'The lengths of `axs` and `xy` must match or `xy` must be of length 1'
    assert len(color) == len(axs) or len(color) == 1, 'The lengths of `axs` and `color` must match or `color` must be of length 1'
    assert case in ['lower', 'upper'], '`case` must be either `lower` or `upper`'

    if bg_color is not None:
        bbox_props = dict(boxstyle='round', fc=bg_color, ec='none', alpha=bg_alpha)
    else:
        bbox_props = None
    
    # If using the latex backend we need to manually insert the \textbf command
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
