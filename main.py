import random

def run_quiz():
    # ANSI color codes
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

    # Original questions
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

    score = 0

    # Shuffle questions
    random.shuffle(questions)

    for q in questions:
        print(f"\n{CYAN}{q['question']}{RESET}")

        # Shuffle options and keep track
        options = q["options"].copy()
        random.shuffle(options)

        # Print options with new numbering
        option_mapping = {}
        for idx, option in enumerate(options, 1):
            print(YELLOW + f"{idx}) {option}" + RESET)
            option_mapping[str(idx)] = option

        user_answer = input("បញ្ចូលលេខចម្លើយរបស់អ្នក (Enter the number of your answer): ")

        # Check if selected option matches the correct answer
        if str(option_mapping.get(user_answer)).lower() == str(q["answer"]).lower():
            score += 1

    # Calculate percentage
    percentage = (score / len(questions)) * 100

    # Choose color based on score
    if percentage < 25:
        color = RED
    elif percentage < 50:
        color = YELLOW
    else:
        color = GREEN

    print(f"\n{color}ពិន្ទុចុងក្រោយរបស់អ្នកគឺ {score}/{len(questions)} ({percentage:.2f}%).{RESET}")

if __name__ == "__main__":
    run_quiz()
