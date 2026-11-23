# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--23_12:14:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **323,563 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 12:14:01 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-23 12:13:58 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-23 12:13:55 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-23 12:08:35 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.039 |  |
| 2026-11-23 12:07:42 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-23 12:06:53 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-23 12:06:42 | Peradeniya (Mahaweli Ganga) | 2.45 | 🟢 Normal | -0.048 |  |
| 2026-11-23 12:06:19 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.095 |  |
| 2026-11-23 12:06:18 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-23 12:05:56 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.028 |  |
| 2026-11-23 12:05:32 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-23 12:04:32 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.000 |  |
| 2026-11-23 12:04:29 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-23 12:04:22 | Hanwella (Kelani Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 12:04:09 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-23 12:04:00 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-23 12:03:53 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-23 12:03:30 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-23 12:03:17 | Moraketiya (Walawe Ganga) | 1.65 | 🟢 Normal | -0.051 |  |
| 2026-11-23 12:03:06 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 12:03:03 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | -0.031 |  |
| 2026-11-23 12:02:53 | Ellagawa (Kalu Ganga) | 5.38 | 🟢 Normal | -0.041 |  |
| 2026-11-23 12:02:37 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.021 |  |
| 2026-11-23 12:02:34 | Glencourse (Kelani Ganga) | 9.44 | 🟢 Normal | -0.031 |  |
| 2026-11-23 12:02:31 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-11-23 12:02:21 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-11-23 12:02:17 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-11-23 12:02:15 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.111 |  |
| 2026-11-23 12:02:12 | Manampitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-11-23 12:01:59 | Panadugama (Nilwala Ganga) | 3.84 | 🟢 Normal | -0.050 |  |
| 2026-11-23 12:01:35 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-11-23 12:01:33 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.000 |  |
| 2026-11-23 12:01:33 | Moragaswewa (Deduru Oya) | 1.20 | 🟢 Normal | -0.044 |  |
| 2026-11-23 12:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-11-23 12:01:28 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 12:01:27 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-11-23 12:01:01 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 12:01:27 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-11-23 12:04:09 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-23 12:03:30 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-23 12:01:01 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-23 12:03:06 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 12:04:22 | Hanwella (Kelani Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 12:01:33 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.000 |  |
| 2026-11-23 12:14:01 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-23 12:01:28 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 12:02:31 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-11-23 11:02:00 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-23 12:03:53 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-23 11:02:39 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 12:06:53 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-23 12:04:32 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.000 |  |
| 2026-11-23 12:06:18 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-23 12:05:32 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-23 12:04:00 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-23 12:07:42 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-23 11:05:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.54 | 🟢 Normal | 0.000 |  |
| 2026-11-23 12:01:35 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-11-23 12:02:17 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-11-23 12:02:12 | Manampitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-11-23 12:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-11-23 11:00:17 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-11-23 12:02:21 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-11-23 12:02:37 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-23 12:05:56 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.028 |  |
| 2026-11-23 12:02:34 | Glencourse (Kelani Ganga) | 9.44 | 🟢 Normal | -0.031 |  |
| 2026-11-23 12:03:03 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | -0.031 |  |
| 2026-11-23 12:08:35 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.039 |  |
| 2026-11-23 12:02:53 | Ellagawa (Kalu Ganga) | 5.38 | 🟢 Normal | -0.041 |  |
| 2026-11-23 12:01:33 | Moragaswewa (Deduru Oya) | 1.20 | 🟢 Normal | -0.044 |  |
| 2026-11-23 12:06:42 | Peradeniya (Mahaweli Ganga) | 2.45 | 🟢 Normal | -0.048 |  |
| 2026-11-23 12:01:59 | Panadugama (Nilwala Ganga) | 3.84 | 🟢 Normal | -0.050 |  |
| 2026-11-23 12:03:17 | Moraketiya (Walawe Ganga) | 1.65 | 🟢 Normal | -0.051 |  |
| 2026-11-23 12:06:19 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.095 |  |
| 2026-11-23 12:02:15 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)