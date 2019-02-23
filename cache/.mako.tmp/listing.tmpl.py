# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1550964077.2786975
_enable_loop = True
_template_filename = '/home/luciana/anaconda3/lib/python3.7/site-packages/nikola/data/themes/bootstrap4/templates/listing.tmpl'
_template_uri = 'listing.tmpl'
_source_encoding = 'utf-8'
_exports = ['content', 'sourcelink']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('ui', context._clean_inheritance_tokens(), templateuri='ui_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'ui')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        crumbs = context.get('crumbs', UNDEFINED)
        source_link = context.get('source_link', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        files = context.get('files', UNDEFINED)
        folders = context.get('folders', UNDEFINED)
        ui = _mako_get_namespace(context, 'ui')
        code = context.get('code', UNDEFINED)
        title = context.get('title', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        crumbs = context.get('crumbs', UNDEFINED)
        source_link = context.get('source_link', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        files = context.get('files', UNDEFINED)
        folders = context.get('folders', UNDEFINED)
        ui = _mako_get_namespace(context, 'ui')
        code = context.get('code', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(ui.breadcrumbs(crumbs)))
        __M_writer('\n')
        if folders or files:
            __M_writer('<ul>\n')
            for name in folders:
                __M_writer('    <li><a href="')
                __M_writer(filters.url_escape(str(name)))
                __M_writer('">📂&nbsp;')
                __M_writer(filters.html_escape(str(name)))
                __M_writer('</a>\n')
            for name in files:
                __M_writer('    <li><a href="')
                __M_writer(filters.url_escape(str(name)))
                __M_writer('.html">📄&nbsp;')
                __M_writer(filters.html_escape(str(name)))
                __M_writer('</a>\n')
            __M_writer('</ul>\n')
        if code:
            __M_writer('<h1>')
            __M_writer(str(title))
            __M_writer('\n')
            if source_link:
                __M_writer('        <small><a href="')
                __M_writer(str(source_link))
                __M_writer('">(')
                __M_writer(str(messages("Source")))
                __M_writer(')</a></small>\n')
            __M_writer('    </h1>\n    ')
            __M_writer(str(code))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        ui = _mako_get_namespace(context, 'ui')
        source_link = context.get('source_link', UNDEFINED)
        def sourcelink():
            return render_sourcelink(context)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if source_link and show_sourcelink:
            __M_writer('    ')
            __M_writer(str(ui.show_sourcelink(source_link)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/luciana/anaconda3/lib/python3.7/site-packages/nikola/data/themes/bootstrap4/templates/listing.tmpl", "uri": "listing.tmpl", "source_encoding": "utf-8", "line_map": {"23": 3, "29": 0, "47": 2, "48": 3, "53": 24, "58": 30, "64": 4, "78": 4, "79": 5, "80": 5, "81": 6, "82": 7, "83": 8, "84": 9, "85": 9, "86": 9, "87": 9, "88": 9, "89": 11, "90": 12, "91": 12, "92": 12, "93": 12, "94": 12, "95": 14, "96": 16, "97": 17, "98": 17, "99": 17, "100": 18, "101": 19, "102": 19, "103": 19, "104": 19, "105": 19, "106": 21, "107": 22, "108": 22, "114": 26, "123": 26, "124": 27, "125": 28, "126": 28, "127": 28, "133": 127}}
__M_END_METADATA
"""
