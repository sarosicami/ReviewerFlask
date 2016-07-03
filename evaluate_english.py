import parse1
import train

reviewsAspect = parse1.trainAspectData('Laptops1.xml')
reviewsAttribute = parse1.trainAttributeData('Laptops1.xml')
reviewsPolarity = parse1.trainPolarityData('Laptops1.xml')
print(len(reviewsAspect))
print(len(reviewsAttribute))
print(len(reviewsPolarity))

train.reviewsAspectData(reviewsAspect)
# train.reviewsAttributeData(reviewsAttribute)
# train.reviewsPolarityData(reviewsPolarity)