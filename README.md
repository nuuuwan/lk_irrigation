# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_11:45:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **228,702 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **5** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 11:45:04 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.006 |  |
| 2026-08-09 11:17:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | -0.018 |  |
| 2026-08-09 11:16:52 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-09 11:12:26 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-08-09 11:11:13 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 11:02:40 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-09 11:02:59 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-08-09 11:03:35 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-08-09 11:10:38 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-09 11:03:27 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 11:01:18 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 11:01:18 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.000 |  |
| 2026-08-09 11:06:43 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-09 11:02:33 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-09 11:05:27 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-09 11:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-09 11:01:44 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 11:08:31 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-09 11:16:52 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-09 11:04:10 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 11:01:21 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 11:02:17 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-09 11:03:25 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-09 11:01:01 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-09 11:06:07 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-08-09 11:04:36 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-09 11:00:44 | Thanthirimale (Malwathu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-09 11:11:13 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-09 11:01:04 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-09 11:45:04 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.006 |  |
| 2026-08-09 11:04:32 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-08-09 11:03:37 | Hanwella (Kelani Ganga) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-08-09 11:12:26 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-08-09 11:02:15 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-08-09 11:04:26 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-08-09 11:06:06 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.012 |  |
| 2026-08-09 11:17:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | -0.018 |  |
| 2026-08-09 11:04:04 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | -0.019 |  |
| 2026-08-09 11:06:53 | Baddegama (Gin Ganga) | 2.32 | 🟢 Normal | -0.022 |  |
| 2026-08-09 11:05:55 | Glencourse (Kelani Ganga) | 10.67 | 🟢 Normal | -0.030 |  |
| 2026-08-09 11:06:37 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.030 |  |
| 2026-08-09 11:08:42 | Peradeniya (Mahaweli Ganga) | 3.63 | 🟢 Normal | -0.037 |  |
| 2026-08-09 11:03:28 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.083 |  |
| 2026-08-09 11:05:20 | Panadugama (Nilwala Ganga) | 4.33 | 🟢 Normal | -0.140 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)