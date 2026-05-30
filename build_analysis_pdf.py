#!/usr/bin/env python3
"""Generates a standalone PDF analytical guide based on the theory of
adult attachment (Bowlby/Ainsworth/Hazan-Shaver/Mikulincer-Shaver),
discussed in popular form in the book 'Attached' by Amir Levine and
Rachel Heller. The document is the assistant's own analysis: critique,
synthesis, applied frameworks, examples. It does NOT reproduce the
book's text or illustrations.

Output: Attached_Analysis.pdf
"""

from __future__ import annotations
import io


# ---------- PDF primitives (Helvetica, WinAnsi, no external deps) ----------

_HELV_AVG = 500
_HELV_W = [_HELV_AVG] * 256
_HELVB_W = [_HELV_AVG] * 256
_HELVI_W = [_HELV_AVG] * 256

_HELV_TABLE = {
    32:278,33:278,34:355,35:556,36:556,37:889,38:667,39:191,40:333,41:333,
    42:389,43:584,44:278,45:333,46:278,47:278,48:556,49:556,50:556,51:556,
    52:556,53:556,54:556,55:556,56:556,57:556,58:278,59:278,60:584,61:584,
    62:584,63:556,64:1015,65:667,66:667,67:722,68:722,69:667,70:611,71:778,
    72:722,73:278,74:500,75:667,76:556,77:833,78:722,79:778,80:667,81:778,
    82:722,83:667,84:611,85:722,86:667,87:944,88:667,89:667,90:611,91:278,
    92:278,93:278,94:469,95:556,96:222,97:556,98:556,99:500,100:556,101:556,
    102:278,103:556,104:556,105:222,106:222,107:500,108:222,109:833,110:556,
    111:556,112:556,113:556,114:333,115:500,116:278,117:556,118:500,119:722,
    120:500,121:500,122:500,123:334,124:260,125:334,126:584,160:278,
    8211:556,8212:1000,8216:222,8217:222,8220:333,8221:333,8226:350,8230:1000,
}
_HELVB_TABLE = {
    32:278,33:333,34:474,35:556,36:556,37:889,38:722,39:238,40:333,41:333,
    42:389,43:584,44:278,45:333,46:278,47:278,48:556,49:556,50:556,51:556,
    52:556,53:556,54:556,55:556,56:556,57:556,58:333,59:333,60:584,61:584,
    62:584,63:611,64:975,65:722,66:722,67:722,68:722,69:667,70:611,71:778,
    72:722,73:278,74:556,75:722,76:611,77:833,78:722,79:778,80:667,81:778,
    82:722,83:667,84:611,85:722,86:667,87:944,88:667,89:667,90:611,91:333,
    92:278,93:333,94:584,95:556,96:333,97:556,98:611,99:556,100:611,101:556,
    102:333,103:611,104:611,105:278,106:278,107:556,108:278,109:889,110:611,
    111:611,112:611,113:611,114:389,115:556,116:333,117:611,118:556,119:778,
    120:556,121:556,122:500,160:278,
    8211:556,8212:1000,8216:278,8217:278,8220:500,8221:500,8226:350,8230:1000,
}
for code, w in _HELV_TABLE.items():
    if code < 256:
        _HELV_W[code] = w
        _HELVI_W[code] = w
for code, w in _HELVB_TABLE.items():
    if code < 256:
        _HELVB_W[code] = w


# WinAnsi extras for codes 0x80..0x9F
_WINANSI_EXTRA = {
    '\u20AC':0x80,'\u201A':0x82,'\u0192':0x83,'\u201E':0x84,'\u2026':0x85,
    '\u2020':0x86,'\u2021':0x87,'\u02C6':0x88,'\u2030':0x89,'\u0160':0x8A,
    '\u2039':0x8B,'\u0152':0x8C,'\u017D':0x8E,'\u2018':0x91,'\u2019':0x92,
    '\u201C':0x93,'\u201D':0x94,'\u2022':0x95,'\u2013':0x96,'\u2014':0x97,
    '\u02DC':0x98,'\u2122':0x99,'\u0161':0x9A,'\u203A':0x9B,'\u0153':0x9C,
    '\u017E':0x9E,'\u0178':0x9F,
}

_FALLBACK = {
    '\u00A0': 0x20,
    '\u2192': ord('>'), '\u2190': ord('<'),
    '\u2212': ord('-'),
    '\u00AB': 0x93, '\u00BB': 0x94,  # << >>
}


