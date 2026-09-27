# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--27_09:11:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **272,246 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 09:11:13 | Baddegama (Gin Ganga) | 4.71 | 🟠 Minor Flood | -0.021 |  |
| 2026-09-27 09:09:37 | Kithulgala (Kelani Ganga) | 2.33 | 🟢 Normal | -0.111 |  |
| 2026-09-27 09:07:37 | Thawalama (Gin Ganga) | 2.60 | 🟢 Normal | -0.085 |  |
| 2026-09-27 09:07:07 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.059 |  |
| 2026-09-27 09:06:40 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.011 |  |
| 2026-09-27 09:06:18 | Glencourse (Kelani Ganga) | 12.10 | 🟢 Normal | -0.049 |  |
| 2026-09-27 09:06:01 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-09-27 09:05:45 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-09-27 09:05:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.54 | 🟠 Minor Flood | -0.011 |  |
| 2026-09-27 09:05:38 | Magura (Kalu Ganga) | 2.91 | 🟢 Normal | -0.044 |  |
| 2026-09-27 09:05:04 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 09:05:00 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 09:04:37 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-27 09:04:36 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-27 09:04:31 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-27 09:04:21 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | -0.020 |  |
| 2026-09-27 09:04:08 | Hanwella (Kelani Ganga) | 4.47 | 🟢 Normal | -0.050 |  |
| 2026-09-27 09:03:57 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-09-27 09:03:55 | Putupaula (Kalu Ganga) | 2.82 | 🟢 Normal | -0.020 |  |
| 2026-09-27 09:03:36 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | -0.020 |  |
| 2026-09-27 09:03:34 | Ellagawa (Kalu Ganga) | 8.53 | 🟢 Normal | -0.032 |  |
| 2026-09-27 09:03:31 | Panadugama (Nilwala Ganga) | 5.40 | 🟡 Alert | -0.043 |  |
| 2026-09-27 09:03:07 | Rathnapura (Kalu Ganga) | 3.70 | 🟢 Normal | -0.090 |  |
| 2026-09-27 09:03:06 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-27 09:02:42 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-27 09:02:41 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 09:02:36 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.051 |  |
| 2026-09-27 09:02:32 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-09-27 09:02:20 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-27 09:02:18 | Peradeniya (Mahaweli Ganga) | 2.99 | 🟢 Normal | -0.011 |  |
| 2026-09-27 09:02:12 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-27 09:02:07 | Deraniyagala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.041 |  |
| 2026-09-27 09:01:42 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-27 09:01:37 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.050 |  |
| 2026-09-27 09:01:33 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.068 |  |
| 2026-09-27 09:01:22 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 09:01:09 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 09:01:01 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 09:00:26 | Nawalapitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 09:02:42 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-27 09:05:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.54 | 🟠 Minor Flood | -0.011 |  |
| 2026-09-27 09:11:13 | Baddegama (Gin Ganga) | 4.71 | 🟠 Minor Flood | -0.021 |  |
| 2026-09-27 09:03:31 | Panadugama (Nilwala Ganga) | 5.40 | 🟡 Alert | -0.043 |  |
| 2026-09-27 09:04:31 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-27 09:01:09 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 09:02:41 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 09:01:01 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 09:05:00 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 09:04:36 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-27 09:05:04 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 09:04:37 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-27 09:03:06 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-27 09:02:12 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-27 09:01:22 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 09:01:42 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-27 09:02:20 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-27 09:06:01 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-09-27 09:03:57 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-09-27 09:02:32 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-09-27 09:00:26 | Nawalapitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-09-27 09:02:18 | Peradeniya (Mahaweli Ganga) | 2.99 | 🟢 Normal | -0.011 |  |
| 2026-09-27 09:06:40 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.011 |  |
| 2026-09-27 09:05:45 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-09-27 09:04:21 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | -0.020 |  |
| 2026-09-27 09:03:36 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | -0.020 |  |
| 2026-09-27 09:03:55 | Putupaula (Kalu Ganga) | 2.82 | 🟢 Normal | -0.020 |  |
| 2026-09-27 09:03:34 | Ellagawa (Kalu Ganga) | 8.53 | 🟢 Normal | -0.032 |  |
| 2026-09-27 09:02:07 | Deraniyagala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.041 |  |
| 2026-09-27 09:05:38 | Magura (Kalu Ganga) | 2.91 | 🟢 Normal | -0.044 |  |
| 2026-09-27 09:06:18 | Glencourse (Kelani Ganga) | 12.10 | 🟢 Normal | -0.049 |  |
| 2026-09-27 09:01:37 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.050 |  |
| 2026-09-27 09:04:08 | Hanwella (Kelani Ganga) | 4.47 | 🟢 Normal | -0.050 |  |
| 2026-09-27 09:02:36 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.051 |  |
| 2026-09-27 09:07:07 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.059 |  |
| 2026-09-27 09:01:33 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.068 |  |
| 2026-09-27 09:07:37 | Thawalama (Gin Ganga) | 2.60 | 🟢 Normal | -0.085 |  |
| 2026-09-27 09:03:07 | Rathnapura (Kalu Ganga) | 3.70 | 🟢 Normal | -0.090 |  |
| 2026-09-27 09:09:37 | Kithulgala (Kelani Ganga) | 2.33 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)