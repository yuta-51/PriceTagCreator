from PIL import Image
from PIL import ImageDraw 
# Local Imports
from .size_config import *
from .fonts import *


class StoreItem:
    def __init__(self, brand:str, name:str, price: str, unit_size:str, packaging_size: str = '', upc:str = "", ):
        """A class made to represent an item sold at a retail store."""
        self.upc = upc
        self.brand = brand.upper()
        self.name = name.upper()
        self.price = price
        self.unit_size = unit_size.upper()
        self.packaging_size = packaging_size.upper()
    

    def create_price_tag(self) -> Image:
        """Returns the price tag of the item as a PIL Image object."""

        price_tag = Image.new('RGBA', (TAG_WIDTH, TAG_HEIGHT), 'white')
        editor = ImageDraw.Draw(price_tag)

        # Calculating the bottom left and top right coordinates of the yellow item price area. 
        price_bottom_left_x = TAG_WIDTH-PRICE_WIDTH
        price_bottom_left_y = round((TAG_HEIGHT-PRICE_HEIGHT)/2)
        price_top_right_x = TAG_WIDTH+1
        price_top_right_y = price_bottom_left_y + PRICE_HEIGHT

        # Yellow Rectangle to Highlight Price
        editor.rectangle([price_bottom_left_x,price_bottom_left_y, price_top_right_x,price_top_right_y], fill ="white")
        # Brand Name
        editor.text((20, 20), self.brand, font=small_font, fill="black")
        # Item Name
        editor.text((20, 20 + pt_to_px(small_font_size)), self.name, font=medium_font, fill="black")
        # Unit Size
        editor.text((20, TAG_HEIGHT-pt_to_px(medium_font_size)), self.unit_size, font=medium_font, fill="black")
        # Packaging Size
        if self.packaging_size:
            editor.text((20, TAG_HEIGHT-(pt_to_px(medium_font_size) * 4)), self.packaging_size, font=small_font, fill="black")
        # Item Price
        editor.text((TAG_WIDTH-large_font.getsize(self.price)[0]-5, round((TAG_HEIGHT - PRICE_HEIGHT)/2)+pt_to_px(large_font_size)/4), self.price, font=large_font, fill="black")
        
        return price_tag
