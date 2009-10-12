def create_html_binary(colors):
	"""
		HTML table
	"""
	from cStringIO import StringIO
	file_str = StringIO()
	
	file_str.write("""<html><body>
	<table border="1">
	<tr>
		<th></th><th></th><th>Decimal</th><th>HEX</th>
	</tr>""")

	row_num = 0
	for color in colors :
		row_num += 1
		if color['type'] == 'rgb' :
			file_str.write("""<tr><td>%d</td><td width="20" height="20" bgcolor="%02X%02X%02X"></td><td>R=%d,G=%d,B=%d</td><td>#%02X%02X%02X</td></tr>"""%(row_num, color['r'], color['g'], color['b'], color['r'], color['g'], color['b'],color['r'], color['g'], color['b']))
			
	file_str.write("""</table>
	</html>""")
	
	return file_str.getvalue()
	
def create_css_binary(colors):
	"""
		CSS
	"""
	from cStringIO import StringIO
	file_str = StringIO()

	row_num = 0
	for color in colors :
		row_num += 1
		if color['type'] == 'rgb' :
			file_str.write(""".color_%d { color: #%02X%02X%02X; }\n"""%(row_num, color['r'], color['g'], color['b']))
			
	return file_str.getvalue()
	
def create_coreldraw4_pal_binary(colors):
	"""
		CorelDRAW 4
	"""
	from cStringIO import StringIO
	file_str = StringIO()

	row_num = 0
	for color in colors :
		row_num += 1
		if color['type'] == 'rgb' :
			c = rgb_to_cmyk(color)
			file_str.write(""""color%d"    %d    %d  %d    %d\n"""%(row_num, c['c'], c['m'], c['y'], c['k']))
			
	return file_str.getvalue()
	
def create_scribus_xml_binary(colors):
	"""
		Scribus
	"""
	from cStringIO import StringIO
	file_str = StringIO()
	
	file_str.write("""<?xml version="1.0" encoding="UTF-8"?>\n<swatch>\n""")

	row_num = 0
	for color in colors :
		row_num += 1
		if color['type'] == 'rgb' :
			file_str.write("""<COLOR RGB="#%02x%02x%02x"    NAME="color%d" />\n"""%(color['r'], color['g'], color['b'], row_num))

	file_str.write("""</swatch>""")
			
	return file_str.getvalue()
	
def create_skp_binary(colors):
	"""
		sK1
	"""
	from cStringIO import StringIO
	file_str = StringIO()
	
	file_str.write("""<?xml version="1.0" encoding="utf-8"?>
<palette>
	<description type="CMYK" name="Standart CMYK Palette" />
""")

	row_num = 0
	for color in colors :
		row_num += 1
		if color['type'] == 'rgb' :
			c = rgb_to_cmyk(color)
			file_str.write("""<color c="%.5f" m="%.5f" y="%.5f" k="%.5f" name="color%d" />\n"""%(c['c']/100.0, c['m']/100.0, c['y']/100.0, c['k']/100.0, row_num))

	file_str.write("""</palette>""")
			
	return file_str.getvalue()
	
def create_acbl_binary(colors):
	"""
		ACBL (Adobe Color Book Legacy)

			Adobe Creative Suite 3

			PANTONE opaque couch?.acbl (Adobe Illustrator CS3)
	"""
	from cStringIO import StringIO
	file_str = StringIO()
	
	file_str.write("""<?xml version="1.0" encoding="UTF-8"?>
<AdobeSwatchbook Version="1" BookID="3002">
	<PrefixPostfixPairs>
		<PrefixPostfixPair Prefix="PANTONE " Postfix=" C"/>
		<PrefixPostfixPair ID="LegacyCVC" Prefix="PANTONE " Postfix=" CVC"/>
		</PrefixPostfixPairs>
	<Formats>
		<Format ColorSpace="CMYK" Encoding="Float" Channels="4" ID="0"/>
		</Formats>
	<Swatches>
""")

	row_num = 0
	for color in colors :
		row_num += 1
		if color['type'] == 'rgb' :
			c = rgb_to_cmyk(color)
			file_str.write("""		<Sp N="color%d"><C>%f %f %f %f</C></Sp>\n"""%(row_num, c['c'], c['m'], c['y'], c['k']))

	file_str.write("""		</Swatches>
	</AdobeSwatchbook>
""")
			
	return file_str.getvalue()
	
