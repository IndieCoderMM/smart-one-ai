import openai

openai.api_key = "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"
ENGINE = "text-davinci-002"


def get_openai_complete(prompt):
    respond = openai.Completion.create(engine=ENGINE,
                                       prompt=prompt,
                                       temperature=0.8,
                                       max_tokens=150,
                                       top_p=1,
                                       frequency_penalty=0.9,
                                       presence_penalty=0.5,
                                       stop=[" You: "])
    return respond.choices[0].text