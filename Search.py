"""
OIG Search Engine Demo

Author: Jacob Voyles
Date 12/30/2022

"""

# External Library Imports
import urllib.parse
import json
import streamlit as st
from elasticsearch import Elasticsearch

# Interanal Imports
from config import config
from pages import About
from utils import elastic_utils, template
from utils.entitiy_recognition import EntityRecognition

st.set_page_config(page_title='OIG Search Engine')

# Set up Elastic Search
es = Elasticsearch(hosts=config.DOMAIN)
elastic_utils.check_and_create_index(es, config.INDEX)

def set_session_state():
    """ """
    # default values
    if 'search' not in st.session_state:
        st.session_state.search = None
    if 'tags' not in st.session_state:
        st.session_state.tags = None
    if 'page' not in st.session_state:
        st.session_state.page = 1

    # get parameters in url
    para = st.experimental_get_query_params()
    if 'search' in para:
        st.experimental_set_query_params()
        st.session_state.search = urllib.parse.unquote(para['search'][0])
    if 'tags' in para:
        st.experimental_set_query_params()
        st.session_state.tags = para['tags'][0]
    if 'page' in para:
        st.experimental_set_query_params()
        st.session_state.page = int(para['page'][0])


def main():
    set_session_state()
    st.write(template.load_css(), unsafe_allow_html=True)
    # switch between pages
    with st.sidebar:
        st.write("This is where filters will go.")
    
    er = EntityRecognition()
    st.title('OIG Data Search')
    if st.session_state.search is None:
        search = st.text_input('Enter search words:')
    else:
        search = st.text_input('Enter search words:', st.session_state.search)
    if search:
        res = er.run(search)
        st.json(res, expanded=True)

        # if search != st.session_state.search:
        #     st.session_state.tags = None
        # # reset search word
        # st.session_state.search = None
        # from_i = (st.session_state.page - 1) * config.PAGE_SIZE
        # results = utils.index_search(es, index, search, st.session_state.tags,
        #                              from_i, config.PAGE_SIZE)
        # total_hits = results['aggregations']['match_count']['value']
        # if total_hits > 0:
        #     # show number of results and time taken
        #     st.write(template.number_of_results(total_hits, results['took'] / 1000),
        #              unsafe_allow_html=True)
        #     # show popular tags
        #     if st.session_state.tags is not None and st.session_state.tags not in results['sorted_tags']:
        #         popular_tags = [st.session_state.tags] + results['sorted_tags']
        #     else:
        #         popular_tags = results['sorted_tags']

        #     popular_tags_html = template.tag_boxes(search,
        #                                             popular_tags[:10],
        #                                             st.session_state.tags)
        #     st.write(popular_tags_html, unsafe_allow_html=True)
        #     # search results
        #     for i in range(len(results['hits']['hits'])):
        #         res = utils.simplify_es_result(results['hits']['hits'][i])
        #         st.write(template.search_result(i + from_i, **res),
        #                  unsafe_allow_html=True)
        #         # render tags
        #         tags_html = template.tag_boxes(search, res['tags'],
        #                                         st.session_state.tags)
        #         st.write(tags_html, unsafe_allow_html=True)

        #     # pagination
        #     if total_hits > config.PAGE_SIZE:
        #         total_pages = (total_hits + config.PAGE_SIZE - 1) // config.PAGE_SIZE
        #         pagination_html = template.pagination(total_pages,
        #                                                search,
        #                                                st.session_state.page,
        #                                                st.session_state.tags,)
        #         st.write(pagination_html, unsafe_allow_html=True)
    else:
        # no result found
        st.write(template.no_result_html(), unsafe_allow_html=True)


if __name__ == '__main__':
    main()