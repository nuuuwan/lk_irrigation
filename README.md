# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_09:10:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **238,465 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-20 09:10:30 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | -0.018 |  |
| 2026-08-20 09:09:58 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-08-20 09:08:25 | Rathnapura (Kalu Ganga) | 2.82 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-08-20 09:08:20 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-08-20 09:08:06 | Magura (Kalu Ganga) | 2.71 | 🟢 Normal | 0.268 | 🔺 Rising |
| 2026-08-20 09:07:16 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-08-20 09:06:35 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-08-20 09:06:05 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-08-20 09:05:46 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-20 09:05:38 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-20 09:05:23 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-20 09:08:06 | Magura (Kalu Ganga) | 2.71 | 🟢 Normal | 0.268 | 🔺 Rising |
| 2026-08-20 09:08:25 | Rathnapura (Kalu Ganga) | 2.82 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-08-20 09:01:27 | Peradeniya (Mahaweli Ganga) | 3.03 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-08-20 09:04:34 | Ellagawa (Kalu Ganga) | 5.23 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-08-20 09:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.91 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-08-20 09:02:35 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-08-20 09:06:35 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-08-20 09:04:12 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-20 09:05:38 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-20 09:02:17 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-20 09:01:11 | Thanthirimale (Malwathu Oya) | 0.75 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-20 09:01:45 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-20 09:01:20 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-20 09:03:13 | Moragaswewa (Deduru Oya) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-20 09:01:22 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 09:04:42 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-20 09:02:16 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-20 09:05:23 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-20 09:06:05 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-08-20 09:09:58 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-08-20 08:02:35 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-20 09:02:36 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-20 09:01:58 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-20 09:02:34 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-20 09:04:09 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-08-20 09:05:46 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-20 09:08:20 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-08-20 09:03:18 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-20 09:05:04 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-20 09:05:10 | Deraniyagala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.009 |  |
| 2026-08-20 09:04:13 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | -0.010 |  |
| 2026-08-20 09:02:57 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-08-20 09:02:17 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-08-20 09:10:30 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | -0.018 |  |
| 2026-08-20 09:01:37 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.021 |  |
| 2026-08-20 09:00:13 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.022 |  |
| 2026-08-20 09:01:38 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.050 |  |
| 2026-08-20 09:04:14 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.117 |  |
| 2026-08-20 09:02:47 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)