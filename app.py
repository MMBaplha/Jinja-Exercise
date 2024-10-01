from flask import Flask, render_template, request
from stories import stories 

app = Flask(__name__)

@app.route("/")
def home_page():
    """Homepage that shows form for selecting a story."""
    return render_template("select_story.html", stories=stories)

@app.route("/questions")
def ask_questions():
    """Show form for the selected story."""
    story_id = request.args.get("story")
    # print(f"Requested story ID: {story_id}")# debug output
    selected_story = stories.get(story_id)
    # print(f"Selected story: {selected_story}")  # Debug output
    
    if selected_story is None:
        return "Story not found!", 404

    return render_template("questions.html", prompts=selected_story.prompts, story_id=story_id)

@app.route("/story")
def display_story():
    """Display the generated story."""
    story_id = request.args.get("story_id")
    selected_story = stories.get(story_id)

    user_answers = request.args.to_dict()

    # Checks for empty answers
    if not all(user_answers.get(prompt) for prompt in selected_story.prompts):
        return "Story not found!", 404
    
    generated_story = selected_story.generate(user_answers)
    return render_template("story.html", story=generated_story)
