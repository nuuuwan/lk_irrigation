# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--27_11:17:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **299,314 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Dunamale — Minor Flood; 🟠 Panadugama — Minor Flood; 🟠 Rathnapura — Minor Flood; 🟡 Baddegama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 11:17:46 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |
| 2026-10-27 11:09:20 | Urawa (Nilwala Ganga) | 1.54 | 🟢 Normal | -0.054 |  |
| 2026-10-27 11:06:29 | Badalgama (Maha Oya) | 5.12 | 🟡 Alert | -0.177 |  |
| 2026-10-27 11:06:19 | Norwood (Kelani Ganga) | 1.46 | 🟢 Normal | -0.009 |  |
| 2026-10-27 11:05:48 | Peradeniya (Mahaweli Ganga) | 3.53 | 🟢 Normal | -0.040 |  |
| 2026-10-27 11:05:36 | Holombuwa (Kelani Ganga) | 1.57 | 🟢 Normal | -0.111 |  |
| 2026-10-27 11:05:20 | Dunamale (Aththanagalu Oya) | 4.83 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-27 11:05:01 | Baddegama (Gin Ganga) | 3.99 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-10-27 11:04:46 | Thawalama (Gin Ganga) | 3.97 | 🟢 Normal | -0.245 |  |
| 2026-10-27 11:04:02 | Thanthirimale (Malwathu Oya) | 3.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-27 11:03:55 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-27 11:03:52 | Moragaswewa (Deduru Oya) | 5.22 | 🟡 Alert | -0.029 |  |
| 2026-10-27 11:03:31 | Moraketiya (Walawe Ganga) | 1.71 | 🟢 Normal | -0.089 |  |
| 2026-10-27 11:03:21 | Galgamuwa (Mee Oya) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-10-27 11:03:14 | Putupaula (Kalu Ganga) | 3.28 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-27 11:02:51 | Nawalapitiya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.030 |  |
| 2026-10-27 11:02:46 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-27 11:02:42 | Glencourse (Kelani Ganga) | 13.21 | 🟢 Normal | -0.194 |  |
| 2026-10-27 11:02:37 | Rathnapura (Kalu Ganga) | 8.42 | 🟠 Minor Flood | -0.071 |  |
| 2026-10-27 11:02:30 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-10-27 11:02:26 | Nagalagam Street (Kelani Ganga) | 1.04 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-27 11:02:21 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | 0.363 | 🔺 Rising |
| 2026-10-27 11:02:19 | Hanwella (Kelani Ganga) | 6.25 | 🟢 Normal | -0.111 |  |
| 2026-10-27 11:02:15 | Kithulgala (Kelani Ganga) | 2.34 | 🟢 Normal | -0.191 |  |
| 2026-10-27 11:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.45 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2026-10-27 11:02:11 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-10-27 11:02:07 | Panadugama (Nilwala Ganga) | 6.37 | 🟠 Minor Flood | -0.035 |  |
| 2026-10-27 11:02:05 | Manampitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.032 |  |
| 2026-10-27 11:01:56 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-10-27 11:01:47 | Ellagawa (Kalu Ganga) | 9.95 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-27 11:01:36 | Pitabeddara (Nilwala Ganga) | 2.75 | 🟢 Normal | -0.142 |  |
| 2026-10-27 11:01:32 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-27 11:01:29 | Magura (Kalu Ganga) | 5.23 | 🟡 Alert | -0.040 |  |
| 2026-10-27 11:01:26 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-27 11:01:02 | Giriulla (Maha Oya) | 3.70 | 🟢 Normal | -0.115 |  |
| 2026-10-27 11:00:46 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-27 11:00:35 | Horowpothana (Yan Oya) | 3.15 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-10-27 11:00:11 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-10-27 11:00:09 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 11:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.45 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2026-10-27 11:05:20 | Dunamale (Aththanagalu Oya) | 4.83 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-27 11:02:07 | Panadugama (Nilwala Ganga) | 6.37 | 🟠 Minor Flood | -0.035 |  |
| 2026-10-27 11:02:37 | Rathnapura (Kalu Ganga) | 8.42 | 🟠 Minor Flood | -0.071 |  |
| 2026-10-27 11:05:01 | Baddegama (Gin Ganga) | 3.99 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-10-27 11:03:14 | Putupaula (Kalu Ganga) | 3.28 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-27 11:17:46 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |
| 2026-10-27 11:03:52 | Moragaswewa (Deduru Oya) | 5.22 | 🟡 Alert | -0.029 |  |
| 2026-10-27 11:01:29 | Magura (Kalu Ganga) | 5.23 | 🟡 Alert | -0.040 |  |
| 2026-10-27 11:06:29 | Badalgama (Maha Oya) | 5.12 | 🟡 Alert | -0.177 |  |
| 2026-10-27 11:02:21 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | 0.363 | 🔺 Rising |
| 2026-10-27 11:00:35 | Horowpothana (Yan Oya) | 3.15 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-10-27 11:01:47 | Ellagawa (Kalu Ganga) | 9.95 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-27 11:02:26 | Nagalagam Street (Kelani Ganga) | 1.04 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-27 11:04:02 | Thanthirimale (Malwathu Oya) | 3.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-27 11:01:26 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-27 11:03:21 | Galgamuwa (Mee Oya) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-10-27 10:00:31 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 11:01:32 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-27 11:02:11 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-10-27 11:03:55 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-27 11:02:46 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-27 11:06:19 | Norwood (Kelani Ganga) | 1.46 | 🟢 Normal | -0.009 |  |
| 2026-10-27 11:00:09 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-10-27 11:00:11 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-10-27 11:01:56 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-10-27 11:02:30 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-10-27 11:02:51 | Nawalapitiya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.030 |  |
| 2026-10-27 11:02:05 | Manampitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.032 |  |
| 2026-10-27 11:05:48 | Peradeniya (Mahaweli Ganga) | 3.53 | 🟢 Normal | -0.040 |  |
| 2026-10-27 11:09:20 | Urawa (Nilwala Ganga) | 1.54 | 🟢 Normal | -0.054 |  |
| 2026-10-27 11:03:31 | Moraketiya (Walawe Ganga) | 1.71 | 🟢 Normal | -0.089 |  |
| 2026-10-27 11:05:36 | Holombuwa (Kelani Ganga) | 1.57 | 🟢 Normal | -0.111 |  |
| 2026-10-27 11:02:19 | Hanwella (Kelani Ganga) | 6.25 | 🟢 Normal | -0.111 |  |
| 2026-10-27 11:01:02 | Giriulla (Maha Oya) | 3.70 | 🟢 Normal | -0.115 |  |
| 2026-10-27 11:01:36 | Pitabeddara (Nilwala Ganga) | 2.75 | 🟢 Normal | -0.142 |  |
| 2026-10-27 11:02:15 | Kithulgala (Kelani Ganga) | 2.34 | 🟢 Normal | -0.191 |  |
| 2026-10-27 11:02:42 | Glencourse (Kelani Ganga) | 13.21 | 🟢 Normal | -0.194 |  |
| 2026-10-27 11:04:46 | Thawalama (Gin Ganga) | 3.97 | 🟢 Normal | -0.245 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)