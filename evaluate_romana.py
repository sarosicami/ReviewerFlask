import parse_romanian
import trainRomanian_evaluate

reviewsAspect = parse_romanian.trainAspectData('Laptops_romanian.xml')
reviewsAttribute = parse_romanian.trainAttributeData('Laptops_romanian.xml')
reviewsPolarity = parse_romanian.trainPolarityData('Laptops_romanian.xml')
reviewsEmotion = parse_romanian.trainEmotionData('Laptops_romanian.xml')
print(len(reviewsAspect))
print(len(reviewsAttribute))
print(len(reviewsEmotion))
print(len(reviewsPolarity))

# trainRomanian_evaluate.reviewsAspectData(reviewsAspect)
# trainRomanian_evaluate.reviewsAttributeData(reviewsAttribute)
# trainRomanian_evaluate.reviewsEmotionData(reviewsEmotion)
# trainRomanian_evaluate.reviewsPolarityData(reviewsPolarity)