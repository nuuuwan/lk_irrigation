# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_03:11:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **236,443 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-18 03:11:40 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:07:40 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-18 03:06:37 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:06:20 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:06:02 | Hanwella (Kelani Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:06:00 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:05:55 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-08-18 03:05:41 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:05:04 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:04:50 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:04:31 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-08-18 03:04:29 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-08-18 03:04:06 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:04:04 | Rathnapura (Kalu Ganga) | 2.98 | 🟢 Normal | -0.031 |  |
| 2026-08-18 03:04:02 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.040 |  |
| 2026-08-18 03:04:02 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:03:45 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:03:08 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 2.118 | 🔺 Rising |
| 2026-08-18 03:02:52 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-18 03:02:36 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-08-18 03:02:34 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 2.118 | 🔺 Rising |
| 2026-08-18 03:02:24 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:02:19 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:02:15 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:02:07 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:02:02 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:01:49 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:01:49 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:01:46 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-08-18 03:01:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.76 | 🟢 Normal | -0.045 |  |
| 2026-08-18 03:01:30 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.011 |  |
| 2026-08-18 03:01:19 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:01:15 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-18 02:49:54 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-08-18 02:37:23 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-18 02:34:40 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.045 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-18 03:04:31 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-08-18 03:03:08 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 2.118 | 🔺 Rising |
| 2026-08-18 02:01:49 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-08-18 03:01:46 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-08-18 03:05:55 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-08-18 03:02:36 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-08-18 03:01:15 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-18 03:02:52 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-18 03:07:40 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-18 03:01:19 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:01:09 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:02:07 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:03:45 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:01:49 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:05:41 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:01:49 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:02:15 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:04:13 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:04:02 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:06:02 | Hanwella (Kelani Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:06:37 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:05:04 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:02:19 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-18 02:37:23 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:02:02 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:02:24 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-18 02:14:19 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:06:00 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:11:40 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:00:44 | Thanthirimale (Malwathu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:04:06 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:04:50 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:06:20 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-18 03:01:30 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.011 |  |
| 2026-08-18 03:04:04 | Rathnapura (Kalu Ganga) | 2.98 | 🟢 Normal | -0.031 |  |
| 2026-08-18 03:04:02 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.040 |  |
| 2026-08-18 02:01:15 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.044 |  |
| 2026-08-18 03:01:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.76 | 🟢 Normal | -0.045 |  |
| 2026-08-17 23:17:12 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.051 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)