from PIL import Image
from pyzbar.pyzbar import decode
from itertools import permutations

# 1. 주어진 이미지 파일을 열고, 각각의 이미지 사이즈를 구한다.
image_files = [f"{num}.png" for num in range(27)]
images = [Image.open(f) for f in image_files]
widths, heights = zip(*(i.size for i in images))

# 2. 이미지 너비, 높이 계산
total_width = sum(widths) - widths[0] * 6
total_height = max(heights)

left = [2, 5, 6, 15, 16, 25, 26]
center = [3, 7, 10, 19, 20, 21, 23]
right = [1, 4, 8, 14, 18, 22, 24]


# 3. 주어진 순서대로 이미지를 붙여서 QR 코드를 생성
def create_qr_code_by_image_orders(image_orders):
    x_offset = 0
    new_image = Image.new('RGB', (total_width, total_height))
    for i, order in enumerate(image_orders):
        image = images[order]
        new_image.paste(image, (x_offset, 0))
        x_offset += image.size[0]
    return new_image


# 4. QR 코드를 생성한 이미지를 읽고 결과 반환
def iterate_orders():
    for i in permutations(left, len(left)):
        for j in permutations(center, len(center)):
            for k in permutations(right, len(right)):
                image_orders = [*i, *j, *k]
                new_image = create_qr_code_by_image_orders(image_orders)
                qr_codes = decode(new_image)

                print(image_orders)

                if qr_codes:
                    new_image.save('flag.png')
                    return qr_codes


def main():
    flag = iterate_orders()
    print('flag', flag)


main()
