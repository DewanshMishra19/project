import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import offline, iplot
st.markdown
fig1 = px.box(
    x =df["budget"], 
    labels= {"x": "Budget"},
    title = "Detect Budget Outlier Using Box-Plot", template="plotly_dark"
)


fig1.update_layout(
    title = {"font": {
        "size" : 25,
        "family" :"tahoma"
        
    }
}
)
iplot(fig1)
rating = rating[0:6]
fig2 = px.bar(data_frame= rating, 
       x = rating.index, 
       y = rating / sum(rating) * 100,
       color=rating.index,
       color_discrete_sequence=["#FF0060", "#45FFCA", "#45FFCA", "#293462", "#FF55BB", "#293462"],
       labels = {"index": "Movie Rating", "y" : "Frequency PCT(%)"},
       title = "Movies Rating Popularity (PCT)",
       text = rating.apply(lambda x: f"{x / sum(rating) * 100: 0.2f}%"),
       template = "plotly_dark",
      )


update_layout(hover_bgcolor="#111")


fig2.update_traces(
    textfont = {
        "family": "tahoma",
         "size": 13,
    },
    hovertemplate= "Rating: %{label}<br>Popularity: %{value:0.2f}%"
)
iplot(fig2)

genre = genre.nlargest(10)[::-1]
fig3 = px.bar(data_frame= genre, 
             orientation = "h",
       x = genre / sum(genre) * 100,
             
       y = genre.index, 
       color_discrete_sequence=["#45FFCA"],
       labels = {"index": "Movie Genre", "x" : "Frequency PCT(%)"},
       title = "Top 10 Movies Genre & Popularity(PCT)",
       text = genre.apply(lambda x: f"{x / sum(genre) * 100: 0.2f}%"),
       template = "plotly_dark",
      )

fig3.update_traces(
    textfont = {
        "family": "tahoma",
         "size": 13,
    },
    hovertemplate= "Rating: %{label}<br>Popularity: %{value:0.2f}%"
)

update_layout()

iplot(fig3)


fig4 = px.area(year, 
        x = year.index, 
        y =year, 
        labels = {"index" :"Year", "y" :"Movie Counts"},
        line_shape="spline", 
        color_discrete_sequence=["#45FFCA"],
        title = "Number of Movies Through Years",
        template="plotly_dark",
       )


update_layout()
iplot(fig4)

fig5 = px.histogram(df["score"], 
                   template = "plotly_dark",
                   color_discrete_sequence=["#45FFCA"],
                   labels={"value" :"Score", "count" :"Frequency"},
                   title = "The Distribution of Scores",
                  )

## ► Adding The Mean Line To The Histogram
fig5.add_shape(type='line',
              x0=df["score"].mean(),
              y0=0,
              x1=df["score"].mean(),
              y1=df["score"].value_counts().max()+25,
              line = {
                  "color" :"#FF0060",
                  "width" : 2,
                  "dash" : "dashdot"
              },
              label={
                  "text" : f"Mean: {df['score'].mean(): 0.1f}\t",
                  "textposition": "end",
                  "yanchor" :"top",
                  "xanchor" :"right",
                  "textangle" :0,
                  "font": {
                      "size": 14,
                      "color" :"#FF0060",
                      "family" : "tahoma"
                      
                  },
              }
             )

## ► Adding The Median Line To The Histogram
fig5.add_shape(type='line',
              x0=df["score"].median(),
              y0=0,
              x1=df["score"].median(),
              y1=df["score"].value_counts().max()+25,
              line = {
                  "color" :"violet",
                  "width" : 2,
                  "dash" : "dashdot"
              },
              label={
                  "text" :f"Median: {df['score'].median(): 0.1f}",
                  "textposition": "end",
                  "yanchor" :"top",
                  "xanchor" :"left",
                  "textangle" :0,
                  "font": {
                      "size": 14,
                      "color" :"violet",
                      "family" : "tahoma"
                      
                  },
              }
             )

update_layout()

iplot(fig5)

director = director.nlargest(5)
fig6 = px.bar(data_frame= director, 
       x = director.index, 
       y = director,

       color_discrete_sequence=["#45FFCA"],
       labels = {"index": "Director", "y" : "Number Of Movies"},
       title = "Top 5 Directors By Number of Movies 🎥",
       text_auto= True,
       template = "plotly_dark",
      )


update_layout()


fig6.update_traces(
    textfont = {
        "family": "tahoma",
         "size": 16,
    },
    hovertemplate= "Director: %{label}<br>No. Movies: %{value}"
)
iplot(fig6)


movie_star = movie_star.nlargest(10)[::-1]
fig7 = px.bar(data_frame= movie_star, 
             orientation = "h", 
       y = movie_star.index, 
       x = movie_star,

       color_discrete_sequence=["#45FFCA"],
       labels = {"index": "Director", "y" : "Number Of Movies"},
       title = "Top 10 Movie Start By Number of Movies✨",
       text_auto= True,
       template = "plotly_dark",
      )


update_layout()


fig7.update_traces(
    textfont = {
        "family": "tahoma",
         "size": 16,
    },
    hovertemplate= "Movie Star: %{label}<br>No. Movies: %{value}"
)
iplot(fig7)