def _ch_to_byte(ch: str):
    if ch in _WINANSI_EXTRA:
        return _WINANSI_EXTRA[ch]
    o = ord(ch)
    if o < 0x100:
        return o
    if ch in _FALLBACK:
        return _FALLBACK[ch]
    return None


def encode_text(s: str) -> bytes:
    out = bytearray()
    for ch in s:
        b = _ch_to_byte(ch)
        if b is None:
            b = ord('?')
        out.append(b)
    return bytes(out)


def text_width(s: str, size: float, table) -> float:
    total = 0
    for ch in s:
        b = _ch_to_byte(ch)
        if b is None:
            total += _HELV_AVG
        else:
            total += table[b]
    return total * size / 1000.0


def wrap_paragraph(text: str, max_w: float, size: float, table) -> list:
    words = text.split(' ')
    lines = []
    cur = []
    cur_w = 0.0
    space_w = text_width(' ', size, table)
    for w in words:
        if not w:
            continue
        ww = text_width(w, size, table)
        if ww > max_w:
            if cur:
                lines.append(' '.join(cur))
                cur, cur_w = [], 0.0
            chunk = ''
            chw = 0.0
            for ch in w:
                cw = text_width(ch, size, table)
                if chw + cw > max_w and chunk:
                    lines.append(chunk)
                    chunk, chw = '', 0.0
                chunk += ch
                chw += cw
            if chunk:
                cur = [chunk]
                cur_w = chw
            continue
        added = ww if not cur else ww + space_w
        if cur_w + added > max_w and cur:
            lines.append(' '.join(cur))
            cur, cur_w = [w], ww
        else:
            cur.append(w)
            cur_w += added
    if cur:
        lines.append(' '.join(cur))
    return lines


