import parse_romanian
import trainRomanian

reviewsAspect = parse_romanian.trainAspectData('Laptops_romanian.xml')
reviewsAttribute = parse_romanian.trainAttributeData('Laptops_romanian.xml')
reviewsPolarity = parse_romanian.trainPolarityData('Laptops_romanian.xml')
reviewsEmotion = parse_romanian.trainEmotionData('Laptops_romanian.xml')

aspect_result = trainRomanian.reviewsAspectData(reviewsAspect)
attribute_result = trainRomanian.reviewsAttributeData(reviewsAttribute)
polarity_result = trainRomanian.reviewsPolarityData(reviewsPolarity)
emotion_result = trainRomanian.reviewsEmotionData(reviewsEmotion)