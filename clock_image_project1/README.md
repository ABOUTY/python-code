# Python Programming - Project 1 [40 marks] - READ FIRST!

The tasks for Project 1 are described in the notebook `project-1.ipynb`.

Make sure to **read the instructions below** before starting. If any of the instructions require clarification, **please ask on Piazza and/or in class!**

---

## Submission structure

Your submission will consist of the files `project-1.ipynb` (the notebook) and `quality_control.py`, which will be a **Python module**. The Week 6 lecture will cover writing and using modules, but to put it simply: a module is a `.py` file which contains function definitions, and that you can `import` somewhere else to use the functions there. Your submission will also include a folder `QC_reports`, containing five `.txt` files which you will create in Task 6.

- When you need to **define a function**, do so in `quality_control.py`.
- The module `quality_control.py` should **only** contain **function definitions**, and any required `import` statements (for example if you need to import `numpy`).
- You are allowed to define **additional functions** in the module at your convenience; often, this will help you write cleaner and more reusable code.
- For each question, a simple **test** will be provided in the notebook `project-1.ipynb`. You can use these to start checking the basic working of your functions. They work similarly to your Coderunner quizzes. Run the code cells in the notebook to run the tests (and please don't edit them!).
    - In some cases, the tests use `assert` statements. We've seen an example in the Week 4 lecture, but as a reminder:
        - `assert X` will do nothing if `X` is `True`.
        - `assert X` will produce an `AssertionError` if `X` is `False`.
        - NumPy also has a `np.testing` suite of functions which can `assert` statements in a similar way -- you will see some examples in the provided tests. The syntax is slightly different, but should be self-explanatory.
    - The provided tests are **minimal** (similar to the "Examples" provided for pre-checking in the Coderunner quizzes), and are here just to help you check that you are on the right track. To make sure that your function works fully with all possible inputs, you should add more of your own tests.
    - Any tests that you write yourself will not be assessed, and you do not need to submit them.
    - When you submit on Gradescope, more automatic tests will be performed. You will see the results of **some** of these tests when you submit; if any fail, you can try to correct your code, and resubmit as many times as you want (until the deadline).
    - Gradescope will also have hidden tests which will test your functions further (similar to the further tests in the Coderunner quizzes, which are run when you click "Check"). You will not see the results of these tests until the grades and feedback are returned to the class. This means, in particular, that **passing all the visible tests on Gradescope does not guarantee full marks.**

---

## Libraries

The packages and libraries available for you to complete the assignment are the same as the default libraries available in your Codespaces, namely:

```
python=3.12.5
numpy=2.1.1
scipy=1.14.1
matplotlib=3.9.2
ipywidgets=8.1.5
pandas=2.2.2
seaborn=0.13.2
requests=2.32.3
```

If you have your local installation of Python/Anaconda, you don't need to match these versions exactly, but make sure your code is compatible. (To check this, open your assignment in a Codespace before submitting, and run the code cells to make sure everything works.)

You should treat this as a **strict constraint** on your assignment --- **you can only use these libraries in your code**. Submissions which make use of other packages/libraries will be penalised. Note that the autograder on Gradescope will be set up with these libraries too, so it will also fail if you try to import anything not installed there.

---

## Marking

There are 7 tasks in total. The number of marks is indicated for each task. It is possible to obtain partial marks for partially correct attempts.

To gain full marks in a question, your code should work as expected, but also:

- Your code should be **well-commented**, with a comment explaining each step of your code. All your functions should have **docstrings**. This is not only good practice -- it is also essential for us to assess your understanding of the code you have written. See [Code comments](#code-comments) below.
- The **structure** and logic should be sensible.
    - Use different object types appropriately, depending on the data you are working with (e.g. strings, floats, lists, arrays...).
    - Your code should follow the DRY principle, avoid magic numbers, etc. See the Week 3 workshop activity for reference, as well as the CR tasks.
    - When appropriate, define **intermediate functions** additionally to those required by the task, to perform the different sub-tasks in your code. Think carefully about how to structure your functions; if you find yourself having to re-write very similar code in multiple places, think about breaking your bigger functions down into smaller, reusable ones.
- Your code should be **pleasant to read**. Use whitespace when it improves clarity, be mindful of where you place your code comments, keep your code style consistent, choose meaningful variable names.
- Any plots/figures should be **clearly labelled** and professionally presented, to understand what is displayed without having to look at the code.

***Up to half*** of the total marks earned in a question may be deducted if your code fails to satisfy these standards.

The hidden automatic tests on Gradescope will allocate marks automatically to your submission. This will then be reviewed manually by a marker, who will provide more feedback where necessary, and change the automatically-allocated mark if needed.

---

## Working on your project with git and GitHub

- While working on the project, **commit and push your changes often** -- every time you make progress on a subtask. If you tend to forget to do this regularly, you could e.g. set a timer to remind you to commit every hour or so. This ensures that
    - you won't have any last-minute technical issues when it comes to submitting, and
    - your progress is **backed up** on GitHub, and not just inside a temporary codespace.
- You will submit the assignment through **Gradescope**, by providing a link to your GitHub repository. You can resubmit to Gradescope as many times as you want before the deadline. (More detailed submission instructions will be available shortly.)

---

## Academic integrity

This is an **individual** assignment -- just like for the Coderunner quizzes, the work your submit must be your own, to reflect and assess your own understanding and knowledge.

### Generative AI

The contents of the assignment have been written by instructors, who **retain the copyright**; in particular, you are not authorised to use any of the text or code provided to you as input or prompt to a generative AI tool (such as ChatGPT, Claude, Copilot, Cursor, ELM, etc.; see e.g. [this blog post](https://srheblog.com/2023/09/18/fair-use-or-copyright-infringement-what-academic-researchers-need-to-know-about-chatgpt-prompts/)).

See [Providing references](#providing-references) below for how to provide appropriate citations for short snippets of code that you have not authored yourself.

### Collaboration vs. collusion

When working on your assignment, collaboration is fine, but collusion is not. Concretely, this means that discussing the assignment **in broad terms** with others students is fine (and encouraged), as well as giving each other hints or general advice on how to approach a problem. You can use Piazza for this, for example -- if you are stuck, then please ask for help!

However, you are **not permitted to share your working** (even partially) with other students -- that includes your code, any detailed description or explanation of code, and any results or analysis you perform.

For example:

- Alice and Bob are discussing the assignment in the library. Bob's code is not working for one of the questions, and he can't figure out why. He asks Alice how she's tackled the problem, and she explains her approach in broad terms. This gives Bob an idea, and he tries it later. *This is all fine.*
- Bob's idea doesn't work out, and he calls Alice later on Teams. He shares his screen with her to show his code. *This is getting dangerous* -- here's why:
    - Alice helps him with understanding the error, and gives him some pointers and ideas to try, without explaining the problem or the solution in much detail. *That would still be fine.*
    - Alice is stuck on the next question, though, and spots a couple of lines of Bob's code at the bottom of the screen. She uses some of that code for the next question in her submission. This is not OK: *both Bob and Alice have now committed misconduct* -- Alice by using Bob's code, and Bob by sharing his screen.
- Bob is still stuck. He posts his code for that question on Piazza. Some students help and also give him some  general advice. Charlie sees the post on Piazza, and didn't know how to start that question. Charlie uses some of Bob's code, with some corrections to fix the problems, and submits it for the assignment. *This is also misconduct* by both Bob and Charlie.
- Bob is still stuck (poor Bob!). It's getting very close to the deadline now, so he asks his friend Dara to *pleaaaase* show their solution, he promises not to copy it. Bob and Dara are really good friends, so Dara finds it difficult to refuse and sends their code. Bob rewrites Dara's code by changing some variable names, rearranging a bit, and paraphrasing the code comments so that they are "in his own words". *This is misconduct* by both Bob and Dara.

Use and trust your own judgement. It's important to understand that even with the best intentions, you expose yourself to academic misconduct as soon as you show your code to another student, and this could have very serious consequences.

### Providing references

For **every** separate question, **most** of the code you submit must be **authored by you**. That being said, you may use any code from the course material (e.g. workshop tasks, notebooks, lectures), without citing it.

You may also use **small pieces of code** (3-4 lines maximum at a time) that you found elsewhere -- e.g. examples from the documentation, a textbook, forums, blogs, etc... You may use this code *verbatim* (i.e. almost exactly as you found it), or adapt it to write your own solution.

A programming assignment is just like any other academic assignment -- and therefore, **you must provide a citation for any such code**, whether you use it *verbatim* or adapt it. To do so, include a code comment at the start of your script or notebook cell, indicating:

- the line numbers where the code was used or adapted,
- the URL of the source (or, if it's from a book, a full reference to the book),
- the date you accessed the source,
- the author of the code (if the information is available). **This includes cases where the "author" is a generative AI tool (e.g. ChatGPT).**

You can use this template -- delete one of the URL or book reference lines as appropriate:

```python
# Lines X-Y: Author Name
# URL: http://...
# Book Title, year published, page number.
# Accessed on 30 Feb 2024.
```

You must also provide **detailed code comments** for any such code, **in your own words**, to demonstrate that you fully understand how it works -- you will lose marks if you use external code without explaining it, even if it's cited correctly.

Your mark will also be negatively affected if a substantial part of your submission (more than approx. 20%) has not been authored by you, even if everything has been cited appropriately. The extent of this will depend on the proportion of your submission which you have authored yourself, and the proportion which comes from other sources.

Remember to exercise caution if you use any code from external sources -- there are a lot of blogs, forums, and genAI tools which will give you very bad code!

With all that, we trust that you'll be able to use your best judgement, and to cite your sources appropriately -- if anything is not clear, please do ask. Note that **all submissions** will be automatically checked (and manually reviewed) for plagiarism and collusion, and [the University's academic misconduct policy](https://www.ed.ac.uk/academic-services/staff/discipline/academic-misconduct) applies.


---

## Code comments

The important thing when writing code comments is that your comments **explain** what you do in detail and why you do it.

Here is an example with a function which finds out whether an integer is prime. Note that the docstring here doesn't have a separate `Input:` and `Output:` section, as the text is already quite self-explanatory and this is a simple function.

---

### ✅ Good:
```python
def is_prime(n):
    """
    Return whether an input positive integer is prime.
    """
    if n == 1:        # If n is 1 ...
        return False  # ... then n is not prime

    for i in range(2, n):  # Test integers i from 2 to n - 1 inclusive
        if n % i == 0:     # If n is divisible by i ...
            return False   # ... then n is not prime

    # If n is not divisible by any integers from 2 to n - 1 inclusive,
    # then n is prime
    return True
```

---

### ✅ Also good (more succinct, but every step is *well explained*):
```python
def is_prime(n):
    """
    Return whether an input positive integer is prime.
    """
    # Special case: 1 is not prime
    if n == 1:
        return False

    # Check if n has any divisors
    for i in range(2, n):
        if n % i == 0:
            # We found a divisor, n is not prime, we can stop immediately
            return False

    # If we haven't found any divisors in the loop above,
    # then n is prime
    return True
```

---

### ❌ Not enough:
```python
def is_prime(n):
    if n == 1:
        return False
    
    # Test numbers between 2 and n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    
    # n is prime
    return True
```

---

### ❌ Also not enough (the comments repeat the code instead of explaining it):
```python
def is_prime(n):
    """
    Return whether an input positive integer is prime.
    """
    # Test if n equals 1
    if n == 1:
        return False   # then it's False
    
    # Loop for 2 until n-1
    for i in range(2, n):
        # Test if n / i has remainder zero
        if n % i == 0:
            return False   # then it's False
    
    # Otherwise it's True
    return True
```
