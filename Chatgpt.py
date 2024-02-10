# Processing course column

import openai
import time

# Set your OpenAI GPT-3 API key
openai.api_key = ''


def categorize_course_with_gpt3(course):
    # Construct a prompt for GPT-3 to perform a web search
    prompt = f"Select the field of this course {course} from these given fields. Do not reply anything else than the given feilds. Reply only the strings of field:\n" \
             "Arts and Humanities\n" \
             "Social Sciences\n" \
             "Natural Sciences\n" \
             "Engineering and Technology\n" \
             "Health Sciences\n" \
             "Business and Economics\n" \
             "Law\n" \
             "Religious Studies\n" \
             "Agriculture and Environmental Studies\n" \
             "Interdisciplinary Studies\n" \
             "Communication and Media\n" \
             "Computer and Information Sciences\n" \
             "Physical Education and Sports Sciences\n" \
             "Mathematics and Statistics\n" \
             "Public Policy and Administration\n" \
             "Interdisciplinary and General Education\n"

    # Make an API call to GPT-3 using the chat completion endpoint
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150  # Adjust as needed
    )
    return response["choices"][0]["message"]["content"]


# Set the rate limit variables
requests_limit = 3
wait_time = 60

'''# Iterate over the DataFrame and update values
for index, row in dataset.iterrows():
    current_value = row['Course']
    if pd.notna(current_value):
        updated_value = categorize_course_with_gpt3(current_value)
        dataset.at[index, 'Course'] = updated_value
        print(updated_value)
    else:
        dataset.at[index, 'Course'] = "General Studies"
        print("General Studies")

    # Check if 3 requests have been made and introduce a wait
    if (index + 1) % requests_limit == 0 and index != 0:
        print(f"Waiting for {wait_time} seconds...")
        time.sleep(wait_time)'''