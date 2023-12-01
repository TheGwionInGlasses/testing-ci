# Python Unittest Exercises

## Morning

In `src/routines.py` are a number of stubs for functions, with
descriptions of what they are meant to do. Your task for this morning
is:

1. In `tests/test_routines.py`, write unit tests for each of these functions
2. Implement the functions in `src/routines.py`
3. Use the unit tests to ensure that your implementations are correct


You will be writing your tests using the [`unittest`
framework](https://docs.python.org/3.7/library/unittest.html) which
was introduced in the lecture. Before starting, you should review the
different [assertion methods it
provides](https://docs.python.org/3.8/library/unittest.html#unittest.TestCase.assertEqual). You
can take a look at the RSE team's [example
repository](https://git.ccfe.ac.uk/soft-eng-group/rse/continuous-integration/Simple-python-unittest)
for this library.


To ask python to find all the unit tests and run them:
```
python3 -m unittest
```
Make sure you run this from the same directory as contains this README.
Note that you do not need to have written all of your tests in order
to run them. Unimplemented tests will just show up as passing.

You can run them with code coverage turned on to determine how much of
your code is being run during the testing:

```
coverage run -m unittest
```

Running with coverage produces a `.coverage` file, which can be made
human readable by executing

```
coverage report -m --omit=tests/*
```

You should aim for as close to 100% coverage as practical. You can
also produce HTML reports which colour-codes lines according to
whether or not they are covered.

```
coverage html --omit=tests/*
```


## Afternoon

This afternoon you will be learning how to run your tests on the
[GitLab Continuous
Integration](https://git.ccfe.ac.uk/help/ci/README.md) (CI) service.

### Creating a New Repo

This afternoon you will be learning how to setup continuous
integration for your tests on GitLab. To do this you'll need to create
a separate repository for your tests. To do this, execute the
following commands:

```bash
cd ..
cp -R python_exercises ..
cd ../python_exercises
git init
git add .
git commit -m 'Initial commit'
```


### Configuring the CI Service

Now open the file `.gitlab-ci.yml` and edit it according to the
instructions it contains in its comments. You may find it useful to
read the GitLab documentation on [the CI
system](https://git.ccfe.ac.uk/help/ci/quick_start/README.md) and the
[configuration files](https://git.ccfe.ac.uk/help/ci/yaml/README.md).


### Pushing Your Repository to GitLab

To place this repository on GitLab you will first need to create an SSH key:

Create a new, empty repository on GitLab, called `testing-ci`, setting
its visibility to internal.
![Button to create a new repo in GitLab](../media/gitlab-new-repo-link.png)
![Dialogue for creating a new repo](../media/create-repo-screen.png)

Now push your work to the repository by running the following commands
on your computer:
```bash
git remote add origin git@git.ccfe.ac.uk:USERNAME/testing-ci.git
git push -u origin master
```


### Check CI Result

Refresh the page for your repository to check if your work has been
uploaded. If it has, click the link "CI/CD" in the menu on the left of
the screen and take a look at the status of your pipeline (the
collection of jobs run by the CI for each push). You can click on the
status icon to find out more about the individual jobs in that
pipeline. Clicking on the icon for a job will show you the commands
which were run and their output. If your job fails, examine the error
message and try to edit your `.gitlab-ci.yml` file to fix it.


### Adding CI Badges

You should have configured the CI to produce statistics on code
coverage. Take a look at the format of the total coverage
statistic. Now, navigate in your repository to _Settings_ >> _CI/CD_
\>> _General Pipelines_ >> _Test coverage parsing_. This asks you to
provide a "regular expression", which is a string used to pick out
patterns in text. You should use `^TOTAL\s+\d+\s+\d+\s+(\d+\%)$`.

Now, scroll down the page a little bit further to the subheadings
"Pipeline status" and "Coverage report". There you will find snippets
of text which will allow you to place badges showing pipeline status
and coverage statistics in your README. Copy the Markdown text into
the top of your README file. Commit your changes and push them to
GitLab. The badges should now show up a the top of your README.


### Bonus: Displaying Coverage Reports

If there is still time after you have finished all of the above, you
can try writing unit tests for one of the other
languages. Alternatively, you can work on improving your CI process as
described below.

Amend your CI Pipeline to produce HTML coverage reports. Save the
output of this as an "artefact" (or "artifact" according to GitLab,
because international English spells things incorrectly&mdash;[see
documentation](https://git.ccfe.ac.uk/help/user/project/pipelines/job_artifacts.md)).

Now take a look at the documentation for 
[GitLab Pages](https://git.ccfe.ac.uk/help/user/project/pages/index.md).
In your YAML file:

- add a job called `pages` which is part of the `deploy` stage
- ensure `pages` depends on the `unit_test` job
- rename directory containing the HTML reports produced when running
  the unit tests to `public/`

Push these changes to GitLab and let the pipeline run to
completion. Refresh your page and check under "Settings" to see if
there is now an option called "Pages". This should take you to a page
with a link to where your coverage reports are now hosted.

Finally, edit the link on the coverage badge in your README so
clicking on it will take you to the full coverage report.
