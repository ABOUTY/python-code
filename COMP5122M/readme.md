 

**Assessment Brief: CW1 Data Science 2023-24**

 

| Module title                     | Data Science                                                 |
| -------------------------------- | ------------------------------------------------------------ |
| Module code                      | COMP5122M                                                    |
| Assignment  title                | Coursework 1: Understanding Players’ Environmental Perception in a Game Environment |
| Assignment type  and description | Assignment                                                   |
| Rationale                        | To learn  how to analyse data and communicate your findings. |
| Word limit and  guidance         | The report has a limit of eight pages and should be written  single-spaced in an 11 pt font (or larger). |
| Weighting                        | 50%                                                          |
| Submission  deadline             | 10am, Wed 6th Dec 2023                                       |
| Submission  method               | Via Minerva                                                  |
| Feedback  provision              | Marks  and feedback will be returned via Minerva.            |
| Learning  outcomes assessed      | Understand the work of a data scientist;  Understand how to acquire, link and investigate the quality of data;  Apply problem-solving skills to effectively analyse data and  communicate findings for a given application scenario. |
| Module leader                    | Roy Ruddle                                                   |
| Other Staff  contact             | Duygu  Sarikaya                                              |

 



 

### 1. Assignment guidance

The objective is to assess your ability to analyse data and communicate your findings. You need to do this coursework in the groups that are defined on Minerva. A group comprises a maximum of four people.

**Animal Crossing: New Horizons (ACNH)** is a typical life-simulation game that hit the market in March 2020 when almost everyone around the globe was forced to stay at home. The game was swiftly sold to more than 13.4 million copies in the first six weeks. When playing ACNH, the players immerse into an idyllic and deserted island with the responsibility of building their island by developing the ecosystem and community. Their daily activities are related to the environment, such as growing flowers, planting fruit, catching fish, snaring bugs, or submitting the fish and bugs to the museum.

![Çizgi film, Animasyon, ağaç, bilgisayar oyunu içeren bir resim  Açıklama otomatik olarak oluşturuldu](file:///C:/Users/32534/AppData/Local/Temp/msohtmlclip1/01/clip_image002.jpg)

You can watch a teaser of the game here: [What Is Animal Crossing: New Horizons? A Guide for the Uninitiated](https://www.youtube.com/watch?v=8AkEFot5UF0) 

A different and free version of the game is also available as a mobile app: [Animal Crossing: Pocket Camp](https://play.google.com/store/apps/details?id=com.nintendo.zaca&hl=en_US)

**Human-centeredness and human-centric attitudes in environmental ethics**

Human centric perspectives in environmental ethics consider the value of non-human beings based on their utilitarian value for humans. For example, White (1967) criticized the human-centric views for identifying humans as the supreme ruler of nature and its non-human members, contributing to the ecological crisis. It inadequately considers nature and fails to acknowledge the intrinsic values of nonhuman contents like trees and animals.

To predict environmental behaviors of humans, many empirical studies used models such as Wildlife Value Orientations, New Environmental Paradigm (Dunlap et al. 2000), Two Major Environmental Values since values are powerful predictors of attitudes and behaviors. 

**Exploring the correlation between the in-game behaviors of game players and their environmental perspectives**

The design of ACNH offers an opportunity to explore the correlation between the in-game behaviors of ACNH players and their environmental perspectives. It is a simulation game where players generate and design the environment of their islands within a pre-programmed ‘‘everyday life’’ narrative. Players follow this pre-programmed narrative with the general goal of building and decorating the island. They are involved in economic activities and human–nature affairs, which resemble those in real life. They collect, create, and sell items (fish, bugs, gold, fruits, etc.) to earn money, pay off mortgages, donate to museums, buy new items, etc. During this process, players must interact with in-game nature and non-human beings (plants, flowers, fish, bugs) and can engage in both pro-environmental activities and environmentally destructive ones. Players have a certain degree of freedom to create their own storyline, explore ways to upgrade their island, and interact with in-game nature because the missions in Animal Crossing are open-ended, and players are not obliged to do them. 

Activities such as catching fish and bugs and seeking fossils could be attractive to players because they help earn money fast and are required items if players want to upgrade their museum collection. In ACNH, a player must tap a tree at least three times to cut it down, so the wood can be exploited without cutting down the tree. Therefore, the decision of whether to cut down the tree or not is worth exploring because it can directly link to the nature-destructive behaviors of game players*. We **hypothesize** that individuals, who exploit in-game resources such as fish, bugs, and trees more frequently, are more likely to agree with the idea of human centeredness than individuals who exploit less frequently.*

Limitations: We are aware that our hypothesis on in-game activities and attitudes is limited as humans can separate games from reality, regardless of how well games resemble reality.

**A multinational dataset of game players’ behaviors in a virtual world and environmental perceptions**

The dataset (Vuong et al. 2021) offers valuable resources regarding environmental perception and behaviors in the virtual world of 640 Animal Crossing: New Horizons (ACNH) gameplayers from 29 countries around the globe. The dataset consists of six major categories: 1) socio-demographic profile, 2) COVID-19 concern, 3) environmental perception, 4) game-playing habit, 5) in-game behavior, and 6) game-playing feeling. The 12th item in New Ecological Paradigm Scale by Dunlap et al. (2000) is used to measure human-centered attitudes of the game players. The players’ attitudes toward the idea of human centeredness were measured ordinally on a 5-point Likert scale from 1 (strongly disagree) to 5 (strongly agree).

