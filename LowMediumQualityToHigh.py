from PIL import Image

def enhance_image_quality(input_path, output_path, scale_factor=2, quality=95, output_format='JPEG'):
    # Open the image
    image = Image.open(input_path)

    # Upscale the image
    width, height = image.size
    new_size = (width * scale_factor, height * scale_factor)
    upscaled_image = image.resize(new_size, Image.BICUBIC)

    # Save the upscaled image with higher quality
    upscaled_image.save(output_path, format=output_format, quality=quality)

# Example usage
input_image_path = r'SampleInputs\ImageWithText\ImageWithText.jpg'
output_image_path = r'OutputFiles\ImageFileFormats\high_quality_image.jpg'

enhance_image_quality(input_image_path, output_image_path)