import csv

header = """
\\documentclass{article}
\\usepackage{fullpage}
\\usepackage{minted}

\\pagestyle{empty}
\\begin{document}

{\Large %s}
"""

q_template = """
\\newpage
\\noindent Question: %s

\\noindent Answer:

\\begin{minted}{python}
%s
\\end{minted}
"""

footer = """
\\end{document}
"""

with open("answers.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    questions = []
    for row in csv_reader:
        if line_count == 0:
            # This gets just the questions
            qs = row[9:-4:2]
            for q in qs:
                # Ditch the number and colon on the front
                l = q.find(": ")
                q = q[l+2:]
                questions.append(q)
            
            with open(f"output/blank.tex","w") as f:
                f.write(header%("Name"))
                
                for i in range(len(questions)):                    
                    f.write(q_template%(questions[i], ""))
                    
                f.write(footer)            
        else:
            idnum = row[1]
            answers = row[9:-4:2]
            with open(f"output/{idnum}.tex","w") as f:
                f.write(header%(row[0]))
                
                for i in range(len(questions)):                    
                    f.write(q_template%(questions[i], answers[i]))
                    
                f.write(footer)
                
        line_count += 1
        
    print(questions)
            