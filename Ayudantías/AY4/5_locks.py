from threading import Lock, Thread


# Este codigo esta inspirado en los contenidos del curso:
# https://github.com/IIC2233/contenidos/blob/main/semana-05/2-concurrencia.ipynb

class FacebookPost:

    def __init__(self) -> None:
        self.likes = 0
        self.lock = Lock()


def count_likes_from_2_sources(post: FacebookPost) -> None:
    for _ in range(500000):
        with post.lock:  # Comentar esta linea para que no funcione.
            post.likes += 1


if __name__ == "__main__":

    post = FacebookPost()

    # create threads
    instagram = Thread(target=count_likes_from_2_sources, args=(post, ))
    facebook = Thread(target=count_likes_from_2_sources, args=(post, ))

    # start the threads
    instagram.start()
    facebook.start()

    # wait for the threads to complete
    instagram.join()
    facebook.join()

    print(f'The final counter is {post.likes}')
