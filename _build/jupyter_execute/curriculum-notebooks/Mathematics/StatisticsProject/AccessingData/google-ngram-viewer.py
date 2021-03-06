![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/StatisticsProject/AccessingData/google-ngram-viewer.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Google Ngram Viewer

The [Google Books Ngram Viewer](https://books.google.com/ngrams) allows you to search for and visualize the frequency of terms in books.

The search terms and options are specified in lists, then the graph generated by the Ngram Viewer is embedded as an iFrame.

search_terms = ['Mars', 'Venus']
options = ['case_insensitive=on', 'year_start=1957', 'year_end=2008', 'corpus=15', 'smoothing=3']

content = '%2C'.join(search_terms)
options.insert(0, content)
parameters = '&'.join(options)
ngram_url_base = 'https://books.google.com/ngrams/interactive_chart?content='
ngram_url = ngram_url_base + parameters

print('Mentions of Mars or Venus in English Books Over Time')
from IPython.display import IFrame
IFrame(ngram_url, width=900, height=500)

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)