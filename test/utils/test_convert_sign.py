# import pytest
# from utils.convert_sign import *

# @pytest.mark.parametrize("input,expected", [
#     ("\U0001D800", "\\U0001D800"),# single unicode
#     ("a", "\\U00061"),# single base (not the right code format)
#     ("\U0001D800\U0001DA9C\U0001DAAB", "\\U0001D800\\U0001DA9C\\U0001DAAB"),# multiple unicode
#     ("", ""),# single base
#     ("", ""),# mix
#     ("", ""),# empty string
# ])
# def test_uni_to_hex(input, expected):
#     assert sign_fsw_to_swu(input) == expected

# @pytest.mark.parametrize("input,expected", [
#     ("", ""),# single unicode
#     ("", ""),# single base
#     ("", ""),# multiple unicode
#     ("", ""),# single base
#     ("", ""),# mix
#     ("", ""),# empty string
# ])
# def test_sign_fsw_to_swu(input, expected):
#     assert sign_fsw_to_swu(input) == expected

# @pytest.mark.parametrize("input,expected", [
#     ("", ""),# single unicode
#     ("", ""),# single base
#     ("", ""),# multiple unicode
#     ("", ""),# single base
#     ("", ""),# mix
#     ("", ""),# empty string
# ])
# def test_sign_swu_to_fsw(input, expected):
#     assert sign_swu_to_fsw(input) == expected
    
# @pytest.mark.parametrize("input,expected", [
#     ("", ""),# single unicode
#     ("", ""),# single base
#     ("", ""),# multiple unicode
#     ("", ""),# single base
#     ("", ""),# mix
#     ("", ""),# empty string
# ])
# def test_sign_fsw_to_fru_core(input, expected):
#     assert sign_fsw_to_fru_core(input) == expected
    
# @pytest.mark.parametrize("input,expected", [
#     ("", ""),# single unicode
#     ("", ""),# single base
#     ("", ""),# multiple unicode
#     ("", ""),# single base
#     ("", ""),# mix
#     ("", ""),# empty string
# ])
# def test_sign_fsw_to_fru_fill(input, expected):
#     assert sign_fsw_to_swu(input) == expected
    
# @pytest.mark.parametrize("input,expected", [
#     ("", ""),# single unicode
#     ("", ""),# single base
#     ("", ""),# multiple unicode
#     ("", ""),# single base
#     ("", ""),# mix
#     ("", ""),# empty string
# ])
# def test_sign_fsw_to_fru_rot(input, expected):
#     assert sign_fsw_to_swu(input) == expected
    
# @pytest.mark.parametrize("input,expected", [
#     ("", ""),# single unicode
#     ("", ""),# single base
#     ("", ""),# multiple unicode
#     ("", ""),# single base
#     ("", ""),# mix
#     ("", ""),# empty string
# ])
# def test_sign_fsw_to_fru(input, expected):
#     assert sign_fsw_to_swu(input) == expected
    
# @pytest.mark.parametrize("input,expected", [
#     ("", ""),# single unicode
#     ("", ""),# single base
#     ("", ""),# multiple unicode
#     ("", ""),# single base
#     ("", ""),# mix
#     ("", ""),# empty string
# ])
# def test_sign_fru_to_fsw(input, expected):
#     assert sign_fsw_to_swu(input) == expected
    
# @pytest.mark.parametrize("input,expected", [
#     ("", ""),# single unicode
#     ("", ""),# single base
#     ("", ""),# multiple unicode
#     ("", ""),# single base
#     ("", ""),# mix
#     ("", ""),# empty string
# ])
# def test_sign_fru_to_swu(input, expected):
#     assert sign_fsw_to_swu(input) == expected
    
# @pytest.mark.parametrize("input,expected", [
#     ("", ""),# single unicode
#     ("", ""),# single base
#     ("", ""),# multiple unicode
#     ("", ""),# single base
#     ("", ""),# mix
#     ("", ""),# empty string
# ])
# def test_sign_swu_to_fru(input, expected):
#     assert sign_fsw_to_swu(input) == expected
    
# @pytest.mark.parametrize("input,expected", [
#     ("", ""),# single unicode
#     ("", ""),# single base
#     ("", ""),# multiple unicode
#     ("", ""),# single base
#     ("", ""),# mix
#     ("", ""),# empty string
# ])