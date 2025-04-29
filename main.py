import random

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

questions = [
    {
        "question": "តើរាជធានីរបស់ប្រទេសបារាំងជាអ្វី?",
        "options": ["ប៉ារីស", "លុងដ៍", "រ៉ូម", "បឺរឡាំង"],
        "answer": "ប៉ារីស"
    },
    {
        "question": "តើភាសាណាដែលប្រើសម្រាប់អភិវឌ្ឍកម្មវិធីគេហទំព័រ?",
        "options": ["Python", "JavaScript", "Java", "ទាំងអស់ខាងលើ"],
        "answer": "ទាំងអស់ខាងលើ"
    },
    {
        "question": "តើអ្នកណាជាអ្នកបង្កើតភាសា Python?",
        "options": ["អីឡុន ម៉ាស្ក", "ប៊ីល ហ្គេត", "គីដូ វ៉ាន់ រ៉ូស៊ុំ", "ម៉ាក ស៊ុគកឺប៊ឺគ"],
        "answer": "គីដូ វ៉ាន់ រ៉ូស៊ុំ"
    }
]

def get_shuffled_questions():
    q_copy = questions.copy()
    random.shuffle(q_copy)
    return q_copy

def shuffle_options(options):
    options_copy = options.copy()
    random.shuffle(options_copy)
    return options_copy

def check_answer(selected_option, correct_answer):
    return selected_option.lower() == correct_answer.lower()

def calculate_percentage(score, total):
    return (score / total) * 100

def run_quiz():
    score = 0
    shuffled_questions = get_shuffled_questions()

    for q in shuffled_questions:
        print(f"\n{CYAN}{q['question']}{RESET}")
        options = shuffle_options(q["options"])
        option_mapping = {}

        for idx, option in enumerate(options, 1):
            print(YELLOW + f"{idx}) {option}" + RESET)
            option_mapping[str(idx)] = option

        user_answer = input("បញ្ចូលលេខចម្លើយរបស់អ្នក (Enter the number of your answer): ")

        if user_answer in option_mapping:
            selected = option_mapping[user_answer]
            if check_answer(selected, q["answer"]):
                score += 1

    percentage = calculate_percentage(score, len(questions))

    if percentage < 25:
        color = RED
    elif percentage < 50:
        color = YELLOW
    else:
        color = GREEN

    print(f"\n{color}ពិន្ទុចុងក្រោយរបស់អ្នកគឺ {score}/{len(questions)} ({percentage:.2f}%).{RESET}")

if __name__ == "__main__":
    run_quiz()
