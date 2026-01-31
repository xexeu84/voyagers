const { chromium } = require('playwright-extra');
const stealth = require('puppeteer-extra-plugin-stealth')();
const shell = require('shelljs');
const os = require('node-os-utils');
chromium.use(stealth);

async function startInvisibleAgent() {
    const cpu = os.cpu;
    
    // Aki: Solo actuar si el CPU está relajado para no ralentizar tu trabajo
    const usage = await cpu.usage();
    if (usage > 70) {
        console.log('📉 L390 con carga alta. KAI esperando en segundo plano...');
        return;
    }

    // Navegador en modo HEADLESS (Totalmente invisible)
    const browser = await chromium.launch({ 
        headless: true, 
        args: [
            '--no-sandbox', 
            '--disable-setuid-sandbox',
            '--disable-dev-shm-usage', // Evita cuelgues en máquinas con RAM limitada
            '--disable-accelerated-2d-canvas',
            '--no-first-run'
        ] 
    });
    
    const context = await browser.newContext();
    const page = await context.newPage();

    try {
        console.log('👻 KAI (Modo Invisible): Verificando activos...');
        await page.goto('https://xexeu84.github.io/voyagers/', { waitUntil: 'networkidle' });
        
        // Lógica de reparación automática de Lukas
        const is404 = await page.title().then(t => t.includes('404'));
        if (is404) {
            shell.exec('git add . && git commit -m "Auto-fix: Redeploy" && git push');
        }
    } catch (e) {
        // Silencioso
    } finally {
        await browser.close();
    }
}
startInvisibleAgent();
