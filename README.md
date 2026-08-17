# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_10:31:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **235,824 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-17 10:31:33 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-17 10:23:41 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-08-17 10:22:56 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.031 |  |
| 2026-08-17 10:18:49 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 10:15:37 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-17 10:11:12 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 10:11:05 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-17 10:10:44 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 10:09:19 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-17 10:09:06 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-17 10:08:54 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 10:08:01 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 10:07:01 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | 0.019 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-17 10:10:44 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 10:04:15 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 10:04:30 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 10:07:01 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-17 10:04:00 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-17 10:02:12 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 10:01:38 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 10:00:13 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-17 10:08:54 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 10:01:50 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 10:09:06 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-17 10:11:05 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-17 10:18:49 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 10:08:01 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 10:06:07 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-17 10:03:24 | Hanwella (Kelani Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-08-17 10:23:41 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-08-17 10:04:12 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 10:03:05 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | 0.000 |  |
| 2026-08-17 10:09:19 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-17 10:03:03 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-17 10:03:59 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-17 10:31:33 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-17 10:11:12 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 10:15:37 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-17 10:01:08 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-17 10:01:39 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-08-17 10:02:08 | Thanamalwila (Kirindi Oya) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-08-17 10:05:25 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-08-17 09:03:00 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-08-17 10:05:17 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | -0.013 |  |
| 2026-08-17 10:04:18 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.019 |  |
| 2026-08-17 10:06:31 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.019 |  |
| 2026-08-17 10:22:56 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.031 |  |
| 2026-08-17 10:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.39 | 🟢 Normal | -0.041 |  |
| 2026-08-17 10:05:04 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.049 |  |
| 2026-08-17 10:02:54 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.049 |  |
| 2026-08-17 10:05:03 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.059 |  |
| 2026-08-17 10:05:47 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -1.007 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)