from model import load_model, answer
from components import create_app_layout

# Load the model and tokenizer
model, tokenizer = load_model()

# Define the function for Gradio to call
def gradio_answer_fn(query):
    return answer(model, tokenizer, query)

# Create the app layout
app = create_app_layout(gradio_answer_fn)

# Launch the app
if __name__ == "__main__":
    app.launch(share=True)
