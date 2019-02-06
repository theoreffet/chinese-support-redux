# Copyright © 2012 Thomas TEMPÉ <thomas.tempe@alysse.org>
# Copyright © 2017-2019 Joseph Lorimer <luoliyan@posteo.net>
#
# This file is part of Chinese Support Redux.
#
# Chinese Support Redux is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# Chinese Support Redux is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# Chinese Support Redux.  If not, see <https://www.gnu.org/licenses/>.

from re import compile, IGNORECASE

vowel_decorations = [
    {},
    {'a': 'ā', 'e': 'ē', 'i': 'ī', 'o': 'ō', 'u': 'ū', 'ü': 'ǖ', 'v': 'ǖ'},
    {'a': 'á', 'e': 'é', 'i': 'í', 'o': 'ó', 'u': 'ú', 'ü': 'ǘ', 'v': 'ǘ'},
    {'a': 'ǎ', 'e': 'ě', 'i': 'ǐ', 'o': 'ǒ', 'u': 'ǔ', 'ü': 'ǚ', 'v': 'ǚ'},
    {'a': 'à', 'e': 'è', 'i': 'ì', 'o': 'ò', 'u': 'ù', 'ü': 'ǜ', 'v': 'ǜ'},
    {'a': 'a', 'e': 'e', 'i': 'i', 'o': 'o', 'u': 'u', 'ü': 'ü', 'v': 'ü'},
]

accents = 'ɑ̄āĀáɑ́ǎɑ̌ÁǍàɑ̀ÀēĒéÉěĚèÈīĪíÍǐǏìÌōŌóÓǒǑòÒūŪúÚǔǓùÙǖǕǘǗǚǙǜǛ'

pinyin_inits = "zh|sh|ch|[bpmfdtnlgkhjqxrzscwy]"
pinyin_finals = "i[ōóǒòo]ng|[ūúǔùu]ng|[āáǎàa]ng|[ēéěèe]ng|i[āɑ̄áɑ́ɑ́ǎɑ̌àɑ̀aāáǎàa]ng|[īíǐìi]ng|i[āáǎàa]n|u[āáǎàa]n|[ōóǒòo]ng|[ēéěèe]r|i[āáǎàa]|i[ēéěèe]|i[āáǎàa]o|i[ūúǔùu]|[īíǐìi]n|u[āáǎàa]|u[ōóǒòo]|u[āáǎàa]i|u[īíǐìi]|[ūúǔùu]n|u[ēéěèe]|ü[ēéěèe]|v[ēéěèe]|i[ōóǒòo]|[āáǎàa]i|[ēéěèe]i|[āáǎàa]o|[ōóǒòo]u|[āáǎàa]n|[ēéěèe]n|[āáǎàa]|[ēéěèe]|[ōóǒòo]|[īíǐìi]|[ūúǔùu]|[ǖǘǚǜüv]"
pinyin_standalones = "'[āáǎàa]ng|'[ēéěèe]ng|'[ēéěèe]r|'[āáǎàa]i|'[ēéěèe]i|'[āáǎàa]o|'[ōóǒòo]u|'[āáǎàa]n|'[ēéěèe]n|'[āáǎàa]|'[ēéěèe]|'[ōóǒòo]"
jyutping_inits = "ng|gw|kw|[bpmfdtnlgkhwzcsj]"
jyutping_finals = "i|ip|it|ik|im|in|ing|iu|yu|yut|yun|u|up|ut|uk|um|un|ung|ui|e|ep|et|ek|em|en|eng|ei|eu|eot|eon|eoi|oe|oet|oek|oeng|oei|o|ot|ok|om|on|ong|oi|ou|ap|at|ak|am|an|ang|ai|au|aa|aap|aat|aak|aam|aan|aang|aai|aau|m|ng"
jyutping_standalones = "'uk|'ung|'e|'ei|'oe|'o|'ok|'om|'on|'ong|'oi|'ou|'ap|'at|'ak|'am|'an|'ang|'ai|'au|'aa|'aap|'aat|'aak|'aam|'aan|'aang|'aai|'aau|'m|'ng"

