def doxygen(parser, xml_parent, data):
    """yaml: junit
    Publish Doxygen documentation

    Example::

      publishers:
        - doxygen:
            doxyfile: path to doxyfile relative to workspace. Required.
            working_directory: path to working directory relative to workspace. Defaults to ""
            node: nodename. Defaults to "".
            keep: whether to keep previous docs. Defaults to false.
    """
    from xml.etree.ElementTree import SubElement
    doxygen = SubElement(xml_parent, 'hudson.plugins.doxygen.DoxygenArchiver')
    SubElement(doxygen, 'doxyfilePath').text = data['doxyfile']
    SubElement(doxygen, 'runOnChild').text = data.get("node", "")
    SubElement(doxygen, 'folderWhereYouRunDoxygen').text = data.get("working_directory", "")
    SubElement(doxygen, 'keepAll').text = data.get("keep", "false")
