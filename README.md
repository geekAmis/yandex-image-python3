get_image_page принимает параметры:

текст(по которому будет идти поиск),
количество нужных картинок(число),
выбрать одно фото из полученного списка(любой параметр, кроме 0 - включит эту функцию, если count > 1),
mask - не советую трогать, это сам массив, в который наполняются url.

возвращает либо ссылку (str)
либо массив ссылок (list)

download_image принимает параметры:
data - либо list(список url) , либо str(1 url),
path - куда будут скачиваться фото (TEXT).
