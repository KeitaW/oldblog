Title: 最初のPelicanブログ
Date: 2014-01-04 22:00
Category: Pelican
Tags: pelican, python
Slug: first-post
Author: KeitaW
Summary: 記事の要約です。

# ペリカン記事のタイトル

- SyntaxHighlitだってバッチリ！

```python
#!/usr/bin/env python
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
```
