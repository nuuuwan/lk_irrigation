# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_23:07:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **238,090 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-19 23:07:57 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-19 23:07:47 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-19 23:06:59 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-08-19 23:05:17 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-19 23:05:06 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.041 |  |
| 2026-08-19 23:05:05 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-08-19 23:04:52 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | -0.012 |  |
| 2026-08-19 23:04:25 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.066 |  |
| 2026-08-19 23:04:14 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.039 |  |
| 2026-08-19 23:03:45 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-19 23:03:42 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-08-19 23:03:16 | Moragaswewa (Deduru Oya) | -0.17 | 🟢 Normal | -33.000 |  |
| 2026-08-19 23:03:14 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-19 23:03:08 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-08-19 23:03:01 | Hanwella (Kelani Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-08-19 23:02:58 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-19 23:02:47 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-19 23:02:40 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | -33.000 |  |
| 2026-08-19 23:02:23 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-19 23:02:16 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-19 23:02:12 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-19 23:02:07 | Ellagawa (Kalu Ganga) | 4.99 | 🟢 Normal | 0.000 |  |
| 2026-08-19 23:02:00 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-19 23:01:45 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-19 23:01:42 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-19 23:01:26 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-19 23:01:22 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-19 23:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-08-19 23:00:08 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-19 22:13:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.12 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-08-19 23:06:59 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-08-19 22:01:14 | Peradeniya (Mahaweli Ganga) | 3.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-19 23:05:17 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-19 23:02:16 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-19 23:02:23 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-19 23:01:45 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-19 22:01:09 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-19 23:00:08 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-19 21:05:48 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-19 23:01:26 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-19 23:07:57 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-19 22:01:27 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-19 18:02:52 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-19 23:02:58 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-19 23:02:47 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-19 23:02:07 | Ellagawa (Kalu Ganga) | 4.99 | 🟢 Normal | 0.000 |  |
| 2026-08-19 23:03:42 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-08-19 22:11:24 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-08-19 23:03:45 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-19 23:01:42 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-19 23:02:12 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-19 23:07:47 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-19 22:04:28 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-19 23:03:14 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-19 18:02:30 | Thanthirimale (Malwathu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-19 23:05:05 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-08-19 22:07:23 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-19 23:02:00 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-19 23:01:22 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-19 23:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-08-19 18:01:56 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | -0.010 |  |
| 2026-08-19 23:03:08 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-08-19 23:04:52 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | -0.012 |  |
| 2026-08-19 23:03:01 | Hanwella (Kelani Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-08-19 23:04:14 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.039 |  |
| 2026-08-19 23:05:06 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.041 |  |
| 2026-08-19 23:04:25 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.066 |  |
| 2026-08-19 23:03:16 | Moragaswewa (Deduru Oya) | -0.17 | 🟢 Normal | -33.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)