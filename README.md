# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--23_05:26:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **323,298 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 05:26:36 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.084 |  |
| 2026-11-23 05:26:12 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-23 05:25:01 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-23 05:13:19 | Rathnapura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.052 |  |
| 2026-11-23 05:13:00 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | 504.000 | 🔺 Rising |
| 2026-11-23 05:12:59 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 504.000 | 🔺 Rising |
| 2026-11-23 05:11:08 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.027 |  |
| 2026-11-23 05:08:26 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | -540.000 |  |
| 2026-11-23 05:08:25 | Thawalama (Gin Ganga) | 2.70 | 🟢 Normal | -540.000 |  |
| 2026-11-23 05:07:39 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 05:06:18 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-23 05:05:58 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | -0.010 |  |
| 2026-11-23 05:05:45 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-11-23 05:05:13 | Glencourse (Kelani Ganga) | 9.42 | 🟢 Normal | -0.167 |  |
| 2026-11-23 05:05:12 | Hanwella (Kelani Ganga) | 1.17 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-11-23 05:04:39 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | 0.000 |  |
| 2026-11-23 05:03:47 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-11-23 05:03:25 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.101 |  |
| 2026-11-23 05:03:24 | Moragaswewa (Deduru Oya) | 1.78 | 🟢 Normal | -0.190 |  |
| 2026-11-23 05:03:18 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 05:02:45 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-23 05:02:41 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-23 05:02:36 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-11-23 05:02:27 | Thanamalwila (Kirindi Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-11-23 05:02:04 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 05:01:43 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-23 05:01:42 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-23 05:01:27 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 05:01:23 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-11-23 05:01:13 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.114 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 05:13:00 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | 504.000 | 🔺 Rising |
| 2026-11-23 05:03:47 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-11-23 04:41:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-11-23 05:05:12 | Hanwella (Kelani Ganga) | 1.17 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-11-23 05:25:01 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-23 05:26:12 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-22 18:00:53 | Weraganthota (Mahaweli Ganga) | -2.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-23 05:00:34 | Thalgahagoda (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-23 04:02:03 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-23 05:07:39 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 05:01:42 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-23 05:02:41 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-23 05:03:18 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 05:01:27 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 05:02:36 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:00:10 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-11-23 05:02:45 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-23 05:04:39 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | 0.000 |  |
| 2026-11-23 05:02:04 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 05:01:00 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-11-23 05:01:43 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:02:00 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-23 05:06:18 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-23 05:02:27 | Thanamalwila (Kirindi Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-11-23 05:05:45 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-11-23 05:05:58 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | -0.010 |  |
| 2026-11-23 05:01:23 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-23 05:11:08 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.027 |  |
| 2026-11-23 05:01:00 | Moraketiya (Walawe Ganga) | 2.55 | 🟢 Normal | -0.049 |  |
| 2026-11-23 05:13:19 | Rathnapura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.052 |  |
| 2026-11-23 04:36:24 | Panadugama (Nilwala Ganga) | 4.14 | 🟢 Normal | -0.052 |  |
| 2026-11-23 05:26:36 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.084 |  |
| 2026-11-23 05:03:25 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.101 |  |
| 2026-11-23 05:01:13 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.114 |  |
| 2026-11-23 04:05:28 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.129 |  |
| 2026-11-23 05:05:13 | Glencourse (Kelani Ganga) | 9.42 | 🟢 Normal | -0.167 |  |
| 2026-11-23 05:03:24 | Moragaswewa (Deduru Oya) | 1.78 | 🟢 Normal | -0.190 |  |
| 2026-11-23 05:08:26 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | -540.000 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)