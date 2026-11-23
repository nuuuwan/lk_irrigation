# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--23_07:13:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **323,377 measurements** from **39** stations.
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
| 2026-11-23 07:13:06 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-23 07:11:37 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-23 07:11:32 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-11-23 07:10:04 | Panadugama (Nilwala Ganga) | 4.04 | 🟢 Normal | -0.032 |  |
| 2026-11-23 07:09:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.46 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-11-23 07:08:31 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | -0.009 |  |
| 2026-11-23 07:06:11 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.145 |  |
| 2026-11-23 07:05:57 | Rathnapura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.073 |  |
| 2026-11-23 07:05:27 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.047 |  |
| 2026-11-23 07:05:18 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 07:05:09 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-11-23 07:04:58 | Moragaswewa (Deduru Oya) | 1.41 | 🟢 Normal | -0.140 |  |
| 2026-11-23 07:04:28 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-11-23 07:04:17 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-23 07:04:09 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-11-23 07:04:08 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-23 07:04:03 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-11-23 07:03:49 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 07:03:41 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-23 07:03:41 | Magura (Kalu Ganga) | 2.47 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-11-23 07:03:20 | Moraketiya (Walawe Ganga) | 2.05 | 🟢 Normal | -0.156 |  |
| 2026-11-23 07:03:04 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | -0.011 |  |
| 2026-11-23 07:03:00 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-11-23 07:02:54 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-23 07:02:53 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-23 07:02:49 | Glencourse (Kelani Ganga) | 9.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-23 07:02:46 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-23 07:02:44 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.131 |  |
| 2026-11-23 07:02:37 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-23 07:02:22 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.003 |  |
| 2026-11-23 07:02:20 | Peradeniya (Mahaweli Ganga) | 2.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-23 07:02:16 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-11-23 07:02:13 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-11-23 07:02:08 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | -0.033 |  |
| 2026-11-23 07:01:56 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 07:01:12 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-23 07:00:43 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.073 |  |
| 2026-11-23 07:00:16 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 07:09:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.46 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-11-23 07:03:41 | Magura (Kalu Ganga) | 2.47 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-11-23 07:01:12 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-23 07:02:54 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-23 07:02:53 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-23 07:02:20 | Peradeniya (Mahaweli Ganga) | 2.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-23 07:02:49 | Glencourse (Kelani Ganga) | 9.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-23 07:04:17 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-23 07:02:37 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-23 07:05:18 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 07:02:46 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-23 07:01:56 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 07:04:08 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-23 07:02:16 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-11-23 07:03:49 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 07:03:00 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-11-23 07:03:41 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-23 07:11:37 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-23 07:13:06 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-23 07:02:22 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.003 |  |
| 2026-11-23 07:11:32 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-11-23 07:08:31 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | -0.009 |  |
| 2026-11-23 07:05:09 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-11-23 07:04:03 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-11-23 07:04:28 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-11-23 07:02:13 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-11-23 07:00:16 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-11-23 07:03:04 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | -0.011 |  |
| 2026-11-23 07:04:09 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-23 07:10:04 | Panadugama (Nilwala Ganga) | 4.04 | 🟢 Normal | -0.032 |  |
| 2026-11-23 07:02:08 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | -0.033 |  |
| 2026-11-23 07:05:27 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.047 |  |
| 2026-11-23 07:00:43 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.073 |  |
| 2026-11-23 07:05:57 | Rathnapura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.073 |  |
| 2026-11-23 07:02:44 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.131 |  |
| 2026-11-23 07:04:58 | Moragaswewa (Deduru Oya) | 1.41 | 🟢 Normal | -0.140 |  |
| 2026-11-23 07:06:11 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.145 |  |
| 2026-11-23 07:03:20 | Moraketiya (Walawe Ganga) | 2.05 | 🟢 Normal | -0.156 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)