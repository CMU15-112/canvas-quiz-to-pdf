import csv

fileheader = """
\\UseRawInputEncoding
\\documentclass{article}
\\usepackage{fullpage}
\\usepackage{listings}
\\lstset{
   breaklines=true,
   basicstyle=\\ttfamily}

\\pagestyle{empty}
\\begin{document}
"""

header = """
{\Large Name: %s}
"""

q_template = """
\\newpage
\\noindent Question: %s

\\noindent Answer:

\\begin{lstlisting}
%s
\\end{lstlisting}
"""

filefooter = """
\\end{document}
"""

with open("answers.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    questions = []

    with open("output/submissions.tex","w") as out:
        
        out.write(fileheader)

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
                    f.write(fileheader)
                    f.write(header%(""))
                    
                    for i in range(len(questions)):                    
                        f.write(q_template%(questions[i], ""))
                        
                    f.write(filefooter)
            else:
                idnum = row[1]
                answers = row[9:-4:2]                
                out.write(header%(row[0]))
                
                for i in range(len(questions)):                    
                    out.write(q_template%(questions[i], answers[i]))

                out.write("\\newpage")
            
            line_count += 1                        
                    
        out.write(filefooter)
                    
            
