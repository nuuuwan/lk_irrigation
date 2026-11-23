# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--23_22:19:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **323,940 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 22:19:03 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | 0.000 |  |
| 2026-11-23 22:17:21 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.301 | 🔺 Rising |
| 2026-11-23 22:12:14 | Pitabeddara (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-11-23 22:11:35 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-23 22:09:10 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-23 22:08:55 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.019 |  |
| 2026-11-23 22:08:22 | Glencourse (Kelani Ganga) | 9.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 22:07:20 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-11-23 22:07:08 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | 0.894 | 🔺 Rising |
| 2026-11-23 22:06:21 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-11-23 22:06:01 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-11-23 22:05:57 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | -0.040 |  |
| 2026-11-23 22:05:39 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.133 |  |
| 2026-11-23 22:04:57 | Deraniyagala (Kelani Ganga) | 1.64 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-11-23 22:04:37 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-23 22:04:26 | Peradeniya (Mahaweli Ganga) | 3.14 | 🟢 Normal | -0.020 |  |
| 2026-11-23 22:04:05 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-23 22:03:52 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | -0.031 |  |
| 2026-11-23 22:03:34 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-11-23 22:02:55 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-23 22:02:46 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-23 22:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.08 | 🟢 Normal | -0.061 |  |
| 2026-11-23 22:02:30 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-11-23 22:01:53 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-11-23 22:01:45 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-11-23 22:01:37 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-11-23 22:01:14 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-23 22:01:11 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-23 22:01:10 | Panadugama (Nilwala Ganga) | 3.53 | 🟢 Normal | -0.021 |  |
| 2026-11-23 22:01:10 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-11-23 22:00:54 | Moraketiya (Walawe Ganga) | 2.10 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-11-23 22:00:39 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-23 22:00:33 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 22:07:08 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | 0.894 | 🔺 Rising |
| 2026-11-23 22:17:21 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.301 | 🔺 Rising |
| 2026-11-23 22:00:54 | Moraketiya (Walawe Ganga) | 2.10 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-11-23 22:01:45 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-11-23 22:04:57 | Deraniyagala (Kelani Ganga) | 1.64 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-11-23 21:03:23 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-23 22:01:53 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-11-23 22:07:20 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-11-23 22:11:35 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-23 22:09:10 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-23 22:04:37 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-23 22:00:33 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-23 22:12:14 | Pitabeddara (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-11-23 22:08:22 | Glencourse (Kelani Ganga) | 9.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 22:01:11 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:01:29 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 22:01:37 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:05:14 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-11-23 22:04:05 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-23 22:19:03 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | 0.000 |  |
| 2026-11-23 22:02:46 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-23 22:02:55 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-23 22:06:21 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-11-23 22:00:39 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-23 22:01:14 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-23 22:06:01 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-11-23 22:03:34 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-11-23 22:02:30 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-11-23 22:08:55 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.019 |  |
| 2026-11-23 22:04:26 | Peradeniya (Mahaweli Ganga) | 3.14 | 🟢 Normal | -0.020 |  |
| 2026-11-23 18:02:13 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-11-23 22:01:10 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-11-23 22:01:10 | Panadugama (Nilwala Ganga) | 3.53 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-23 22:03:52 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | -0.031 |  |
| 2026-11-23 22:05:57 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | -0.040 |  |
| 2026-11-23 18:00:35 | Weraganthota (Mahaweli Ganga) | -2.49 | 🟢 Normal | -0.050 |  |
| 2026-11-23 22:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.08 | 🟢 Normal | -0.061 |  |
| 2026-11-23 22:05:39 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.133 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)