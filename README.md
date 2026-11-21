# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--21_08:32:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **321,659 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 08:32:16 | Urawa (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.120 |  |
| 2026-11-21 08:09:47 | Dunamale (Aththanagalu Oya) | 1.69 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-21 08:09:14 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-21 08:06:52 | Giriulla (Maha Oya) | 2.80 | 🟢 Normal | 1.379 | 🔺 Rising |
| 2026-11-21 08:06:38 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | 13.341 | 🔺 Rising |
| 2026-11-21 08:05:52 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-11-21 08:05:41 | Thawalama (Gin Ganga) | 2.60 | 🟢 Normal | -0.048 |  |
| 2026-11-21 08:05:37 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-11-21 08:05:35 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-21 08:05:33 | Moraketiya (Walawe Ganga) | 2.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 08:05:30 | Horowpothana (Yan Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-11-21 08:05:21 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-21 08:05:17 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-21 08:05:14 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.032 |  |
| 2026-11-21 08:04:43 | Rathnapura (Kalu Ganga) | 3.21 | 🟢 Normal | -0.009 |  |
| 2026-11-21 08:04:38 | Kuda Oya (Kirindi Oya) | 2.16 | 🟢 Normal | -0.019 |  |
| 2026-11-21 08:04:36 | Thalgahagoda (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-21 08:04:22 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.049 |  |
| 2026-11-21 08:04:16 | Glencourse (Kelani Ganga) | 9.94 | 🟢 Normal | -0.030 |  |
| 2026-11-21 08:03:57 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-21 08:03:48 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 13.341 | 🔺 Rising |
| 2026-11-21 08:03:35 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.021 |  |
| 2026-11-21 08:03:33 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-21 08:03:22 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-21 08:03:19 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-11-21 08:02:57 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-21 08:02:54 | Panadugama (Nilwala Ganga) | 5.35 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-11-21 08:02:45 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-21 08:02:31 | Thanamalwila (Kirindi Oya) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-11-21 08:02:28 | Peradeniya (Mahaweli Ganga) | 3.43 | 🟢 Normal | -0.173 |  |
| 2026-11-21 08:02:26 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-21 08:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.69 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-21 08:02:15 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-21 08:01:37 | Weraganthota (Mahaweli Ganga) | -2.08 | 🟢 Normal | -0.059 |  |
| 2026-11-21 08:01:36 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 08:01:27 | Manampitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-11-21 08:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.031 |  |
| 2026-11-21 08:00:18 | Pitabeddara (Nilwala Ganga) | 2.73 | 🟢 Normal | -0.071 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 08:02:54 | Panadugama (Nilwala Ganga) | 5.35 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-11-21 08:06:38 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | 13.341 | 🔺 Rising |
| 2026-11-21 08:06:52 | Giriulla (Maha Oya) | 2.80 | 🟢 Normal | 1.379 | 🔺 Rising |
| 2026-11-21 08:05:52 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-11-21 08:03:19 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-11-21 08:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.69 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-21 08:02:45 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-21 08:09:47 | Dunamale (Aththanagalu Oya) | 1.69 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-21 08:05:17 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-21 08:03:22 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-21 07:08:34 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 08:04:36 | Thalgahagoda (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-21 08:09:14 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-21 08:05:21 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-21 08:05:33 | Moraketiya (Walawe Ganga) | 2.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 08:05:37 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-11-21 08:02:57 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-21 08:02:15 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-21 08:01:36 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 08:05:30 | Horowpothana (Yan Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-11-21 08:03:33 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-21 08:05:35 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-21 08:03:57 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-21 08:02:26 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-21 08:04:43 | Rathnapura (Kalu Ganga) | 3.21 | 🟢 Normal | -0.009 |  |
| 2026-11-21 08:04:38 | Kuda Oya (Kirindi Oya) | 2.16 | 🟢 Normal | -0.019 |  |
| 2026-11-21 08:01:27 | Manampitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-11-21 08:02:31 | Thanamalwila (Kirindi Oya) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-11-21 08:03:35 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.021 |  |
| 2026-11-21 08:04:16 | Glencourse (Kelani Ganga) | 9.94 | 🟢 Normal | -0.030 |  |
| 2026-11-21 08:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.031 |  |
| 2026-11-21 08:05:14 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.032 |  |
| 2026-11-21 08:05:41 | Thawalama (Gin Ganga) | 2.60 | 🟢 Normal | -0.048 |  |
| 2026-11-21 08:04:22 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.049 |  |
| 2026-11-21 08:01:37 | Weraganthota (Mahaweli Ganga) | -2.08 | 🟢 Normal | -0.059 |  |
| 2026-11-21 08:00:18 | Pitabeddara (Nilwala Ganga) | 2.73 | 🟢 Normal | -0.071 |  |
| 2026-11-21 08:32:16 | Urawa (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.120 |  |
| 2026-11-21 08:02:28 | Peradeniya (Mahaweli Ganga) | 3.43 | 🟢 Normal | -0.173 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)