# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_13:31:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **238,621 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-20 13:31:55 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-20 13:18:12 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.019 |  |
| 2026-08-20 13:12:39 | Glencourse (Kelani Ganga) | 9.98 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-08-20 13:11:54 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -0.009 |  |
| 2026-08-20 13:10:46 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | -0.044 |  |
| 2026-08-20 13:10:08 | Magura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.106 |  |
| 2026-08-20 13:07:35 | Dunamale (Aththanagalu Oya) | 0.53 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-20 13:07:22 | Rathnapura (Kalu Ganga) | 3.08 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-08-20 13:06:59 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-20 13:06:32 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.185 |  |
| 2026-08-20 13:05:38 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-08-20 13:05:18 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-08-20 13:05:04 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-20 13:04:45 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-20 13:04:45 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-08-20 13:04:31 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-20 13:04:31 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-20 13:04:20 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-20 13:04:12 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.079 |  |
| 2026-08-20 13:04:01 | Thanthirimale (Malwathu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-20 13:03:33 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-20 13:03:24 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.019 |  |
| 2026-08-20 13:03:20 | Ellagawa (Kalu Ganga) | 5.73 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-08-20 13:03:14 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-20 13:03:02 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 13:02:57 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-08-20 13:02:50 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-20 13:02:28 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-20 13:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.25 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-20 13:02:14 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-20 13:01:56 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 13:01:54 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-08-20 13:01:51 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-20 13:01:42 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-20 13:01:39 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | -0.032 |  |
| 2026-08-20 13:01:35 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 13:01:10 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.010 |  |
| 2026-08-20 13:00:29 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-20 13:00:26 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-20 13:12:39 | Glencourse (Kelani Ganga) | 9.98 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-08-20 13:07:22 | Rathnapura (Kalu Ganga) | 3.08 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-08-20 13:03:20 | Ellagawa (Kalu Ganga) | 5.73 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-08-20 13:02:28 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-20 13:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.25 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-20 13:00:29 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-20 13:31:55 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-20 13:05:04 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-20 13:04:20 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-20 13:03:02 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 13:01:56 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 13:07:35 | Dunamale (Aththanagalu Oya) | 0.53 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-20 13:04:31 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-20 13:02:14 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-20 13:03:33 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-20 13:01:35 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 13:03:14 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-20 13:02:50 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-20 13:01:51 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-20 13:04:31 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-20 13:05:18 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-08-20 13:05:38 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-08-20 13:06:59 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-20 13:04:01 | Thanthirimale (Malwathu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-20 13:04:45 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-20 13:01:42 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-20 13:11:54 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -0.009 |  |
| 2026-08-20 13:04:45 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-08-20 13:02:57 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-08-20 13:01:54 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-08-20 13:01:10 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.010 |  |
| 2026-08-20 13:18:12 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.019 |  |
| 2026-08-20 13:03:24 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.019 |  |
| 2026-08-20 13:00:26 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | -0.021 |  |
| 2026-08-20 13:01:39 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | -0.032 |  |
| 2026-08-20 13:10:46 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | -0.044 |  |
| 2026-08-20 13:04:12 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.079 |  |
| 2026-08-20 13:10:08 | Magura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.106 |  |
| 2026-08-20 13:06:32 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.185 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)