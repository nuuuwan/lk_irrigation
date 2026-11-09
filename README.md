# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--09_09:04:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **310,959 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Dunamale — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Baddegama — Alert; 🟡 Thalgahagoda — Alert; 🟡 Panadugama — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 09:04:02 | Glencourse (Kelani Ganga) | 11.71 | 🟢 Normal | -0.181 |  |
| 2026-11-09 09:03:59 | Moraketiya (Walawe Ganga) | 2.10 | 🟢 Normal | -0.399 |  |
| 2026-11-09 09:03:34 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.030 |  |
| 2026-11-09 09:03:21 | Horowpothana (Yan Oya) | 2.83 | 🟢 Normal | -0.144 |  |
| 2026-11-09 09:03:20 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-11-09 09:03:09 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-09 09:03:06 | Badalgama (Maha Oya) | 4.40 | 🟢 Normal | -0.119 |  |
| 2026-11-09 09:02:57 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.103 |  |
| 2026-11-09 09:02:52 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | 0.000 |  |
| 2026-11-09 09:02:52 | Giriulla (Maha Oya) | 3.09 | 🟢 Normal | -0.107 |  |
| 2026-11-09 09:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.97 | 🟡 Alert | 0.026 | 🔺 Rising |
| 2026-11-09 09:02:47 | Hanwella (Kelani Ganga) | 4.81 | 🟢 Normal | -0.132 |  |
| 2026-11-09 09:02:42 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-09 09:02:36 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.080 |  |
| 2026-11-09 09:02:35 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-11-09 09:02:21 | Kuda Oya (Kirindi Oya) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-11-09 09:02:18 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-09 09:01:14 | Pitabeddara (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-09 09:01:02 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-09 09:00:26 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 08:04:42 | Dunamale (Aththanagalu Oya) | 4.40 | 🟠 Minor Flood | 0.078 | 🔺 Rising |
| 2026-11-09 09:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.97 | 🟡 Alert | 0.026 | 🔺 Rising |
| 2026-11-09 08:11:20 | Baddegama (Gin Ganga) | 3.61 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-09 09:02:52 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | 0.000 |  |
| 2026-11-09 08:03:51 | Panadugama (Nilwala Ganga) | 5.74 | 🟡 Alert | -0.014 |  |
| 2026-11-09 08:07:42 | Magura (Kalu Ganga) | 5.20 | 🟡 Alert | -0.110 |  |
| 2026-11-09 09:02:35 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-11-09 09:01:14 | Pitabeddara (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-09 08:03:41 | Thanamalwila (Kirindi Oya) | 1.56 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-09 09:02:18 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-09 09:00:26 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-11-09 07:03:23 | Galgamuwa (Mee Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-09 09:03:20 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-11-09 09:03:09 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-09 09:02:42 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-09 08:01:00 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-09 09:01:02 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-09 08:07:15 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | -0.009 |  |
| 2026-11-09 08:02:09 | Putupaula (Kalu Ganga) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-11-09 08:08:47 | Holombuwa (Kelani Ganga) | 1.60 | 🟢 Normal | -0.012 |  |
| 2026-11-09 08:08:56 | Peradeniya (Mahaweli Ganga) | 3.18 | 🟢 Normal | -0.018 |  |
| 2026-11-08 23:07:10 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.018 |  |
| 2026-11-09 09:02:21 | Kuda Oya (Kirindi Oya) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-11-09 09:03:34 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.030 |  |
| 2026-11-09 08:00:55 | Moragaswewa (Deduru Oya) | 2.86 | 🟢 Normal | -0.040 |  |
| 2026-11-09 08:05:25 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | -0.045 |  |
| 2026-11-09 08:03:25 | Ellagawa (Kalu Ganga) | 7.91 | 🟢 Normal | -0.055 |  |
| 2026-11-09 08:06:00 | Urawa (Nilwala Ganga) | 1.27 | 🟢 Normal | -0.055 |  |
| 2026-11-09 09:02:36 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.080 |  |
| 2026-11-09 08:04:28 | Rathnapura (Kalu Ganga) | 3.29 | 🟢 Normal | -0.080 |  |
| 2026-11-09 08:09:21 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | -0.099 |  |
| 2026-11-09 09:02:57 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.103 |  |
| 2026-11-09 09:02:52 | Giriulla (Maha Oya) | 3.09 | 🟢 Normal | -0.107 |  |
| 2026-11-09 09:03:06 | Badalgama (Maha Oya) | 4.40 | 🟢 Normal | -0.119 |  |
| 2026-11-09 09:02:47 | Hanwella (Kelani Ganga) | 4.81 | 🟢 Normal | -0.132 |  |
| 2026-11-09 09:03:21 | Horowpothana (Yan Oya) | 2.83 | 🟢 Normal | -0.144 |  |
| 2026-11-09 09:04:02 | Glencourse (Kelani Ganga) | 11.71 | 🟢 Normal | -0.181 |  |
| 2026-11-09 08:10:25 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.222 |  |
| 2026-11-09 09:03:59 | Moraketiya (Walawe Ganga) | 2.10 | 🟢 Normal | -0.399 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)