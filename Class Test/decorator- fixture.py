import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_servey():
    """A survey that will be available to all test functions."""
    question = "What language did you first learn to speak?"
    language_servey= AnonymousSurvey(question)
    return language_servey

def test_store_single_response(language_survey):
    """Test that a single response is stored properly"""
    language_servey.store_response("English")
    assert "English" in language_servey.responses

def test_store_three_responses(language_survey):
    """Test that three individual responses are stored properly"""
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_servey.store_response(response)

    for response in responses:
        assert response in language_servey.responses