# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--27_13:15:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **272,403 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 13:15:27 | Baddegama (Gin Ganga) | 4.64 | 🟠 Minor Flood | -0.017 |  |
| 2026-09-27 13:13:36 | Magura (Kalu Ganga) | 2.79 | 🟢 Normal | -0.037 |  |
| 2026-09-27 13:12:04 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:10:05 | Panadugama (Nilwala Ganga) | 5.28 | 🟡 Alert | -0.028 |  |
| 2026-09-27 13:09:27 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.009 |  |
| 2026-09-27 13:08:43 | Glencourse (Kelani Ganga) | 11.90 | 🟢 Normal | -0.047 |  |
| 2026-09-27 13:08:32 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:08:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.42 | 🟡 Alert | -0.038 |  |
| 2026-09-27 13:08:02 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:07:33 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:07:30 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-27 13:06:21 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:05:41 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:05:20 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | -0.019 |  |
| 2026-09-27 13:04:54 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.152 |  |
| 2026-09-27 13:04:45 | Putupaula (Kalu Ganga) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-09-27 13:04:08 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.040 |  |
| 2026-09-27 13:04:06 | Rathnapura (Kalu Ganga) | 3.30 | 🟢 Normal | -0.068 |  |
| 2026-09-27 13:03:48 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.121 |  |
| 2026-09-27 13:03:47 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-09-27 13:03:45 | Ellagawa (Kalu Ganga) | 8.35 | 🟢 Normal | -0.058 |  |
| 2026-09-27 13:03:38 | Hanwella (Kelani Ganga) | 4.25 | 🟢 Normal | -0.060 |  |
| 2026-09-27 13:03:27 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-09-27 13:03:12 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-09-27 13:03:06 | Weraganthota (Mahaweli Ganga) | -3.48 | 🟢 Normal | -0.020 |  |
| 2026-09-27 13:02:50 | Deraniyagala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-09-27 13:02:35 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:02:29 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:02:19 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.021 |  |
| 2026-09-27 13:02:11 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-09-27 13:02:11 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:01:57 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:01:44 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:01:26 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-09-27 13:01:15 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:01:04 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:00:50 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:00:45 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-09-27 13:00:43 | Thalgahagoda (Nilwala Ganga) | 1.89 | 🟠 Minor Flood | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 13:00:43 | Thalgahagoda (Nilwala Ganga) | 1.89 | 🟠 Minor Flood | -0.011 |  |
| 2026-09-27 13:15:27 | Baddegama (Gin Ganga) | 4.64 | 🟠 Minor Flood | -0.017 |  |
| 2026-09-27 13:10:05 | Panadugama (Nilwala Ganga) | 5.28 | 🟡 Alert | -0.028 |  |
| 2026-09-27 13:08:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.42 | 🟡 Alert | -0.038 |  |
| 2026-09-27 13:07:30 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-27 13:01:15 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:01:04 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:01:44 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:12:04 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:06:21 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:02:11 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:00:50 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:01:57 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:02:35 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:05:41 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:02:29 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:08:02 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:08:32 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:09:27 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.009 |  |
| 2026-09-27 13:03:12 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-09-27 13:04:45 | Putupaula (Kalu Ganga) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-09-27 13:03:27 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-09-27 13:02:11 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-09-27 13:00:45 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-09-27 13:03:47 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-09-27 13:05:20 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | -0.019 |  |
| 2026-09-27 13:03:06 | Weraganthota (Mahaweli Ganga) | -3.48 | 🟢 Normal | -0.020 |  |
| 2026-09-27 13:02:50 | Deraniyagala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-09-27 13:01:26 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-09-27 13:02:19 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.021 |  |
| 2026-09-27 13:13:36 | Magura (Kalu Ganga) | 2.79 | 🟢 Normal | -0.037 |  |
| 2026-09-27 13:04:08 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.040 |  |
| 2026-09-27 12:02:11 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | -0.045 |  |
| 2026-09-27 13:08:43 | Glencourse (Kelani Ganga) | 11.90 | 🟢 Normal | -0.047 |  |
| 2026-09-27 13:03:45 | Ellagawa (Kalu Ganga) | 8.35 | 🟢 Normal | -0.058 |  |
| 2026-09-27 13:03:38 | Hanwella (Kelani Ganga) | 4.25 | 🟢 Normal | -0.060 |  |
| 2026-09-27 13:04:06 | Rathnapura (Kalu Ganga) | 3.30 | 🟢 Normal | -0.068 |  |
| 2026-09-27 13:03:48 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.121 |  |
| 2026-09-27 13:04:54 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.152 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)