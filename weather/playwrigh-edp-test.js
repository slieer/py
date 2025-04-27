import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('https://edp.skyworthdigital.com/edp/#/login');
  await page.getByRole('textbox', { name: '请输入账号' }).click();
  await page.getByRole('textbox', { name: '请输入账号' }).fill('SDT14467');
  await page.getByRole('textbox', { name: '请输入账号' }).press('Tab');
  await page.getByRole('textbox', { name: '请输入密码' }).fill('nji99ol.');
  await page.getByRole('button', { name: '登录' }).click();
  await page.getByText('销售', { exact: true }).click();
  await page.getByText('国内运营商报盘').click();
  await page.getByRole('menuitem', { name: '元数据管理' }).click();
  await page.locator('iframe').contentFrame().getByRole('textbox', { name: '元数据类别' }).click();
  await page.locator('iframe').contentFrame().getByRole('listitem').filter({ hasText: '客户端数据' }).locator('span').click();
  await page.locator('iframe').contentFrame().locator('div:nth-child(5) > .el-form-item__content > .el-select > .el-input > .el-input__suffix > .el-input__suffix-inner > .el-select__caret').click();
  await page.locator('iframe').contentFrame().locator('div:nth-child(2) > .el-input__suffix > .el-input__suffix-inner > .el-select__caret').click();
  await page.locator('iframe').contentFrame().getByRole('listitem').filter({ hasText: '机顶盒' }).locator('span').click();
  await page.locator('iframe').contentFrame().getByRole('button', { name: ' 搜索' }).click();
  await page.locator('iframe').contentFrame().getByRole('tab', { name: '控制元数据' }).click();
  await page.locator('iframe').contentFrame().getByRole('tab', { name: '数据元数据' }).click();
  await page.locator('iframe').contentFrame().locator('i:nth-child(2)').first().click();
  await page.locator('iframe').contentFrame().getByRole('button', { name: ' 搜索' }).click();
  await page.locator('iframe').contentFrame().locator('.el-tabs__content').click();
  await page.locator('iframe').contentFrame().getByLabel('数据元数据').locator('div').filter({ hasText: '机顶盒是否是 否 搜索重置 收起部分搜索项 新增 导出 #元数据名称元数据描述元数据属性审核状态产品类别数据类型表字段表字段名正则长度可重复可为空常量备注操作' }).nth(3).click({
    button: 'right'
  });
  await page.locator('iframe').contentFrame().getByLabel('数据元数据').locator('div').filter({ hasText: '机顶盒是否是 否 搜索重置 收起部分搜索项 新增 导出 #元数据名称元数据描述元数据属性审核状态产品类别数据类型表字段表字段名正则长度可重复可为空常量备注操作' }).nth(3).click({
    button: 'right'
  });
  await page.locator('iframe').contentFrame().locator('.avue-shade').click();
  await page.locator('iframe').contentFrame().getByRole('cell', { name: '#' }).locator('div').click();
  await page.locator('iframe').contentFrame().locator('.el-table').first().click();
});