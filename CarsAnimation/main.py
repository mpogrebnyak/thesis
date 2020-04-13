from AnimationManager import Animation
from AnimationManager import AnimationTypes

def main():

    animationS = Animation(AnimationTypes.animateSpeed)
    animationS.animate()

    animationD = Animation(AnimationTypes.animateDistance)
    animationD.animate()

main()
