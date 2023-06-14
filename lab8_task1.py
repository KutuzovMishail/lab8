import cv2 as cv

def main():
    print("""
    Zoom In-Out demo
    ------------------
    * [i] -> Zoom [i]n
    * [o] -> Zoom [o]ut
    """)
    filename = 'variant-9.png'
    src = cv.imread(cv.samples.findFile(filename))

    while 1:
        rows, cols, _channels = map(int, src.shape)
        cv.imshow('Pyramids Demo', src)
        k = cv.waitKey(0)

        if k == 27:
            break
        elif chr(k) == 'i':
            src = cv.pyrUp(src, dstsize=(2 * cols, 2 * rows))
        elif chr(k) == 'o':
            src = cv.pyrDown(src, dstsize=(cols // 2, rows // 2))
    cv.destroyAllWindows()
    return 0

if __name__ == "__main__":
    main()