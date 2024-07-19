import base64

def get_image_description(client, uploaded_file, prompt, model_choice):
    # Encode the uploaded image in base64
    encoded_image = base64.b64encode(uploaded_file.getvalue()).decode('utf-8')

    # Create the GPT-4o or GPT-4o-mini API request
    response = client.chat.completions.create(
        model=model_choice,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{encoded_image}"}
                    },
                ],
            }
        ],
        max_tokens=300,
    )

    # Extract and return the description
    return response.choices[0].message.content
