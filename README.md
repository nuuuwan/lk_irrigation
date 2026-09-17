# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--17_12:27:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **263,333 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **1** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 12:27:50 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.014 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 12:11:29 | Baddegama (Gin Ganga) | 3.60 | 🟡 Alert | 0.000 |  |
| 2026-09-17 12:03:35 | Magura (Kalu Ganga) | 3.75 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-09-17 12:04:49 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-17 12:03:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.44 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-17 12:05:17 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-17 12:03:47 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-17 12:03:09 | Panadugama (Nilwala Ganga) | 4.69 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-17 12:02:22 | Glencourse (Kelani Ganga) | 9.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-17 12:27:50 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-09-17 12:02:22 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-09-17 12:01:56 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-17 12:01:51 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-09-17 12:12:08 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 12:02:16 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-17 12:02:13 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-17 12:00:35 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-17 12:08:43 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-17 12:03:16 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-17 11:07:31 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-17 12:04:28 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-17 12:04:44 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-17 12:04:45 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-17 12:04:55 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-09-17 12:06:04 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-17 12:11:18 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-09-17 12:01:38 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-17 12:04:47 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-17 12:07:29 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-09-17 12:08:37 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | -0.009 |  |
| 2026-09-17 12:03:35 | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | -0.010 |  |
| 2026-09-17 12:01:16 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-09-17 12:00:27 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-09-17 12:14:00 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | -0.017 |  |
| 2026-09-17 12:08:53 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | -0.019 |  |
| 2026-09-17 12:01:17 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.020 |  |
| 2026-09-17 12:03:37 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.029 |  |
| 2026-09-17 12:01:47 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.030 |  |
| 2026-09-17 12:03:21 | Hanwella (Kelani Ganga) | 1.33 | 🟢 Normal | -0.031 |  |
| 2026-09-17 12:03:17 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.063 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)