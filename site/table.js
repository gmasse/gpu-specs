document.addEventListener("DOMContentLoaded", () => {
    const container = document.getElementById("specs");

    // Fetch JSON data
    fetch("specs.json")
        .then(response => response.json())
        .then(jsonData => {
            // Extract header and rows
            const { _header, ...rows } = jsonData;

            // Helper function to format ordinal numbers
            const ordinal = (n) => {
                if (11 <= n % 100 && n % 100 <= 13) return `${n}th`;
                switch (n % 10) {
                    case 1: return `${n}st`;
                    case 2: return `${n}nd`;
                    case 3: return `${n}rd`;
                    default: return `${n}th`;
                }
            };

            // Helper function to format values
            const formatValue = (value) => {
                if (value === 0) return "N/A";
                if (value === null) return "?";
                return value;
            };

            // Helper function to concatenate base attributes with "_generation"
            const getConcatenatedValue = (gpuData, baseKey, generationKey) => {
                const baseValue = formatValue(gpuData[baseKey]);
                const generationValue = gpuData[generationKey];
                if (generationValue !== undefined && generationValue !== null) {
                    return `${baseValue} (${ordinal(generationValue)} gen)`;
                }
                return baseValue;
            };

            // Helper function to transpose data
            const transposeData = (keys, data) => {
                return keys.filter((key) => !key.endsWith("_generation")).map(key => {
                    const headerDetails = _header[key];
                    const headerName = headerDetails.full_name;
                    const unit = headerDetails.unit ? ` (${headerDetails.unit})` : "";

                    // Check for corresponding "_generation" attribute
                    const generationKey = `${key}_generation`;
                    const rowData = { Attribute: headerName + unit };

                    Object.values(data).forEach(gpuData => {
                        rowData[gpuData.name] = _header[generationKey]
                            ? getConcatenatedValue(gpuData, key, generationKey)
                            : formatValue(gpuData[key]);
                    });

                    return rowData;
                });
            };           

            // Separate specs (recognized by FLOPS and TOPS unit) and architecture details
            const specsKeys = Object.keys(_header).filter(key =>
                _header[key].unit === "TFLOPS" || _header[key].unit === "TOPS"
            );
            const architectureKeys = Object.keys(_header).filter(
                key => !specsKeys.includes(key)
            );

            // Combine specs and architecture data
            const specsData = transposeData(specsKeys, rows);
            const architectureRowIndex = specsData.length; // get the index delimiting specsData and architectureData
            const architectureData = transposeData(architectureKeys,rows);
            const combinedData = specsData.concat(architectureData);

            // Render Handsontable
            new Handsontable(container, {
                data: combinedData,
                colHeaders: Object.keys(combinedData[0]),
                rowHeaders: false,
                stretchH: 'all',
                licenseKey: "non-commercial-and-evaluation",
                filters: true,
                hiddenColumns: true,
                allowInsertColumn: false,
                allowInsertRow: false,
                allowRemoveColumn: false,
                allowRemoveRow: false,
                dropdownMenu: ['filter_by_value', 'filter_action_bar'],
                // `afterGetColHeader()` is a Handsontable hook
                afterGetColHeader(col, TH) {
                    // remove the column menu button from columns 1 and above
                    if (col > 0) {
                        const button = TH.querySelector('.changeType');
                        if (!button) {
                            return;
                        }
                        button.parentElement.removeChild(button);
                    }
                },
                contextMenu: ['undo','redo','---------','hidden_columns_hide','hidden_columns_show'],
                cells: (row, col) => {
                    const classes = [];
                    if (row < architectureRowIndex) {
                        // class depending on the precision
                        const precision = combinedData[row].Attribute.split(" ")[0] || combinedData[row].Attribute
                        classes.push(`precision-${precision}`);
                    } else {
                        if (row === architectureRowIndex) {
                            // class for the first row of Architecture Details section
                            classes.push("architecture-details-border");
                        }
                        // class for the Architecture Details section
                        classes.push("architecture-details");
                    }
                    return { className: classes.join(" ") };
                },
            });
        })
        .catch(error => console.error("Error loading JSON data:", error));
});