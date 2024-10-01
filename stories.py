class Story:
    def __init__(self, id, title, prompts, text):
        self.id = id
        self.title = title
        self.prompts = prompts
        self.templates = text

    def generate(self, answers):
        text = self.templates
        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)
        return text

stories = {
    "1": Story(
        id="1",
        title="Adventure",
        prompts=["noun", "verb", "adjective"],
        text="The {adjective} {noun} decided to {verb}."
    ),
    "2": Story(
        id="2",
        title="Mystery",
        prompts=["place", "person", "object"],
        text="At {place}, {person} found the {object}."
    )
}