def create_acf_binary(colors):
	"""
		ASCII Color Format
		Aldus/Adobe PageMaker + Aldus/Macromedia/Adobe Freehand + Adobe FrameMaker
	"""
	from cStringIO import StringIO
	file_str = StringIO()
	
	file_str.write(("""ACF 1.0
My Color Library
LibraryVersion: 1.0
Copyright: 
AboutMessage: 
Names: Partial
Rows: 4
Columns: 4
Entries: %d
Prefix:
Suffix:
Type: Process
Models: CMYK RGB
PreferredModel: RGB
Data:
""")%(len(colors)))

	row_num = 0
	for color in colors :
		row_num += 1
		if color['type'] == 'rgb' :
			c = rgb_to_cmyk(color)
			file_str.write("""%f %f %f %f
%d %d %d
color%d
"""%(c['c']/100.0, c['m']/100.0, c['y']/100.0, c['k']/100.0, color['r'] * 256, color['g'] * 256, color['b'] * 256, row_num))
			
	return file_str.getvalue()
	
def create_soc_binary(colors):
	"""
		OpenOffice.org
	"""
	from cStringIO import StringIO
	file_str = StringIO()
	
	file_str.write("""<?xml version="1.0" encoding="UTF-8"?>\n<office:color-table xmlns:office="http://openoffice.org/2000/office" xmlns:style="http://openoffice.org/2000/style" xmlns:text="http://openoffice.org/2000/text" xmlns:table="http://openoffice.org/2000/table" xmlns:draw="http://openoffice.org/2000/drawing" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:meta="http://openoffice.org/2000/meta" xmlns:number="http://openoffice.org/2000/datastyle" xmlns:svg="http://www.w3.org/2000/svg" xmlns:chart="http://openoffice.org/2000/chart" xmlns:dr3d="http://openoffice.org/2000/dr3d" xmlns:math="http://www.w3.org/1998/Math/MathML" xmlns:form="http://openoffice.org/2000/form" xmlns:script="http://openoffice.org/2000/script" xmlns:config="http://openoffice.org/2001/config">\n""")

	row_num = 0
	for color in colors :
		row_num += 1
		if color['type'] == 'rgb' :
			file_str.write(""" <draw:color draw:name="0-0-0-%d" draw:color="#%02x%02x%02x"/>\n"""%(row_num, color['r'], color['g'], color['b']))

	file_str.write("""</office:color-table>""")
			
	return file_str.getvalue()
	
def create_spl_binary(colors):
	"""
		Skencil
	"""
	from cStringIO import StringIO
	file_str = StringIO()
	
	file_str.write("""##Sketch RGBPalette 0\n""")

	row_num = 0
	for color in colors :
		row_num += 1
		if color['type'] == 'rgb' :
			file_str.write("""%.06f %.06f %.06f	color%d\n"""%(color['r']/255.0, color['g']/255.0, color['b']/255.0, row_num))
			
	return file_str.getvalue()
	
def create_colors_binary(colors):
	"""
		KOffice
	"""
	from cStringIO import StringIO
	file_str = StringIO()
	
	file_str.write("""KDE RGB Palette\n""")

	row_num = 0
	for color in colors :
		row_num += 1
		if color['type'] == 'rgb' :
			file_str.write("""%d %d %d	color%d\n"""%(color['r'], color['g'], color['b'], row_num))
			
	return file_str.getvalue()
	
