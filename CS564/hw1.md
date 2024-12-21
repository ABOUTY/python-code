Problem Set 1 [100 points]
=======

### Deliverables:

Submit your queries (and only those) using the `submission_template.txt` file that is posted on Canvas. Follow the instructions on the file! Upload the file at Canvas.


### Instructions / Notes:

* Run the top cell above to load the database `hw1.db` (make sure the database file, `hw1.db`, is in the same directory as this IPython notebook is running in)
* Some of the problems involve _changing_ this database (e.g. deleting rows)- you can always re-download `hw1.db` or make a copy if you want to start fresh!
* You **may** create new IPython notebook cells to use for e.g. testing, debugging, exploring, etc.- this is encouraged in fact!- **just make sure that your final answer for each question is _in its own cell_ and _clearly indicated_**
* When you see `In [*]:` to the left of the cell you are executing, this means that the code / query is _running_.
    * **If the cell is hanging- i.e. running for too long: To restart the SQL connection, you must restart the entire python kernel**
    * To restart kernel using the menu bar: "Kernel >> Restart >> Clear all outputs & restart"), then re-execute the sql connection cell at top
    * You will also need to restart the connection if you want to load a different version of the database file
* Remember:
    * `%sql [SQL]` is for _single line_ SQL queries
    * `%%sql [SQL]` is for _multi line_ SQL queries
* _Have fun!_



Problem 1: Linear Algebra [30 points]

**------------------------**

Two random 3x3 ($N=3$) matrices have been provided in tables `A` and `B`, having the following schema:

\> * `i INT`:  Row index

\> * `j INT`:  Column index

\> * `val INT`: Cell value

***\*Note: all of your answers below** *_must_* **work for any** *_square_* **matrix sizes, i.e. any value of $****N****$*****\***.

Note how the matrices are represented - why do we choose this format?  Run the following queries to see the matrices in a nice format: