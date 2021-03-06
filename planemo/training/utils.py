"""Module contains code for the Requirement, Reference and some general functions for training."""

import collections

import oyaml as yaml


class Requirement:
    """Class to describe a training requirement."""

    def __init__(self, title="", req_type="internal", link="/introduction/"):
        """Init a Requirement instance."""
        self.title = title
        self.type = req_type
        self.link = link

    def init_from_dict(self, dict):
        """Init from a dictionary generated by export_to_ordered_dict."""
        self.title = dict['title']
        self.type = dict['type']
        self.link = dict['link']

    def export_to_ordered_dict(self):
        """Export the requirement into an ordered dictionary."""
        req = collections.OrderedDict()
        req['title'] = self.title
        req['type'] = self.type
        req['link'] = self.link
        return req


class Reference:
    """Class to describe a training reference."""

    def __init__(self, authors="authors et al", title="the title", link="link", summary="Why this reference is useful"):
        """Init a Reference instance."""
        self.authors = authors
        self.title = title
        self.link = link
        self.summary = summary

    def init_from_dict(self, dict):
        """Init from a dictionary generated by export_to_ordered_dict."""
        self.authors = dict['authors']
        self.title = dict['title']
        self.link = dict['link']
        self.summary = dict['summary']

    def export_to_ordered_dict(self):
        """Export the reference into an ordered dictionary."""
        ref = collections.OrderedDict()
        ref['authors'] = self.authors
        ref['title'] = self.title
        ref['link'] = self.link
        ref['summary'] = self.summary
        return ref


def load_yaml(filepath):
    """Load the content of a YAML file to a dictionary."""
    with open(filepath, "r") as m_file:
        content = yaml.load(m_file)
    return content


def save_to_yaml(content, filepath):
    """Save a dictionary to a YAML file."""
    with open(filepath, 'w') as stream:
        yaml.safe_dump(content,
                       stream,
                       indent=2,
                       default_flow_style=False,
                       default_style='',
                       explicit_start=True,
                       encoding='utf-8',
                       allow_unicode=True)
