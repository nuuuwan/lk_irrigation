# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--23_13:10:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **323,605 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 13:10:19 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:09:04 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | -0.009 |  |
| 2026-11-23 13:08:36 | Peradeniya (Mahaweli Ganga) | 2.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-23 13:08:03 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-23 13:07:40 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:07:25 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:07:15 | Moragaswewa (Deduru Oya) | 1.16 | 🟢 Normal | -0.037 |  |
| 2026-11-23 13:06:43 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:06:07 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:05:58 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.031 |  |
| 2026-11-23 13:05:27 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:05:19 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:04:38 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-11-23 13:04:19 | Ellagawa (Kalu Ganga) | 5.34 | 🟢 Normal | -0.039 |  |
| 2026-11-23 13:04:13 | Thalgahagoda (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-23 13:04:12 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-11-23 13:04:08 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.059 |  |
| 2026-11-23 13:04:05 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-11-23 13:04:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.44 | 🟢 Normal | -10.800 |  |
| 2026-11-23 13:03:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.50 | 🟢 Normal | -10.800 |  |
| 2026-11-23 13:03:44 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | -0.039 |  |
| 2026-11-23 13:03:09 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 13:03:08 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-11-23 13:03:05 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.127 |  |
| 2026-11-23 13:02:51 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 13:02:40 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.025 |  |
| 2026-11-23 13:02:38 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-23 13:02:23 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | -0.020 |  |
| 2026-11-23 13:02:20 | Glencourse (Kelani Ganga) | 9.43 | 🟢 Normal | -0.010 |  |
| 2026-11-23 13:02:17 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:01:46 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:01:44 | Moraketiya (Walawe Ganga) | 1.68 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-23 13:01:41 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:01:37 | Manampitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:01:29 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | -0.011 |  |
| 2026-11-23 13:01:11 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:00:35 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:00:31 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:00:19 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-23 13:00:11 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 13:08:03 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-23 13:00:19 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-23 13:01:44 | Moraketiya (Walawe Ganga) | 1.68 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-23 13:02:38 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-23 13:04:13 | Thalgahagoda (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-23 13:08:36 | Peradeniya (Mahaweli Ganga) | 2.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-23 13:03:09 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 13:02:51 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 13:05:19 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:01:41 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:01:46 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:00:35 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:06:07 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:01:11 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:02:17 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:10:19 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:05:27 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:07:25 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:01:37 | Manampitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:07:40 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:06:43 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-11-23 13:09:04 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | -0.009 |  |
| 2026-11-23 13:04:38 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-11-23 13:04:05 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-11-23 13:03:08 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-11-23 13:02:20 | Glencourse (Kelani Ganga) | 9.43 | 🟢 Normal | -0.010 |  |
| 2026-11-23 13:01:29 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | -0.011 |  |
| 2026-11-23 13:04:12 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-11-23 13:02:23 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | -0.020 |  |
| 2026-11-23 13:00:11 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-23 13:02:40 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.025 |  |
| 2026-11-23 13:05:58 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.031 |  |
| 2026-11-23 13:07:15 | Moragaswewa (Deduru Oya) | 1.16 | 🟢 Normal | -0.037 |  |
| 2026-11-23 13:03:44 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | -0.039 |  |
| 2026-11-23 13:04:19 | Ellagawa (Kalu Ganga) | 5.34 | 🟢 Normal | -0.039 |  |
| 2026-11-23 13:04:08 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.059 |  |
| 2026-11-23 13:03:05 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.127 |  |
| 2026-11-23 13:04:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.44 | 🟢 Normal | -10.800 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)