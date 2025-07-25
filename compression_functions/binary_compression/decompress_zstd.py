import zstandard as zstd


def decompress_zstd(compressed_data: bytes) -> bytes:
    """
    Decompress Zstandard (zstd)-compressed data.

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
        # Create a Zstandard decompressor
        decompressor = zstd.ZstdDecompressor()
        # Decompress the data using Zstandard
        decompressed: bytes = decompressor.decompress(compressed_data)
        return decompressed
    except Exception as e:
        # Raise a ValueError if an error occurs during decompression
        raise ValueError(f"An error occurred during decompression: {e}")
