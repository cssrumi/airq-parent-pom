import subprocess
import xml.etree.ElementTree as ET

NS = '{http://maven.apache.org/POM/4.0.0}'

pom_tree = ET.parse('pom.xml')
pom_root = pom_tree.getroot()
version = pom_root.find(NS + 'version').text
group_id = pom_root.find(NS + 'groupId').text
company = group_id.split('.')[-1]
artifact_id = pom_root.find(NS + 'artifactId').text

tag = company + '/' + artifact_id + ':' + version

build = subprocess.Popen(['docker', 'build', '-f', 'Dockerfile', '-t', tag, '.'])
build.wait()
