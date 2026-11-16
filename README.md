# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--16_13:21:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **317,418 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-16 13:21:52 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:16:18 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | -0.024 |  |
| 2026-11-16 13:12:37 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.008 |  |
| 2026-11-16 13:09:50 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | -0.009 |  |
| 2026-11-16 13:09:48 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | -0.019 |  |
| 2026-11-16 13:08:04 | Glencourse (Kelani Ganga) | 10.36 | 🟢 Normal | -0.029 |  |
| 2026-11-16 13:07:29 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.010 |  |
| 2026-11-16 13:06:40 | Panadugama (Nilwala Ganga) | 4.41 | 🟢 Normal | -0.020 |  |
| 2026-11-16 13:06:37 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:06:32 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:06:15 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-11-16 13:05:57 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:05:50 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:05:20 | Moraketiya (Walawe Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:04:56 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-16 13:04:10 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.040 |  |
| 2026-11-16 13:03:40 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:03:15 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:03:11 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:03:11 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-11-16 13:03:07 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-11-16 13:03:04 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-11-16 13:02:47 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.91 | 🟢 Normal | -0.020 |  |
| 2026-11-16 13:02:35 | Hanwella (Kelani Ganga) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-11-16 13:02:23 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:02:22 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:02:17 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-11-16 13:02:11 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:02:10 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:02:08 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:02:02 | Ellagawa (Kalu Ganga) | 5.32 | 🟢 Normal | -0.010 |  |
| 2026-11-16 13:01:54 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 13:01:52 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | -0.081 |  |
| 2026-11-16 13:01:48 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-11-16 13:01:45 | Dunamale (Aththanagalu Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:01:03 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-11-16 13:00:35 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-11-16 13:00:27 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-16 13:16:18 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | -0.024 |  |
| 2026-11-16 13:04:56 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-16 13:01:54 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 13:06:37 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:03:40 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:02:47 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:02:11 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:03:11 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:02:10 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:05:50 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:03:15 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:05:20 | Moraketiya (Walawe Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:02:08 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:01:45 | Dunamale (Aththanagalu Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:05:57 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:21:52 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:02:23 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:06:32 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:02:22 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-11-16 13:12:37 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.008 |  |
| 2026-11-16 13:09:50 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | -0.009 |  |
| 2026-11-16 13:07:29 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.010 |  |
| 2026-11-16 13:03:04 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-11-16 13:06:15 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-11-16 13:02:35 | Hanwella (Kelani Ganga) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-11-16 13:00:27 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-11-16 13:02:02 | Ellagawa (Kalu Ganga) | 5.32 | 🟢 Normal | -0.010 |  |
| 2026-11-16 13:00:35 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-11-16 13:09:48 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | -0.019 |  |
| 2026-11-16 13:06:40 | Panadugama (Nilwala Ganga) | 4.41 | 🟢 Normal | -0.020 |  |
| 2026-11-16 13:03:11 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-11-16 13:03:07 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-11-16 13:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.91 | 🟢 Normal | -0.020 |  |
| 2026-11-16 13:01:48 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-11-16 13:02:17 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-11-16 13:08:04 | Glencourse (Kelani Ganga) | 10.36 | 🟢 Normal | -0.029 |  |
| 2026-11-16 13:01:03 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-11-16 13:04:10 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.040 |  |
| 2026-11-16 13:01:52 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)