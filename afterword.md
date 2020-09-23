# Afterword

This [Jupyter Book](https://jupyterbook.org) was created using 
- jupyter-book-0.8.1
- nbformat-5.0.7
- sphinx-togglebutton-0.2.2
- python-3.7.4

The Jupyter Notebooks that are the main source for this book come
from the [Callysto project](https://callysto.ca) and are stored in a
[Callysto Github repository](https://github.com/callysto/curriculum-notebooks). 

Some small changes were made to the notebooks in order to make them compatible with Jupyter Books.
In particular, we needed to fix the way code is hidden (using cell metadata) and be careful with
how the Geogebra and Javascript are loaded into the notebooks. You can read the code yourself to see what worked. 

The finished book is stored in a private repo in Callysto, using the ghp-import tool references in the Jupyter Book documentation.

September 19, 2020. 

Michael Lamoureux

Some technical notes for future work:

- the notebooks are fragile. When using IFrame, HTML, YouTube for IPython.display, it iteracts badly with %%html command like <iframe...> I don't know of a fix, so I avoid the IFRAME, HTML, YouTube python calls. (But they do often work.)
- it is useful to turn off execution in the _config.yml file, so that building the JBook does not re-run all your notebooks. It is faster to build the book, and less likely to introduce strage changes to individual notebooks.
- try to avoid html formatting commands in Markdown cells. They tend to get messed up in the Jupyter book.
- avoid Latex-strings in plot headers, and in widgets. Use only regular strings. The Jupyter book will otherwise mess up.
- when using double dollar signs for indicating display math, it is best to put the stuff in three lines, with blank spaces above and below. Like this
```

$$
some math formulas here
$$

```
- To use GeoGebra apps, best to save online in the GeoGebra site, then use the share command. Create a cell like this
```
%%html
<iframe scrolling="no" title="ParaEx2" src="https://www.geogebra.org/material/iframe/id/YFS3rJVz/width/700/height/400/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false" width="700px" height="400px" style="border:0px;"> </iframe>
```
- The Image() command does not work well for inserting sized images. Use Markdown format, or
```
<img style="float: left;" src="images/ParaStep1.png"  width="400">
```
- our Creators have several different methods of hiding code. We should choose one way, and be consistent. The cell metadata seems like a good way, can make it compatible with JupyterBooks method. 
- Javascript rarely works! But sometimes it does, which is cool. 
- To insert YouTube videos, copy the embed code from YouTube website. It looks like this:
```
%%html
<iframe width="560" height="315" src="https://www.youtube.com/embed/pLm07s8fnzM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```


