from django.conf import settings
from behave import given, then, when, use_step_matcher
from articles.models import Article


@given(u'the fixture {fixture}')
@given(u'la fixture {fixture}')
def load_fixture(context, fixture):
    pass


use_step_matcher('re')

@when(
    r'i access the url (?P<reverse_name>\w+)'
    r'(?: on page (?P<page>\d+))?'
    r'(?: filtered on (?P<filter_name>\w+))?'
)
@when(
    r"j'accède à l'URL (?P<reverse_name>\w+)"
    r"(?: sur la page (?P<page>\d+))?"
    r"(?: filtré sur (?P<filter_name>\w+))?"
)
def reverse_url_access(context, reverse_name, page=0, filter_name=''):
    context.browser.visit(
        context.get_url(reverse_name)
        + (f'?page={page}' if page else '')
        + (f'?filter={filter_name}' if filter_name else '')
    )


use_step_matcher('parse')

@when(u'i open article {article_number}')
@when(u"que j'ouvre l'article {article_number}")
def open_article(context, article_number):
    element = context.browser.find_by_css('.btn-article')[int(article_number)]
    context.test.assertTrue(element['id'].startswith('article-'))
    context.between_step = element['id'].replace('article-', '')
    element.click()


@then(u"i have {nb_articles} articles listed")
@then(u"j'ai {nb_articles} articles de listés")
def list_articles(context, nb_articles):
    context.test.assertEqual(
        len(context.browser.find_by_css('.articles_card')),
        int(nb_articles)
    )


@then(u'i am on page {page} over {page_number}')
@then(u'je suis sur la page {page} sur {page_number}')
def test_paginations(context, page, page_number):
    context.test.assertEqual(
        context.browser.find_by_css('.page-current').first.text,
        f'Page {page} of {page_number}.'
    )


@then(u'i am redirected to {reverse_name}')
@then(u'je suis redirigé vers {reverse_name}')
def is_redirected(context, reverse_name):
    context.test.assertEqual(
        context.browser.url,
        context.get_url(reverse_name),
    )


@then(u'i am on the good article')
@then(u"je suis sur le bon article")
def is_detail_page(context):
    context.test.assertEqual(
        context.browser.find_by_tag('h3').text,
        Article.objects.get(pk=context.between_step).title
    )
    context.test.assertEqual(len(context.browser.find_by_css('.article_detail_title')), 1)
    context.test.assertEqual(len(context.browser.find_by_css('.article_detail_img')), 1)
    context.test.assertEqual(len(context.browser.find_by_css('.article_detail_content')), 1)


@then(u"i don't have article's list")
@then(u"je n'ai plus de liste d'article")
def not_articles_list(context):
    context.test.assertEqual(
        len(context.browser.find_by_css('.articles_card')),
        0
    )
