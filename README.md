# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--21_17:17:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **322,003 measurements** from **39** stations.
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
| 2026-11-21 17:17:32 | Urawa (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:14:38 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-21 17:13:42 | Baddegama (Gin Ganga) | 1.89 | 🟢 Normal | -0.021 |  |
| 2026-11-21 17:12:49 | Pitabeddara (Nilwala Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:10:32 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-11-21 17:10:13 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | -0.056 |  |
| 2026-11-21 17:10:05 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-11-21 17:08:40 | Giriulla (Maha Oya) | 3.13 | 🟢 Normal | -0.209 |  |
| 2026-11-21 17:08:29 | Horowpothana (Yan Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:08:27 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-11-21 17:07:51 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.019 |  |
| 2026-11-21 17:07:05 | Peradeniya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.009 |  |
| 2026-11-21 17:06:59 | Kuda Oya (Kirindi Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:06:31 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-11-21 17:05:25 | Badalgama (Maha Oya) | 4.45 | 🟢 Normal | -0.102 |  |
| 2026-11-21 17:05:20 | Panadugama (Nilwala Ganga) | 4.81 | 🟢 Normal | -0.077 |  |
| 2026-11-21 17:05:14 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-11-21 17:04:30 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.011 |  |
| 2026-11-21 17:04:29 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | -0.050 |  |
| 2026-11-21 17:04:14 | Ellagawa (Kalu Ganga) | 6.09 | 🟢 Normal | -0.010 |  |
| 2026-11-21 17:04:05 | Moraketiya (Walawe Ganga) | 2.94 | 🟢 Normal | -0.058 |  |
| 2026-11-21 17:04:05 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-11-21 17:03:49 | Rathnapura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.132 |  |
| 2026-11-21 17:03:26 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.030 |  |
| 2026-11-21 17:03:09 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:02:41 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.020 |  |
| 2026-11-21 17:02:34 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:02:33 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-11-21 17:02:30 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.62 | 🟢 Normal | -0.061 |  |
| 2026-11-21 17:02:27 | Glencourse (Kelani Ganga) | 9.87 | 🟢 Normal | -0.135 |  |
| 2026-11-21 17:01:43 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:01:41 | Thanamalwila (Kirindi Oya) | 1.88 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-21 17:01:36 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:01:16 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:00:59 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.094 |  |
| 2026-11-21 17:00:44 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:00:41 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 17:10:05 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-11-21 17:05:14 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-11-21 17:01:41 | Thanamalwila (Kirindi Oya) | 1.88 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-21 17:10:32 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-11-21 17:14:38 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-21 17:01:16 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:01:43 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:08:29 | Horowpothana (Yan Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:12:49 | Pitabeddara (Nilwala Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:02:34 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:01:36 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:00:44 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:03:09 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:00:41 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:02:30 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:17:32 | Urawa (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:06:59 | Kuda Oya (Kirindi Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:08:27 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-11-21 17:07:05 | Peradeniya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.009 |  |
| 2026-11-21 17:02:33 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-11-21 17:04:14 | Ellagawa (Kalu Ganga) | 6.09 | 🟢 Normal | -0.010 |  |
| 2026-11-21 17:04:05 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-11-21 17:04:30 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.011 |  |
| 2026-11-21 17:07:51 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.019 |  |
| 2026-11-21 17:02:41 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.020 |  |
| 2026-11-21 17:13:42 | Baddegama (Gin Ganga) | 1.89 | 🟢 Normal | -0.021 |  |
| 2026-11-21 17:06:31 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-11-21 17:03:26 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.030 |  |
| 2026-11-21 17:04:29 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | -0.050 |  |
| 2026-11-21 17:10:13 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | -0.056 |  |
| 2026-11-21 17:04:05 | Moraketiya (Walawe Ganga) | 2.94 | 🟢 Normal | -0.058 |  |
| 2026-11-21 17:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.62 | 🟢 Normal | -0.061 |  |
| 2026-11-21 17:05:20 | Panadugama (Nilwala Ganga) | 4.81 | 🟢 Normal | -0.077 |  |
| 2026-11-21 17:00:59 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.094 |  |
| 2026-11-21 17:05:25 | Badalgama (Maha Oya) | 4.45 | 🟢 Normal | -0.102 |  |
| 2026-11-21 17:03:49 | Rathnapura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.132 |  |
| 2026-11-21 17:02:27 | Glencourse (Kelani Ganga) | 9.87 | 🟢 Normal | -0.135 |  |
| 2026-11-21 17:08:40 | Giriulla (Maha Oya) | 3.13 | 🟢 Normal | -0.209 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)