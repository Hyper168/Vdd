
import time

def slow(txt):
	for word in txt:
		print(word,end = "",flush = True)
		time.sleep(0.03)
	print()
	
	
leonardoai="""
-Leonardo AI is a generative AI platform that empowers users to effortlessly generate captivating images and artwork, with a specific emphasis on game assets.
It is a free to use platform, but there is currently a queue-based system for sign-ups.
-The platform offers a variety of features, including:
*The ability to generate images from text descriptions
"The ability to upsample low-resolution images
"The ability to remove backgrounds from images
*The ability to create variations of an image
*The ability to train your own AI models
Visit-https://leonardo.ai/
"""
nightcafe = """
NightCafe is a text-to-image AI generator that allows you to create images from text descriptions. It is based on the Neural Style Transfer model, which is a deep learning algorithm that can transfer the style of one image to another.

Here are some of the features of NightCafe:

* Generate images from text descriptions
* Customize the style, colors, and other aspects of the image
* Import your own images to use as a starting point
* Collaborate with others on image creation
* Share your images with others

NightCafe is a free to use platform, but there is a premium subscription that offers additional features, such as:

* Increased image quality
* More image styles
* Access to the latest features

For more information visit-https://creator.nightcafe.studio/
"""
openaidalle2 = """
OpenAI DALL-E 2 is a text-to-image diffusion model that can create realistic and creative images from text descriptions. It is trained on a massive dataset of text and images, and it can generate images of a wide variety of objects and scenes.

DALL-E 2 is still under development, but it has the potential to be a powerful tool for creativity. It can be used to create images for a variety of purposes, such as:

* **Art:** DALL-E 2 can be used to create realistic and creative paintings, drawings, and other artworks.
* **Design:** DALL-E 2 can be used to create designs for products, logos, and other visual elements.
* **Entertainment:** DALL-E 2 can be used to create images for movies, TV shows, and other entertainment content.
* **Education:** DALL-E 2 can be used to create educational images that help people learn about different concepts.
* **Research:** DALL-E 2 can be used to research the capabilities of text-to-image generation and to develop new applications for this technology.

Visit-https://openai.com/dall-e-2
"""

question = {"What is the current population of india in 2023":"The current population of India in 2023 is 1,428,627,663",
"Text to ai image tools in 2023":f"Here are some Text to ai image tools in 2023\n[1]Leornado Ai\n{leonardoai}\n[2]Nightcafe\n{nightcafe}\n[3]Openai Dalle-2 Image creator{openaidalle2}"}

slow("Hello,Buddy I am your ai chatbot!!!")
slow("Version 1.2023.5\n")
name = input("What name i should call you:")
slow(f"Bot:Hello,{name}\n")
slow("Ask me a question")
slow("Enter 'exit' to exit\n")

while(True):
	q = input("Enter your question:")
	if (q in question):
		slow(f"Input:{q}\n")
		slow(f"Searching '{q}' ")
		time.sleep(9)
		slow(f"Output:{question[q]}")
	else:
	   slow(f"Searching '{q}' ")
	   time.sleep(7)
	   print("Sorry, I don't know the answer of that question.")
