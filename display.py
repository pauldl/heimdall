from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import json
import re
from settings import DEBUGGING, INVERT_COLORS

title_font = ImageFont.truetype('fonts/DidactGothic-Regular.ttf', 50)
body_font = ImageFont.truetype('fonts/DidactGothic-Regular.ttf', 24)

# Colors for flip-flopping
BLACK = 'black'
WHITE = 'white'
if (INVERT_COLORS):
	BLACK = 'white'
	WHITE = 'black'

screen = Image.new('1', (480, 800), color=WHITE)

f = open('events.json')
data = json.load(f)

today = datetime.today()
#title = today.strftime('%a, %b %d, %Y')
title = "Captain's Schedule"

title_size = title_font.getsize(title)

# Screen Dimensions for calculating
xmin = 0
ymin = 0
ymax = 799
xmax = 479

# Desired screen edge margin, in px
margin = 10
line_margin = 3
column_width = (xmax+1) / 12 # columns of 12 are helpful
side_width = column_width * 2

# Helper vars to add margins
xmargmax = xmax - margin
ymargmax = ymax - margin
xmargmin = xmin + margin
ymargmin = ymin + margin

title_max_x = column_width * 8

def wrap_text_for_font(text, base_width, font):
	line = ""
	lines = []
	width_of_line = 0
	number_of_lines = 0
	# break string into multi-lines that fit base_width
	for token in text.split():
		token = token+' '
		token_width = font.getsize(token)[0]
		if width_of_line + token_width < base_width:
			line += token
			width_of_line += token_width
		else:
			lines.append(line)
			width_of_line = 0
			line = ""
			line += token
			width_of_line += token_width
	if line:
		lines.append(line)
	return lines

d = ImageDraw.Draw(screen)

y = margin + title_size[1] + margin

body_line_size = body_font.getsize('The quick brown fox jumped over the lazy dog.')

# Header
d.text((xmargmax - title_size[0], margin), title, font=title_font, fill=BLACK)
d.rectangle([(xmin, y), (xmax, y+4)], fill=BLACK)

y += 8;

# Body
y += margin + 4

tf = (r"([+-][\d]{2}):([\d]{2})", r"\1\2", '%Y-%m-%dT%H:%M:%S%z')

cur_date = None

for event in data['events']:
	if re.match(r"^Canceled", event['title']):
		continue
	title_lines = wrap_text_for_font(event['title'], title_max_x - margin - side_width, body_font)
	time_start = datetime.strptime(re.sub(tf[0], tf[1], event['dtstart']), tf[2])
	time_end = datetime.strptime(re.sub(tf[0], tf[1], event['dtend']), tf[2])
	time_string = '%s - %s' % (time_start.strftime('%-I:%M'), time_end.strftime('%-I:%M%p'))
	time_size = body_font.getsize(time_string)
	
	date_string = time_start.strftime('%b %d')
	if (cur_date != date_string):
		cur_date = date_string
		date_size = body_font.getsize(date_string)
		d.text((side_width - date_size[0] - 2, y), date_string, font=body_font, fill=BLACK)
		d.line([(0, y - 2), (side_width, y-2)], fill=BLACK, width=2)
		
	d.text((xmargmax-time_size[0], y), time_string, font=body_font, fill=BLACK)
	for line in title_lines:
		d.text((side_width + margin, y), line, font=body_font, fill=BLACK)
		y += body_line_size[1] + line_margin
	y += line_margin * 6
	if (y > ymax):
		break

if (DEBUGGING):
	screen.show()

screen.save("screen.bmp", "BMP")
