import pyjokes

# English joke
joke = pyjokes.get_joke()
print(joke)

# Specific language joke (Hindi, English, etc.)
joke_hindi = pyjokes.get_joke(language="hi")
print(joke_hindi)
