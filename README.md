# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--13_13:03:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **232,350 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-13 13:03:18 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-13 13:03:13 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-08-13 13:03:07 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-08-13 13:03:05 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -7.700 |  |
| 2026-08-13 13:03:04 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-13 13:03:01 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-13 13:02:44 | Hanwella (Kelani Ganga) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-08-13 13:02:38 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-08-13 13:02:28 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-08-13 13:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.030 |  |
| 2026-08-13 13:02:08 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-08-13 13:02:08 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -7.700 |  |
| 2026-08-13 13:02:02 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-13 13:01:27 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-13 13:00:57 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-13 13:00:57 | Thanthirimale (Malwathu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-13 13:00:32 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-13 13:00:14 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-13 13:02:38 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-08-13 13:02:28 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-08-13 13:02:08 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-08-13 13:03:18 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-13 12:02:14 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-13 13:00:14 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-13 12:03:11 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-13 13:03:13 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-08-13 13:03:01 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-13 13:00:57 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-13 13:02:02 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-13 12:03:16 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-13 12:07:01 | Ellagawa (Kalu Ganga) | 4.92 | 🟢 Normal | 0.000 |  |
| 2026-08-13 13:03:04 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-13 12:00:44 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-13 12:02:23 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-13 12:02:47 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-13 12:01:14 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-13 12:02:51 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-13 12:05:35 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-08-13 12:07:18 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-13 13:01:27 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-13 13:00:57 | Thanthirimale (Malwathu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-13 12:01:14 | Peradeniya (Mahaweli Ganga) | 3.22 | 🟢 Normal | 0.000 |  |
| 2026-08-13 12:03:14 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-08-13 13:00:32 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-13 12:03:24 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-08-13 12:05:15 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-08-13 13:03:07 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-08-13 12:01:56 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-08-13 12:06:49 | Magura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-08-13 12:06:59 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-08-13 12:09:12 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.012 |  |
| 2026-08-13 13:02:44 | Hanwella (Kelani Ganga) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-08-13 12:05:31 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.021 |  |
| 2026-08-13 13:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.030 |  |
| 2026-08-13 12:05:32 | Glencourse (Kelani Ganga) | 10.16 | 🟢 Normal | -0.042 |  |
| 2026-08-13 12:01:13 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | -0.085 |  |
| 2026-08-13 13:03:05 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -7.700 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)