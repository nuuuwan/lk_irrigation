# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--23_11:27:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **323,526 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 11:27:48 | Moraketiya (Walawe Ganga) | 1.68 | 🟢 Normal | -0.008 |  |
| 2026-11-23 11:13:03 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-23 11:09:03 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-23 11:08:00 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-11-23 11:07:23 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.057 |  |
| 2026-11-23 11:07:09 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | -0.027 |  |
| 2026-11-23 11:06:29 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 11:05:59 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.028 |  |
| 2026-11-23 11:05:40 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | -0.019 |  |
| 2026-11-23 11:05:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.54 | 🟢 Normal | 0.000 |  |
| 2026-11-23 11:04:50 | Ellagawa (Kalu Ganga) | 5.42 | 🟢 Normal | -0.039 |  |
| 2026-11-23 11:04:49 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.115 |  |
| 2026-11-23 11:04:42 | Hanwella (Kelani Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 11:04:08 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-23 11:04:01 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 11:03:57 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-23 11:03:52 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-11-23 11:03:44 | Glencourse (Kelani Ganga) | 9.47 | 🟢 Normal | -0.031 |  |
| 2026-11-23 11:03:33 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-23 11:03:08 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-23 11:02:52 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.097 |  |
| 2026-11-23 11:02:51 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-11-23 11:02:51 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | -0.010 |  |
| 2026-11-23 11:02:42 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.059 |  |
| 2026-11-23 11:02:39 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 11:02:27 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.040 |  |
| 2026-11-23 11:02:17 | Panadugama (Nilwala Ganga) | 3.89 | 🟢 Normal | -0.054 |  |
| 2026-11-23 11:02:13 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.051 |  |
| 2026-11-23 11:02:07 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-11-23 11:02:00 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-23 11:01:26 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-11-23 11:01:26 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.030 |  |
| 2026-11-23 11:01:23 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-11-23 11:01:17 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.031 |  |
| 2026-11-23 11:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-23 11:00:42 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-23 11:00:40 | Pitabeddara (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 11:00:17 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 11:08:00 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-11-23 11:04:08 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-23 11:00:42 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-23 11:04:42 | Hanwella (Kelani Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 11:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-23 11:04:01 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 11:02:51 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-11-23 11:06:29 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 11:02:00 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-23 11:00:40 | Pitabeddara (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 11:03:08 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-23 11:03:57 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-23 11:02:39 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 11:03:33 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-23 11:09:03 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-23 11:13:03 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-23 11:05:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.54 | 🟢 Normal | 0.000 |  |
| 2026-11-23 11:27:48 | Moraketiya (Walawe Ganga) | 1.68 | 🟢 Normal | -0.008 |  |
| 2026-11-23 11:03:52 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-11-23 11:01:26 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-11-23 11:02:07 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-11-23 11:00:17 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-11-23 11:02:51 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | -0.010 |  |
| 2026-11-23 11:05:40 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | -0.019 |  |
| 2026-11-23 11:01:23 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-23 11:07:09 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | -0.027 |  |
| 2026-11-23 11:05:59 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.028 |  |
| 2026-11-23 11:01:26 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.030 |  |
| 2026-11-23 11:01:17 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.031 |  |
| 2026-11-23 11:03:44 | Glencourse (Kelani Ganga) | 9.47 | 🟢 Normal | -0.031 |  |
| 2026-11-23 11:04:50 | Ellagawa (Kalu Ganga) | 5.42 | 🟢 Normal | -0.039 |  |
| 2026-11-23 11:02:27 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.040 |  |
| 2026-11-23 11:02:13 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.051 |  |
| 2026-11-23 11:02:17 | Panadugama (Nilwala Ganga) | 3.89 | 🟢 Normal | -0.054 |  |
| 2026-11-23 11:07:23 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.057 |  |
| 2026-11-23 11:02:42 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.059 |  |
| 2026-11-23 11:02:52 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.097 |  |
| 2026-11-23 11:04:49 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.115 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)