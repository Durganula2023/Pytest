## pytest

'''
Pytest is a test framework where we can run tests
in pytest framework class name should start with test and functuon name also should start with 'test_' without test
 pytest won't recognize its tests.

 how to run ?
Pytest is mainly used to test the api's
Pytest allow you to run specifics tasks with grouping / markers
pytest "file"
pytest -m "file"
-m is for marker to run selected test cases
py.test -k <string>
-k is used to match the substring
py.test <options> "file"
python -m pytest <options> <file>
command to generate Html report "pytest --html=report.html"
 pip install allure-pytes
 pytest allows you to run the tests in parllel using pytest-xdist
 Fixtures are used when we want to run some code before every test method.
 So instead of repeating the same code in every test we define fixtures.
 Usually, fixtures are used to initialize database connections, pass the base , etc

pytest parameters
The purpose of parameterizing a test is to run a test against multiple sets of arguments.
 We can do this by @pytest.mark.parametrize

 xfail : if we don't want to display the result or skip the execution of the test case we use this
 skip : If we want to skip the execution of the test step we use this
 @pytestz.mark.skip,@pytest.mark.xfail
'''

