# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--18_16:32:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **319,311 measurements** from **39** stations.
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
| 2026-11-18 16:32:46 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.014 |  |
| 2026-11-18 16:25:15 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | -0.025 |  |
| 2026-11-18 16:23:18 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:13:32 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.009 |  |
| 2026-11-18 16:09:09 | Dunamale (Aththanagalu Oya) | 1.49 | 🟢 Normal | -0.009 |  |
| 2026-11-18 16:09:06 | Moraketiya (Walawe Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:08:15 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-11-18 16:07:56 | Glencourse (Kelani Ganga) | 10.08 | 🟢 Normal | -0.039 |  |
| 2026-11-18 16:07:44 | Panadugama (Nilwala Ganga) | 3.53 | 🟢 Normal | -0.028 |  |
| 2026-11-18 16:07:35 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:07:22 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:06:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:06:42 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:05:43 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-18 16:05:37 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:05:27 | Manampitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-18 16:04:32 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:04:30 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-18 16:04:09 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 16:04:00 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:03:35 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-11-18 16:03:34 | Ellagawa (Kalu Ganga) | 5.02 | 🟢 Normal | -0.010 |  |
| 2026-11-18 16:03:33 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | -0.010 |  |
| 2026-11-18 16:03:23 | Hanwella (Kelani Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-11-18 16:02:59 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:02:58 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-18 16:02:58 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-11-18 16:02:46 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:02:30 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 16:02:09 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-11-18 16:02:08 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:02:07 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:02:07 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.022 |  |
| 2026-11-18 16:01:55 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-11-18 16:01:36 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-11-18 16:01:15 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:01:14 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:00:46 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-18 15:04:13 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-18 16:02:58 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-18 16:04:30 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-18 16:02:30 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 16:04:09 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 16:05:27 | Manampitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-18 16:02:59 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:04:00 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:23:18 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:01:14 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:00:46 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:07:22 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:02:46 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:09:06 | Moraketiya (Walawe Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:02:08 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:01:15 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:07:35 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:04:32 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:06:42 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:05:37 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:02:07 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:06:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-18 16:13:32 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.009 |  |
| 2026-11-18 16:09:09 | Dunamale (Aththanagalu Oya) | 1.49 | 🟢 Normal | -0.009 |  |
| 2026-11-18 16:08:15 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-11-18 16:03:35 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-11-18 16:03:33 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | -0.010 |  |
| 2026-11-18 16:03:34 | Ellagawa (Kalu Ganga) | 5.02 | 🟢 Normal | -0.010 |  |
| 2026-11-18 16:01:36 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-11-18 16:05:43 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-18 16:02:09 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-11-18 16:01:55 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-11-18 16:03:23 | Hanwella (Kelani Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-11-18 16:32:46 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.014 |  |
| 2026-11-18 16:02:58 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-11-18 16:02:07 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.022 |  |
| 2026-11-18 16:25:15 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | -0.025 |  |
| 2026-11-18 16:07:44 | Panadugama (Nilwala Ganga) | 3.53 | 🟢 Normal | -0.028 |  |
| 2026-11-18 16:07:56 | Glencourse (Kelani Ganga) | 10.08 | 🟢 Normal | -0.039 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)