def create_hpl_binary(colors):
	"""
		Allaire Homesite / ColdFusion
	"""
	from cStringIO import StringIO
	file_str = StringIO()
	
	file_str.write("""Palette\nVersion 4.0\n\n""")

	row_num = 0
	for color in colors :
		row_num += 1
		if color['type'] == 'rgb' :
			file_str.write("""%d %d %d\n"""%(color['r'], color['g'], color['b']))
			
	return file_str.getvalue()
	
def create_act_binary(colors):
	"""
		Adobe Color Table
	"""
	from cStringIO import StringIO
	from struct import pack
	
	file_str = StringIO()
	
	row_num = 0
	for color in colors :
		row_num += 1
		if color['type'] == 'rgb' :
			file_str.write(pack("BBB",color['r'], color['g'], color['b']))
			
	while row_num < 256 :
		row_num += 1
		file_str.write(pack('BBB',0,0,0))
			
	return file_str.getvalue()
	

def create_wpf_xaml_binary(colors):
	"""
		WPF
	"""
	
	from cStringIO import StringIO
	file_str = StringIO()
	
	file_str.write("""<ResourceDictionary xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">\n""")
	
	row_num = 0
	for color in colors :
		row_num += 1
		if color['type'] == 'rgb' :
			file_str.write("""<SolidColorBrush x:Key="Brush%d" Color="#FF%02X%02X%02X" />\n"""%(row_num, color['r'], color['g'], color['b']))
			
	file_str.write("""</ResourceDictionary>""")
			
	return file_str.getvalue()
	
def create_silverlight_xaml_binary(colors):
	"""
		Silverlight
	"""
	
	from cStringIO import StringIO
	file_str = StringIO()
	
	file_str.write("""<!-- paste the code below in the Application.Resources section of your App.xaml -->\n""")
	
	row_num = 0
	for color in colors :
		row_num += 1
		if color['type'] == 'rgb' :
			file_str.write("""<SolidColorBrush x:Key="Brush%d" Color="#FF%02X%02X%02X" />\n"""%(row_num, color['r'], color['g'], color['b']))
			
	file_str.write("""</ResourceDictionary>""")
			
	return file_str.getvalue()
	
def create_paint_net_txt_binary(colors):
	"""
		Paint.NET
	"""
	
	from cStringIO import StringIO
	file_str = StringIO()
	
	file_str.write(""";comment\n""")
	
	row_num = 0
	for color in colors :
		row_num += 1
		if color['type'] == 'rgb' :
			file_str.write("""%02X%02X%02X\n"""%(color['r'], color['g'], color['b']))
			
	return file_str.getvalue()
	
def create_paintshoppro_pal_binary(colors):
	"""
		Paint Shop Pro
	"""
	
	from cStringIO import StringIO
	file_str = StringIO()
	
	file_str.write("""JASC-PAL\n0100\n256\n""")
	
	row_num = 0
	for color in colors :
		row_num += 1
		if color['type'] == 'rgb' :
			file_str.write("""%d %d %d\n"""%(color['r'], color['g'], color['b']))
			
	while row_num < 256 :
		row_num += 1
		file_str.write("0 0 0\n")
			
	return file_str.getvalue()
	
def create_design_xml_binary(colors):
	"""
		Expression Design
	"""
	
	from cStringIO import StringIO
	file_str = StringIO()
	
	file_str.write("""<?xml version="1.0" encoding="utf-8"?>
<SwatchLibrary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" Name="River Runs Red" xmlns="http://schemas.microsoft.com/expression/design/2007">
""")
	
	row_num = 0
	for color in colors :
		row_num += 1
		if color['type'] == 'rgb' :
			file_str.write("""<SolidColorSwatch Color="#FF%02X%02X%02X" />\n"""%(color['r'], color['g'], color['b']))
			
	file_str.write("""</SwatchLibrary>""")
			
	return file_str.getvalue()
	

def create_gpl_binary(colors, name='New Palette'):
	"""
		GIMP
	"""
	from cStringIO import StringIO
	file_str = StringIO()
	
	file_str.write("GIMP Palette\nName: %s\n#\n"%(name))
	
	for color in colors :
		if color['type'] == 'rgb' :
			file_str.write("%d %d %d %s\n"%(color['r'], color['g'], color['b'], 'Untitled'))

	return file_str.getvalue()
	
