import qrcode
from PIL import Image, ImageDraw

def save_qr(data, image_name, box_size=10, main_color=(0,0,0), background_color=(255,255,255)):
    qr = qrcode.QRCode(
        version=11,
        box_size=box_size,
    )
    qr.add_data(data)
    qr.make(fit=False)
    img = qr.make_image(fill_color=main_color, background_color=background_color)
    textify = Image.new(img.mode, img.size, background_color)
    draw = ImageDraw.Draw(textify)
    counter = 0

    for i in range(0, img.size[0], box_size):
        for j in range(0, img.size[1], box_size):
            xy = (j, i)
            if img.getpixel(xy) == main_color:
                draw.rectangle((xy, (xy[0] + box_size, xy[1] + box_size)), fill=main_color)
                draw.text((xy[0] + 3, xy[1]), data[counter], fill=background_color)
                counter += 1
                counter %= len(data)
    
    img.save("og_qr_codes/" + image_name + ".png")
    textify.save("created_qr_codes/" + image_name + ".png")

gettysburg = "No score and seventeen years ago our founders brought forth upon this world, a new universe, conceived in Binary, and dedicated to the proposition that all websites are created equal."
save_qr(gettysburg, "gettysburg")

pride_and_prejudice = "It is a truth universally acknowledged, that a single person in possession of any fortune, must be in need of an intelligent cellular device."
save_qr(pride_and_prejudice, "pride_and_prejudice")

jfk = "Ask not what your social media following can do for you - ask what you can do for your social media following."
save_qr(jfk, "jfk")

hamlet = "To be on social media, or not to be on social media: that is the question: Whether 'tis nobler in the mind to suffer."
save_qr(hamlet, "hamlet")

romeo_and_juliet = "O Instagram, Instagram, wherefore art thou Instagram? Deny thy father and refuse thy name. Or if thou wilt not, be but sworn my love, and I'll no longer be an influencer."
save_qr(romeo_and_juliet, "romeo_and_juliet")

declaration_of_independence = "We hold these truths to be self-evident, that all websites are created equal, that they are endowed by their Coder with certain unalienable Rights, that among these are Connection, Clarity and the pursuit of Information."
save_qr(declaration_of_independence, "declaration_of_independence")