# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1550964029.3776588
_enable_loop = True
_template_filename = 'templates/book.tmpl'
_template_uri = 'book.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'extra_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('pheader', context._clean_inheritance_tokens(), templateuri='post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pheader')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        post = context.get('post', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        parent = context.get('parent', UNDEFINED)
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer("\n    <link href='https://fonts.googleapis.com/css?family=Gentium+Book+Basic' rel='stylesheet' type='text/css'>\n    <style>\n        .smallcaps {\n            font-variant: small-caps;\n        }\n        .chapter {\n            width: 100%;\n            padding: 10px;\n            -webkit-column-gap: 40px;\n               -moz-column-gap: 40px;\n                    column-gap: 40px;\n            -webkit-column-width: 400px;\n               -moz-column-width: 400px;\n                    column-width: 400px;\n            -webkit-column-count: 2;\n               -moz-column-count: 2;\n                    column-count: 2;\n            -webkit-column-rule: 1px solid #ddd;\n               -moz-column-rule: 1px solid #ddd;\n                    column-rule: 1px solid #ddd;\n            height: 90vh;\n            font-family: 'Gentium Book Basic', serif;\n            color: #2d2e2e;\n            font-weight: 500;\n        }\n        div.frame {\n            overflow: hidden;\n            padding: 0;\n            margin: 0;\n        }\n        div.scrolling-cont {\n            overflow-x: scroll;\n            padding: 0;\n            margin: 0;\n        }\n        h1, h2, h3, h4 {\n            text-align: center;\n            width: 100%;\n            font-family: 'Gentium Book Basic', serif;\n            font-size: 120%;\n            font-weight: 900;\n        }\n        h1 {\n            font-size: 150%;\n        }\n        .subtitle {\n            text-align: center;\n            width: 100%;\n        }\n        .bookfig {\n            width: 100%;\n            height: auto;\n            max-width: 100%;\n            max-height: 100%;\n        }\n        div.figure {\n            height: 88vh;\n            margin: 0;\n        }\n        div.topic {\n            margin: 0;\n        }\n        div.section > p {\n            text-indent: 1em;\n            margin-bottom: 0;\n            text-align: justify;\n        }\n    </style>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<article class="storypage" itemscope="itemscope" itemtype="http://schema.org/Article">\n    <div class="frame">\n    <div class="scrolling-cont" id="scrolling-cont" name="scrolling-cont">\n    <div class="e-content entry-content chapter" itemprop="articleBody text">\n    <h1>')
        __M_writer(str(post.title()))
        __M_writer('</h1>\n    ')
        __M_writer(str(post.text()))
        __M_writer('\n    </div>\n    </div>\n    </div>\n</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        __M_writer('\n    <script src="https://cdnjs.cloudflare.com/ajax/libs/Flowtype.js/1.1.0/flowtype.min.js"></script>\n    <script>\n        $(\'#scrolling-cont\').flowtype({\n            minimum: 500,\n            maximum: 1200,\n            minFont: 20,\n            maxFont: 40,\n            fontRatio: 50\n        });\n        $(document).ready(function() {\n            var elem = $(\'#scrolling-cont\');\n            elem.click(function(event) {\n                var x1 = elem.position().left;\n                var pw = elem.width() + 20;\n                var x2 = event.pageX;\n                if (x2 - x1 < pw / 2) {\n                    pw = -pw;\n                }\n                elem.animate({\n                    scrollLeft: \'+=\' + pw\n                }, 500)\n            });\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "templates/book.tmpl", "uri": "book.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "35": 0, "48": 2, "49": 3, "50": 4, "51": 5, "56": 77, "61": 90, "66": 117, "72": 7, "79": 7, "80": 8, "81": 8, "87": 79, "94": 79, "95": 84, "96": 84, "97": 85, "98": 85, "104": 92, "110": 92, "116": 110}}
__M_END_METADATA
"""
