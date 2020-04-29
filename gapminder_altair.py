#%%
import altair as alt
import pandas as pd
from vega_datasets import data as vega_data

#%%
gap = pd.read_json(vega_data.gapminder.url)
gap.head(10)

#%%
gap.year.unique()

#%%
gap2005 = gap.loc[gap['year'] == 2005]

#%%
from IPython.display import display

#%%
def vegify(spec):
    display({
        'application/vnd.vegalite+json': spec.to_dict()
    }, raw=True)

#%%
# this does not work
# alt.renderers.enable('mimetype')

# opens in new browser windows
alt.renderers.enable('altair_viewer')

#%%
gap.year.unique()

# %%
gap2005 = gap.loc[gap['year'] == 2005]

# %%
alt.Chart(gap2005).mark_point().encode(
    alt.X('fertility'),
    alt.Y('life_expect')
)

# %%
alt.Chart(gap2005).mark_point().encode(
    x='fertility',
    y='life_expect'
)

# %%
alt.Chart(gap2005).mark_point().encode(
    alt.X('fertility', scale=alt.Scale(zero=False)),
    alt.Y('life_expect', scale=alt.Scale(zero=False))
)

# %%
alt.Chart(gap2005).mark_point().encode(
    alt.X('fertility', scale=alt.Scale(zero=False)),
    alt.Y('life_expect', scale=alt.Scale(zero=False)),
    alt.Size('pop')
)

# %%
alt.Chart(gap2005).mark_point(filled=True).encode(
    alt.X('fertility:Q', scale=alt.Scale(zero=False)),
    alt.Y('life_expect:Q', scale=alt.Scale(zero=False)),
    alt.Size('pop:Q'),
    alt.Color('cluster:N'),
    alt.OpacityValue(0.5)
)

# %%
alt.Chart(gap2005).mark_point(filled=True).encode(
    alt.X('fertility:Q', scale=alt.Scale(zero=False)),
    alt.Y('life_expect:Q', scale=alt.Scale(zero=False)),
    alt.Size('pop:Q'),
    alt.Color('cluster:N'),
    alt.OpacityValue(0.5),
    alt.Order('pop:Q', sort='descending'),
    tooltip = [alt.Tooltip('country:N'),
               alt.Tooltip('fertility:Q'),
               alt.Tooltip('life_expect:Q')
              ]
)

# %%
# to use arrow keys, click first the slider
select_year = alt.selection_single(
    name='select', fields=['year'], init={'year': 1955},
    bind=alt.binding_range(min=1955, max=2005, step=5)
)
alt.Chart(gap).mark_point(filled=True).encode(
    alt.X('fertility', scale=alt.Scale(domain=[1, 9])),
    alt.Y('life_expect', scale=alt.Scale(domain=[25, 90])),
    alt.Size('pop:Q'),
    alt.Color('cluster:N'),
    alt.Order('pop:Q', sort='descending'),

).add_selection(select_year).transform_filter(select_year)
