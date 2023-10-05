#!/usr/bin/env python3

# Standard library imports
# from random import randint, choice as rc

# # Remote library imports
# from faker import Faker

# Local imports
from app import app
from models import db, User, Question, Answer, QuizAttempt

if __name__ == '__main__':
    with app.app_context():
        print("Deleting all records...")
        User.query.delete()
        Question.query.delete()
        Answer.query.delete()
        QuizAttempt.query.delete()

        print("Creating users...")

        user1 = User(username="user1", email="user1@example.com")
        user1.password_hash="user1" + "password"
        user2 = User(username="user2", email="user2@example.com")
        user2.password_hash="user2" + "password"
        user3 = User(username="user3", email="user3@example.com")
        user3.password_hash="user3" + "password"

        db.session.add_all([user1, user2, user3])
        db.session.commit()

        print("Creating questions...")

        questions_to_add = [ 
            Question(question_text="What is the supreme law of the land?"),
            Question(question_text="What does the Constitution do?"),
            Question(question_text="The idea of self-government is in the first three words of the Constitution. What are these words?"),
            Question(question_text="What is an amendment?"),
            Question(question_text="What do we call the first ten amendments to the Constitution?"),
            Question(question_text="What is one right or freedom from the First Amendment?*"),
            Question(question_text="How many amendments does the Constitution have?"),
            Question(question_text="How many amendments does the Constitution have?"),
            Question(question_text="What are two rights in the Declaration of Independence?"),
            Question(question_text="What is freedom of religion?"),
            Question(question_text="What is the economic system in the United States?*"),
            Question(question_text="What is the “rule of law”?"),
            Question(question_text="Name one branch or part of the government.*"),
            Question(question_text="What stops one branch of government from becoming too powerful?"),
            Question(question_text="Who is in charge of the executive branch?"),
            Question(question_text="Who makes federal laws?"),
            Question(question_text="What are the two parts of the U.S. Congress?*"),
            Question(question_text="How many U.S. Senators are there?"),
            Question(question_text="We elect a U.S. Senator for how many years? "),
            Question(question_text="Who is one of your state’s U.S. Senators now?*"),
            Question(question_text="The House of Representatives has how many voting members?"),
            Question(question_text="We elect a U.S. Representative for how many years?"),
            Question(question_text="Name your U.S. Representative."),
            Question(question_text="Who does a U.S. Senator represent?"),
            Question(question_text="Why do some states have more Representatives than other states?"),
            Question(question_text="We elect a President for how many years?"),
            Question(question_text="In what month do we vote for President?*"),
            Question(question_text="What is the name of the President of the United States now?*"),
            Question(question_text="What is the name of the Vice President of the United States now?"),
            Question(question_text="If the President can no longer serve, who becomes President?"),
            Question(question_text="If both the President and the Vice President can no longer serve, who becomes President?"),
            Question(question_text="Who is the Commander in Chief of the military?"),
            Question(question_text="Who signs bills to become laws?"),
            Question(question_text="Who vetoes bills?"),
            Question(question_text="What does the President’s Cabinet do?"),
            Question(question_text="What are two Cabinet-level positions?"),
            Question(question_text="What does the judicial branch do?"),
            Question(question_text="What is the highest court in the United States?"),
            Question(question_text="How many justices are on the Supreme Court?"),
            Question(question_text="Who is the Chief Justice of the United States now?"),
            Question(question_text="Under our Constitution, some powers belong to the federal government. What is one power of the federal government?"),
            Question(question_text="Under our Constitution, some powers belong to the states. What is one power of the states?"),
            Question(question_text="Who is the Governor of your state now?"),
            Question(question_text="What is the capital of your state?*"),
            Question(question_text="What are the two major political parties in the United States?*"),
            Question(question_text="What is the political party of the President now?"),
            Question(question_text="What is the name of the Speaker of the House of Representatives now?"),
            Question(question_text="There are four amendments to the Constitution about who can vote. Describe one of them."),
            Question(question_text="What is one responsibility that is only for United States citizens?*"),
            Question(question_text="Name one right only for United States citizens."),
            Question(question_text="What are two rights of everyone living in the United States?"),
            Question(question_text="What do we show loyalty to when we say the Pledge of Allegiance?"),
            Question(question_text="What is one promise you make when you become a United States citizen?"),
            Question(question_text="How old do citizens have to be to vote for President?*"),
            Question(question_text="What are two ways that Americans can participate in their democracy?"),
            Question(question_text="When is the last day you can send in federal income tax forms?*"),
            Question(question_text="When must all men register for the Selective Service?"),
            Question(question_text="What is one reason colonists came to America?"),
            Question(question_text="Who lived in America before the Europeans arrived?"),
            Question(question_text="What group of people was taken to America and sold as slaves?"),
            Question(question_text="Why did the colonists fight the British?"),
            Question(question_text="Who wrote the Declaration of Independence?"),
            Question(question_text="When was the Declaration of Independence adopted?"),
            Question(question_text="There were 13 original states. Name three."),
            Question(question_text="What happened at the Constitutional Convention?"),
            Question(question_text="When was the Constitution written?"),
            Question(question_text="The Federalist Papers supported the passage of the U.S. Constitution. Name one of the writers."),
            Question(question_text="What is one thing Benjamin Franklin is famous for?"),
            Question(question_text="Who is the “Father of Our Country”?"),
            Question(question_text="Who was the first President?*"),
            Question(question_text="What territory did the United States buy from France in 1803?"),
            Question(question_text="Name one war fought by the United States in the 1800s."),
            Question(question_text="Name the U.S. war between the North and the South. "),
            Question(question_text="Name one problem that led to the Civil War."),
            Question(question_text="What was one important thing that Abraham Lincoln did?*"),
            Question(question_text="What did the Emancipation Proclamation do?"),
            Question(question_text="What did Susan B. Anthony do?"),
            Question(question_text="Name one war fought by the United States in the 1900s.*"),
            Question(question_text="Who was President during World War I?"),
            Question(question_text="Who was President during the Great Depression and World War II?"),
            Question(question_text="Who did the United States fight in World War II?"),
            Question(question_text="Before he was President, Eisenhower was a general. What war was he in?"),
            Question(question_text="During the Cold War, what was the main concern of the United States?"),
            Question(question_text="What movement tried to end racial discrimination?"),
            Question(question_text="What did Martin Luther King, Jr. do?*"),
            Question(question_text="What major event happened on September 11, 2001, in the United States?"),
            Question(question_text="Name one American Indian tribe in the United States."),
            Question(question_text="Name one of the two longest rivers in the United States."),
            Question(question_text="What ocean is on the West Coast of the United States?"),
            Question(question_text="What ocean is on the East Coast of the United States?"),
            Question(question_text="Name one U.S. territory."),
            Question(question_text="Name one state that borders Canada."),
            Question(question_text="Name one state that borders Mexico"),
            Question(question_text="What is the capital of the United States?*"),
            Question(question_text="Where is the Statue of Liberty?*"),
            Question(question_text="Why does the flag have 13 stripes?"),
            Question(question_text="Why does the flag have 50 stars?*"),
            Question(question_text="What is the name of the national anthem?"),
            Question(question_text="When do we celebrate Independence Day?*"),
            Question(question_text="Name two national U.S. holidays.")
        ]

        db.session.add_all(questions_to_add)
        db.session.commit()

        print("Creating answer...")

        answers_to_add = [
            Answer(answer_text="The Constitution", correct=True, question=questions_to_add[0]),
            Answer(answer_text="The Supreme Court", correct=False, question=questions_to_add[0]),
            Answer(answer_text="Sets up the government", correct=True, question=questions_to_add[1]),
            Answer(answer_text="Defines the government", correct=True, question=questions_to_add[1]),
            Answer(answer_text="Protects basic rights of Americans", correct=True, question=questions_to_add[1]),
            Answer(answer_text="Protects the goverment", correct=False, question=questions_to_add[1]),
            Answer(answer_text="We the People", correct=True, question=questions_to_add[2]),
            Answer(answer_text="We the Human", correct=False, question=questions_to_add[2]),
            Answer(answer_text="A change to the Constitution", correct=True, question=questions_to_add[3]),
            Answer(answer_text="An addition to the Constitution", correct=True, question=questions_to_add[3]),
            Answer(answer_text="A change to the Goverment", correct=False, question=questions_to_add[3]),
            Answer(answer_text="The Bill of Rights", correct=True, question=questions_to_add[4]),
            Answer(answer_text="The Right of Bill", correct=False, question=questions_to_add[4]),
            Answer(answer_text="Speech", correct=True, question=questions_to_add[5]),
            Answer(answer_text="Religion", correct=True, question=questions_to_add[5]),
            Answer(answer_text="Travel", correct=False, question=questions_to_add[5]),
            Answer(answer_text="Twenty-seven (27)", correct=True, question=questions_to_add[6]),
            Answer(answer_text="Twenty-six (26)", correct=False, question=questions_to_add[6]),
            Answer(answer_text="Announced/declared our independence (from Great Britain)", correct=True, question=questions_to_add[7]),
            Answer(answer_text="Said that the United States is free (from Great Britain)", correct=True, question=questions_to_add[7]),
            Answer(answer_text="Announced our goverment", correct=False, question=questions_to_add[7]),
            Answer(answer_text="Life and liberty", correct=True, question=questions_to_add[8]),
            Answer(answer_text="People and the world", correct=False, question=questions_to_add[8]),
            Answer(answer_text="You can practice any religion, or not practice a religion.", correct=True, question=questions_to_add[9]),
            Answer(answer_text="You can not practice any religion, or practice a religion.", correct=False, question=questions_to_add[9]),
            Answer(answer_text="Capitalist economy", correct=True, question=questions_to_add[10]),
            Answer(answer_text="Market economy", correct=True, question=questions_to_add[10]),
            Answer(answer_text="Stock market", correct=False, question=questions_to_add[10]),
            Answer(answer_text="Everyone must follow the law", correct=True, question=questions_to_add[11]),
            Answer(answer_text="Goverment is above the law", correct=False, question=questions_to_add[11]),
            Answer(answer_text="Congress", correct=True, question=questions_to_add[12]),
            Answer(answer_text="President", correct=True, question=questions_to_add[12]),
            Answer(answer_text="Judicial", correct=True, question=questions_to_add[12]),
            Answer(answer_text="Federal", correct=False, question=questions_to_add[12]),
            Answer(answer_text="Checks and balances", correct=True, question=questions_to_add[13]),
            Answer(answer_text="Separation of powers", correct=True, question=questions_to_add[13]),
            Answer(answer_text="Power of money", correct=False, question=questions_to_add[13]),
            Answer(answer_text="The President", correct=True, question=questions_to_add[14]),
            Answer(answer_text="The Goverment", correct=False, question=questions_to_add[14]),
            Answer(answer_text="Congress", correct=True, question=questions_to_add[15]),
            Answer(answer_text="Senate and House (of Representatives)", correct=True, question=questions_to_add[15]),
            Answer(answer_text="The President", correct=False, question=questions_to_add[15]),
            Answer(answer_text="The Senate and House (of Representatives)", correct=True, question=questions_to_add[16]),
            Answer(answer_text="The Speaker of the House and the vice president", correct=False, question=questions_to_add[16]),
            Answer(answer_text="One hundred (100)", correct=True, question=questions_to_add[17]),
            Answer(answer_text="Two hundred (200)", correct=False, question=questions_to_add[17]),
            Answer(answer_text="Six (6)", correct=True, question=questions_to_add[18]),
            Answer(answer_text="Nine (9)", correct=False, question=questions_to_add[18]),
            Answer(answer_text="Answers will vary. [District of Columbia residents and residents of U.S. territories should answer that D.C. (or the territory where the applicant lives) has no U.S. Senators.]", correct=True, question=questions_to_add[19]),
            Answer(answer_text="Four hundred thirty-five (435)", correct=True, question=questions_to_add[20]),
            Answer(answer_text="Three hundred thirty-five (335)", correct=False, question=questions_to_add[20]),
            Answer(answer_text="Two (2)", correct=True, question=questions_to_add[21]),
            Answer(answer_text="Four (4)", correct=False, question=questions_to_add[21]),
            Answer(answer_text="Answers will vary. [Residents of territories with nonvoting Delegates or Resident Commissioners may provide the name of that Delegate or Commissioner. Also acceptable is any statement that the territory has no (voting) Representatives in Congress.]", correct=True, question=questions_to_add[22]),
            Answer(answer_text="All people of the state", correct=True, question=questions_to_add[23]),
            Answer(answer_text="All people of the country", correct=False, question=questions_to_add[23]),
            Answer(answer_text="Because of the state’s population", correct=True, question=questions_to_add[24]),
            Answer(answer_text="Because of the goverment", correct=False, question=questions_to_add[24]),
            Answer(answer_text="Four (4)", correct=True, question=questions_to_add[25]),
            Answer(answer_text="Five (5)", correct=False, question=questions_to_add[25]),
            Answer(answer_text="November", correct=True, question=questions_to_add[26]),
            Answer(answer_text="December", correct=False, question=questions_to_add[26]),
            Answer(answer_text="Joe Biden", correct=True, question=questions_to_add[27]),
            Answer(answer_text="Donald Trump", correct=False, question=questions_to_add[27]),
            Answer(answer_text="Kamala Harris", correct=True, question=questions_to_add[28]),
            Answer(answer_text="Anthony N", correct=False, question=questions_to_add[28]),
            Answer(answer_text="The vice president", correct=True, question=questions_to_add[29]),
            Answer(answer_text="The Speaker of the House", correct=False, question=questions_to_add[29]),
            Answer(answer_text="The Speaker of the House", correct=True, question=questions_to_add[30]),
            Answer(answer_text="The Chief Justice", correct=False, question=questions_to_add[30]),
            Answer(answer_text="The President", correct=True, question=questions_to_add[31]),
            Answer(answer_text="The Vice President", correct=False, question=questions_to_add[31]),
            Answer(answer_text="The President", correct=True, question=questions_to_add[32]),
            Answer(answer_text="The Chief Justice", correct=False, question=questions_to_add[32]),
            Answer(answer_text="The President", correct=True, question=questions_to_add[33]),
            Answer(answer_text="The Speaker of the House", correct=False, question=questions_to_add[33]),
            Answer(answer_text="Advises the President", correct=True, question=questions_to_add[34]),
            Answer(answer_text="Reviews law", correct=False, question=questions_to_add[34]),
            Answer(answer_text="Attorney General and Vice President", correct=True, question=questions_to_add[35]),
            Answer(answer_text="The Speaker of the House and Representative", correct=False, question=questions_to_add[35]),
            Answer(answer_text="Reviews laws", correct=True, question=questions_to_add[36]),
            Answer(answer_text="Sets up the Goverment", correct=False, question=questions_to_add[36]),
            Answer(answer_text="The Supreme Court", correct=True, question=questions_to_add[37]),
            Answer(answer_text="The Federal Court", correct=False, question=questions_to_add[37]),
            Answer(answer_text="Nine (9)", correct=True, question=questions_to_add[38]),
            Answer(answer_text="Six (6)", correct=False, question=questions_to_add[38]),
            Answer(answer_text="John Roberts", correct=True, question=questions_to_add[39]),
            Answer(answer_text="Kevin McCarthy", correct=False, question=questions_to_add[39]),
            Answer(answer_text="To print money", correct=True, question=questions_to_add[40]),
            Answer(answer_text="To protect the goverment", correct=False, question=questions_to_add[40]),
            Answer(answer_text="Provide Schooling and Education", correct=True, question=questions_to_add[41]),
            Answer(answer_text="To give a driver license", correct=True, question=questions_to_add[41]),
            Answer(answer_text="To declare war", correct=False, question=questions_to_add[41]),
            Answer(answer_text="Answers will vary. [District of Columbia residents should answer that D.C. does not have a Governor.]", correct=True, question=questions_to_add[42]),
            Answer(answer_text="Answers will vary. [District of Columbia residents should answer that D.C. is not a state and does not have a capital. Residents of U.S. territories should name the capital of the territory.]", correct=True, question=questions_to_add[43]),
            Answer(answer_text="Democratic and Republican", correct=True, question=questions_to_add[44]),
            Answer(answer_text="Libertarian and Independent", correct=False, question=questions_to_add[44]),
            Answer(answer_text="Democratic", correct=True, question=questions_to_add[45]),
            Answer(answer_text="Republican", correct=False, question=questions_to_add[45]),
            Answer(answer_text="Kevin McCarthy", correct=True, question=questions_to_add[46]),
            Answer(answer_text="Susan Anthony B", correct=False, question=questions_to_add[46]),
            Answer(answer_text="Any citizen can vote.", correct=True, question=questions_to_add[47]),
            Answer(answer_text="Any resident can vote", correct=False, question=questions_to_add[47]),
            Answer(answer_text="Vote in a federal election", correct=True, question=questions_to_add[48]),
            Answer(answer_text="Run for office", correct=False, question=questions_to_add[48]),
            Answer(answer_text="Vote in a federal election", correct=True, question=questions_to_add[49]),
            Answer(answer_text="Run for federal office", correct=True, question=questions_to_add[49]),
            Answer(answer_text="Print money", correct=False, question=questions_to_add[49]),
            Answer(answer_text="Freedom of speach and freedom of religion", correct=True, question=questions_to_add[50]),
            Answer(answer_text="Free to have money", correct=False, question=questions_to_add[50]),
            Answer(answer_text="The United States", correct=True, question=questions_to_add[51]),
            Answer(answer_text="The religion", correct=False, question=questions_to_add[51]),
            Answer(answer_text="Be loyal to the United States", correct=True, question=questions_to_add[52]),
            Answer(answer_text="Be loyal to the other countries", correct=False, question=questions_to_add[52]),
            Answer(answer_text="Eighteen (18) and older", correct=True, question=questions_to_add[53]),
            Answer(answer_text="Sixteen (18) and older", correct=False, question=questions_to_add[53]),
            Answer(answer_text="Vote and join a political party", correct=True, question=questions_to_add[54]),
            Answer(answer_text="Print money and tell lies", correct=False, question=questions_to_add[54]),
            Answer(answer_text="April 15th", correct=True, question=questions_to_add[55]),
            Answer(answer_text="June 15th", correct=False, question=questions_to_add[55]),
            Answer(answer_text="Between eighteen (18) and twenty-six (26)", correct=True, question=questions_to_add[56]),
            Answer(answer_text="Between eighteen (16) and twenty-one (21)", correct=False, question=questions_to_add[56]),
            Answer(answer_text="Freedom", correct=True, question=questions_to_add[57]),
            Answer(answer_text="Slavery", correct=False, question=questions_to_add[57]),
            Answer(answer_text="American Indians", correct=True, question=questions_to_add[58]),
            Answer(answer_text="British", correct=False, question=questions_to_add[58]),
            Answer(answer_text="Africans", correct=True, question=questions_to_add[59]),
            Answer(answer_text="Chineese", correct=False, question=questions_to_add[59]),
            Answer(answer_text="Because of high taxes", correct=True, question=questions_to_add[60]),
            Answer(answer_text="Because they wanted money", correct=False, question=questions_to_add[60]),
            Answer(answer_text="Thomas Jefferson", correct=True, question=questions_to_add[61]),
            Answer(answer_text="James Madison", correct=False, question=questions_to_add[61]),
            Answer(answer_text="July 4, 1776", correct=True, question=questions_to_add[62]),
            Answer(answer_text="July 4, 1876", correct=False, question=questions_to_add[62]),
            Answer(answer_text="New Jork - New Jersey - New Hampshire", correct=True, question=questions_to_add[63]),
            Answer(answer_text="California - Texas - Louisiana", correct=False, question=questions_to_add[63]),
            Answer(answer_text="The Constitution was written", correct=True, question=questions_to_add[64]),
            Answer(answer_text="The Federalist Papers was written", correct=False, question=questions_to_add[64]),
            Answer(answer_text="1787", correct=True, question=questions_to_add[65]),
            Answer(answer_text="1877", correct=False, question=questions_to_add[65]),
            Answer(answer_text="John Jay", correct=True, question=questions_to_add[66]),
            Answer(answer_text="Martin Luther King", correct=False, question=questions_to_add[66]),
            Answer(answer_text="U.S diplomat", correct=True, question=questions_to_add[67]),
            Answer(answer_text="Fought for civil rights", correct=False, question=questions_to_add[67]),
            Answer(answer_text="George Washington", correct=True, question=questions_to_add[68]),
            Answer(answer_text="George Bush", correct=False, question=questions_to_add[68]),
            Answer(answer_text="George Washington", correct=True, question=questions_to_add[69]),
            Answer(answer_text="Alexander Hamilton", correct=False, question=questions_to_add[69]),
            Answer(answer_text="Louisiana", correct=True, question=questions_to_add[70]),
            Answer(answer_text="Pennsylvania ", correct=False, question=questions_to_add[70]),
            Answer(answer_text="Civil War", correct=True, question=questions_to_add[71]),
            Answer(answer_text="Drug War", correct=False, question=questions_to_add[71]),
            Answer(answer_text="Civil War", correct=True, question=questions_to_add[72]),
            Answer(answer_text="World War I", correct=False, question=questions_to_add[72]),
            Answer(answer_text="Slavery", correct=True, question=questions_to_add[73]),
            Answer(answer_text="Women's rights", correct=False, question=questions_to_add[73]),
            Answer(answer_text="Freed the slaves", correct=True, question=questions_to_add[74]),
            Answer(answer_text="Freed the womens", correct=False, question=questions_to_add[74]),
            Answer(answer_text="Freed the slaves", correct=True, question=questions_to_add[75]),
            Answer(answer_text="Set up the goverment", correct=False, question=questions_to_add[75]),
            Answer(answer_text="Fought for women's rights", correct=True, question=questions_to_add[76]),
            Answer(answer_text="Fought for children's rights", correct=False, question=questions_to_add[76]),
            Answer(answer_text="World War I or World War II", correct=True, question=questions_to_add[77]),
            Answer(answer_text="Cold War", correct=False, question=questions_to_add[77]),
            Answer(answer_text="Woodrow Wilson", correct=True, question=questions_to_add[78]),
            Answer(answer_text="Thomas Jefferson", correct=False, question=questions_to_add[78]),
            Answer(answer_text="Franklin Roosevelt", correct=True, question=questions_to_add[79]),
            Answer(answer_text="James Madison", correct=False, question=questions_to_add[79]),
            Answer(answer_text="Japan, Germany, and Italy", correct=True, question=questions_to_add[80]),
            Answer(answer_text="Japan, Germany, and Russia", correct=False, question=questions_to_add[80]),
            Answer(answer_text="World War 2", correct=True, question=questions_to_add[81]),
            Answer(answer_text="World War 1", correct=False, question=questions_to_add[81]),
            Answer(answer_text="Communism", correct=True, question=questions_to_add[82]),
            Answer(answer_text="Chineese", correct=False, question=questions_to_add[82]),
            Answer(answer_text="Civil rights movement", correct=True, question=questions_to_add[83]),
            Answer(answer_text="Women's rights movement", correct=False, question=questions_to_add[83]),
            Answer(answer_text="Fought for civil rights", correct=True, question=questions_to_add[84]),
            Answer(answer_text="Fought for women's rights", correct=False, question=questions_to_add[84]),
            Answer(answer_text="Terrorists attacked the United States.", correct=True, question=questions_to_add[85]),
            Answer(answer_text="The United States attacked terrorists", correct=False, question=questions_to_add[85]),
            Answer(answer_text="Cherokee", correct=True, question=questions_to_add[86]),
            Answer(answer_text="Guam", correct=False, question=questions_to_add[86]),
            Answer(answer_text="Mississippi river", correct=True, question=questions_to_add[87]),
            Answer(answer_text="Columbia river", correct=False, question=questions_to_add[87]),
            Answer(answer_text="Pacific Ocean", correct=True, question=questions_to_add[88]),
            Answer(answer_text="Arctic Ocean", correct=False, question=questions_to_add[88]),
            Answer(answer_text="Atlantic Ocean", correct=True, question=questions_to_add[89]),
            Answer(answer_text="Indian Ocean", correct=False, question=questions_to_add[89]),
            Answer(answer_text="Puerto Rico", correct=True, question=questions_to_add[90]),
            Answer(answer_text="Hawaii", correct=False, question=questions_to_add[90]),
            Answer(answer_text="New York", correct=True, question=questions_to_add[91]),
            Answer(answer_text="Texas", correct=False, question=questions_to_add[91]),
            Answer(answer_text="Texas", correct=True, question=questions_to_add[92]),
            Answer(answer_text="Louisiana", correct=False, question=questions_to_add[92]),
            Answer(answer_text="Washington, D.C.", correct=True, question=questions_to_add[93]),
            Answer(answer_text="Washington", correct=False, question=questions_to_add[93]),
            Answer(answer_text="New York", correct=True, question=questions_to_add[94]),
            Answer(answer_text="California", correct=False, question=questions_to_add[94]),
            Answer(answer_text="Because there were 13 original colonies", correct=True, question=questions_to_add[95]),
            Answer(answer_text="Because there were 13 states", correct=False, question=questions_to_add[95]),
            Answer(answer_text="Because there are 50 states", correct=True, question=questions_to_add[96]),
            Answer(answer_text="Because there are 50 religions", correct=False, question=questions_to_add[96]),
            Answer(answer_text="The Star-Spangled Banner", correct=True, question=questions_to_add[97]),
            Answer(answer_text="The Lone Star", correct=False, question=questions_to_add[97]),
            Answer(answer_text="July 4", correct=True, question=questions_to_add[98]),
            Answer(answer_text="Febuary 14", correct=False, question=questions_to_add[98]),
            Answer(answer_text="New Year's Day and Christmas", correct=True, question=questions_to_add[99]),
            Answer(answer_text="Valentine's Day and Haloween", correct=False, question=questions_to_add[99]),
        ]

        db.session.add_all(answers_to_add)
        db.session.commit()

        print("Creating QuizAttempt...")

        quizs_attempt_to_add = [
            QuizAttempt(user_id=user1.id, score=8, questions_attempted=10),
            QuizAttempt(user_id=user2.id, score=7, questions_attempted=10),
            QuizAttempt(user_id=user3.id, score=9, questions_attempted=10)
        ]

        db.session.add_all(quizs_attempt_to_add)
        db.session.commit()

        print("Seeding complete.")