from transformers import pipeline

# Load the image captioning model
captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

# Provide the path to a local image file
image_path = "street.jpeg"  # Replace with the actual path to your image file

# Perform image captioning
captions = captioner(image_path)

print(captions)
# Print the generated captions
# for caption in captions:
#     print(caption['caption'])