def create_aco_binary(colors, endian='big'):
	"""
		Photoshop
	"""
	from cStringIO import StringIO
	from struct import pack
	
	file_str = StringIO()
		
	endian_marker = ''
	if endian == 'big' :
		endian_marker = '>'
	if endian == 'little' : 
		endian_marker = '<'
	
	file_str.write(pack(endian_marker + 'H', 1))
	file_str.write(pack(endian_marker + 'H', len(colors)))
	
	for color in colors :
		if color['type'] == 'rgb' :
			file_str.write(pack(endian_marker + 'H',0))
			file_str.write(pack(endian_marker + 'H', color['r'] * 256))
			file_str.write(pack(endian_marker + 'H', color['g'] * 256))
			file_str.write(pack(endian_marker + 'H', color['b'] * 256))
			file_str.write(pack(endian_marker + 'H',0))
			
			
	file_str.write(pack(endian_marker + 'H', 2))
	file_str.write(pack(endian_marker + 'H', len(colors)))
	
	for color in colors :
		if color['type'] == 'rgb' :
			file_str.write(pack(endian_marker + 'H',0))
			file_str.write(pack(endian_marker + 'H', color['r'] * 256))
			file_str.write(pack(endian_marker + 'H', color['g'] * 256))
			file_str.write(pack(endian_marker + 'H', color['b'] * 256))
			file_str.write(pack(endian_marker + 'H',0))
			file_str.write(pack(endian_marker + 'H',0))
			
			file_str.write(pack(endian_marker + 'H',0)) # length color name | for ease here just 0
			# here is the place for UTF-16 representation of the name | just blank for ease here
			
			file_str.write(pack(endian_marker + 'H',0))

	return file_str.getvalue()
	
def create_ai_binary(colors):
	"""
		Illustrator
	"""
	from cStringIO import StringIO
	file_str = StringIO()
	
	file_str.write("""%!PS-Adobe-3.0
%%Creator: Adobe Illustrator(r) 6.0
%%For: (indigo go) (COLOURlovers)
%%Title: (hot robot)
%%CreationDate: (10/08/09) (03.45 AM)
%%BoundingBox: 0 0 0 0
%%HiResBoundingBox: 0 0 0 0
%%DocumentProcessColors:
%AI5_FileFormat 2.0
%AI3_ColorUsage: Color
%AI5_ArtSize: 612 792
%AI5_RulerUnits: 2
%AI5_ArtFlags: 1 0 0 1 0 0 0 1 0
%AI5_TargetResolution: 800
%AI5_NumLayers: 1
%AI3_DocumentPreview: None
%%EndComments
%%BeginProlog
%%EndProlog
%%BeginSetup
%AI5_BeginPalette
0 0 Pb
""")
	
	for color in colors :
		if color['type'] == 'rgb' :
			file_str.write("""%.14f %.14f %.14f Xa
Pc
"""%(color['r']/255.0, color['g']/255.0, color['b']/255.0))
	file_str.write("""PB
%AI5_EndPalette
%%EndSetup
%%Trailer
%%EOF""")

	return file_str.getvalue()	
	
def rgb_to_cmyk(color):
	r = color['r'] / 255.0
	g = color['g'] / 255.0
	b = color['b'] / 255.0
	
	c = 1.0 - r
	m = 1.0 - g
	y = 1.0 - b
	k = 1.0
	
	if (c < k) :
		k = c
	if (m < k) :
		k = m
	if (y < k) :
		k = y
	if k == 1.0 :
		c = 0.0
		m = 0.0
		y = 0.0
	else :
		c = (c - k) / (1.0 - k)
		m = (m - k) / (1.0 - k)
		y = (y - k) / (1.0 - k)
		
	return {'type' : 'cmyk', 'c' : int(c * 100), 'm' : int(m * 100), 'y' : int(y * 100), 'k' : int(k * 100)}
	
