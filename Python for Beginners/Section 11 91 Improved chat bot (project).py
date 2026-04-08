from difflib import get_close_matches



def get_best_match(user_question: str, knowledge: dict) -> str | None:
    questions: list[str] = [q for q in knowledge]
    matches:list[str] = get_close_matches(user_question, questions, n=1, cutoff=0.6)

    if matches:
        return matches[0]

def run_chatbot(knowledge: dict) -> None:
    while True:
        user_input: str = input('You: ')

        best_match: str | None = get_best_match(user_input, knowledge)
        response: str | None = knowledge.get(best_match)

        if response:
            print(f'Bot: {response}')


        else:
            print(f'Bot: I do not understand...')

def main() -> None:
    brain: dict[str, str] = {'hello': 'Hey there!',
                             'do you know what the time is?': 'Not at all',
                             'what time is it?': 'No clue!',
                         'what can you do?': 'I can answer questions!',
                             'ok': 'Great'}

    run_chatbot(knowledge=brain)

if __name__ == '__main__':
    main()