**Dataset**

The dataset is publicly available for download at [Science Data k](https://www.scidb.cn/en/detail?dataSetId=cb5d36cce29f4e5695a586c9b85d04b6)

You can find more information about the dataset and its collection here: [A Multinational Data Set of Game Players' Behaviors in a Virtual World and Environmental Perceptions](https://direct.mit.edu/dint/article/3/4/606/107672/A-Multinational-Data-Set-of-Game-Players-Behaviors)

### 2. Assessment tasks

Your tasks are:

·    **Data quality**: Thoroughly investigate and describe the data quality issues that are present in the whole dataset.

·    **Detailed analysis:**

a)   Do exploratory data analysis to show:

o Age distribution of the players

o The relationship between the biological sex as defined by the dataset and the players’ environmental perception.

o A comparison of the frequency of the male and female players’ in-game behaviour: cutting down the tree.

b)   Identify the most important socio-demographic variables to indicate the environmental perception of the players. 

c)   Develop a classification model that can be used to predict a player’s environmental perception based on socio-demographic variables only. To do this, you will need to split the dataset into training (%70), test (%15), and evaluation sets (%15). Evaluate your classification model’s performance using appropriate metrics. Please describe the method you used for classification, and your motivation to choose the method.

### 3. General guidance and study support

See skills@library

### 4. Assessment criteria and marking process

The report has a limit of eight pages and should be written single-spaced in an 11 pt font (or larger). The report should have the following section headings and content:

1. **Group members**: Name & student ID
2. **Introduction** [3 marks]. State the aim of each aspect of the coursework (data quality; data characterisation; detailed analysis objectives) and describe the data file that was used. One paragraph is sufficient.
3. **Data quality** [18 marks]: For details, see §2.
4. **Detailed analysis** [26 marks]: 

a)   [5 marks] For the items mentioned in the data exploratory analysis, please use appropriate visualizations and report findings.

b)   [5 marks] Please describe the method you used for identifying the most important socio-demographic variables, and your motivation to choose the method. 

c)   [16 marks] Please describe the method you used to develop your classification model, and your motivation to choose the method. Give details on how you split your dataset, preprocess data, how you evaluate the performance of your classification model, the metrics you used to evaluate your model, and the motivation to choose these metrics. Please report the performance of your model.

5. **Conclusions** [3 marks]: Restate your main findings. One paragraph is sufficient.

To gain full marks your report needs to adhere to the specified structure, be well presented and easy to understand.

*Do not include references in your report.*

### 5. Presentation and referencing

The quality of written English will be assessed in this work. As a minimum, you must ensure:

·    Paragraphs are used

·    There are links between and within paragraphs although these may be ineffective at times

·    Word choice and grammar do not seriously undermine the meaning and comprehensibility of the argument

·    Word choice and grammar are generally appropriate to an academic text

**
 These are pass/ fail criteria. So irrespective of marks awarded else-where, if you do not meet these criteria you will fail overall.**

### 6. Submission requirements

One person should make the submission on behalf of the group.

Submit a PDF file that contains your report. 

*Optionally:* Before the first page of the report, insert a signed copy of the COMP5122M Data Science *Group Work Form* for your group. You only need to do that if the group members did not contribute equally to the coursework.

### 7. Academic misconduct and plagiarism

Leeds students are part of an academic community that shares ideas and develops new ones. 

You need to learn how to work with others, how to interpret and present other people's ideas, and how to produce your own independent academic work. It is essential that you can distinguish between other people's work and your own, and correctly acknowledge other people's work. 

All students new to the University are expected to complete an online [Academic Integrity tutorial and test](https://desystemshelp.leeds.ac.uk/student-guides/assessment/the-academic-integrity-tutorial-and-test/), and all Leeds students should ensure that they are aware of the principles of Academic integrity. 

When you submit work for assessment it is expected that it will meet the University’s academic integrity standards. 

If you do not understand what these standards are, or how they apply to your work, then please ask the module teaching staff for further guidance.

**By submitting this assignment you are confirming that the work is a true expression of your own work and ideas and that you have given credit to others where their work has contributed to yours.**

### 8. Assessment/ marking criteria grid

For details, see §4.

References:

Dunlap, R., K.V. Liere, A. Mertig, and R.E. Jones. 2000. Measuring endorsement of the new ecological paradigm: A revised NEP scale. Journal of Social Issues 56: 425–442. https://doi.org/10.1111/0022-4537.00176.

Vuong QH., Ho MT., La VP., Le TT., Nguyen THT., Nguyen MH.; A Multinational Data Set of Game Players' Behaviors in a Virtual World and Environmental Perceptions. Data Intelligence 2021; 3 (4): 606–630. doi: https://doi.org/10.1162/dint_a_00111

Ho, MT., Nguyen, TH.T., Nguyen, MH. et al. Good ethics cannot stop me from exploiting: The good and bad of anthropocentric attitudes in a game environment. Ambio 51, 2294–2307 (2022). https://doi.org/10.1007/s13280-022-01742-y

 