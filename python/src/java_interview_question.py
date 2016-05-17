import sys


# Solution to programmingpraxis.com/2016/04/05/java-interview-question/


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: %s filename' % sys.argv[0])
        sys.exit(1)
    with open(sys.argv[1]) as input_file:
        courses = {}
        for line in input_file:
            student_id, title, score = line.split('|')
            student_id = int(student_id)
            score = int(score)
            if title in courses:
                old_id = courses[title][0]
                if old_id > student_id:
                    courses[title] = (student_id, score)
            else:
                courses[title] = (student_id, score)
        for k, v in courses.iteritems():
            print('%s %d' % (k, v[1]))
