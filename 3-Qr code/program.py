import qrcode
link="https://www.linkedin.com/in/sujoy-maity-033b68252/"
name="SujoyLinkedIn.png"
img=qrcode.make(link)
img.save(name)