class PDF:
    def __init__(self, w=612.0, h=792.0, ml=54.0, mr=54.0, mt=60.0, mb=60.0):
        self.w, self.h = w, h
        self.ml, self.mr, self.mt, self.mb = ml, mr, mt, mb
        self.cw = w - ml - mr
        self.streams = []
        self._lines = []
        self._y = h - mt
        self._page_no = 0
        self._start_page()

    def _start_page(self):
        self._page_no += 1
        self._lines = []
        self._y = self.h - self.mt
        # Footer with page number
        # We'll add the footer when finalizing the page

    def _finish_page(self):
        # Add footer
        footer = f"{self._page_no}"
        size = 9
        fw = text_width(footer, size, _HELV_W)
        x = (self.w - fw) / 2
        y = 30
        payload = encode_text(footer)
        cmd = (
            b'BT /F1 ' + str(size).encode() + b' Tf '
            + f'{x:.2f} {y:.2f}'.encode() + b' Td ('
            + payload + b') Tj ET'
        )
        self._lines.append(cmd)
        self.streams.append(b'\n'.join(self._lines))

    def new_page(self):
        self._finish_page()
        self._start_page()

    def _ensure(self, need):
        if self._y - need < self.mb + 20:  # leave room for footer
            self.new_page()

    def _draw_line(self, font, size, text, x=None):
        if x is None:
            x = self.ml
        y = self._y - size
        payload = encode_text(text)
        payload = payload.replace(b'\\', b'\\\\').replace(b'(', b'\\(').replace(b')', b'\\)')
        cmd = (
            b'BT /' + font.encode() + b' ' + str(size).encode() + b' Tf '
            + f'{x:.2f} {y:.2f}'.encode() + b' Td ('
            + payload + b') Tj ET'
        )
        self._lines.append(cmd)

    def add(self, style: str, text: str):
        if style == 'title':
            font, size, table = 'F2', 26, _HELVB_W
            sb, sa, lead = 30, 18, size * 1.25
        elif style == 'h1':
            font, size, table = 'F2', 18, _HELVB_W
            sb, sa, lead = 22, 10, size * 1.25
        elif style == 'h2':
            font, size, table = 'F2', 14, _HELVB_W
            sb, sa, lead = 16, 8, size * 1.25
        elif style == 'h3':
            font, size, table = 'F2', 12, _HELVB_W
            sb, sa, lead = 12, 6, size * 1.25
        elif style == 'p':
            font, size, table = 'F1', 11, _HELV_W
            sb, sa, lead = 0, 7, size * 1.35
        elif style == 'bullet':
            font, size, table = 'F1', 11, _HELV_W
            sb, sa, lead = 0, 4, size * 1.30
        elif style == 'quote':
            font, size, table = 'F1', 10, _HELV_W
            sb, sa, lead = 4, 6, size * 1.30
        elif style == 'small':
            font, size, table = 'F1', 9, _HELV_W
            sb, sa, lead = 0, 4, size * 1.30
        elif style == 'mono':
            font, size, table = 'F1', 10, _HELV_W
            sb, sa, lead = 6, 8, size * 1.20
        else:
            font, size, table = 'F1', 11, _HELV_W
            sb, sa, lead = 0, 6, size * 1.30

        self._y -= sb
        if self._y < self.mb + 20:
            self.new_page()

        # Bullet handling: indent + bullet char
        indent = 0
        prefix = ''
        if style == 'bullet':
            indent = 16
            prefix = '\u2022 '
        elif style == 'quote':
            indent = 20

        max_w = self.cw - indent
        full = (prefix + text) if prefix else text

        # Hard line breaks via "\n"
        for para in full.split('\n'):
            lines = wrap_paragraph(para, max_w, size, table)
            if not lines:
                lines = ['']
            for i, ln in enumerate(lines):
                self._ensure(lead)
                x = self.ml + (indent if (style == 'bullet' and i == 0) else (indent if style == 'quote' else (indent if style == 'bullet' else 0)))
                # For bullet continuation lines align under text (indent), keep same x
                self._draw_line(font, size, ln, x=x)
                self._y -= lead

        self._y -= sa

    def hr(self):
        # Decorative blank space (no graphics ops to keep things simple)
        self._y -= 6
        if self._y < self.mb + 20:
            self.new_page()

    def finalize(self) -> bytes:
        self._finish_page()
        objs = []

        def add(body):
            objs.append(body)
            return len(objs)

        cat = add(b'')
        pages = add(b'')
        f1 = add(b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>')
        f2 = add(b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>')

        page_ids = []
        for s in self.streams:
            cid = add(b'<< /Length ' + str(len(s)).encode() + b' >>\nstream\n' + s + b'\nendstream')
            pid = add(
                b'<< /Type /Page /Parent ' + str(pages).encode() + b' 0 R '
                b'/MediaBox [0 0 ' + f'{self.w} {self.h}'.encode() + b'] '
                b'/Resources << /Font << /F1 ' + str(f1).encode() + b' 0 R /F2 '
                + str(f2).encode() + b' 0 R >> >> '
                b'/Contents ' + str(cid).encode() + b' 0 R >>'
            )
            page_ids.append(pid)

        kids = b' '.join(str(p).encode() + b' 0 R' for p in page_ids)
        objs[pages-1] = (
            b'<< /Type /Pages /Count ' + str(len(page_ids)).encode()
            + b' /Kids [' + kids + b'] >>'
        )
        objs[cat-1] = b'<< /Type /Catalog /Pages ' + str(pages).encode() + b' 0 R >>'

        out = io.BytesIO()
        out.write(b'%PDF-1.4\n%\xe2\xe3\xcf\xd3\n')
        offs = [0]
        for i, body in enumerate(objs, 1):
            offs.append(out.tell())
            out.write(f'{i} 0 obj\n'.encode())
            out.write(body)
            out.write(b'\nendobj\n')
        xref = out.tell()
        out.write(f'xref\n0 {len(objs)+1}\n'.encode())
        out.write(b'0000000000 65535 f \n')
        for o in offs[1:]:
            out.write(f'{o:010d} 00000 n \n'.encode())
        out.write(b'trailer\n')
        out.write(b'<< /Size ' + str(len(objs)+1).encode() + b' /Root '
                  + str(cat).encode() + b' 0 R >>\n')
        out.write(b'startxref\n' + f'{xref}\n'.encode() + b'%%EOF\n')
        return out.getvalue()


# ---------- Helper to add structured content ----------

def add_blocks(pdf: PDF, blocks):
    for kind, text in blocks:
        if kind == 'pagebreak':
            pdf.new_page()
        else:
            pdf.add(kind, text)


def main():
    pdf = PDF()
    from analysis_content import build_blocks
    blocks = build_blocks()
    add_blocks(pdf, blocks)
    data = pdf.finalize()
    with open('Attached_Analysis.pdf', 'wb') as f:
        f.write(data)
    print(f"Wrote Attached_Analysis.pdf ({len(data)} bytes)")


if __name__ == '__main__':
    main()
