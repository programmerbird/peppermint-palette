# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseServerError
from ragendja.template import render_to_response
import converter


def convert(request, extension):
	import re
	colors = []
	
	# -------- parse input
	
	if 'rgb' in request.REQUEST :
		data_str = request.REQUEST['rgb']
		if re.match('(\d+(\.\d+)?)(\,(\d+(\.\d+)?)){2}(\|(\d+(\.\d+)?)(\,(\d+(\.\d+)?)){2})*$', data_str) :
			# decimal format
			str_rows = data_str.split('|')
			for str_row in str_rows :
				parts = str_row.split(',')
				colors.append({'type' : 'rgb', 'r' : int(float(parts[0])), 'g' : int(float(parts[1])), 'b' : int(float(parts[2]))})
		if re.match('[0-9a-fA-F]{6}(\|[0-9a-fA-F]{6})*$', data_str) :
			# hexadecimal format
			str_rows = data_str.split('|')
			for str_row in str_rows :
				r = int(str_row[0:2], 16)
				g = int(str_row[2:4], 16)
				b = int(str_row[4:6], 16)
				colors.append({'type' : 'rgb', 'r' : r, 'g' : g, 'b' : b})
	if 'cmyk' in request.REQUEST :
		data_str = request.REQUEST['cmyk']
		str_rows = data_str.split('|')
		for str_row in str_rows :
			parts = str_row.split(',')
			cmyk_color = {'type' : 'cmyk', 'c' : int(float(parts[0])), 'm' : int(float(parts[1])), 'y' : int(float(parts[2])), 'k' : int(float(parts[3]))}
			rgb_color = converter.cmyk_to_rgb(cmyk_color)
			colors.append(rgb_color)
	if 'hsv' in request.REQUEST :
		data_str = request.REQUEST['hsv']
		str_rows = data_str.split('|')
		for str_row in str_rows :
			parts = str_row.split(',')
			hsv_color = {'type' : 'cmyk', 'h' : int(float(parts[0])), 's' : int(float(parts[1])), 'v' : int(float(parts[2]))}
			rgb_color = converter.hsv_to_rgb(hsv_color)
			colors.append(rgb_color)
	if 'lab' in request.REQUEST :
		data_str = request.REQUEST['lab']
		str_rows = data_str.split('|')
		for str_row in str_rows :
			parts = str_row.split(',')
			lab_color = {'type' : 'lab', 'l' : int(float(parts[0])), 'a' : int(float(parts[1])), 'b' : int(float(parts[2]))}
			rgb_color = converter.lab_to_rgb(lab_color)
			colors.append(rgb_color)
	
	
	# --------- create binary
	
	result = None
	if extension == 'gpl' :
		result = converter.create_gpl_binary(colors)
	if extension == 'aco' :
		result = converter.create_aco_binary(colors)
	if extension == 'ai' :
		result = converter.create_ai_binary(colors)
	if extension == 'html' :
		result = converter.create_html_binary(colors)
	if extension == 'css' :
		result = converter.create_css_binary(colors)
	if extension == 'design.xml' :
		result = converter.create_design_xml_binary(colors)
	if extension == 'wpf.xaml' :
		result = converter.create_wpf_xaml_binary(colors)
	if extension == 'silverlight.xaml' :
		result = converter.create_silverlight_xaml_binary(colors)
	if extension == 'paint.net.txt' :
		result = converter.create_paint_net_txt_binary(colors)
	if extension == 'psp.pal' :
		result = converter.create_paintshoppro_pal_binary(colors)
	if extension == 'scribus.xml' :
		result = converter.create_scribus_xml_binary(colors)
	if extension == 'soc' :
		result = converter.create_soc_binary(colors)
	if extension == 'spl' :
		result = converter.create_spl_binary(colors)
	if extension == 'colors' :
		result = converter.create_colors_binary(colors)
	if extension == 'act' :
		result = converter.create_act_binary(colors)
	if extension == 'hpl' :
		result = converter.create_hpl_binary(colors)
	if extension == 'skp' :
		result = converter.create_skp_binary(colors)
	if extension == 'acbl' :
		result = converter.create_acbl_binary(colors)
	if extension == 'acf' :
		result = converter.create_acf_binary(colors)
	if extension == 'coreldraw4.pal' :
		result = converter.create_coreldraw4_pal_binary(colors)
		
	# --------- output
	
	return HttpResponse(result, mimetype='application/octet-stream')

def index(request):
	return render_to_response(request, 'palette/index.html', {})