HANZI_RANGE = r'\u3400-\u9fff'
BOPOMOFO_RANGE = r'\u3100-\u312F'
bopomofo_regex = f'[{BOPOMOFO_RANGE}]'
hanzi_regex = f'[{HANZI_RANGE}]'

TONE_SUPERS = '¹²³⁴⁵⁶⁷⁸⁹'
CMN_TONE_NUMBERS = '1-5¹²³⁴⁵'
YUE_TONE_NUMBERS = '1-7¹²³⁴⁵⁶⁷'
TONE_NUMBERS = f'{CMN_TONE_NUMBERS}{YUE_TONE_NUMBERS}'
tone_number_regex = f'[{TONE_NUMBERS}]'
tone_superscript_regex = r'[{TONE_SUPERS}]'

sound_tag_regex = r'\[sound:.*?\]'

ruby_regex = r'([%s]\[\s*)([a-zü%s]+[%s]?)(.*?\])' % (
    HANZI_RANGE,
    accents,
    TONE_NUMBERS,
)
half_ruby_regex = f'([A-Za-zü{accents}]+[{TONE_NUMBERS}]?)'
pinyin_regex = (
    f'([A-Za-zü{BOPOMOFO_RANGE}{accents}]+[{CMN_TONE_NUMBERS}ˊˇˋ˙]?)'
)
not_pinyin_regex = (
    f'([^A-Za-zü{BOPOMOFO_RANGE}{accents}{CMN_TONE_NUMBERS}ˊˇˋ˙])'
)

TRANSCRIPT_SPLIT_TEMPLATE_BASE = (
    '(({initials})({finals})[{tones}]?|({standalones})[{tones}]?)'
)

PINYIN_SPLIT_TEMPLATE = TRANSCRIPT_SPLIT_TEMPLATE_BASE.format(
    initials=pinyin_inits,
    finals=pinyin_finals,
    standalones=pinyin_standalones,
    tones=CMN_TONE_NUMBERS,
)
JYUTPING_SPLIT_TEMPLATE = TRANSCRIPT_SPLIT_TEMPLATE_BASE.format(
    initials=jyutping_inits,
    finals=jyutping_finals,
    standalones=jyutping_standalones,
    tones=YUE_TONE_NUMBERS,
)

TRANSCRIPT_SPLIT_TEMPLATE = '(?P<one>{pattern})(?P<two>{pattern})'

pinyin_split_regex = compile(
    TRANSCRIPT_SPLIT_TEMPLATE.format(pattern=PINYIN_SPLIT_TEMPLATE), IGNORECASE
)
jyutping_split_regex = compile(
    TRANSCRIPT_SPLIT_TEMPLATE.format(pattern=JYUTPING_SPLIT_TEMPLATE),
    IGNORECASE,
)

COLOR_TEMPLATE = '<span class="tone{tone}">{chars}</span>'
COLOR_RUBY_TEMPLATE = ruby_template = (
    '<span class="tone{tone}">'
    '<ruby>{chars}<rt>{transcript}</rt></ruby>'
    '</span>'
)

# early replacements
bopomofo_replacements = [
    ('jue', 'ㄐㄩㄝ'),
    ('lue', 'ㄌㄩㄝ'),
    ('nue', 'ㄋㄩㄝ'),
    ('que', 'ㄑㄩㄝ'),
    ('juan', 'ㄐㄩㄢ'),
    ('jun', 'ㄐㄩㄣ'),
    ('quan', 'ㄑㄩㄢ'),
    ('qun', 'ㄑㄩㄣ'),
    ('v', 'u:'),
    ('wong', 'ㄨㄥ'),
    ('wu', 'u'),
    ('w', 'u'),
    ('xue', 'ㄒㄩㄝ'),
    ('xuan', 'ㄒㄩㄢ'),
    ('xun', 'ㄒㄩㄣ'),
    ('yi', 'i'),
    ('you', 'ㄧㄡ'),
    ('yue', 'ㄩㄝ'),
    ('yuan', 'ㄩㄢ'),
    ('yun', 'ㄩㄣ'),
    ('yu', 'u:'),
    ('y', 'i'),
    ('ü', 'u:'),
]

