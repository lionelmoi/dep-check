"""
Test functions in models module.
"""
import re

from dep_check.models import Module, get_parent, wildcard_to_regex


class TestBuildModuleRegex:
    """
    Test build module regex function.
    """

    @staticmethod
    def test_empty() -> None:
        """
        Test empty case.
        """
        # Given
        module = Module("")

        # When
        regex = wildcard_to_regex(module)

        # Then
        assert regex == ""

    @staticmethod
    def test_simple_module() -> None:
        """
        Test simple case.
        """
        # Given
        module = Module("toto")

        # When
        regex = wildcard_to_regex(module)

        # Then
        assert re.match(regex, "toto")
        assert not re.match(regex, "tata")
        assert not re.match(regex, "titi.toto")

    @staticmethod
    def test_nested_module() -> None:
        """
        Test nested case.
        """
        # Given
        module = Module("toto.tata")

        # When
        regex = wildcard_to_regex(module)

        # Then
        assert re.match(regex, "toto.tata")
        assert not re.match(regex, "toto")
        assert not re.match(regex, "tata")
        assert not re.match(regex, "titi.toto")

    @staticmethod
    def test_quesiton_mark() -> None:
        """
        Test question mark case
        """
        # Given
        module = Module("t?to.?at?")

        # When
        regex = wildcard_to_regex(module)

        # Then
        assert re.match(regex, "toto.tata")
        assert re.match(regex, "t2to.bato")
        assert re.match(regex, "t#to.!at&")
        assert not re.match(regex, "toto")
        assert not re.match(regex, "tata")
        assert not re.match(regex, "toti.toto")

    @staticmethod
    def test_asterisk() -> None:
        """
        Test asterisk case
        """
        # Given
        module = Module("toto*.*")

        # When
        regex = wildcard_to_regex(module)

        # Then
        assert re.match(regex, "toto.tata")
        assert re.match(regex, "toto_2351.titi")
        assert re.match(regex, "toto_azerty.titi.toto.tata")
        assert not re.match(regex, "toto")
        assert not re.match(regex, "tototata")
        assert not re.match(regex, "toti.toto")

    @staticmethod
    def test_percentage() -> None:
        """
        Test percentage case
        """
        # Given
        module = Module("toto.tata%")

        # When
        regex = wildcard_to_regex(module)

        # Then
        assert re.match(regex, "toto.tata")
        assert re.match(regex, "toto.tata.titi")
        assert re.match(regex, "toto.tata.titi.tutu.tototata.tititutu")
        assert not re.match(regex, "toto")
        assert not re.match(regex, "toto.tata_123")


class TestBuildRule:
    """
    Test build_rule function.
    """

    @staticmethod
    def test_empty() -> None:
        """
        Test empty case.
        """
        # Given
        module = Module("")

        # When
        regex = wildcard_to_regex(module)

        # Then
        assert regex == ""

    @staticmethod
    def test_simple_module() -> None:
        """
        Test simple case.
        """
        # Given
        module = Module("toto")

        # When
        regex = wildcard_to_regex(module)

        # Then
        assert re.match(regex, "toto")
        assert not re.match(regex, "tata")
        assert not re.match(regex, "titi.toto")

    @staticmethod
    def test_nested_module() -> None:
        """
        Test nested case.
        """
        # Given
        module = Module("toto.tata")

        # When
        regex = wildcard_to_regex(module)

        # Then
        assert re.match(regex, "toto.tata")
        assert not re.match(regex, "toto")
        assert not re.match(regex, "tata")
        assert not re.match(regex, "titi.toto")

    @staticmethod
    def test_quesiton_mark() -> None:
        """
        Test question mark case
        """
        # Given
        module = Module("t?to.?at?")

        # When
        regex = wildcard_to_regex(module)

        # Then
        assert re.match(regex, "toto.tata")
        assert re.match(regex, "t2to.bato")
        assert re.match(regex, "t#to.!at&")
        assert not re.match(regex, "toto")
        assert not re.match(regex, "tata")
        assert not re.match(regex, "toti.toto")

    @staticmethod
    def test_asterisk() -> None:
        """
        Test asterisk case
        """
        # Given
        module = Module("toto*.*")

        # When
        regex = wildcard_to_regex(module)

        # Then
        assert re.match(regex, "toto.tata")
        assert re.match(regex, "toto_2351.titi")
        assert re.match(regex, "toto_azerty.titi.toto.tata")
        assert not re.match(regex, "toto")
        assert not re.match(regex, "tototata")
        assert not re.match(regex, "toti.toto")

    @staticmethod
    def test_percentage() -> None:
        """
        Test percentage case
        """
        # Given
        module = Module("toto.tata%")

        # When
        regex = wildcard_to_regex(module)

        # Then
        assert re.match(regex, "toto.tata")
        assert re.match(regex, "toto.tata.titi")
        assert re.match(regex, "toto.tata.titi.tutu.tototata.tititutu")
        assert not re.match(regex, "toto")
        assert not re.match(regex, "toto.tata_123")


class TestGetParent:
    """
    Test get_parent function.
    """

    @staticmethod
    def test_empty() -> None:
        """
        Test empty case.
        """
        # Given
        module = Module("")

        # When
        parent = get_parent(module)

        # Then
        assert parent == ""

    @staticmethod
    def test_simple_module() -> None:
        """
        Test simple case.
        """
        # Given
        module = Module("toto")

        # When
        parent = get_parent(module)

        # Then
        assert parent == Module("")

    @staticmethod
    def test_nested_module() -> None:
        """
        Test nested case.
        """
        # Given
        module = Module("toto.tata")

        # When
        parent = get_parent(module)

        # Then
        assert parent == Module("toto")

    @staticmethod
    def test_long_nested_module() -> None:
        """
        Test long nested case.
        """
        # Given
        module = Module("toto.titi.tete.tata")

        # When
        parent = get_parent(module)

        # Then
        assert parent == Module("toto.titi.tete")
