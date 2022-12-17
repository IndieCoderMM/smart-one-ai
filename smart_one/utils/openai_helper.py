import openai
import os

# Set OpenAI API key
openai.api_key = os.environ["OPENAI_KEY"]
ENGINE = "text-davinci-003"


def get_openai_respond(prompt):
    respond = openai.Completion.create(engine=ENGINE,
                                       prompt=prompt,
                                       temperature=0.8,
                                       max_tokens=256,
                                       top_p=1,
                                       frequency_penalty=0.0,
                                       presence_penalty=0.5,
                                       stop=[" You: "])
    return respond.choices[0].text