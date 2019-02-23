# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1550964076.8726192
_enable_loop = True
_template_filename = '/home/luciana/anaconda3/lib/python3.7/site-packages/nikola/data/themes/bootblog4/templates/base.tmpl'
_template_uri = 'base.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'belowtitle', 'sourcelink', 'before_content', 'content', 'extra_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

    ns = runtime.TemplateNamespace('notes', context._clean_inheritance_tokens(), templateuri='annotation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'notes')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        momentjs_locales = _import_ns.get('momentjs_locales', context.get('momentjs_locales', UNDEFINED))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        theme_config = _import_ns.get('theme_config', context.get('theme_config', UNDEFINED))
        date_fanciness = _import_ns.get('date_fanciness', context.get('date_fanciness', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        def belowtitle():
            return render_belowtitle(context._locals(__M_locals))
        def before_content():
            return render_before_content(context._locals(__M_locals))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        js_date_format = _import_ns.get('js_date_format', context.get('js_date_format', UNDEFINED))
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        navigation_alt_links = _import_ns.get('navigation_alt_links', context.get('navigation_alt_links', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer(str(set_locale(lang)))
        __M_writer('\n')
        __M_writer(str(base.html_headstart()))
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n')
        __M_writer(str(template_hooks['extra_head']()))
        __M_writer('\n</head>\n<body>\n<a href="#content" class="sr-only sr-only-focusable">')
        __M_writer(str(messages("Skip to main content")))
        __M_writer('</a>\n\n<!-- Header and menu bar -->\n<div class="container">\n      <header class="blog-header py-3">\n        <div class="row nbb-header align-items-center">\n          <div class="col-md-3 col-xs-2 col-sm-2" style="width: auto;">\n            <button class="navbar-toggler navbar-light bg-light nbb-navbar-toggler" type="button" data-toggle="collapse" data-target=".bs-nav-collapsible" aria-controls="bs-navbar" aria-expanded="false" aria-label="Toggle navigation">\n                <span class="navbar-toggler-icon"></span>\n            </button>\n            <div class="collapse bs-nav-collapsible bootblog4-search-form-holder">\n                ')
        __M_writer(str(search_form))
        __M_writer('\n            </div>\n        </div>\n          <div class="col-md-6 col-xs-10 col-sm-10 bootblog4-brand" style="width: auto;">\n            <a class="navbar-brand blog-header-logo text-dark" href="')
        __M_writer(str(abs_link(_link("root", None, lang))))
        __M_writer('">\n')
        if logo_url:
            __M_writer('            <img src="')
            __M_writer(str(logo_url))
            __M_writer('" alt="')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('" id="logo" class="d-inline-block align-top">\n')
        __M_writer('\n')
        if show_blog_title:
            __M_writer('            <span id="blog-title">')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</span>\n')
        __M_writer('        </a>\n          </div>\n            <div class="col-md-3 justify-content-end align-items-center bs-nav-collapsible collapse flex-collapse bootblog4-right-nav">\n            <nav class="navbar navbar-light bg-white">\n            <ul class="navbar-nav bootblog4-right-nav">\n                    ')
        __M_writer(str(base.html_navigation_links_entries(navigation_alt_links)))
        __M_writer('\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'belowtitle'):
            context['self'].belowtitle(**pageargs)
        

        __M_writer('\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('\n                    ')
        __M_writer(str(template_hooks['menu_alt']()))
        __M_writer('\n            </ul></nav>\n            </div>\n    </div>\n</header>\n\n<nav class="navbar navbar-expand-md navbar-light bg-white static-top">\n        <div class="collapse navbar-collapse bs-nav-collapsible" id="bs-navbar">\n            <ul class="navbar-nav nav-fill d-flex w-100">\n                ')
        __M_writer(str(base.html_navigation_links_entries(navigation_links)))
        __M_writer('\n                ')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\n            </ul>\n        </div><!-- /.navbar-collapse -->\n</nav>\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'before_content'):
            context['self'].before_content(**pageargs)
        

        __M_writer('\n</div>\n\n<div class="container" id="content" role="main">\n    <div class="body-content">\n')
        if theme_config.get('sidebar'):
            __M_writer('            <div class="row"><div class="col-md-8 blog-main">\n')
        __M_writer('        <!--Body content-->\n        ')
        __M_writer(str(template_hooks['page_header']()))
        __M_writer('\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n        <!--End of body content-->\n')
        if theme_config.get('sidebar'):
            __M_writer('        </div><aside class="col-md-4 blog-sidebar">')
            __M_writer(str(theme_config.get('sidebar')))
            __M_writer('</aside></div>\n')
        __M_writer('\n        <footer id="footer">\n            ')
        __M_writer(str(content_footer))
        __M_writer('\n            ')
        __M_writer(str(template_hooks['page_footer']()))
        __M_writer('\n        </footer>\n    </div>\n</div>\n\n')
        __M_writer(str(base.late_load_js()))
        __M_writer('\n')
        if date_fanciness != 0:
            __M_writer('        <!-- fancy dates -->\n        <script>\n        moment.locale("')
            __M_writer(str(momentjs_locales[lang]))
            __M_writer('");\n        fancydates(')
            __M_writer(str(date_fanciness))
            __M_writer(', ')
            __M_writer(str(js_date_format))
            __M_writer(');\n        </script>\n        <!-- end fancy dates -->\n')
        __M_writer('    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer("\n    <script>\n    baguetteBox.run('div#content', {\n        ignoreClass: 'islink',\n        captions: function(element) {\n            return element.getElementsByTagName('img')[0].alt;\n    }});\n    </script>\n")
        __M_writer(str(body_end))
        __M_writer('\n')
        __M_writer(str(template_hooks['body_end']()))
        __M_writer('\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_belowtitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        def belowtitle():
            return render_belowtitle(context)
        base = _mako_get_namespace(context, 'base')
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            __M_writer('                        ')
            __M_writer(str(base.html_translations()))
            __M_writer('\n')
        __M_writer('                    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_before_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        def before_content():
            return render_before_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/luciana/anaconda3/lib/python3.7/site-packages/nikola/data/themes/bootblog4/templates/base.tmpl", "uri": "base.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 0, "70": 2, "71": 3, "72": 4, "73": 4, "74": 5, "75": 5, "80": 8, "81": 9, "82": 9, "83": 12, "84": 12, "85": 23, "86": 23, "87": 27, "88": 27, "89": 28, "90": 29, "91": 29, "92": 29, "93": 29, "94": 29, "95": 31, "96": 32, "97": 33, "98": 33, "99": 33, "100": 35, "101": 40, "102": 40, "107": 45, "112": 46, "113": 47, "114": 47, "115": 56, "116": 56, "117": 57, "118": 57, "123": 61, "124": 66, "125": 67, "126": 69, "127": 70, "128": 70, "133": 71, "134": 73, "135": 74, "136": 74, "137": 74, "138": 76, "139": 78, "140": 78, "141": 79, "142": 79, "143": 84, "144": 84, "145": 85, "146": 86, "147": 88, "148": 88, "149": 89, "150": 89, "151": 89, "152": 89, "153": 93, "158": 93, "159": 101, "160": 101, "161": 102, "162": 102, "168": 6, "177": 6, "183": 41, "195": 41, "196": 42, "197": 43, "198": 43, "199": 43, "200": 45, "206": 46, "220": 61, "234": 71, "248": 93, "262": 248}}
__M_END_METADATA
"""