def cmyk_to_rgb(color):
	c = color['c'] / 100.0
	m = color['m'] / 100.0
	y = color['y'] / 100.0
	k = color['k'] / 100.0
	
	r=int((1-c)*(1-k)*255);
	b=int((1-y)*(1-k)*255);
	g=int((1-m)*(1-k)*255);
	
	return {'type' : 'rgb', 'r' : r, 'g' : g, 'b' : b}
	
def hsv_to_rgb(color):
	h = color['h'] / 359.0
	s = color['s'] / 100.0
	v = color['v'] / 100.0
	
	if s == 0.0 :
		result = {'type' : 'rgb', 'h' : h, 's' : s, 'v' : v}
	else :
		var_h = h * 6.0
		if var_h == 6.0 :
			var_h  = 0.0
		var_i = int(var_h)
		var_1 = v * (1.0 - s)
		var_2 = v * ( 1.0 - s * ( var_h - var_i ) )
		var_3 = v * ( 1.0 - s * ( 1.0 - ( var_h - var_i ) ) )
		
		if var_i == 0 :
			result = {'type'  :'rgb', 'r' : v, 'g' : var_3, 'b' : var_1}
		if var_i == 1 :
			result = {'type'  :'rgb', 'r' : var_2, 'g' : v, 'b' : var_1}
		if var_i == 2 :
			result = {'type'  :'rgb', 'r' : var_1, 'g' : v, 'b' : var_3}
		if var_i == 3 :
			result = {'type'  :'rgb', 'r' : var_1, 'g' : var_2, 'b' : v}
		if var_i == 4 :
			result = {'type'  :'rgb', 'r' : var_3, 'g' : var_1, 'b' : v}
		if not var_i in [0,1,2,3,4] :
			result = {'type'  :'rgb', 'r' : v, 'g' : var_1, 'b' : var_2}
			
	result['r'] = min(255, max(0, int(result['r']  *255)))
	result['g'] = min(255, max(0, int(result['g']  *255)))
	result['b'] = min(255, max(0, int(result['b']  *255)))
	return result

def lab_to_rgb(color):
	REF_X = 95.047
	REF_Y = 100.000
	REF_Z = 108.882

	y = (color['l']+16.0)/116.0;
	x = (float(color['a']) / 500.0)+y;
	z = y - float(color['b']) / 200.0;
	
	
	if y ** 3  > 0.008856 :
		y = y ** 3
	else :
		y = ( y - 16.0 / 116.0 ) / 7.787
	if x ** 3 > 0.008856 :
		x = x ** 3
	else :
		x = ( x - 16.0 / 116.0 ) / 7.787
	if z ** 3 > 0.008856  :
		z = z ** 3
	else :
		z = ( z - 16.0 / 116.0 ) / 7.787
	
	x = REF_X * x     
	y = REF_Y * y 
	z = REF_Z * z 
	
	x = x / 100.0
	y = y / 100.0
	z = z / 100.0
	
	r = x * 3.2406 + y * -1.5372 + z * -0.4986
	g = x * -0.9689 + y * 1.8758 + z * 0.0415
	b = x * 0.0557 + y * -0.2040 + z * 1.0570
	
	if ( r > 0.0031308 ) :
		r = 1.055 * ( r ** ( 1 / 2.4 ) ) - 0.055
	else :
		r = 12.92 * r
	if ( g > 0.0031308 ) :
		g = 1.055 * ( g ** ( 1 / 2.4 ) ) - 0.055
	else :
		g = 12.92 * g
	if ( b > 0.0031308 ) :
		b = 1.055 * ( b ** ( 1 / 2.4 ) ) - 0.055
	else :
		b = 12.92 * b
	
	return {'type' : 'rgb', 'r' : min(255, max(0, int(r  *255))), 'g' : min(255, max(0, int(g  *255))), 'b' : min(255, max(0, int(b  *255)))}