bopomofo_special = [
    ('chi', 'ㄔ'),
    ('shi', 'ㄕ'),
    ('zhi', 'ㄓ'),
    ('ci', 'ㄘ'),
    ('ju', 'ㄐㄩ'),
    ('qu', 'ㄑㄩ'),
    ('er', 'ㄦ'),
    ('ri', 'ㄖ'),
    ('si', 'ㄙ'),
    ('xu', 'ㄒㄩ'),
    ('zi', 'ㄗ'),
]

bopomofo_initials = [
    ('ch', 'ㄔ'),
    ('sh', 'ㄕ'),
    ('zh', 'ㄓ'),
    ('b', 'ㄅ'),
    ('c', 'ㄘ'),
    ('d', 'ㄉ'),
    ('f', 'ㄈ'),
    ('g', 'ㄍ'),
    ('h', 'ㄏ'),
    ('j', 'ㄐ'),
    ('k', 'ㄎ'),
    ('l', 'ㄌ'),
    ('m', 'ㄇ'),
    ('n', 'ㄋ'),
    ('p', 'ㄆ'),
    ('q', 'ㄑ'),
    ('r', 'ㄖ'),
    ('s', 'ㄙ'),
    ('t', 'ㄊ'),
    ('x', 'ㄒ'),
    ('z', 'ㄗ'),
]

bopomofo_finals = [
    ('iang', 'ㄧㄤ'),
    ('iong', 'ㄩㄥ'),
    ('uang', 'ㄨㄤ'),
    ('u:an', 'ㄩㄢ'),
    ('ang', 'ㄤ'),
    ('eng', 'ㄥ'),
    ('iai', 'ㄧㄞ'),
    ('ian', 'ㄧㄢ'),
    ('iao', 'ㄧㄠ'),
    ('ing', 'ㄧㄥ'),
    ('ong', 'ㄨㄥ'),
    ('uai', 'ㄨㄞ'),
    ('uan', 'ㄨㄢ'),
    ('u:e', 'ㄩㄝ'),
    ('u:n', 'ㄩㄣ'),
    ('ai', 'ㄞ'),
    ('an', 'ㄢ'),
    ('ao', 'ㄠ'),
    ('ei', 'ㄟ'),
    ('en', 'ㄣ'),
    ('er', 'ㄦ'),
    ('ia', 'ㄧㄚ'),
    ('ie', 'ㄧㄝ'),
    ('in', 'ㄧㄣ'),
    ('io', 'ㄧㄛ'),
    ('iu', 'ㄧㄡ'),
    ('ou', 'ㄡ'),
    ('ua', 'ㄨㄚ'),
    ('ui', 'ㄨㄟ'),
    ('un', 'ㄨㄣ'),
    ('uo', 'ㄨㄛ'),
    ('u:', 'ㄩ'),
    ('a', 'ㄚ'),
    ('e', 'ㄜ'),
    ('i', 'ㄧ'),
    ('o', 'ㄛ'),
    ('u', 'ㄨ'),
    ('ê', 'ㄝ'),
]

bopomofo_tones = [('1', ''), ('2', 'ˊ'), ('3', 'ˇ'), ('4', 'ˋ'), ('5', '˙')]

table = bopomofo_special + bopomofo_initials + bopomofo_finals + bopomofo_tones
table.sort(key=lambda pair: len(pair[0]), reverse=True)
bopomofo_replacements.extend(table)

punc_map = {'。': '.', '，': ','}

DIACRITIC_TO_TONE = {
    'COMBINING MACRON': '1',
    'COMBINING ACUTE ACCENT': '2',
    'COMBINING CARON': '3',
    'COMBINING GRAVE ACCENT': '4',
}

CLOZE = compile(r'\{\{c[0-9]+::(.*?)(::.*?)?\}\}')
