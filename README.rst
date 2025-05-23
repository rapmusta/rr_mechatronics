
# RR Mechatronics Documentation

This repository contains the full engineering and operational documentation for RR Mechatronics platforms, primarily focusing on the **Sootballs** and **OKS** product lines.

Documentation is structured to support teams across hardware, embedded systems, electrical integration, and operations.

---

## 📁 Directory Structure

```
docs/
├── index.rst                    # Master TOC for Read the Docs
├── includes/                   # Reusable snippets (warnings, tables)
├── assets/                     # Diagrams, images, schematics
│   ├── hardware/
│   ├── electrical/
│   ├── embedded/
│   └── shared/
├── sootballs/
│   ├── hardware_specs_gen3_1.rst
│   ├── hardware_bom_gen3_1.rst
│   ├── firmware_guide_gen3_1.rst
│   ├── sb_manual_charger.rst
│   └── ...
├── oks/
│   ├── oks_overview.rst
│   └── ...
```

---

## 🧭 How to Navigate the Docs

### Main Sections:

- **Hardware**: Specs, BOMs, mounting guides
- **Embedded**: Firmware structure, comm interfaces
- **Electrical**: Wiring diagrams, power specs
- **Charging**: Autocharging calibration, docking dimensions
- **Support**: Maintenance procedures, quick links

Each file corresponds to one topic and is named semantically for easy search and linking.

You can start from `index.rst` or go directly to `sootballs_overview.rst`.

---

## ✍️ How to Contribute

### 🔹 1. Create or Edit `.rst` Files
- Use reStructuredText syntax (`.rst`)
- Keep sections short and focused
- Use grid tables for BOMs, specs

### 🔹 2. Add to the ToC
- If it’s a new doc, add it to the right `.. toctree::` in:
  - `index.rst` for global sections
  - `sootballs_overview.rst` or `oks_overview.rst` for product-specific ones

### 🔹 3. Rebuild the Site
```bash
cd docs/
make html
```
Output will be in `docs/build/html`. Open `index.html` in a browser.

### 🔹 4. Submit or Archive
If under version control, push your changes.
If working offline, zip the updated docs and share with the team.

---

## 🧪 Style Guidelines

- Use `.. include::` for reusable content
- Use semantic filenames: `hardware_specs_gen3_1.rst`, not `doc3.rst`
- Prefer section headers (`===`, `---`) over long paragraphs
- Add diagrams to `/assets/` and reference relatively

---

## 🤝 Thanks

This project is maintained collaboratively by RRUS.  
For questions, raise an issue in the repo or tag the current doc lead.
