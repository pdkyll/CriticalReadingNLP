import re


class Section:
    '''
    Section represents a critical reading section of an SAT test
    Members:
        - questions (list of Question)
    '''
    def __init__(self, number):
        self.questions = []
        self.number = number

    def set_questions(self, questions):
        self.questions = questions


class SAT:
    '''
    SAT represents an SAT test.
    '''
    def __init__(self):
        self.sections = []
        self.scoring_key = {}

    def set_sections(self, sections):
        self.sections = sections

    def score(self):
        raw_score = 0.
        correct = 0
        incorrect = 0
        for section in self.sections:
            for question in section.questions:
                if question.check_answer():
                    correct += 1
                else:
                    incorrect += 1
        raw_score = round(correct - incorrect * 0.25)
        score = self.scoring_key.get(raw_score, self.scoring_key[-2])
        return raw_score, score

    def __repr__(self):
        output = ""
        for section in self.sections:
            output += "SECTION" + str(section.number) + "\n\n"
            for question in section.questions:
                output += "Question: " + question.question + "\n"
                output += "Choices: " + str(question.choices) + "\n"
                output += "Answer: " + question.answer + "\n"
                output += "Selection: " + question.selection + "\n"
                output += "\n"
        return output
