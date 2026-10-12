from unittest.mock import MagicMock, patch

import app as app_module


def test_index_increments_and_displays_hits():
    fake_db = MagicMock()
    fake_db.incr.return_value = 5
    with patch.object(app_module, "db", fake_db):
        response = app_module.app.test_client().get("/")
    assert response.status_code == 200
    assert "5 fois" in response.get_data(as_text=True)
    fake_db.incr.assert_called_once_with("hits")