# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--22_20:07:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **268,145 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 20:07:45 | Ellagawa (Kalu Ganga) | 8.65 | 🟢 Normal | -0.028 |  |
| 2026-09-22 20:07:44 | Putupaula (Kalu Ganga) | 2.96 | 🟢 Normal | 0.000 |  |
| 2026-09-22 20:07:08 | Giriulla (Maha Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-09-22 20:06:12 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-22 20:06:01 | Hanwella (Kelani Ganga) | 4.53 | 🟢 Normal | -0.030 |  |
| 2026-09-22 20:05:58 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 20:05:45 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.029 |  |
| 2026-09-22 20:05:26 | Holombuwa (Kelani Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-09-22 20:05:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.16 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 20:04:52 | Glencourse (Kelani Ganga) | 12.40 | 🟢 Normal | -0.010 |  |
| 2026-09-22 20:04:41 | Nawalapitiya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 20:04:33 | Deraniyagala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.020 |  |
| 2026-09-22 20:04:19 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-09-22 20:04:11 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-09-22 20:03:48 | Peradeniya (Mahaweli Ganga) | 3.42 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-09-22 20:03:45 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 20:03:14 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.054 |  |
| 2026-09-22 20:03:11 | Rathnapura (Kalu Ganga) | 4.10 | 🟢 Normal | -0.033 |  |
| 2026-09-22 20:03:03 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.012 |  |
| 2026-09-22 20:02:35 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-22 20:02:27 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-09-22 20:02:16 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-22 20:02:06 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-22 20:02:04 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-09-22 20:01:45 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 20:01:38 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 20:01:31 | Pitabeddara (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-09-22 20:01:26 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 20:01:23 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-22 20:01:02 | Thalgahagoda (Nilwala Ganga) | 1.53 | 🟡 Alert | 0.000 |  |
| 2026-09-22 20:00:57 | Magura (Kalu Ganga) | 4.61 | 🟡 Alert | -0.031 |  |
| 2026-09-22 20:00:36 | Thawalama (Gin Ganga) | 2.73 | 🟢 Normal | -0.029 |  |
| 2026-09-22 19:23:09 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.016 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 19:04:27 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 20:05:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.16 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 20:01:02 | Thalgahagoda (Nilwala Ganga) | 1.53 | 🟡 Alert | 0.000 |  |
| 2026-09-22 20:00:57 | Magura (Kalu Ganga) | 4.61 | 🟡 Alert | -0.031 |  |
| 2026-09-22 20:03:48 | Peradeniya (Mahaweli Ganga) | 3.42 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-09-22 20:02:16 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-22 20:02:06 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-22 19:23:09 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-09-22 20:05:58 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 20:04:41 | Nawalapitiya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 20:01:45 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 18:00:33 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:00:39 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 20:01:38 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 20:07:08 | Giriulla (Maha Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-09-22 20:02:04 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:04:56 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-22 20:06:12 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-22 20:02:27 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-09-22 20:03:45 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 20:07:44 | Putupaula (Kalu Ganga) | 2.96 | 🟢 Normal | 0.000 |  |
| 2026-09-22 20:01:26 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 20:02:35 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-22 20:01:23 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:02:46 | Thanthirimale (Malwathu Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-09-22 20:04:11 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-09-22 20:04:19 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-09-22 20:04:52 | Glencourse (Kelani Ganga) | 12.40 | 🟢 Normal | -0.010 |  |
| 2026-09-22 20:01:31 | Pitabeddara (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-09-22 20:03:03 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.012 |  |
| 2026-09-22 19:13:53 | Panadugama (Nilwala Ganga) | 4.79 | 🟢 Normal | -0.019 |  |
| 2026-09-22 20:04:33 | Deraniyagala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.020 |  |
| 2026-09-22 20:05:26 | Holombuwa (Kelani Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-09-22 20:07:45 | Ellagawa (Kalu Ganga) | 8.65 | 🟢 Normal | -0.028 |  |
| 2026-09-22 20:05:45 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.029 |  |
| 2026-09-22 20:00:36 | Thawalama (Gin Ganga) | 2.73 | 🟢 Normal | -0.029 |  |
| 2026-09-22 20:06:01 | Hanwella (Kelani Ganga) | 4.53 | 🟢 Normal | -0.030 |  |
| 2026-09-22 20:03:11 | Rathnapura (Kalu Ganga) | 4.10 | 🟢 Normal | -0.033 |  |
| 2026-09-22 20:03:14 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.054 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)