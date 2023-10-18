import pytest
import json
import requests


def test_login_valid(supply_url):
    url = supply_url + "/login/"
    data = {'email':'test@test.com','password':'something'}
    res = requests.post(url,data=data)
    j = json.loads(res.text)
    assert res.status_code == 200, res.text
    assert j['token'] == "QpwL5tke4Pnpja7X", res.text


def test_login_no_password(supply_url):
    url = supply_url + "/login/"
    data = {'email': 'test@test.com'}
    res = requests.post(url,data=data)
    j = json.loads(res.text)
    assert res.status_code == 200,res.text
    assert j['error'] == 'Missing password',res.text


def test_login_no_email(supply_url):
    url = supply_url + "/login/"
    data = {}
    resp = requests.post(url, data=data)
    j = json.loads(resp.text)
    assert resp.status_code == 400, resp.text
    assert j['error'] == "Missing email or username", resp.text