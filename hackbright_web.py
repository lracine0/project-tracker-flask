"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    # github = "jhacks"
    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    student_grade = hackbright.get_grades_by_github(github)

    html = render_template('student_info.html',
                            first=first,
                            last=last,
                            github=github,
                            grade=student_grade)
    return html 

@app.route('/student-search') 
def get_student_form():
    """ Show form for searching for a student. """

    return render_template('student_search.html')


@app.route('/student-add')
def student_add():
    """Add a student."""
    
    # first_name = request.form.get('fname')
    # print(first_name)

    # last_name = request.form.get('lname')
    # print(last_name)

    # github = request.form.get('gitname')
    # # QUERY = """
    # #     INSERT INTO students (first_name, last_name, github)
    # #       VALUES (:fname, :lname, :gitname)
    # #     """

    # # hackbright.db.session.execute(QUERY, {'fname': first_name,
    # #                            'lname': last_name,
    # #                            'gitname': github})

    # # hackbright.db.session.commit()

    # hackbright.make_new_student(first_name, last_name, github)

    # print(f"Successfully added student: {first_name} {last_name} {github}")

    return render_template('add_student.html')
        # fname=first_name,
        #                    lname=last_name, gitname=github)


@app.route('/student-display', methods=['POST'])
def student_display():
    """Display success message and link to student account."""

    first_name = request.form.get('fname')
    print(first_name)

    last_name = request.form.get('lname')
    print(last_name)

    github = request.form.get('gitname')
    # QUERY = """
    #     INSERT INTO students (first_name, last_name, github)
    #       VALUES (:fname, :lname, :gitname)
    #     """

    # hackbright.db.session.execute(QUERY, {'fname': first_name,
    #                            'lname': last_name,
    #                            'gitname': github})

    # hackbright.db.session.commit()

    hackbright.make_new_student(first_name, last_name, github)

    print(f"Successfully added student: {first_name} {last_name} {github}")
      
    return render_template('success_student.html', first=first_name, last=last_name,
                            github=github)
        

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