country = country.nlargest(5)[::-1]
fig8 = px.bar(data_frame= country, 
             orientation = "h", 
       y = country.index, 
       x = country,

       color_discrete_sequence=["#45FFCA"],
       labels = {"index": "Director", "y" : "Number Of Movies"},
       title = "Top 5 Country By Released Movies",
       text_auto= ".2s",
       template = "plotly_dark",
      )


update_layout()


fig8.update_traces(
    textposition = "outside",
    textfont = {
        "family": "tahoma",
         "size": 13,
    },
    hovertemplate= "Country: %{label}<br>No. Movies: %{value}"
)
iplot(fig8)


fig9 = px.scatter(top_rated_movie[::-1],  
                 y = "name", 
                 x = "score", 
                 size = "score",
                 color = "score",
                 template = "plotly_dark",
                 labels={"name" :"Movie Name", "score" :"Rate"},
                 opacity = 0.89,
                title = "Top-Rated Movies",
                color_continuous_scale=['#A084E8', '#8BE8E5', '#00FFAB'])


update_layout(hover_bgcolor="#222", hover_font_size=14)

fig9.update_traces(
    textfont = {
        "family": "tahoma",
         "size": 13,
    },
    hovertemplate= "Movie: %{y}<br>Rate: %{x}"
)
iplot(fig9)



fig10 = px.area(gross_per_year, 
            x = gross_per_year.index, 
            y =gross_per_year, 
            labels = {"index" :"Year", "y" :"Movie Counts"},
            line_shape="spline", 
            color_discrete_sequence=["#45FFCA"],
            title = "AVG Gross Through Years ⌛",
            template="plotly_dark",
              markers="O",
              
       )


update_layout()

fig10.update_traces(
    textfont = {
        "family": "tahoma",
         "size": 13,
    },
    hovertemplate= "Year: %{x}<br>AVG Gross: %{y:0.2s}"
)
iplot(fig10)


fig11 = px.bar(
    data_frame= gross_via_comapny[::-1], 
    orientation = "h", 
    y = gross_via_comapny[::-1].index, 
    x = gross_via_comapny[::-1],
    color = gross_via_comapny[::-1],

    labels = {"x": "AVG Gross Revenu", "y" : "Movies Company"},
    title = "Top 10 Comapny By Average Gross Revenu",
    text_auto= ".2s",
    template = "plotly_dark",
     color_continuous_scale=['#A084E8', '#00FFAB', '#00FFAB']
      )

update_layout(hover_bgcolor="#222", hover_font_size=14)

fig11.update_traces(
    textposition = "outside",
    textfont = {
        "family": "tahoma",
         "size": 13,
    },
    hovertemplate= "Movie Company: %{y}<br>AVG Gross Revnue: %{x:0.3s}"
)
iplot(fig11)



fig12 = px.bar(year_vs_genre,  
                 x = "year", 
                 y = "count", 
                 color = "genre",
                 template = "plotly_dark",
                 color_discrete_sequence=["#45FFCA","#FF0060","#FF55BB", "#FFFDAF"],
                 labels={"year" :"Released Year", "count" :"Counts", "genre" :"Genre"},
                 opacity = 0.89,
                title = "Top 3 Genres for Each Year From 2015:2019 📆")


update_layout(showlegend=True, hover_bgcolor="#222", hover_font_size=14)

fig12.update_traces(
    textfont = {
        "family": "tahoma",
         "size": 13,
    },
    hovertemplate= "Year: %{x}<br>Frequency: %{y}"
)
iplot(fig12)


# Create The Plotly Heat Map
fig13 = px.imshow(
    df_corr.corr(numeric_only = True), 
    text_auto="0.2f", aspect="auto", template="plotly_dark",
    title="Correlation That Influence the Gross Revenue",
    color_continuous_scale = "earth"
) 

update_layout(showlegend=True, hover_bgcolor="#222", hover_font_size=15)

fig13.update_traces(
    textfont = {
        "family": "tahoma",
         "size": 16,
    },
    hovertemplate= "Feature[1]: %{x}<br>Feature[2]: %{y}"
)
iplot(fig13)



fig14 = px.scatter(
    df, 
    x = df["budget"], 
    y = df["gross"], 
    trendline="ols",
    template="plotly_dark",
    color = df["gross"],
    color_discrete_sequence=["#45FFCA"],
    title = "Relation Between Budget & Gross Revnue",
    labels={"gross" :"Gross Revenue", "budget" :"Budget"},

                 
          )

update_layout(showlegend=True, hover_bgcolor="#222", hover_font_size=15)
fig14.update_traces(
    textfont = {
        "family": "tahoma",
         "size": 16,
    },
    hovertemplate= "Budget: %{x:0.3s}<br>Gross Revenue: %{y:0.3s}"
)
iplot(fig14)


fig15 = px.scatter(
    df, 
    x = df["votes"], 
    y = df["gross"], 
    trendline="ols",
    template="plotly_dark",
    color = df["gross"],
    color_discrete_sequence=["#45FFCA"],
    title = "Relation Between Votes & Gross Revenue",
    labels={"gross" :"Gross Revenue", "budget" :"Budget"}
                 
          )

update_layout(showlegend=True, hover_bgcolor="#222", hover_font_size=15)
fig15.update_traces(
    textfont = {
        "family": "tahoma",
         "size": 16,
    },
    hovertemplate= "Votes: %{x:0.4s}<br>Gross Revenue: %{y:0.4s}"
)
iplot(fig15)


