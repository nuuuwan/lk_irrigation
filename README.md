# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--25_14:14:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **325,389 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 14:14:40 | Urawa (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-11-25 14:09:04 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.205 |  |
| 2026-11-25 14:07:49 | Rathnapura (Kalu Ganga) | 2.74 | 🟢 Normal | -0.178 |  |
| 2026-11-25 14:06:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.78 | 🟢 Normal | -0.047 |  |
| 2026-11-25 14:05:59 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.019 |  |
| 2026-11-25 14:05:27 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | -0.034 |  |
| 2026-11-25 14:05:11 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-25 14:05:07 | Moragaswewa (Deduru Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-25 14:05:03 | Dunamale (Aththanagalu Oya) | 2.86 | 🟢 Normal | -0.020 |  |
| 2026-11-25 14:04:59 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-11-25 14:04:44 | Moraketiya (Walawe Ganga) | 2.03 | 🟢 Normal | -0.038 |  |
| 2026-11-25 14:04:21 | Badalgama (Maha Oya) | 3.59 | 🟢 Normal | -0.031 |  |
| 2026-11-25 14:04:12 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-11-25 14:04:11 | Ellagawa (Kalu Ganga) | 6.72 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 14:02:45 | Thanamalwila (Kirindi Oya) | 1.84 | 🟢 Normal | 16.000 | 🔺 Rising |
| 2026-11-25 14:04:12 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-11-25 14:03:28 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-11-25 14:02:32 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-25 14:01:05 | Putupaula (Kalu Ganga) | 1.50 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-25 14:01:22 | Horowpothana (Yan Oya) | 2.71 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-25 14:03:30 | Nagalagam Street (Kelani Ganga) | 0.78 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-25 14:02:53 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-25 14:01:22 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-25 14:02:24 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-25 14:01:02 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-11-25 14:05:07 | Moragaswewa (Deduru Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-25 14:01:38 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-25 14:03:40 | Manampitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-25 14:05:11 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-25 13:03:25 | Kuda Oya (Kirindi Oya) | 1.84 | 🟢 Normal | -0.006 |  |
| 2026-11-25 14:14:40 | Urawa (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-11-25 14:04:59 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-11-25 14:01:55 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-11-25 14:05:59 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.019 |  |
| 2026-11-25 14:02:41 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-11-25 14:05:03 | Dunamale (Aththanagalu Oya) | 2.86 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-25 13:07:22 | Baddegama (Gin Ganga) | 2.21 | 🟢 Normal | -0.029 |  |
| 2026-11-25 14:04:11 | Ellagawa (Kalu Ganga) | 6.72 | 🟢 Normal | -0.030 |  |
| 2026-11-25 14:04:21 | Badalgama (Maha Oya) | 3.59 | 🟢 Normal | -0.031 |  |
| 2026-11-25 14:01:36 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.031 |  |
| 2026-11-25 14:05:27 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | -0.034 |  |
| 2026-11-25 14:04:44 | Moraketiya (Walawe Ganga) | 2.03 | 🟢 Normal | -0.038 |  |
| 2026-11-25 14:03:41 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | -0.040 |  |
| 2026-11-25 14:02:07 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.041 |  |
| 2026-11-25 14:06:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.78 | 🟢 Normal | -0.047 |  |
| 2026-11-25 14:02:37 | Giriulla (Maha Oya) | 2.27 | 🟢 Normal | -0.062 |  |
| 2026-11-25 14:00:42 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | -0.077 |  |
| 2026-11-25 14:03:27 | Panadugama (Nilwala Ganga) | 4.52 | 🟢 Normal | -0.080 |  |
| 2026-11-25 14:01:14 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | -0.139 |  |
| 2026-11-25 14:07:49 | Rathnapura (Kalu Ganga) | 2.74 | 🟢 Normal | -0.178 |  |
| 2026-11-25 14:03:09 | Hanwella (Kelani Ganga) | 3.00 | 🟢 Normal | -0.180 |  |
| 2026-11-25 14:09:04 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.205 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)