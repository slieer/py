import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('https://edp.skyworthdigital.com/edp/#/login');
  await page.getByRole('textbox', { name: '请输入账号' }).click();
  await page.getByRole('textbox', { name: '请输入账号' }).fill('SDT14467');
  await page.getByRole('textbox', { name: '请输入密码' }).click();
  await page.getByRole('textbox', { name: '请输入密码' }).fill('nji99ol.');
  await page.getByRole('button', { name: '登录' }).click();
  
  await page.getByText('销售', { exact: true }).click();
  await page.getByRole('menuitem', { name: '国内运营商报盘 ' }).locator('div').click();
  await page.getByRole('menuitem', { name: '元数据管理' }).click();

  await page.locator('iframe').contentFrame().getByRole('listitem').filter({ hasText: '100条/页' }).locator('span').click();

});


