Title: Test blog post
Date: 2014-01-04 22:00
Category: Pelican
Tags: pelican, python
Slug: first-post
Author: KeitaW
Summary: Test page 
Lang: en

# Title

- SyntaxHighlight Test 

python

    :::python
    import numpy as np
    import sys, os
    import datetime
    import subprocess
    from scipy import io
    from scipy.sparse import lil_matrix, coo_matrix
    scriptdir  = os.path.dirname(sys.argv[0])
    projectdir = os.path.dirname(scriptdir)
    sys.path.append(os.path.join(projectdir, "chaldea"))
    coprafile  = os.path.join(projectdir, "chaldea", "copra.sh")
    print("coprafile: ", coprafile)
    from OpticsAutomaticClustering import *

Math test
 
$$
\int_0^\infty \exp df
$$

Inline math $\int_0^\infty \exp{x} dx$ test.$e=mc^2$
thauthu $e=mc^2$ desu.

Slideshare embedding test

<iframe src="//www.slideshare.net/slideshow/embed_code/key/1GYa6eAoguN0SM" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/KeitaWatanabe8/journal-club-80676462" title="Journal Club" target="_blank">Journal Club</a> </strong> from <strong><a href="https://www.slideshare.net/KeitaWatanabe8" target="_blank">Keita Watanabe</a></strong> </div>

Gist embedding test

<script src="https://gist.github.com/KeitaW/50a9941a1d493352b18a5530c4587381.js"></script>


Notebook test
{% notebook test_notebook.ipynb %}
3
