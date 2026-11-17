# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--17_17:15:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **318,457 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-17 17:15:11 | Panadugama (Nilwala Ganga) | 3.71 | 🟢 Normal | -0.011 |  |
| 2026-11-17 17:13:38 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-11-17 17:11:46 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.084 |  |
| 2026-11-17 17:11:05 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 17:10:42 | Hanwella (Kelani Ganga) | 1.94 | 🟢 Normal | -0.018 |  |
| 2026-11-17 17:10:27 | Urawa (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-11-17 17:07:42 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.011 |  |
| 2026-11-17 17:07:32 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-17 17:07:30 | Manampitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-17 17:06:34 | Weraganthota (Mahaweli Ganga) | -2.13 | 🟢 Normal | -0.051 |  |
| 2026-11-17 17:06:16 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-17 17:06:14 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-17 17:05:42 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-17 17:05:24 | Kithulgala (Kelani Ganga) | 2.14 | 🟢 Normal | -0.005 |  |
| 2026-11-17 17:04:51 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-17 17:04:20 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-17 17:04:16 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-17 17:04:05 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-11-17 17:04:00 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-17 17:03:26 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | -0.010 |  |
| 2026-11-17 17:03:20 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-17 17:03:06 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-11-17 17:03:06 | Dunamale (Aththanagalu Oya) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-11-17 17:02:56 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-11-17 17:02:34 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-17 17:02:13 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 17:02:13 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.075 |  |
| 2026-11-17 17:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-11-17 17:02:09 | Pitabeddara (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-17 17:02:07 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 17:01:57 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-11-17 17:01:41 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.038 |  |
| 2026-11-17 17:01:30 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-17 17:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-17 17:01:13 | Ellagawa (Kalu Ganga) | 5.05 | 🟢 Normal | -0.021 |  |
| 2026-11-17 17:00:08 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-17 17:04:20 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-17 17:04:16 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-17 17:02:34 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-17 17:02:13 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 17:02:07 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 15:06:15 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 17:07:30 | Manampitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-17 17:06:14 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-17 17:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-17 17:11:05 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 17:07:32 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-17 17:02:09 | Pitabeddara (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-17 17:06:16 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:58:45 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-17 17:13:38 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-11-17 17:05:42 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-17 17:00:08 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 17:04:51 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-17 17:04:00 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-17 17:03:20 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-17 17:01:30 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-17 17:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-11-17 17:05:24 | Kithulgala (Kelani Ganga) | 2.14 | 🟢 Normal | -0.005 |  |
| 2026-11-17 17:04:05 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-11-17 17:10:27 | Urawa (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-11-17 17:03:26 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | -0.010 |  |
| 2026-11-17 17:03:06 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-11-17 16:03:20 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-11-17 17:03:06 | Dunamale (Aththanagalu Oya) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-11-17 17:01:57 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-11-17 17:15:11 | Panadugama (Nilwala Ganga) | 3.71 | 🟢 Normal | -0.011 |  |
| 2026-11-17 17:07:42 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.011 |  |
| 2026-11-17 17:10:42 | Hanwella (Kelani Ganga) | 1.94 | 🟢 Normal | -0.018 |  |
| 2026-11-17 17:01:13 | Ellagawa (Kalu Ganga) | 5.05 | 🟢 Normal | -0.021 |  |
| 2026-11-17 17:02:56 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-11-17 17:01:41 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.038 |  |
| 2026-11-17 17:06:34 | Weraganthota (Mahaweli Ganga) | -2.13 | 🟢 Normal | -0.051 |  |
| 2026-11-17 17:02:13 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.075 |  |
| 2026-11-17 17:11:46 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.084 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)