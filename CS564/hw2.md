## Homework Overview

*"Visualization gives you answers to questions you didn't know you have" - Ben Schneiderman*

 

This homework focuses on exploring and creating data visualizations using two of the most popular tools in the field. Data visualization is an integral part of exploratory analysis and communicating key insights. All questions use data on the same topic to highlight the uses and strengths of different types of visualizations. The data comes from [BoardGameGeek ](https://boardgamegeek.com/)and includes games' ratings, popularity, and metadata.

 

Below are some terms you will often see in the questions:

·    **Rating** – a value from 0 to 10 given to each game. *BoardGameGeek* calculates a game's overall rating in different ways including **Average** and **Bayes**, so make sure you are using the correct rating called for in a question. A higher rating is better than a lower rating.

·    **Rank** – the overall rank of a boardgame from 1 to *n,* with ranks closer to 1 being better and *n* being the total number of games. The rank may be for all games or for a subgroup of games such as abstract games or family games.

## Q1 [25 points] Designing a good table. Visualizing data with Tableau.

 

| Goal         | Design a table, a grouped bar chart, and a stacked bar chart with  filters in Tableau. |
| ------------ | ------------------------------------------------------------ |
| Technology   | Tableau Desktop                                              |
| Deliverables | **Gradescope:** After selecting HW2 - Q1, click **Submit Images**. You will be taken to a list  of questions for your assignment. Click **Select Images** and submit the following four PNG images  under the corresponding questions:  ●         **table.png**: Image/screenshot of the table  in Q1.a  ●         **grouped_barchart.png**: Image of the chart in Q1.b  ●         **stacked_barchart_1.png**: Image of the chart  in Q1.c after  filtering data for Max.Players = 2  ●         **stacked_barchart_2.png**: Image of the chart  in Q1.c after  filtering data for Max.Players = 4  **Q1 will  be manually graded  after the grace  period.** |

### Setting Up Tableau

Install and activate Tableau Desktop by following “HW2 Instructions” on Canvas. The product activation key is for your use in this course only. **Do not share the key with anyone.** If you already have Tableau Desktop installed on your machine, you may use this key to reactivate it.

If you do not have access to a Mac or Windows machine, use the 14-day trial version of *Tableau Online*:

1. Visi[t ](https://www.tableau.com/trial/tableau-online)https://www.tableau.com/trial/tableau-online
2. Enter your information (name, email, GT details, etc.)
3. You will then receive an email to access your Tableau Online site
4. Go to your site and create a workbook

If neither of the above methods work, use [Tableau for Students](https://www.tableau.com/academic/students)**.** Follow the link and select "Get Tableau For Free". You should be able to receive an activation key which offers you a one-year use of Tableau Desktop at no cost by providing a valid Georgia Tech email.

 

### Connecting to Data

1. It is optional to use Tableau for Q1a. Otherwise, complete all parts using **a single Tableau workbook**.
2. Q1 will require connecting Tableau to two different data sources. You can connect to multiple data sources within one workbook by following the [directions here](https://kb.tableau.com/articles/howto/connecting-multiple-data-sources-without-joining-or-blending).
3. For Q1a and Q1b:

a.   Open Tableau and connect to a data source. Choose To a File – **Text file**. Select the ***popular_board_game.csv\*** file from the skeleton.

b.   Click on the graph area at the bottom section next to "Data Source" to [create worksheets](https://help.tableau.com/current/pro/desktop/en-us/environ_workbooksandsheets.htm).

4. For Q1c:

a.   You will need a *data.world* account to access the data for Q1c. Add a new data source by clicking on Data – **New Data Source**.

*b.*   When connecting to a data source, choose To a Server – **Web Data Connector***.*

c.   Enter [this URL ](https://tableau.data.world/?dataset_name=mjpetrey%2Fboardgamegeek&query=SELECT * FROM games_detailed_info_filtered&queryType=SQL)to connect to the [data.world data set on board games](https://data.world/mjpetrey/boardgamegeek). You may be prompted to log in to *data-world* and authorize Tableau. Do not edit the provided SQL query.

**NOTE:** If you cannot connect to *data-world*, you can use the provided csv files for Q1 in the skeleton. The provided csv files are identical to those hosted online and can be loaded directly into Tableau.

d.   Click the graph area at the bottom section to create another worksheet, and Tableau will automatically create a data extract.



### Table and Chart Design

a. **[5 points] Good table design.** Visualize the data contained in *popular_board_game.csv a*s a data table. In this part (Q1a), you can use any tool (e.g., Excel, HTML, Pandas, Tableau) to create the table.

We are interested in grouping popular games into "support solo" (min player = 1) and

"not support solo" (min player > 1). Your table should clearly communicate information about these two groups simultaneously. For each group (Solo Supported, Solo Not Supported), show:

1. Total number of games in each category (fighting, economic, ...)
2. The most representative game (game with the highest number of ratings) in each category. If more than one game has the same maximum number of rating, pick the game you prefer. **NOTE:** [Level of](https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_lod.htm) [Detail expressions ](https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_lod.htm)may be useful if you use Tableau.
3. Average rating of games in each category (use simple average), rounded to 2 decimal places.
4. Average playtime of games in each category, rounded to 2 decimal places.
5. In the bottom left corner below your table, include your GT username (In Tableau, this can be done by including a caption when exporting an image of a worksheet or by adding a text box to a dashboard. If you use Tableau, refer to the tutorial [here](https://youtu.be/fRwQenvBJ6I)).
6. Save the table as **table.png**. (If you use Tableau, go to Worksheet/Dashboard à Export à Image). **NOTE****:** Do not take screenshots in Tableau since your image must have high resolution. You can take a screenshot If you use HTML, Pandas, etc.

![img](file:///C:/Users/32534/AppData/Local/Temp/msohtmlclip1/01/clip_image001.gif)Your learning goal here is to practice good table design, which is not strongly dependent on the tool that you use. Thus, we do not require that you use Tableau in this part. You may decide the most meaningful column names, the number of columns, and the column order. You are not limited to only the techniques described in the lecture. For OMS students, the lecture video on this topic is *Week 4 - Fixing Common Visualization Issues - Fixing Bar Charts, Line Charts*. For campus students, review [lecture slides 43 and 44](https://poloclub.github.io/cse6242-2022fall-campus/slides/CSE6242-510-VisFix.pdf).

 

 

 

b.  **[10 points] Grouped bar chart.** Visualize *popular_board_game.csv* as a grouped bar chart in Tableau. Your chart should display game category (e.g., fighting, economic,...) along the horizontal axis and game count along the vertical axis. Show game playtime (e.g., <=30, (30, 60]) for each category. **NOTE:** Do not differentiate between “support solo” and “non-support solo” for this question.

1. Design a vertically grouped bar chart. For each category, show the game count for each playtime.
2. Include clearly labeled axes, a clear chart title, and a legend.
3. In the bottom left corner of your image, include your GT username. **NOTE:** In Tableau, this can be done by including a caption when exporting an image of a worksheet or by adding a text box to a dashboard. Refer to the tutorial [here](https://www.youtube.com/watch?v=fRwQenvBJ6I&feature=youtu.be).
4. **Save the chart as grouped_barchart.png (**go to Worksheet/Dashboard à Export à Image.

**NOTE****:** Do not take screenshots in Tableau since your image must have high resolution.

The main goal here is for you to get familiarized with Tableau. Thus, we kept this open-ended, so you can practice making design decisions. **We will accept most designs.** We show one possible design in Figure 1b, based on the tutorial from [Tableau](https://kb.tableau.com/articles/howto/stacked-bar-chart-multiple-measures).



![img](file:///C:/Users/32534/AppData/Local/Temp/msohtmlclip1/01/clip_image003.jpg)

**Figure 1b:** Example of a grouped bar chart. Your chart may appear different and can earn full credit if it meets all the stated requirements. Your submitted image should include your GT username in the bottom left.

 

 

 

c.  **[10 points] Stacked bar chart.** Visualize the *data.world* dataset (or *games_detailed_info_filtered.csv* if using the local files in the skeleton) as a stacked bar chart. Showcase the count of games in different categories and the relationship between game categories, their mechanics, and max player size.

1. Create a **Worksheet** with a stacked bar chart that shows game counts for each playing mechanic (sub-bars) for each game category. **NOTE:** This data contains duplicate rows, as each row represents a distinct game. Do not remove duplicate rows from the data.
2. Display game counts along the vertical axis and category along the horizontal axis.
3. Include clear axes labels, a clear chart title, and a legend.
4. Create a ***Dashboard\*** using the worksheet you created in Step 1.
5. Add a filter for number of 'Max.Players' allowed in each game. Update the chart using this filter to generate the following chart images (Refer to the tutorial [here ](https://kb.tableau.com/articles/howto/adding-filters-to-dashboards)on how to add a filter in a dashboard. Make sure to add 'Max.Players' in the filter shelf in the Worksheet first, like [this](https://help.tableau.com/current/pro/desktop/en-us/filtering.htm#drag-dimensions-measures-and-date-fields-to-the-filters-shelf)):

a.   Select "2 Players" only in the filter. Save the resulting chart as '**stacked_barchart_1.png**'

b.   Select "4 Players" only in the filter. Save the resulting chart as '**stacked_barchart_2.png**'

c.   Both images must include your GT username in the bottom left. This can be added using a text box. Refer to the tutorial [here](https://www.youtube.com/watch?v=fRwQenvBJ6I&feature=youtu.be)[.https://youtu.be/fRwQenvBJ6I](https://youtu.be/fRwQenvBJ6I)

d.   In each image, the filter must be visible. If you are using Tableau Online, you may need to add your worksheet containing the chart to a dashboard and then download an image of the dashboard that contains both the filter and the chart.

**Note:** To save a dashboard image, go to Dashboard - Export Image. Do not submit screenshots.



![img](file:///C:/Users/32534/AppData/Local/Temp/msohtmlclip1/01/clip_image005.jpg)

 

**Figure 1c**: Example of a stacked bar chart after selecting "4 Players" in Max.Players filter. Your chart may appear different and can earn full credit if it meets all the stated requirements. Your submitted image should include your GT username in the bottom left.

 

**Optional Reading:** The effectiveness of stacked bar charts is often debated—sometimes, [they can be confusing,](https://www.smashingmagazine.com/2017/03/understanding-stacked-bar-charts/) [difficult to understand, and may make data series comparisons challenging](https://www.smashingmagazine.com/2017/03/understanding-stacked-bar-charts/).



# Important Points about Developing with D3 in Questions 2–5

**1.**   We highly recommend that you use the latest Chrome browser to complete this question. We will grade your work using Chrome v92 (or higher)**.**

2. You will work with **version 5** of D3 in this homework. You must **NOT** use any D3 libraries (d3*.js) other than the ones provided in the **lib** folder.
3. For Q3–5, your D3 visualization **MUST** produce a [DOM structure ](https://en.wikipedia.org/wiki/Document_Object_Model)as specified at the end of each question. Not only does the structure help guide your D3 code design, but it also enables your code to be auto-graded (the auto-grader identifies and evaluates relevant elements in the rendered HTML). We highly recommend you review the specified DOM structure **before** starting to code.
4. ![img](file:///C:/Users/32534/AppData/Local/Temp/msohtmlclip1/01/clip_image006.gif)![img](file:///C:/Users/32534/AppData/Local/Temp/msohtmlclip1/01/clip_image007.gif)**You need to setup a local HTTP server in the root (hw2-skeleton) folder to run your D3 visualizations**, as discussed in the D3 lecture (OMS students: the video "Week 5 - Data Visualization for the Web (D3) - Prerequisites: JavaScript and SVG". Campus students: see [lecture PDF](https://poloclub.github.io/cse6242-2021fall-campus/slides/CSE6242-520-d3-stolper.pdf).). The easiest way is to use [http.server ](https://medium.com/@ryanblunden/create-a-http-server-with-one-command-thanks-to-python-29fcfdcd240e)for Python 3.x. (for more details, see [link](https://medium.com/@ryanblunden/create-a-http-server-with-one-command-thanks-to-python-29fcfdcd240e)).
5. **All d3\*.js files in the lib folder must be referenced using relative paths**, e.g., **"../lib/<filename>**" in your html files. For example, if the file "Q2/submission.html" uses d3, its header should contain:

##### <script type="text/javascript" src="../lib/d3.v5.min.js"></script> It is incorrect to use an absolute path such as:

<script type="text/javascript" src="C:/Users/polo/hw2-skeleton/lib/d3.v5.min.js"></script>

6. For questions that require reading from a dataset, use a **relative path** to read in the dataset file**.** For example, suppose a question reads data from earthquake.csv, the path should simply be "earthquake.csv" and **NOT** an absolute path such as "C:/Users/polo/hw2-skeleton/Q/earthquake.csv".
7. You can and are encouraged to decouple the style, functionality and markup in the code for each question. That is, you can use separate files for CSS, JavaScript and html.



## Q2 [15 points] Force-directed graph layout

 

| Goal              | Create a network graph shows relationships between games  in D3. Use interactive features like pinning nodes  to give the  viewer some control over the visualization. |
| ----------------- | ------------------------------------------------------------ |
| Technology        | D3 Version 5 (included in the lib  folder)  Chrome v92.0 (or higher): the browser for grading your code Python http server (for  local testing) |
| Allowed Libraries | D3  library is provided to you in the **lib** folder. You must **NOT** use any D3 libraries  (d3*.js) other than the ones provided. On Gradescope, these  libraries are provided for you in  the auto-grading  environment. |
| Deliverables      | [Gradescope] Q2**.(html/js/css)**: The HTML,  JavaScript, CSS to render the  graph. Do not include the D3 libraries or board_games.csv  dataset. |

You will experiment with many aspects of D3 for graph visualization. To help you get started, we have provided the Q2.html file (in the Q2 folder) and an undirected graph dataset of boardgames, board_games.csv file (in the Q2 folder). The dataset for this question was inspired by [a reddit post ](https://www.reddit.com/r/boardgames/comments/9aphuw/a_network_visualization_of_the_board_game/)about visualizing boardgames as a network, where the author calculates the similarity between board games based on categories and game mechanics where the edge value between each board game (node) is the total weighted similarity index. This dataset has been modified and simplified for this question and does not fully represent actual data found from the post. The provided Q2.html file will display a graph (network) in a web browser. The goal of this question is for you to experiment with the visual styling of this graph to make a more meaningful representation of the data. [Here ](https://www.oreilly.com/library/view/interactive-data-visualization/9781491921296/ch13.html)is a helpful resource (about graph layout) for this question.

 

**Note:** You can submit a single Q2.html that contains all the css and js components; or you can split Q2.html into Q2.html, Q2.css, and Q2.js.

 

a. **[2 points] Adding node labels**: Modify Q2.html to show the node label (the node name, e.g., the source) at the **top right** of each node in **bold**. If a node is dragged, its label must move with it.

 

b. **[3 points] Styling edges**: Style the edges based on the "value" field in the links array:

·    If the value of the edge is equal to 0 (similar), the edge should be gray, thick, and **solid** (The dashed line with zero gap is not considered as solid).

·    If the value of the edge is equal to 1 (not similar), the edge should be green, thin, and **dashed**.

 

##### c. [3 points] Scaling nodes:

 

1. **[1.5 points]** Scale the radius of each node in the graph based on the degree of the node (you may try linear or squared scale, but you are not limited to these choices).

 

**Note:** Regardless of which scale you decide to use, you should avoid extreme node sizes, which will likely lead to low-quality visualization (e.g., nodes that are mere points, barely visible, or of huge sizes with overlaps).

 

**Note:** D3 v5 does not support d.weight (which was the typical approach to obtain node degree in D3 v3). You may need to calculate node degrees yourself. Example relevant approach is [here](https://stackoverflow.com/questions/43906686/d3-node-radius-depends-on-number-of-links-weight-property).

 

2. **[1.5 points]** The degree of each node should be represented by varying colors. Pick a meaningful color scheme (hint: color gradients). There should be at least 3 color gradations and it must be visually evident that the nodes with a higher degree use darker/deeper colors and the nodes with lower degrees use lighter colors. You can find example color gradients at [Color Brewer](http://colorbrewer2.org/).



##### d. [6 points] Pinning nodes:

1. **[2 points]** Modify the code so that dragging a node will fix (i.e., "pin") the node's position such that it will not be modified by the graph layout algorithm (**Note**: pinned nodes can be further dragged around by the user. Additionally, pinning a node should not affect the free movement of the other nodes). Node pinning is an effective interaction technique to help users spatially organize nodes during graph exploration. The D3 API for pinning nodes has evolved over time. We recommend reading [this post](https://stackoverflow.com/questions/10392505/fix-node-position-in-d3-force-directed-layout) when you work on this sub-question.
2. **[1 points]** Mark pinned nodes to visually distinguish them from unpinned nodes, i.e., show pinned nodes in a different color.
3. **[3 points]** Double clicking a pinned node should unpin (unfreeze) its position and unmark it. When a node is no longer pinned, it should move freely again.

 

##### IMPORTANT:

1. For part 1 to consistently pass the autograder (which tests that a dragged node becomes pinned and retains its position), you may need to increase the radius of the highly-weighted nodes and reduce their label sizes, so that the nodes can be more easily detected by the autograder's webdriver mouse cursor.
2. To avoid timeout errors on Gradescope, complete the double click function in part 3 before submitting.
3. If you receive timeout messages for all parts and your code works locally on your computer, verify that you are indeed using the appropriate ids provided in the "add the nodes" section in the skeleton code.
4. D3 v5 does not support the d.fixed method (it was deprecated after D3 v3). For our purposes, it is used as a Boolean value to indicate whether a node has been pinned or not.

 

e.   

|      |                                                              |
| ---- | ------------------------------------------------------------ |
|      | ![img](file:///C:/Users/32534/AppData/Local/Temp/msohtmlclip1/01/clip_image009.jpg) |

**[1 points] Add GT username:** Add your Georgia Tech username (usually includes a mix of letters and numbers, e.g., gburdell3) to the top right corner of the force-directed graph (see example image). The GT username must be a <text> element having the id: "credit"



 

**Figure 2a:** Example of Visualization with pinned node (yellow). Your chart may appear different, and can earn full credit if it meets all the stated requirements.



## Q3 [15 points] Line Charts

 

| Goal              | Explore temporal patterns  in the *BoardGameGeek* data using line charts  in D3 to  compare how the number of  ratings grew. Integrate additional data about board game rankings onto these  line charts and explore the effect of axis scale  choice. |
| ----------------- | ------------------------------------------------------------ |
| Technology        | D3  Version 5 (included in the lib  folder)  Chrome v92.0 (or higher): the browser for grading your code Python http server (for  local testing) |
| Allowed Libraries | D3  library is provided to you in the **lib** folder. You must **NOT** use any D3 libraries  (d3*.js) other than the ones provided. On Gradescope, these  libraries are provided for you in  the auto-grading  environment. |
| Deliverables      | [Gradescope] **Q3.(html / js / css)**: The HTML,  JavaScript, CSS to render the line  charts. Do not include the D3 libraries or boardgame_ratings.csv dataset. |

Use the dataset provided in the file *boardgame_ratings.csv* (in the Q3 folder) to create line charts. Refer to the tutorial for line chart [here ](https://bl.ocks.org/gordlea/27370d1eea8464b04538e6d8ced39e89)or [here](https://datawanderings.com/2019/11/01/tutorial-making-an-interactive-line-chart-in-d3-js-v-5/).

**Note:** You will create four charts in this question, which should be placed one after the other **on a single HTML page**, similar to the example image below (Figure 3). Note that your design need NOT be identical to the example; however, the submission must follow the DOM structure specified at the end of this question.

 

**IMPORTANT:** use the [Margin Convention ](https://observablehq.com/d/78de05f1b179dfa5)guide for specifying chart dimensions and layout. The autograder will assume this convention has been followed for grading purposes.

 

**a.** **[5 points] Creating line chart.** Create a line chart (Figure 3a) that visualizes the number of board game ratings from November 2016 to August 2020 (inclusively), for the eight board games: ['Catan', 'Dominion', 'Codenames', 'Terraforming Mars', 'Gloomhaven', 'Magic: The Gathering', 'Dixit', 'Monopoly']. Use [d3.schemeCategory10](https://bl.ocks.org/ericd9799/d7534b92d9c30edf4726aadd49cffabe)() to differentiate these board games. Add each board game's name next to its corresponding line. For the x-axis, show a tick label for every three months. Use D3 [axis.tickFormat() ](https://github.com/d3/d3-scale#tickFormat)and [d3.timeFormat() ](https://github.com/d3/d3-time-format)to format the ticks to display abbreviated months and years. For example, Jan 17, Apr 17, Jul 17. (See Figure 3a and its x-axis ticks).

 

●       Chart title: Number of Ratings 2016-2020

●       Horizontal axis label: Month. Use [D3.scaleTime()](https://github.com/d3/d3-scale#scaleTime).

●       Vertical axis label: Num of Ratings. Use a linear scale (for this part a).

 

**VERY IMPORTANT — Beware of “Silent Date Conversion":** Opening the csv file in an application like Excel may silently modify date strings without warning you, e.g., converting hyphen-separated date strings (e.g., 2016-11-01) into slash-separated date strings (e.g., 11/01/16). Impacted students would see a “correct” line chart visualization on their local computers, but when they upload their code to Gradescope, test cases will fail (e.g., tick labels are not found, lines are not drawn) because the x-scale cannot be computed (as the dates are parsed as NaN). **To view the content of a csv file, we recommend you only use text editors (e.g., sublime text, notepad) that do not silently modify csv files.**

 

 

**b.** **[5 points] Adding board game rankings.** Create a line chart (Figure 3b) for this part (append to the same HTML page) whose design is a variant of what you have created in part a. Start with your chart from part a. Modify the code to visualize how the rankings of ['Catan', 'Codenames', 'Terraforming Mars', 'Gloomhaven'] change over time by adding a symbol with the ranking text on their corresponding lines. Show the symbol for every three months, similar to the x-axis ticks in part a. (See Figure 3b). Add a legend to explain what this symbol represents next to your chart (See the Figure 3b bottom right).