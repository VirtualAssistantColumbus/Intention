from enum import StrEnum


class StaticDir(StrEnum):
    """ List the location of static assets relative to /static """

    SIGN_1 = "signs/1.jpg"
    SIGN_2 = "signs/2.jpg"
    SIGN_3 = "signs/3.jpg"
    SIGN_4 = "signs/4.jpg"
    SIGN_5 = "signs/5.jpg"
    SIGN_6 = "signs/6.jpg"
    SIGN_7 = "signs/7.jpg"
    SIGN_8 = "signs/8.jpg"
    SIGN_9 = "signs/9.jpg"
    SIGN_10 = "signs/10.jpg"
    SIGN_11 = "signs/11.jpg"
    SIGN_12 = "signs/12.jpg"

    RAY = "team/ray.jpg"

    def full_path(self) -> str:
        return "/static/" + str(self)