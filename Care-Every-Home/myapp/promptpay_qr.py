# -*- coding: utf-8 -*-
"""
Generates and displays Thai PromptPay QR codes as standalone Python script (for VS Code or CLI).
"""
import libscrc
import qrcode
from PIL import Image
from typing import Union, Optional

# --- EMVCo Tag Constants ---
TAG_PAYLOAD_FORMAT_INDICATOR = "00"
TAG_POINT_OF_INITIATION_METHOD = "01"
TAG_MERCHANT_ACCOUNT_INFORMATION = "29"
SUB_TAG_AID_PROMPTPAY = "00"
SUB_TAG_MOBILE_NUMBER_PROMPTPAY = "01"
SUB_TAG_NATIONAL_ID_PROMPTPAY = "02"
TAG_TRANSACTION_CURRENCY = "53"
TAG_TRANSACTION_AMOUNT = "54"
TAG_COUNTRY_CODE = "58"
TAG_CRC = "63"

# --- Standard Values ---
VALUE_PAYLOAD_FORMAT_INDICATOR = "01"
VALUE_POINT_OF_INITIATION_MULTIPLE = "11"
VALUE_POINT_OF_INITIATION_ONETIME = "12"
VALUE_PROMPTPAY_AID = "A000000677010111"
VALUE_COUNTRY_CODE_TH = "TH"
VALUE_CURRENCY_THB = "764"
LEN_CRC_VALUE_HEX = "04"

class QRError(Exception):
    pass

class InvalidInputError(QRError):
    pass

def _format_tlv(tag: str, value: str) -> str:
    length_str = f"{len(value):02d}"
    return f"{tag}{length_str}{value}"

def calculate_crc(code_string: str) -> str:
    try:
        encoded_string = str.encode(code_string, 'ascii')
    except UnicodeEncodeError:
        raise InvalidInputError("Payload contains non-ASCII characters.")
    crc_val = libscrc.ccitt_false(encoded_string)  # type: ignore
    crc_hex_str = hex(crc_val)[2:].upper()
    return crc_hex_str.rjust(4, '0')

def generate_promptpay_qr_payload(
    mobile: Optional[str] = None,
    nid: Optional[str] = None,
    amount: Optional[Union[float, int, str]] = None,
    one_time: bool = False
) -> str:
    if not mobile and not nid:
        raise InvalidInputError("Provide either mobile number or National ID.")
    if mobile and nid:
        raise InvalidInputError("Only one of mobile or National ID allowed.")

    payload_elements = []
    payload_elements.append(_format_tlv(TAG_PAYLOAD_FORMAT_INDICATOR, VALUE_PAYLOAD_FORMAT_INDICATOR))
    initiation_method_value = VALUE_POINT_OF_INITIATION_ONETIME if one_time else VALUE_POINT_OF_INITIATION_MULTIPLE
    payload_elements.append(_format_tlv(TAG_POINT_OF_INITIATION_METHOD, initiation_method_value))

    merchant_account_sub_elements = [_format_tlv(SUB_TAG_AID_PROMPTPAY, VALUE_PROMPTPAY_AID)]

    if mobile:
        mobile_cleaned = mobile.strip()
        if not (len(mobile_cleaned) == 10 and mobile_cleaned.isdigit()):
            raise InvalidInputError("Mobile number must be 10 digits.")
        formatted_mobile_value = f"00{VALUE_COUNTRY_CODE_TH}{mobile_cleaned[1:]}"
        merchant_account_sub_elements.append(_format_tlv(SUB_TAG_MOBILE_NUMBER_PROMPTPAY, formatted_mobile_value))
    elif nid:
        nid_cleaned = nid.strip().replace('-', '')
        if not (len(nid_cleaned) == 13 and nid_cleaned.isdigit()):
            raise InvalidInputError("NID must be 13 digits.")
        merchant_account_sub_elements.append(_format_tlv(SUB_TAG_NATIONAL_ID_PROMPTPAY, nid_cleaned))

    payload_elements.append(_format_tlv(TAG_MERCHANT_ACCOUNT_INFORMATION, "".join(merchant_account_sub_elements)))
    payload_elements.append(_format_tlv(TAG_TRANSACTION_CURRENCY, VALUE_CURRENCY_THB))

    if amount is not None:
        try:
            amount_float = float(str(amount).strip())
            if amount_float < 0:
                raise InvalidInputError("Amount cannot be negative.")
            if amount_float > 0:
                formatted_amount_value = f"{amount_float:.2f}"
                payload_elements.append(_format_tlv(TAG_TRANSACTION_AMOUNT, formatted_amount_value))
        except ValueError:
            raise InvalidInputError("Amount must be numeric.")

    payload_elements.append(_format_tlv(TAG_COUNTRY_CODE, VALUE_COUNTRY_CODE_TH))

    data_for_crc = "".join(payload_elements)
    crc_input = data_for_crc + TAG_CRC + LEN_CRC_VALUE_HEX
    crc_value = calculate_crc(crc_input)
    final_payload = crc_input + crc_value
    return final_payload.upper()

def display_promptpay_qr(
    mobile: Optional[str] = None,
    nid: Optional[str] = None,
    amount: Optional[Union[float, int, str]] = None,
    one_time: bool = False,
    box_size: int = 10,
    border: int = 4,
    save_path: Optional[str] = None
):
    try:
        payload = generate_promptpay_qr_payload(mobile=mobile, nid=nid, amount=amount, one_time=one_time)
        print(f"\nGenerated Payload:\n{payload}\n")

        qr_img = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=box_size,
            border=border,
        )
        qr_img.add_data(payload)
        qr_img.make(fit=True)
        img = qr_img.make_image(fill_color="black", back_color="white")

        if save_path:
            img.save(save_path)
            print(f"QR code saved to: {save_path}")
        else:
            img.show()

    except QRError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# --- Main Execution ---
if __name__ == "__main__":
    display_promptpay_qr(
        mobile="0941234567",
        one_time=True,
        save_path="promptpay_qr.png"  # หรือใช้ None เพื่อแสดงภาพแทน
    )
