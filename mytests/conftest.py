import pytest

@pytest.fixture
def supply_AA_BB_CC():
	aa=25
	bb =25
	cc=45
	return [aa,bb,cc]