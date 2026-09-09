# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--10_04:03:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **256,721 measurements** from **39** stations.
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
| 2026-09-10 04:03:01 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-10 04:02:43 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-10 04:02:37 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-10 04:02:33 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-10 04:02:08 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-10 04:02:06 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | -0.273 |  |
| 2026-09-10 04:02:06 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-10 04:01:41 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-10 04:01:19 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-10 04:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-10 04:01:11 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-10 04:01:10 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-10 04:00:54 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-10 04:00:47 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-09-10 04:00:47 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-10 04:00:31 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-09-10 03:55:47 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.012 |  |
| 2026-09-10 03:27:40 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-10 03:26:45 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.015 |  |
| 2026-09-10 03:20:07 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-09-10 03:19:00 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-09-10 03:17:15 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-10 03:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.730 | 🔺 Rising |
| 2026-09-10 02:04:59 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-09-10 02:20:51 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-10 04:02:08 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-09 18:02:14 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-10 03:02:24 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-10 03:08:13 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-10 03:15:35 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-09-10 04:01:19 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-10 04:01:10 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-10 04:00:47 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-10 04:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-10 04:01:41 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-10 03:02:14 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-10 04:03:01 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-09 18:00:54 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-10 03:06:34 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-10 04:02:33 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-10 03:19:00 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-09-10 03:20:07 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-09-10 04:01:11 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-10 03:04:37 | Glencourse (Kelani Ganga) | 9.29 | 🟢 Normal | 0.000 |  |
| 2026-09-10 04:00:54 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-10 04:02:43 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-10 03:01:37 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-10 03:27:40 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-10 03:06:04 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-10 04:00:31 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-09-10 04:02:37 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-10 04:02:06 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-10 02:06:56 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-10 03:03:44 | Hanwella (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-09-10 04:00:47 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-09-10 03:55:47 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.012 |  |
| 2026-09-10 03:26:45 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.015 |  |
| 2026-09-10 03:03:27 | Ellagawa (Kalu Ganga) | 4.61 | 🟢 Normal | -0.030 |  |
| 2026-09-10 03:09:05 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.039 |  |
| 2026-09-09 18:06:33 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.121 |  |
| 2026-09-10 04:02:06 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | -0.273 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)