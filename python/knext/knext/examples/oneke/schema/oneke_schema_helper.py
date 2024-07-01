# -*- coding: utf-8 -*-
# Copyright 2023 OpenSPG Authors
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.

# ATTENTION!
# This file is generated by Schema automatically, it will be refreshed after schema has been committed
# PLEASE DO NOT MODIFY THIS FILE!!!
#

from knext.schema.model.schema_helper import (
    SPGTypeHelper,
    PropertyHelper,
    RelationHelper,
)


class OneKE:
    class Album(SPGTypeHelper):

        award = PropertyHelper("award")
        alias = PropertyHelper("alias")
        name = PropertyHelper("name")
        description = PropertyHelper("description")
        id = PropertyHelper("id")

    class AwardRecipient(SPGTypeHelper):

        name = PropertyHelper("name")
        description = PropertyHelper("description")
        id = PropertyHelper("id")
        subject = PropertyHelper("subject")
        eventTime = PropertyHelper("eventTime")
        eventType = PropertyHelper("eventType")

    class CertificateRecognition(SPGTypeHelper):

        name = PropertyHelper("name")
        description = PropertyHelper("description")
        id = PropertyHelper("id")
        subject = PropertyHelper("subject")
        eventTime = PropertyHelper("eventTime")

    class Company(SPGTypeHelper):

        name = PropertyHelper("name")
        alias = PropertyHelper("alias")
        description = PropertyHelper("description")
        id = PropertyHelper("id")

    class Concert(SPGTypeHelper):

        name = PropertyHelper("name")
        alias = PropertyHelper("alias")
        description = PropertyHelper("description")
        id = PropertyHelper("id")

    class ConductConcert(SPGTypeHelper):

        object = PropertyHelper("object")
        name = PropertyHelper("name")
        description = PropertyHelper("description")
        id = PropertyHelper("id")
        subject = PropertyHelper("subject")
        eventTime = PropertyHelper("eventTime")

    class EstablishCompany(SPGTypeHelper):

        object = PropertyHelper("object")
        name = PropertyHelper("name")
        description = PropertyHelper("description")
        id = PropertyHelper("id")
        subject = PropertyHelper("subject")
        eventTime = PropertyHelper("eventTime")

    class Movies(SPGTypeHelper):

        award = PropertyHelper("award")
        alias = PropertyHelper("alias")
        name = PropertyHelper("name")
        description = PropertyHelper("description")
        id = PropertyHelper("id")

    class Person(SPGTypeHelper):

        alias = PropertyHelper("alias")
        name = PropertyHelper("name")
        profession = PropertyHelper("profession")
        birthPlace = PropertyHelper("birthPlace")
        description = PropertyHelper("description")
        id = PropertyHelper("id")
        graduated = PropertyHelper("graduated")
        ancestryPlace = PropertyHelper("ancestryPlace")
        birthDate = PropertyHelper("birthDate")

    class PublishMovies(SPGTypeHelper):

        object = PropertyHelper("object")
        name = PropertyHelper("name")
        description = PropertyHelper("description")
        id = PropertyHelper("id")
        eventTime = PropertyHelper("eventTime")
        subject = PropertyHelper("subject")

    class PublishMusicAlbum(SPGTypeHelper):

        object = PropertyHelper("object")
        name = PropertyHelper("name")
        description = PropertyHelper("description")
        id = PropertyHelper("id")
        subject = PropertyHelper("subject")
        eventTime = PropertyHelper("eventTime")

    Album = Album("OneKE.Album")
    AwardRecipient = AwardRecipient("OneKE.AwardRecipient")
    CertificateRecognition = CertificateRecognition("OneKE.CertificateRecognition")
    Company = Company("OneKE.Company")
    Concert = Concert("OneKE.Concert")
    ConductConcert = ConductConcert("OneKE.ConductConcert")
    EstablishCompany = EstablishCompany("OneKE.EstablishCompany")
    Movies = Movies("OneKE.Movies")
    Person = Person("OneKE.Person")
    PublishMovies = PublishMovies("OneKE.PublishMovies")
    PublishMusicAlbum = PublishMusicAlbum("OneKE.PublishMusicAlbum")

    pass