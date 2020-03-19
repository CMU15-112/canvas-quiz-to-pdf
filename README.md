# Canvas to PDF

The purpose of this quick script is to convert student answers on a canvas quiz to a PDF that can be uploaded to Gradescope.  (Because it will take a lot more than a pandemic to make me grade on Canvas...)

## Usage

### Getting the student answers

After students take the canvas quiz, click on "Quiz Statistics" on the quiz settings page.  Then click the "Student Analysis" button.  Save the resulting csv as `answers.csv` in this directory

### Canvas -> LaTeX

Run `python3 convert.py`.  This will fill up your output directory with `.tex` files of each submission.

### LaTeX -> PDF

There is a `Makefile` in `output/` to build the PDFs.  So...

```
cd output
make
```

### Uploading to Gradescope

The file `output/blank.pdf` can serve as a template for Gradescope.

After you have that configured, just upload all the other PDFs.