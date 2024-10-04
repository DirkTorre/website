you can set up test data using the class method [SetUpTestData()](https://docs.djangoproject.com/en/5.1/topics/testing/tools/#django.test.TestCase.setUpTestData)

but you can also use [fixtures](https://docs.djangoproject.com/en/5.1/topics/db/fixtures/#fixtures-explanation)

you can use multiple test databases.

you can override the settings

if you don't want database data to be shared between apps in a test, you can isolate the whole app using: @isolate_apps("app_label")

there are asserts specificily for formss, which also allows adding multiple values to test in one go!

you can give tests a tag, so you can include and exclude tetsts when you want to.

it's possible to skip tests using  @skipIf and @skipUnless.