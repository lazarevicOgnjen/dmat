import os
from dhooks import Webhook, Embed, File

image2_path = 'cs elfak.jpg'

WEBHOOK_URL = [os.getenv('WEBHOOK_MAIN1')]
for url in WEBHOOK_URL:
    hook = Webhook(url)

    embed.set_image(url="attachment://cs elfak.jpg")
    file = File(image2_path, name="cs elfak.jpg")
    hook.send("@everyone 📢 BP [main page link - click here -](https://cs.elfak.ni.ac.rs/nastava/course/view.php?id=97)**", embed=embed, file=file)
