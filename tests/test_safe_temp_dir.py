"""Tests for safe-temp-dir."""

import os
import tempfile
import pytest
from safe_temp_dir import dir


class TestDir:
    """Test suite for dir."""

    def test_basic(self):
        """Test basic usage with a real temp directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a sample file inside
            sample = os.path.join(tmpdir, "sample.txt")
            with open(sample, "w") as f:
                f.write("hello world")
            result = dir(tmpdir)
            assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            dir("")
        except (ValueError, TypeError, FileNotFoundError, OSError):
            pass  # Expected for path-based utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = dir(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
