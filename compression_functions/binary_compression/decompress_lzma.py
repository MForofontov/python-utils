import lzma


def decompress_lzma(compressed_data: bytes) -> bytes:
    """
    Decompress lzma-compressed data.

    Parameters
    ----------
    compressed_data : bytes
        The compressed data as bytes.

    Returns
    -------
    bytes
        The decompressed data as bytes.

    Raises
    ------
    TypeError
        If compressed_data is not bytes.
    ValueError
        If an error occurs during decompression.
    """
    # Check if compressed_data is bytes
    if not isinstance(compressed_data, bytes):
        raise TypeError("compressed_data must be bytes")

    try:
        # Decompress the data using lzma
        decompressed: bytes = lzma.decompress(compressed_data)
        return decompressed
    except Exception as e:
        # Raise a ValueError if an error occurs during decompression
        raise ValueError(f"An error occurred during decompression: {e}")
