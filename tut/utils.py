import settings

# percentage #
def height_prct(percentage):
    return (settings.HEIGHT / 100) * percentage

print(height_prct(25))