import csv
import unicodedata

fileheader = """
\\documentclass{article}
\\usepackage{fullpage}
\\usepackage{listings}
\\usepackage[utf8]{inputenc}
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

        dup_detector = dict()

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
                student_num = row[1]
                if student_num in dup_detector:
                    previous = dup_detector[student_num]
                    if int(row[8]) > int(previous[8]):
                        dup_detector[student_num] = row
                else:
                    dup_detector[student_num] = row
            
            line_count += 1

        for student_num in dup_detector:
                student = dup_detector[student_num]
                idnum = student[1]
                answers = student[9:-4:2]                
                out.write(header%(student[0]))
                
                for i in range(len(questions)):
                    decoded_answer = answers[i].replace(u"\xa0"," ")
                    out.write(q_template%(questions[i], decoded_answer))
                    if student_num == "54564":
                        print(repr(decoded_answer))

                out.write("\\newpage")
                    
        out.write(filefooter)
                    
            
