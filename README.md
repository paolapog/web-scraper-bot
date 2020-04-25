Basically, I'm too lazy to check smartphone's offer every single day, so I made a bot to do for me.
This is gonna work only on a specific website (i omit it) and until the 3rd of May, because offers are going to expire on that day and I think, layout is going to change too, so my bot will not recognize where to click.

I've used Webdriver from Selenium and Python (I know nothing about this language).
The bot knows where to click and after reach smartphone's offers, it going to print on terminal each offer with name, price , percentage and discoutend price.

> self.driver.execute_script("window.scrollTo(0, 1500)")
I've scrolled a little bit because smartphone's label was too far to reach it (viewport too small).