class SumOfMarks:
    def calculate_marks(self, marks):
        # returns -
        # marks - dictionary which contains subject name and marks
        total_marks = 0
        for m in marks.values():
            total_marks += m
        print("Total marks:", total_marks)


som = SumOfMarks()
som.calculate_marks({"Maths": 80, "Science": 90, "SocialScience": 70, "English": 90})