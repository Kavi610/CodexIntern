import requests
import os
import time

# Function to generate image using Replicate's Stable Diffusion API
def generate_image(prompt, output_path):
    # Set the API URL for Stable Diffusion via Replicate
    api_url = "https://api.replicate.com/v1/predictions"
    
    # Replace with your Replicate API key
    replicate_api_key = input("Enter your Replicate API key: ")

    headers = {
        "Authorization": f"Token {replicate_api_key}",
        "Content-Type": "application/json",
    }

    # Stable Diffusion model
    model_version = "stability-ai/stable-diffusion:28f8787"

    # Data to send in the request (the text prompt)
    data = {
        "version": model_version,
        "input": {
            "prompt": prompt,
            "width": 512,
            "height": 512
        }
    }

    # Send the POST request to the API
    response = requests.post(api_url, json=data, headers=headers)

    # Check for errors
    if response.status_code != 201:
        print(f"Failed to generate image: {response.text}")
        return

    # Get the prediction ID to check the image generation status
    prediction_id = response.json()["id"]
    print(f"Generating image, prediction ID: {prediction_id}")

    # Check the status until the image is ready
    while True:
        status_response = requests.get(f"{api_url}/{prediction_id}", headers=headers)
        status = status_response.json()["status"]

        if status == "succeeded":
            image_url = status_response.json()["output"][0]
            print(f"Image generated: {image_url}")

            # Download the image and save it locally
            img_data = requests.get(image_url).content
            with open(output_path, 'wb') as img_file:
                img_file.write(img_data)
            print(f"Image saved as '{output_path}'.")
            break
        elif status == "failed":
            print("Image generation failed.")
            break
        else:
            print("Image still being generated... Waiting for 5 seconds.")
            time.sleep(5)

# Main program to gather user input and generate the image
def main():
    prompt = input("Enter the image description (e.g., 'A black dog wearing a hat'): ")
    output_path = input("Enter the output file name (e.g., 'output_image.png'): ")

    # Default to .png extension if not provided
    if not output_path.endswith('.png'):
        output_path += '.png'

    generate_image(prompt, output_path)

if __name__ == "__main__":
    main()
