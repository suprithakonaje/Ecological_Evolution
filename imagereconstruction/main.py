from imagereconstruction import imageutils
from imagereconstruction.imageutils import getVectorFromImage
from imagereconstruction.monto_carlo_simulation import start_simulation

if __name__ == '__main__':
    # hot_climate = "C:/Users/Supritha Konaje/PycharmProjects/Dissertation2022/images/hot_20.png"
    # wet_climate = "C:/Users/Supritha Konaje/PycharmProjects/Dissertation2022/images/cold_20.png"
    no_env = "C:/Users/Supritha Konaje/PycharmProjects/Dissertation2022/images/no_env.png"

    # hot_rgb_array = imageutils.convertImageToRGBArray(hot_climate)
    # wet_rgb_array = imageutils.convertImageToRGBArray(wet_climate)
    no_env_rgb_array = imageutils.convertImageToRGBArray(no_env)

    # hot_vector = getVectorFromImage(hot_rgb_array)
    # wet_vector = getVectorFromImage(wet_rgb_array)
    no_env_vector = getVectorFromImage(no_env_rgb_array)

    sol = start_simulation(no_env_vector)

    print(sol)





