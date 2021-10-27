from splinter import Browser


def before_scenario(context, scenario):
    context.between_step = None
    context.browser = Browser()
    context.fixtures = []
    for step in scenario.steps:
        if step.step_type == 'given':
            context.fixtures += [
                f"{step.name.replace(key, '')}.json"
                for key in ['la fixture ', 'the fixture ']
                if step.name.startswith(key)
            ]


def after_scenario(context, scenario):
    context.browser.quit()
