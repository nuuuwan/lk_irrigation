# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--29_11:18:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **301,124 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Putupaula — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 11:18:21 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-29 11:17:22 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | -0.008 |  |
| 2026-10-29 11:13:50 | Pitabeddara (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.041 |  |
| 2026-10-29 11:10:46 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:09:20 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-10-29 11:08:21 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.009 |  |
| 2026-10-29 11:07:35 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.009 |  |
| 2026-10-29 11:07:22 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.019 |  |
| 2026-10-29 11:07:15 | Panadugama (Nilwala Ganga) | 5.82 | 🟡 Alert | -0.031 |  |
| 2026-10-29 11:05:52 | Badalgama (Maha Oya) | 3.16 | 🟢 Normal | -0.010 |  |
| 2026-10-29 11:05:42 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 11:05:37 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-10-29 11:05:28 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:04:51 | Moragaswewa (Deduru Oya) | 1.29 | 🟢 Normal | -0.029 |  |
| 2026-10-29 11:04:42 | Baddegama (Gin Ganga) | 4.11 | 🟠 Minor Flood | -0.019 |  |
| 2026-10-29 11:04:06 | Glencourse (Kelani Ganga) | 11.06 | 🟢 Normal | -0.060 |  |
| 2026-10-29 11:03:50 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:03:50 | Hanwella (Kelani Ganga) | 3.72 | 🟢 Normal | -0.051 |  |
| 2026-10-29 11:03:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.37 | 🟠 Minor Flood | -0.011 |  |
| 2026-10-29 11:03:17 | Rathnapura (Kalu Ganga) | 4.73 | 🟢 Normal | -0.105 |  |
| 2026-10-29 11:03:00 | Giriulla (Maha Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-10-29 11:02:47 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:02:47 | Ellagawa (Kalu Ganga) | 9.98 | 🟢 Normal | -0.039 |  |
| 2026-10-29 11:02:41 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:02:16 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.040 |  |
| 2026-10-29 11:02:11 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:02:09 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | -0.049 |  |
| 2026-10-29 11:02:04 | Thawalama (Gin Ganga) | 2.43 | 🟢 Normal | -0.044 |  |
| 2026-10-29 11:01:49 | Putupaula (Kalu Ganga) | 3.71 | 🟡 Alert | -0.010 |  |
| 2026-10-29 11:01:48 | Galgamuwa (Mee Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:01:27 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:01:23 | Peradeniya (Mahaweli Ganga) | 2.97 | 🟢 Normal | -0.011 |  |
| 2026-10-29 11:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:01:03 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | -0.022 |  |
| 2026-10-29 11:00:55 | Magura (Kalu Ganga) | 3.47 | 🟢 Normal | -0.032 |  |
| 2026-10-29 11:00:30 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:00:21 | Weraganthota (Mahaweli Ganga) | -2.17 | 🟢 Normal | -0.032 |  |
| 2026-10-29 11:00:11 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:00:10 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 11:05:42 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 11:03:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.37 | 🟠 Minor Flood | -0.011 |  |
| 2026-10-29 11:04:42 | Baddegama (Gin Ganga) | 4.11 | 🟠 Minor Flood | -0.019 |  |
| 2026-10-29 11:01:49 | Putupaula (Kalu Ganga) | 3.71 | 🟡 Alert | -0.010 |  |
| 2026-10-29 11:07:15 | Panadugama (Nilwala Ganga) | 5.82 | 🟡 Alert | -0.031 |  |
| 2026-10-29 11:18:21 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-29 11:00:30 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:03:50 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:01:48 | Galgamuwa (Mee Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:05:28 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:02:47 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:00:11 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:02:41 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:10:46 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:01:27 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:02:11 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:00:10 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-29 11:17:22 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | -0.008 |  |
| 2026-10-29 11:09:20 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-10-29 11:07:35 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.009 |  |
| 2026-10-29 11:08:21 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.009 |  |
| 2026-10-29 11:03:00 | Giriulla (Maha Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-10-29 11:05:52 | Badalgama (Maha Oya) | 3.16 | 🟢 Normal | -0.010 |  |
| 2026-10-29 11:01:23 | Peradeniya (Mahaweli Ganga) | 2.97 | 🟢 Normal | -0.011 |  |
| 2026-10-29 11:07:22 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.019 |  |
| 2026-10-29 11:05:37 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-10-29 11:01:03 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | -0.022 |  |
| 2026-10-29 11:04:51 | Moragaswewa (Deduru Oya) | 1.29 | 🟢 Normal | -0.029 |  |
| 2026-10-29 11:00:55 | Magura (Kalu Ganga) | 3.47 | 🟢 Normal | -0.032 |  |
| 2026-10-29 11:00:21 | Weraganthota (Mahaweli Ganga) | -2.17 | 🟢 Normal | -0.032 |  |
| 2026-10-29 11:02:47 | Ellagawa (Kalu Ganga) | 9.98 | 🟢 Normal | -0.039 |  |
| 2026-10-29 11:02:16 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.040 |  |
| 2026-10-29 11:13:50 | Pitabeddara (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.041 |  |
| 2026-10-29 11:02:04 | Thawalama (Gin Ganga) | 2.43 | 🟢 Normal | -0.044 |  |
| 2026-10-29 11:02:09 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | -0.049 |  |
| 2026-10-29 11:03:50 | Hanwella (Kelani Ganga) | 3.72 | 🟢 Normal | -0.051 |  |
| 2026-10-29 11:04:06 | Glencourse (Kelani Ganga) | 11.06 | 🟢 Normal | -0.060 |  |
| 2026-10-29 11:03:17 | Rathnapura (Kalu Ganga) | 4.73 | 🟢 Normal | -0.105 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)