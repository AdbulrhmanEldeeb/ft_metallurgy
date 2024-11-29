import gradio as gr

def create_app_layout(answer_fn):
    with gr.Blocks() as app:
        with gr.Row():
            with gr.Column(scale=1, min_width=200):  # Sidebar
                gr.Image("assets/lama.webp", label=None, elem_id="sidebar-image")
                gr.Markdown(
                    """
                    **Metallurgy Expert Assistant**  
                    This app provides technical insights in metallurgy, materials science, and engineering. 
                    Enter your query below or choose an example to get started.
                    """
                )
            with gr.Column(scale=3):  # Main content
                gr.Markdown("# Metallurgy Expert Assistant")
                gr.Markdown("### Example Questions:")

                examples = gr.Dropdown(
                    choices=[
                        "What are the effects of adding rare earth elements to magnesium alloys?",
                        "What are the advantages of TIG welding over MIG welding for aluminum alloys?",
                        "How does ultrasonic testing (UT) detect internal flaws in materials?",
                        "How does cathodic protection (CP) work in marine environments?",
                    ],
                    label="Select an example question",
                )
                query_input = gr.Textbox(
                    label="Enter your technical question",
                    placeholder="e.g., How to improve the toughness of Mg-Al-Mn alloys?",
                    lines=3,
                )
                submit_btn = gr.Button("Get Response")
                response_output = gr.Textbox(
                    label="Generated Response",
                    placeholder="The model's generated response will appear here.",
                    lines=10,
                    interactive=False,
                )

                examples.change(fn=lambda ex: ex, inputs=examples, outputs=query_input)
                submit_btn.click(fn=answer_fn, inputs=query_input, outputs=response_output)
    return app
