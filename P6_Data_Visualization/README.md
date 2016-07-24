## P6. Data Visualization: Titanic Data Exploration

### Summary
The scatter chart shows the survival rates as per the age of the passengers. The next visualization compares the survival rates of those were travelling alone to those were not. The last one, is a stacked bar graph that compares the survival rates as per the class and sex of passengers.

### Design
I chose the Titanic dataset: giving passenger information aboard RMS Titanic. On April 15, 1912, during her maiden voyage, the Titanic sank after colliding with an iceberg, killing 1502 out of 2224 passengers and crew. 
One of the reasons that the shipwreck led to such loss of life was that there were not enough lifeboats for the passengers and crew. Although there was some element of luck involved in surviving the sinking, some groups of people were more likely to survive than others, such as women, children, and the upper-class. 
The dataset is explored for such patterns and the visualizations are plotted on demonstrate the findings. 

Patterns explored:

1. Survival rate variation as per age
2. Survival rate variation as per class
3. Survival rate variation as per sex
4. Survival rate variation considering whether the passenger was travelling alone or with company  (The code for the same can be found in /code file)

Findings from the explorations: 

1. From a total of 577 male passengers, only 109 i.e less than 20 percent survived. However, out of the total 314 female passengers, 233 i.e upto 74 percent of the female population aboard RMS Titanic survived. The survival rate of female passengers was much greater than that of male passengers.

2. A higher percentage of children made it through as compared to the adults.

3. 62.96 percent of the 1st class passengers survived whereas, the survival percentage amongst the third class passengers was only a third of this.

4. It is observed that the rate of survival is higher for the passengers travelling with family as compared to those travelling alone.

The preliminary visualization were plotted using Python (matplotlib) and Tableau. After data exploration, visualizations are drawn using dimple. The charts used are: Stacked bar chart, Standard bar chart as well as Scatter chart. The choice aws made after trying different variations. 

### Before feedback:
The html made before feedback can be found in: index_initial.html

### Feedback

The feedback was gathered as per Udacity guidelines:

#### #1

> The chart does not have headings and explanations as to the data it represents. Also, the findings from the chart are not stated. The visualization is very much to left, that does not look good.

#### #2

> It is given in easy to understand format. The charts are intuitive even though not named properly. With proper headings it would look better. The charts are boring and can use some more colors and somde text to give it a better feel. 

####  #3

> The charts are intuitive. Like from the forst it can be understood that the survival rate of children was kind of higher. But the visualizations in terms of looks can use some more animation to give it a story feel. 

#### #4
> I feel that the findings from the visualizations need to be highlighted. I need to know something about the dataset too. Somehow, without the information it all looks incomplete. Better color scheme can be used, like the dots in first as not visible properly. 

### After Feedback:
Certain changes are made:

- Headings and legends are added as required
- Findings from the chart 
- Result of the data exploration
- Central alignment of the charts and the text
- Red bubbles are used for the scatter plot


The html made before feedback can be found in: index_final.html


### Resources


- [Data Visualization course](https://www.udacity.com/course/viewer#!/c-ud507-nd)
- [Investigate a dataset exploration from P2](https://github.com/aashika/Investigate-a-dataset/blob/master/P2.%20Investigate%20a%20Dataset.ipynb)
- [Kaggle: Predict survival on the Titanic using Excel, Python, R & Random Forests](https://www.kaggle.com/c/titanic)
- [dimple.js Doc](http://dimplejs.org/)
