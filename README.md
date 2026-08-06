# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--06_14:14:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **226,543 measurements** from **39** stations.
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
| 2026-08-06 14:14:20 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:11:51 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.009 |  |
| 2026-08-06 14:11:11 | Horowpothana (Yan Oya) | 1.59 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-06 14:09:32 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:08:28 | Peradeniya (Mahaweli Ganga) | 4.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-06 14:08:18 | Rathnapura (Kalu Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:07:55 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 14:06:46 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:05:44 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.040 |  |
| 2026-08-06 14:05:24 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:05:10 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:05:08 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 14:04:34 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:04:13 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:04:10 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:04:10 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | -0.048 |  |
| 2026-08-06 14:04:06 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-08-06 14:03:47 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-08-06 14:03:29 | Kithulgala (Kelani Ganga) | 2.98 | 🟢 Normal | -0.070 |  |
| 2026-08-06 14:03:20 | Glencourse (Kelani Ganga) | 11.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-06 14:03:09 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.030 |  |
| 2026-08-06 14:03:06 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.016 |  |
| 2026-08-06 14:02:54 | Hanwella (Kelani Ganga) | 2.95 | 🟢 Normal | -0.031 |  |
| 2026-08-06 14:02:40 | Ellagawa (Kalu Ganga) | 6.84 | 🟢 Normal | -0.159 |  |
| 2026-08-06 14:02:37 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:02:35 | Deraniyagala (Kelani Ganga) | 1.77 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-08-06 14:02:33 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.28 | 🟢 Normal | -0.042 |  |
| 2026-08-06 14:02:01 | Nawalapitiya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-08-06 14:01:39 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-06 14:01:10 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:01:08 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:01:06 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-06 14:01:06 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:01:05 | Thanthirimale (Malwathu Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:01:03 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:00:44 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:00:06 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-06 14:02:35 | Deraniyagala (Kelani Ganga) | 1.77 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-08-06 14:02:01 | Nawalapitiya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-08-06 14:01:06 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-06 14:03:20 | Glencourse (Kelani Ganga) | 11.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-06 14:08:28 | Peradeniya (Mahaweli Ganga) | 4.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-06 14:01:39 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-06 14:07:55 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 14:05:08 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 14:11:11 | Horowpothana (Yan Oya) | 1.59 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-06 14:01:03 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:00:06 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-06 13:03:42 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:02:37 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:02:33 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:06:46 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:05:10 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:14:20 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:09:32 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:04:13 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:00:44 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:04:10 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:05:24 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:08:18 | Rathnapura (Kalu Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:01:05 | Thanthirimale (Malwathu Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:04:34 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:01:10 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:01:06 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:01:08 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-06 14:11:51 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.009 |  |
| 2026-08-06 14:03:47 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-08-06 14:04:06 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-08-06 14:03:06 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.016 |  |
| 2026-08-06 14:03:09 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.030 |  |
| 2026-08-06 14:02:54 | Hanwella (Kelani Ganga) | 2.95 | 🟢 Normal | -0.031 |  |
| 2026-08-06 14:05:44 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.040 |  |
| 2026-08-06 14:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.28 | 🟢 Normal | -0.042 |  |
| 2026-08-06 14:04:10 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | -0.048 |  |
| 2026-08-06 14:03:29 | Kithulgala (Kelani Ganga) | 2.98 | 🟢 Normal | -0.070 |  |
| 2026-08-06 14:02:40 | Ellagawa (Kalu Ganga) | 6.84 | 🟢 Normal | -0.159 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)