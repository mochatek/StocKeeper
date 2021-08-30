/**
 * Retrieve items available in the shop
 * @returns {Array} items list
 */
export async function getItems() {
  try {
    const items = await window.eel.getItems()();
    return JSON.parse(items);
  } catch (error) {
    console.log(error);
    return [];
  }
}

/**
 * Retrieve invoice history following the category
 * @param {String} category [Purchase/Sale]
 * @returns {Array}         invoices list
 */
export async function getInvoices(category) {
  try {
    const invoices = await window.eel.getInvoices(category)();
    return JSON.parse(invoices);
  } catch (error) {
    console.log(error);
    return [];
  }
}

/**
 * Add new item to items
 * @returns {Number} Status code {0: fail, 200: success}
 */
export async function insertItem(item) {
  try {
    const status = await window.eel.insertItem(item)();
    return status;
  } catch (error) {
    console.log(error);
    return 0;
  }
}

/**
 * Add new invoice to invoices
 * @param {Object} invoice  invoice details
 * @param {String} category Purchase/Sale
 * @returns {Number}        Status code {0: fail, 200: success}
 */
export async function insertInvoice(invoice, category) {
  try {
    const status = await window.eel.insertInvoice(invoice, category)();
    return status;
  } catch (error) {
    console.log(error);
    return 0;
  }
}

/**
 * Generate and save report as PDF
 * @param {String} category    Category of report [Purchase/Sale]
 * @param {String} period      Period under consideration [Today/Month/year]
 * @param {String} filter      Search query to filter records
 * @param {Boolean} isSummary  If the report is stock summary or not
 * @param {Array} invoices     Invoice results
 */
export async function saveToPDF(category, period, filter, invoices, isSummary) {
  try {
    const report = await window.eel.generateReport(
      category,
      period,
      filter,
      invoices,
      isSummary
    )();
    if (report) {
      const win = window.open("", "");
      win.document.write(report);
      win.document.close();
      win.print();
    }
  } catch (error) {
    console.log(error);
  }
}
