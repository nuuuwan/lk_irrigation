# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--23_14:05:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **323,633 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 14:05:19 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-23 14:04:51 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.028 |  |
| 2026-11-23 14:04:26 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-23 14:03:58 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-11-23 14:03:35 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-23 14:03:08 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-23 14:03:07 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-23 14:03:04 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-23 14:03:03 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-23 14:02:52 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | -0.011 |  |
| 2026-11-23 14:02:47 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-23 14:02:47 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-23 14:02:28 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-23 14:02:20 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.041 |  |
| 2026-11-23 14:02:18 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 14:02:15 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.040 |  |
| 2026-11-23 14:02:12 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.112 |  |
| 2026-11-23 14:02:01 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 14:02:01 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-23 14:01:43 | Moraketiya (Walawe Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-11-23 14:01:34 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-23 14:01:34 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-23 14:01:10 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-11-23 14:01:00 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | -0.045 |  |
| 2026-11-23 14:00:59 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 14:00:11 | Weraganthota (Mahaweli Ganga) | -2.11 | 🟢 Normal | -0.070 |  |
| 2026-11-23 14:00:09 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:59:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.42 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 14:02:28 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-23 14:02:01 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-23 14:01:34 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-23 14:04:26 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-23 14:02:47 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-23 13:04:13 | Thalgahagoda (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-23 13:08:36 | Peradeniya (Mahaweli Ganga) | 2.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-23 13:03:09 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 14:00:59 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 14:00:09 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-23 14:01:34 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-23 14:02:01 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 14:02:47 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:01:11 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-23 14:03:08 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-23 14:03:04 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-23 14:01:43 | Moraketiya (Walawe Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-11-23 14:02:18 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 14:03:35 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-23 14:05:19 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:07:40 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:09:04 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | -0.009 |  |
| 2026-11-23 13:04:38 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-11-23 13:03:08 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-11-23 13:02:20 | Glencourse (Kelani Ganga) | 9.43 | 🟢 Normal | -0.010 |  |
| 2026-11-23 14:01:10 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-11-23 14:03:58 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-11-23 14:02:52 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | -0.011 |  |
| 2026-11-23 13:59:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.42 | 🟢 Normal | -0.022 |  |
| 2026-11-22 17:02:02 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-23 13:02:40 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.025 |  |
| 2026-11-23 14:04:51 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.028 |  |
| 2026-11-23 13:05:58 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.031 |  |
| 2026-11-23 13:03:44 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | -0.039 |  |
| 2026-11-23 14:02:15 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.040 |  |
| 2026-11-23 14:02:20 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.041 |  |
| 2026-11-23 14:01:00 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | -0.045 |  |
| 2026-11-23 14:00:11 | Weraganthota (Mahaweli Ganga) | -2.11 | 🟢 Normal | -0.070 |  |
| 2026-11-23 14:02:12 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)