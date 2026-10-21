# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--21_06:25:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **293,738 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 06:25:49 | Galgamuwa (Mee Oya) | 1.60 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-21 06:18:11 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-21 06:11:49 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | -0.037 |  |
| 2026-10-21 06:09:57 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-21 06:09:45 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | -0.061 |  |
| 2026-10-21 06:08:31 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.009 |  |
| 2026-10-21 06:07:53 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.031 |  |
| 2026-10-21 06:07:40 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | -0.019 |  |
| 2026-10-21 06:07:25 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.046 |  |
| 2026-10-21 06:06:16 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-21 06:06:16 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.048 |  |
| 2026-10-21 06:06:04 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-21 06:05:29 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | -0.010 |  |
| 2026-10-21 06:05:23 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.039 |  |
| 2026-10-21 06:05:05 | Panadugama (Nilwala Ganga) | 4.14 | 🟢 Normal | -0.030 |  |
| 2026-10-21 06:04:33 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | -0.095 |  |
| 2026-10-21 06:04:13 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.009 |  |
| 2026-10-21 06:03:58 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-21 06:03:48 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-10-21 06:03:35 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-21 06:03:31 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-21 06:03:27 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-21 06:03:09 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-10-21 06:03:01 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.024 |  |
| 2026-10-21 06:02:59 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.060 |  |
| 2026-10-21 06:02:48 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-21 06:02:31 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-21 06:02:20 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.013 |  |
| 2026-10-21 06:01:57 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-21 06:01:44 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-21 06:01:29 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.055 |  |
| 2026-10-21 06:01:26 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-10-21 06:00:42 | Ellagawa (Kalu Ganga) | 5.61 | 🟢 Normal | -0.010 |  |
| 2026-10-21 06:00:33 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-21 06:00:16 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-21 06:00:09 | Siyambalanduwa (Heda Oya) | 0.85 | 🟢 Normal | -0.080 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 06:09:45 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | -0.061 |  |
| 2026-10-21 05:01:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.10 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-10-21 06:25:49 | Galgamuwa (Mee Oya) | 1.60 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-21 06:01:57 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-21 06:18:11 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-21 06:06:16 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-21 06:03:31 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-21 06:03:27 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-20 18:04:50 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-21 06:09:57 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-21 06:00:16 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-21 06:03:35 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-21 06:02:48 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-21 06:03:58 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-21 06:01:44 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-21 06:03:09 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-10-21 06:06:04 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:01:22 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-21 06:00:33 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-21 06:08:31 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.009 |  |
| 2026-10-21 06:04:13 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.009 |  |
| 2026-10-21 06:05:29 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | -0.010 |  |
| 2026-10-21 06:02:31 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-21 06:00:42 | Ellagawa (Kalu Ganga) | 5.61 | 🟢 Normal | -0.010 |  |
| 2026-10-21 06:03:48 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-10-21 06:02:20 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.013 |  |
| 2026-10-21 06:07:40 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | -0.019 |  |
| 2026-10-21 06:01:26 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-10-21 06:03:01 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.024 |  |
| 2026-10-21 06:05:05 | Panadugama (Nilwala Ganga) | 4.14 | 🟢 Normal | -0.030 |  |
| 2026-10-21 06:07:53 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.031 |  |
| 2026-10-21 06:11:49 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | -0.037 |  |
| 2026-10-21 06:05:23 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.039 |  |
| 2026-10-21 06:07:25 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.046 |  |
| 2026-10-21 06:06:16 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.048 |  |
| 2026-10-21 06:01:29 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.055 |  |
| 2026-10-21 06:02:59 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.060 |  |
| 2026-10-21 06:00:09 | Siyambalanduwa (Heda Oya) | 0.85 | 🟢 Normal | -0.080 |  |
| 2026-10-21 06:04:33 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)