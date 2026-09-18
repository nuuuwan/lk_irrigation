# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--18_20:18:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **264,537 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 20:18:05 | Panadugama (Nilwala Ganga) | 3.43 | 🟢 Normal | -0.033 |  |
| 2026-09-18 20:13:43 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-18 20:07:27 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-09-18 20:07:02 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.087 |  |
| 2026-09-18 20:06:53 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-18 20:06:40 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-09-18 20:06:39 | Baddegama (Gin Ganga) | 2.90 | 🟢 Normal | -0.049 |  |
| 2026-09-18 20:06:33 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-18 20:06:08 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.019 |  |
| 2026-09-18 20:05:20 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | -0.039 |  |
| 2026-09-18 20:04:40 | Glencourse (Kelani Ganga) | 9.73 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-09-18 20:04:17 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | -0.019 |  |
| 2026-09-18 20:04:01 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | -0.009 |  |
| 2026-09-18 20:04:01 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-18 20:03:33 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-09-18 20:03:29 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-09-18 20:03:28 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-09-18 20:03:24 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-09-18 20:03:02 | Magura (Kalu Ganga) | 3.75 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-18 20:02:51 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.077 |  |
| 2026-09-18 20:02:46 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.091 |  |
| 2026-09-18 20:02:39 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-18 20:02:29 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 20:02:25 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-18 20:02:24 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | 0.000 |  |
| 2026-09-18 20:02:09 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 20:02:08 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-18 20:02:06 | Deraniyagala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.178 |  |
| 2026-09-18 20:02:04 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | -0.011 |  |
| 2026-09-18 20:02:01 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-09-18 20:01:52 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-18 20:01:50 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.045 |  |
| 2026-09-18 20:01:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-09-18 20:01:09 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-18 20:00:08 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 20:03:24 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-09-18 20:04:40 | Glencourse (Kelani Ganga) | 9.73 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-09-18 20:03:02 | Magura (Kalu Ganga) | 3.75 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-18 20:01:52 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-18 20:04:01 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-18 20:06:53 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-18 20:00:08 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-18 20:02:29 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 20:02:09 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 20:01:09 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:04:24 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-18 20:13:43 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-18 20:02:39 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-18 20:02:24 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | 0.000 |  |
| 2026-09-18 20:02:25 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-18 20:03:33 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-09-18 20:06:33 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-18 20:06:40 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:03:43 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-18 20:02:08 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-18 20:01:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-09-18 20:04:01 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | -0.009 |  |
| 2026-09-18 18:03:43 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.010 |  |
| 2026-09-18 19:03:35 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-09-18 20:07:27 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-09-18 20:03:28 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-09-18 20:03:29 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-09-18 20:02:01 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-09-18 20:02:04 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | -0.011 |  |
| 2026-09-18 20:06:08 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.019 |  |
| 2026-09-18 20:04:17 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | -0.019 |  |
| 2026-09-18 20:18:05 | Panadugama (Nilwala Ganga) | 3.43 | 🟢 Normal | -0.033 |  |
| 2026-09-18 20:05:20 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | -0.039 |  |
| 2026-09-18 20:01:50 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.045 |  |
| 2026-09-18 20:06:39 | Baddegama (Gin Ganga) | 2.90 | 🟢 Normal | -0.049 |  |
| 2026-09-18 20:02:51 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.077 |  |
| 2026-09-18 20:07:02 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.087 |  |
| 2026-09-18 20:02:46 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.091 |  |
| 2026-09-18 20:02:06 | Deraniyagala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.178 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)