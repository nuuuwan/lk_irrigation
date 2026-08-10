# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_13:25:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **229,673 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **6** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 13:25:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.42 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-08-10 13:16:40 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.026 |  |
| 2026-08-10 13:15:31 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.061 |  |
| 2026-08-10 13:14:29 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-10 13:14:26 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-10 13:12:54 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.009 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 13:00:34 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | 0.337 | 🔺 Rising |
| 2026-08-10 13:25:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.42 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-08-10 13:04:58 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-10 13:14:26 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-10 13:02:37 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-10 13:03:24 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 13:00:08 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-10 13:02:03 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 13:00:45 | Nawalapitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-08-10 13:03:29 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 13:02:25 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 13:00:35 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 12:04:24 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 13:05:44 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-10 13:01:50 | Baddegama (Gin Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-08-10 13:03:20 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 13:02:03 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-10 13:02:27 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 13:03:47 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-10 13:05:48 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-08-10 13:06:04 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-10 13:09:23 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-10 13:00:48 | Thanthirimale (Malwathu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-10 13:14:29 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-10 13:06:09 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-10 13:12:54 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.009 |  |
| 2026-08-10 13:02:02 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-08-10 13:10:51 | Panadugama (Nilwala Ganga) | 3.78 | 🟢 Normal | -0.010 |  |
| 2026-08-10 13:08:23 | Peradeniya (Mahaweli Ganga) | 3.62 | 🟢 Normal | -0.018 |  |
| 2026-08-10 13:04:19 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-08-10 13:16:40 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.026 |  |
| 2026-08-10 13:02:15 | Hanwella (Kelani Ganga) | 2.31 | 🟢 Normal | -0.041 |  |
| 2026-08-10 13:01:08 | Ellagawa (Kalu Ganga) | 6.26 | 🟢 Normal | -0.041 |  |
| 2026-08-10 13:02:51 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | -0.045 |  |
| 2026-08-10 13:04:45 | Rathnapura (Kalu Ganga) | 2.45 | 🟢 Normal | -0.049 |  |
| 2026-08-10 13:15:31 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.061 |  |
| 2026-08-10 13:07:03 | Glencourse (Kelani Ganga) | 10.55 | 🟢 Normal | -0.117 |  |
| 2026-08-10 13:02:30 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.175 |  |
| 2026-08-10 13:09:27 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.179 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)