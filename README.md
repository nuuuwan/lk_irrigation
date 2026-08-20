# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_02:34:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **239,105 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **9** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-21 02:34:09 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-08-21 02:21:18 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.016 |  |
| 2026-08-21 02:19:13 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-21 02:07:00 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-21 02:05:47 | Glencourse (Kelani Ganga) | 9.95 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-21 02:05:42 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-21 02:05:26 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-08-21 02:05:25 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-08-21 02:05:07 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-21 02:03:08 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-08-21 02:01:05 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-21 02:05:47 | Glencourse (Kelani Ganga) | 9.95 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-21 02:05:26 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-08-21 02:02:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.54 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-21 02:19:13 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-21 01:03:53 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-21 02:01:10 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-20 18:02:56 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-21 02:00:19 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-21 02:03:06 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-21 02:01:46 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-21 02:07:00 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-20 18:04:45 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-21 02:04:46 | Hanwella (Kelani Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-08-21 02:02:36 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-21 02:05:25 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:07:14 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:59:08 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-21 02:00:49 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-21 02:01:43 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-21 02:02:30 | Dunamale (Aththanagalu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-21 02:02:29 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-21 02:05:42 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-21 02:04:34 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-08-21 02:05:07 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 18:02:19 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-21 02:34:09 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-08-21 02:01:32 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-21 02:03:53 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-21 02:03:49 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-08-21 01:02:34 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.013 |  |
| 2026-08-21 02:21:18 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.016 |  |
| 2026-08-21 02:02:23 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.034 |  |
| 2026-08-21 02:01:43 | Ellagawa (Kalu Ganga) | 6.21 | 🟢 Normal | -0.040 |  |
| 2026-08-21 02:04:56 | Rathnapura (Kalu Ganga) | 2.36 | 🟢 Normal | -0.058 |  |
| 2026-08-21 02:03:17 | Peradeniya (Mahaweli Ganga) | 2.94 | 🟢 Normal | -0.058 |  |
| 2026-08-21 00:14:30 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.063 |  |
| 2026-08-21 02:03:02 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.210 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)