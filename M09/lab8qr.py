# Data taken from the Death Penalty Information Center Fact Sheet
# https://deathpenaltyinfo.org/documents/FactSheet.pdf
# And from Death Sentences in the United States From 1977 By State And By Year
# https://deathpenaltyinfo.org/death-sentences-united-states-1977-present
# A State object represents death penalty statistics for a particular state in the US. For each State,
# the following information is tracked:
#
# Name: the name of the state (e.g., "Florida").
# Abbrev: the two-letter abbreviation for the state (e.g., "FL")
# Sentences: the number of people who were sentenced to death between the years 1977 and 2017
# Exoneration: the number of people who were sentenced to death but subsequently were cleared of wrongdoing.
# Inmates: the number of people who are sitting on Death Row.
# Executions: the number of people who have been executed.
class State:
    __name = ""
    __abbrev = ""
    __exoneration = 0
    __inmates = 0
    __executions = 0
    __sentences = 0

    def __init__(self, name, abbrev, exonerate, inmates, executions, sentences):
        self.__name = name
        self.__abbrev = abbrev
        self.__exoneration = exonerate
        self.__inmates = inmates
        self.__executions = executions
        self.__sentences = sentences

    def exonerations_per_sentence(self):
        return self.__exoneration / self.__sentences

    def get_name(self):
        return self.__name

    def get_abbrev(self):
        return self.__abbrev

    def get_sentences(self):
        return self.__sentences

    def get_exonerations(self):
        return self.__exoneration

def make_data():
    data = [
        State("Florida", "FL", 28, 354, 94, 965),
        State("Illinois", "IL", 21, 0, 12, 304),
        State("Texas", "TX", 13, 235, 556, 979),
        State("Louisiana", "LA", 11, 70, 28, 166),
        State("Oklahoma", "OK", 10, 49, 112, 317),
        State("North Carolina", "NC", 9, 144, 43, 451),
        State("Ohio", "OH", 9, 141, 56, 342),
        State("Alabama", "AL", 6, 188, 63, 471),
        State("Georgia", "GA", 6, 58, 72, 234),
        State("Pennsylvania", "PA", 6, 160, 3, 383),
        State("California", "CA", 5, 740, 13, 971),
        State("Missouri", "MO", 4, 25, 88, 198),
        State("Mississippi", "MS", 4, 47, 21, 177),
        State("New Mexico", "NM", 4, 2, 1, 14),
        State("Tennessee", "TN", 3, 62, 8, 175),
        State("Indiana", "IN", 2, 12, 20, 99),
        State("South Carolina", "SC", 2, 39, 43, 195),
        State("Delaware", "DE", 1, 0, 16, 50),
        State("Idaho", "ID", 1, 9, 3, 43),
        State("Kentucky", "KY", 1, 33, 3, 86),
        State("Maryland", "MD", 1, 0, 5, 53),
        State("Nebraska", "NE", 1, 11, 4, 29),
        State("Nevada", "NV", 1, 77, 12, 156),
        State("Washington", "WA", 1, 8, 5, 40),
        State("Utah", "UT", 1, 9, 7, 19),
        State("Colorado", "CO", 1, 3, 1, 15),
        State("South Dakota", "SD", 1, 3, 4, 11),
        State("Oregon", "OR", 1, 33, 2, 77),
        State("Virginia", "VA", 1, 3, 113, 151),
        State("Arkansas", "AR", 1, 31, 31, 124),
        State("Montana", "MT", 1, 2, 3, 10),
        State("New Hampshire", "NH", 1, 1, 0, 1),
        State("Wyoming", "WY", 1, 1, 1, 7)
    ]

    return data

# Calculates the percentage of people who were sentenced to death who were later
# cleared of wrongdoing, nationwide.
def calc_percent_exonerations(states):
    total_exonerations = 0
    total_sentences = 0

    for state in states:
        total_exonerations = total_exonerations + state.get_exonerations()
        total_sentences = total_sentences + state.get_sentences()

    return (total_exonerations / total_sentences)

# This function returns the number of death sentences handed out in a given state since 1977.
# It is used to provide a sort key function so that we can sort states in descending order by
# number of death sentences
def get_sentences(state):
    return state.get_sentences()

# Calculate and output death penalty statistics
def main():
    states = make_data()

    # Sort states in descending order by number of death sentences
    states.sort(key=get_sentences, reverse=True)
    percent_exonerated_sentences = calc_percent_exonerations(states)

    print("Nationwide, {:.2f}% of death sentences handed out resulted in exonerations.".format(percent_exonerated_sentences))
    print("For the 5 states in the US with the highest number of death sentences handed")
    print("out, here are the expected and actual number of exonerations:")
    print()
    print("State Name      Sentences    Exonerated    Expected Exonerations    Difference")
    print("==========      =========    ==========    =====================    ==========")

    for i in range(5): # Display data for top 5 states
        state = states[i]
        sentences = state.get_sentences()
        actual_exonerations = state.get_exonerations()
        expected_exonerations = percent_exonerated_sentences * sentences;
        difference = expected_exonerations - actual_exonerations
        print(
            "{:15s}".format(state.get_name()),
            "{:6d}".format(sentences),
            "{:12d}".format(actual_exonerations),
            "{:19.0f}".format(expected_exonerations),
            "{:19.0f}".format(difference)
        )

main()