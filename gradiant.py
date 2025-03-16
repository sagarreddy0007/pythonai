import gradio as gr

# Define the function to handle the form submission
def submit_form(product_line, customer_requirements, mbp_requirements, customer_requirements_link, mbp_requirements_link):
    # Process the form data (for demonstration, we just return the inputs)
    return f"Product Line: {product_line}\nCustomer Requirements: {customer_requirements or customer_requirements_link}\nMBP Requirements: {mbp_requirements or mbp_requirements_link}"

# Create the Gradio app
with gr.Blocks() as demo:
    # Create a dropdown for product lines
    product_line = gr.Dropdown(
        choices=["Retail", "Commercial", "Lending"],
        label="Product Line",
        info="Select the product line for which you want to submit requirements."
    )

    with gr.Group():
      # Create a radio button to choose between file upload or link for customer requirements
      customer_requirements_type = gr.Radio(
          choices=["Upload File", "Provide Link"],
          label="Customer Requirements Type",
          info="Choose whether to upload a file or provide a link for customer requirements."
      )
  
    
      # Create a file upload component for customer requirements
      customer_requirements = gr.File(
          label="Upload Customer Requirements",
          visible=False
      )
      
      # Create a text input for customer requirements link
      customer_requirements_link = gr.Textbox(
          label="Customer Requirements Link",
          visible=False
      )
  
    with gr.Group():
     # Create a radio button to choose between file upload or link for mbp requirements
      mbp_requirements_type = gr.Radio(
          choices=["Upload File", "Provide Link"],
          label="MBP Requirements Type",
          info="Choose whether to upload a file or provide a link for customer requirements."
      )
    
      # Create a file upload component for MBP requirements
      mbp_requirements = gr.File(
          label="Upload MBP Requirements",
          visible=False
      )
      # Create a text input for customer requirements link
      mbp_requirements_link = gr.Textbox(
          label="MBP Requirements Link",
          visible=False
      )
    
    # Create a button to submit the form
    submit_button = gr.Button("Submit")
    
    # Define the function to toggle visibility of file upload and link input
    def toggle_cust_requirements_type(requirements_type):
        if requirements_type == "Upload File":
            return {customer_requirements: gr.File(visible=True), customer_requirements_link: gr.Textbox(visible=False)}
        else:
            return {customer_requirements: gr.File(visible=False), customer_requirements_link: gr.Textbox(visible=True)}
    
    # Attach the toggle function to the radio button
    customer_requirements_type.change(toggle_cust_requirements_type, customer_requirements_type, [customer_requirements, customer_requirements_link])

     # Define the function to toggle visibility of file upload and link input
    def toggle_mbp_requirements_type(requirements_type):
        if requirements_type == "Upload File":
            return {mbp_requirements: gr.File(visible=True), mbp_requirements_link: gr.Textbox(visible=False)}
        else:
            return {mbp_requirements: gr.File(visible=False), mbp_requirements_link: gr.Textbox(visible=True)}
 
    # Attach the toggle function to the radio button
    mbp_requirements_type.change(toggle_mbp_requirements_type, mbp_requirements_type, [mbp_requirements, mbp_requirements_link])
  
    # Attach the form submission function to the submit button
    submit_button.click(submit_form, [product_line, customer_requirements, mbp_requirements, customer_requirements_link,mbp_requirements_link], gr.Textbox(label="Form Submission"))

# Launch the Gradio app
demo.launch(show_error=True)