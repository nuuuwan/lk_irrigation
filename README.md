# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--12_23:34:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **314,203 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Norwood — Alert; 🟡 Kalawellawa (Millakanda) — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 23:34:28 | Siyambalanduwa (Heda Oya) | 1.11 | 🟢 Normal | -0.040 |  |
| 2026-11-12 23:24:45 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.007 |  |
| 2026-11-12 23:24:10 | Panadugama (Nilwala Ganga) | 6.42 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 23:22:34 | Wellawaya (Kirindi Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-11-12 23:22:23 | Rathnapura (Kalu Ganga) | 4.71 | 🟢 Normal | -0.062 |  |
| 2026-11-12 23:14:53 | Urawa (Nilwala Ganga) | 2.82 | 🟡 Alert | -0.126 |  |
| 2026-11-12 23:09:25 | Magura (Kalu Ganga) | 4.61 | 🟡 Alert | -0.074 |  |
| 2026-11-12 23:08:47 | Thawalama (Gin Ganga) | 3.29 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-12 23:07:54 | Badalgama (Maha Oya) | 3.74 | 🟢 Normal | -0.029 |  |
| 2026-11-12 23:07:28 | Norwood (Kelani Ganga) | 1.71 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-11-12 23:06:49 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | -0.021 |  |
| 2026-11-12 23:05:35 | Pitabeddara (Nilwala Ganga) | 3.05 | 🟢 Normal | -0.047 |  |
| 2026-11-12 23:05:21 | Dunamale (Aththanagalu Oya) | 3.87 | 🟡 Alert | -0.056 |  |
| 2026-11-12 23:04:45 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-12 23:04:34 | Manampitiya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.049 |  |
| 2026-11-12 23:04:11 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-12 23:03:49 | Wellawaya (Kirindi Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-11-12 23:03:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.27 | 🟡 Alert | -0.010 |  |
| 2026-11-12 23:03:22 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-12 23:03:18 | Thaldena (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.155 |  |
| 2026-11-12 23:02:46 | Putupaula (Kalu Ganga) | 2.49 | 🟢 Normal | -0.010 |  |
| 2026-11-12 23:02:45 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-11-12 23:02:40 | Giriulla (Maha Oya) | 2.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-12 23:02:29 | Katharagama (Menik Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-11-12 23:02:15 | Moragaswewa (Deduru Oya) | 1.96 | 🟢 Normal | -0.072 |  |
| 2026-11-12 23:02:14 | Hanwella (Kelani Ganga) | 4.40 | 🟢 Normal | -0.071 |  |
| 2026-11-12 23:02:11 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 23:02:05 | Ellagawa (Kalu Ganga) | 8.25 | 🟢 Normal | 0.000 |  |
| 2026-11-12 23:02:04 | Peradeniya (Mahaweli Ganga) | 4.49 | 🟢 Normal | -0.081 |  |
| 2026-11-12 23:01:51 | Glencourse (Kelani Ganga) | 11.82 | 🟢 Normal | -0.062 |  |
| 2026-11-12 23:01:18 | Baddegama (Gin Ganga) | 4.14 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 23:01:01 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-11-12 23:00:55 | Thalgahagoda (Nilwala Ganga) | 1.84 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 23:00:39 | Nakkala (Kumbukkan Oya) | 2.13 | 🟢 Normal | -0.118 |  |
| 2026-11-12 23:00:39 | Ellagawa (Kalu Ganga) | 8.25 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 23:01:18 | Baddegama (Gin Ganga) | 4.14 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 23:24:10 | Panadugama (Nilwala Ganga) | 6.42 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 23:00:55 | Thalgahagoda (Nilwala Ganga) | 1.84 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 23:07:28 | Norwood (Kelani Ganga) | 1.71 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-11-12 23:03:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.27 | 🟡 Alert | -0.010 |  |
| 2026-11-12 22:01:59 | Moraketiya (Walawe Ganga) | 3.15 | 🟡 Alert | -0.010 |  |
| 2026-11-12 23:05:21 | Dunamale (Aththanagalu Oya) | 3.87 | 🟡 Alert | -0.056 |  |
| 2026-11-12 23:09:25 | Magura (Kalu Ganga) | 4.61 | 🟡 Alert | -0.074 |  |
| 2026-11-12 23:14:53 | Urawa (Nilwala Ganga) | 2.82 | 🟡 Alert | -0.126 |  |
| 2026-11-12 18:00:35 | Weraganthota (Mahaweli Ganga) | -1.97 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-11-12 23:04:45 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-12 23:08:47 | Thawalama (Gin Ganga) | 3.29 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-12 22:02:09 | Thanamalwila (Kirindi Oya) | 2.72 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-12 23:02:40 | Giriulla (Maha Oya) | 2.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-12 18:01:04 | Thanthirimale (Malwathu Oya) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 23:02:11 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 23:22:34 | Wellawaya (Kirindi Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-11-12 23:01:01 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-11-12 23:03:22 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-12 23:02:05 | Ellagawa (Kalu Ganga) | 8.25 | 🟢 Normal | 0.000 |  |
| 2026-11-12 23:04:11 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-12 23:24:45 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.007 |  |
| 2026-11-12 18:06:48 | Galgamuwa (Mee Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-11-12 23:02:46 | Putupaula (Kalu Ganga) | 2.49 | 🟢 Normal | -0.010 |  |
| 2026-11-12 22:02:25 | Kuda Oya (Kirindi Oya) | 3.10 | 🟢 Normal | -0.010 |  |
| 2026-11-12 23:02:45 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-11-12 23:02:29 | Katharagama (Menik Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-11-12 23:06:49 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | -0.021 |  |
| 2026-11-12 23:07:54 | Badalgama (Maha Oya) | 3.74 | 🟢 Normal | -0.029 |  |
| 2026-11-12 23:34:28 | Siyambalanduwa (Heda Oya) | 1.11 | 🟢 Normal | -0.040 |  |
| 2026-11-12 23:05:35 | Pitabeddara (Nilwala Ganga) | 3.05 | 🟢 Normal | -0.047 |  |
| 2026-11-12 23:04:34 | Manampitiya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.049 |  |
| 2026-11-12 23:01:51 | Glencourse (Kelani Ganga) | 11.82 | 🟢 Normal | -0.062 |  |
| 2026-11-12 23:22:23 | Rathnapura (Kalu Ganga) | 4.71 | 🟢 Normal | -0.062 |  |
| 2026-11-12 23:02:14 | Hanwella (Kelani Ganga) | 4.40 | 🟢 Normal | -0.071 |  |
| 2026-11-12 23:02:15 | Moragaswewa (Deduru Oya) | 1.96 | 🟢 Normal | -0.072 |  |
| 2026-11-12 23:02:04 | Peradeniya (Mahaweli Ganga) | 4.49 | 🟢 Normal | -0.081 |  |
| 2026-11-12 23:00:39 | Nakkala (Kumbukkan Oya) | 2.13 | 🟢 Normal | -0.118 |  |
| 2026-11-12 23:03:18 | Thaldena (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.155 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)