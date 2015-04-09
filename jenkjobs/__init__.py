def rsdt_doxygen(parser, xml_parent, data):
    """yaml: junit
    Publish Doxygen documentation

    Sameas as jenkins

    Example::

      publishers:
        - rsdt_doxygen:
            doxyfile: path to doxyfile relative to workspace. Required.
            folder: path to working directory relative to workspace.
            Defaults to ""
            node: nodename. Defaults to "".
            keep: whether to keep previous docs. Defaults to false.
    """
    from jenkins_jobs.errors import JenkinsJobsException
    from xml.etree.ElementTree import SubElement
    doxygen = SubElement(xml_parent, 'hudson.plugins.doxygen.DoxygenArchiver')
    if not data['doxyfile']:
        raise JenkinsJobsException("The path to a doxyfile must be specified.")
    SubElement(doxygen, 'doxyfilePath').text = data['doxyfile']
    SubElement(doxygen, 'runOnChild').text = data.get("node", "")
    SubElement(doxygen, 'folderWhereYouRunDoxygen').text \
        = data.get("folder", "")
    SubElement(doxygen, 'keepAll').text = data.get("keep", "false")


def trac(parser, xml_parent, data):
    """yaml: trac
    Adds trac property.
    Requires trac plugin.

    Example::

        properties:
            - track:
                url: url to trac
    """

    from jenkins_jobs.errors import JenkinsJobsException
    from xml.etree.ElementTree import SubElement
    trac = SubElement(xml_parent, 'hudson.plugins.trac.TracProjectProperty')
    if not data['url']:
        raise JenkinsJobsException("The path to a doxyfile must be specified.")
    SubElement(trac, 'tracWebsite').text = data['url']
