FROM quay.io/quarkus/centos-quarkus-maven:20.2.0-java11
COPY pom.xml /usr/src/lib/parent-pom/
#RUN mvn -f /usr/src/lib/parent-pom/pom.xml -B de.qaware.maven:go-offline-maven-plugin:1.2.5:resolve-dependencies
USER root
RUN chown -R quarkus /usr/src/lib/parent-pom
USER quarkus
RUN mvn -f /usr/src/lib/parent-pom/pom.xml clean install
