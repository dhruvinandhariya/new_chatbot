import pytest
from utils.scraper import scrape_website

def test_scrape_website_success(mocker):
    mock_response = mocker.patch('utils.scraper.requests.get')
    mock_response.return_value.status_code = 200
    mock_response.return_value.text = '<html><body><h1>Test Title</h1><p>Test content.</p></body></html>'
    
    content = scrape_website()
    
    assert "Test Title" in content
    assert "Test content." in content

def test_scrape_website_failure(mocker):
    mock_response = mocker.patch('utils.scraper.requests.get')
    mock_response.side_effect = Exception("Network error")
    
    content = scrape_website()
    
    assert content == ""  # Expecting empty content on failure
