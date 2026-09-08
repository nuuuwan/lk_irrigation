# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--09_03:03:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **255,784 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-09 03:03:34 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-09 03:03:29 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.005 |  |
| 2026-09-09 03:03:25 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-09 03:03:22 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.030 |  |
| 2026-09-09 03:03:20 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-09 03:02:41 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-09 03:01:59 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-09 03:01:55 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.037 |  |
| 2026-09-09 03:01:54 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-09 03:01:53 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 03:01:52 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-09 03:01:40 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-09 03:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.045 |  |
| 2026-09-09 03:01:24 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | -0.005 |  |
| 2026-09-09 03:01:11 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-09-09 03:00:33 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-09-09 03:00:30 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-09 03:00:29 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 02:53:11 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-09 02:45:51 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-09 02:39:05 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-09-09 02:35:22 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-09 02:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 9.000 | 🔺 Rising |
| 2026-09-09 01:04:24 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-09-09 02:06:38 | Glencourse (Kelani Ganga) | 9.54 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-09-09 03:00:33 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-09-09 00:07:22 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-09 03:03:34 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-09 03:01:11 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-09-09 03:03:29 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.005 |  |
| 2026-09-09 02:07:43 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-09 03:00:30 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-09 03:01:53 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 02:02:07 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-09 03:01:59 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-09 03:01:40 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:05:02 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-09 02:03:37 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-09-09 02:22:50 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-09-09 01:10:37 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-09-09 03:01:52 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-09 03:00:29 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 02:24:57 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-09 03:01:54 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-09 02:35:22 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-09 03:03:20 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-09 03:02:41 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:00:29 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-09 02:01:31 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-09 03:03:25 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-09 03:01:24 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | -0.005 |  |
| 2026-09-09 02:15:59 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | -0.023 |  |
| 2026-09-09 02:09:01 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.028 |  |
| 2026-09-09 03:03:22 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.030 |  |
| 2026-09-09 02:00:45 | Peradeniya (Mahaweli Ganga) | 2.27 | 🟢 Normal | -0.030 |  |
| 2026-09-08 18:00:11 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.034 |  |
| 2026-09-09 03:01:55 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.037 |  |
| 2026-09-09 03:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.045 |  |
| 2026-09-09 02:19:49 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.057 |  |
| 2026-09-09 02:02:21 | Rathnapura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.078 |  |
| 2026-09-09 02:03:17 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | -0.106 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)