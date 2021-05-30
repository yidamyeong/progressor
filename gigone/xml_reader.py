from lxml import etree


def read_xpath(tree, xpath):
    tags = tree.xpath(xpath)
    if tags and len(tags) > 0:
        return True, tags[0]
    else:
        return False, None


def open_xml_file(filename):
    with open(filename, encoding='UTF8') as file:
        try:
            return etree.parse(file, parser=etree.XMLParser(encoding='utf-8'))
        except KeyError as e:
            print('XML 데이터를 파싱하는 데 실패했습니다. 사유={0}'.format(e))
            return None


# message1.xml 파일이 같은 디렉터리 내에 있어야!
xml_tree = open_xml_file('message1.xml')
if not xml_tree:
    # 더 이상 로직 진행 불가하므로 종료
    exit(0)

# Xpath 기반 데이터 접근

root_tree = xml_tree.getroot()
print('root={0}'.format(root_tree.tag))  # root=message

exist, number_t = read_xpath(xml_tree, '/message/number')
if not exist:
    # XPath 가 존재하지 않는 경우 여기서 처리할 수 있다.
    exit(0)
print('number={0}'.format(number_t.text))  # number=12345

_, pi_t = read_xpath(xml_tree, '/message/pi')
print('pi={0}'.format(pi_t.text))  # pi=3.14

_, str_t = read_xpath(xml_tree, '/message/str')
print('str={0}'.format(str_t.text))

for attr in str_t.attrib:
    print('str attribute: {0}={1}'.format(attr, str_t.attrib[attr]))

exist, null_t = read_xpath(xml_tree, '/message/null_tag')
assert exist
print('null_tag={0}'.format(null_t.text))

_, object_t = read_xpath(xml_tree, '/message/object')
_, str2_t = read_xpath(object_t, 'str2')
print('str2={0}'.format(str2_t.text))

_, number2_t = read_xpath(object_t, 'object2/number2')
print('number2={0}'.format(number2_t.text))

number2_t = read_xpath(object_t, '/message/object/object2/number2')
print('number2={0}'.format(number2_t.text))

_, num_array_t = read_xpath(xml_tree, '/message/num_array')
for element in num_array_t.xpath('element'):
    print('element={0}'.format(element.text))
    for attr in element.attrib:
        print('\telement attribute: {0}={1}'.format(attr, element.attrib[attr]))

_, str_array_t = read_xpath(xml_tree, '/message/str_array')
for element in str_array_t.xpath('element'):
    print('str element={0}'.format(element.text))

