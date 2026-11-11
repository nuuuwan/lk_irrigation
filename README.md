# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--11_23:34:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,302 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Holombuwa — Alert; 🟡 Magura — Alert; 🟡 Thawalama — Alert; 🟡 Urawa — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 23:34:49 | Nawalapitiya (Mahaweli Ganga) | 2.91 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-11 23:30:47 | Pitabeddara (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-11 23:27:10 | Peradeniya (Mahaweli Ganga) | 4.92 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-11 23:10:21 | Baddegama (Gin Ganga) | 4.05 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-11 23:09:54 | Magura (Kalu Ganga) | 5.16 | 🟡 Alert | 0.123 | 🔺 Rising |
| 2026-11-11 23:08:40 | Padiyathalawa (Maduru Oya) | 3.80 | 🟢 Normal | 2.661 | 🔺 Rising |
| 2026-11-11 23:07:23 | Katharagama (Menik Ganga) | 1.03 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-11 23:06:29 | Badalgama (Maha Oya) | 3.52 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-11 23:06:16 | Norwood (Kelani Ganga) | 1.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-11 23:06:06 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-11 23:05:57 | Nakkala (Kumbukkan Oya) | 3.80 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-11-11 23:05:55 | Panadugama (Nilwala Ganga) | 5.46 | 🟡 Alert | 0.057 | 🔺 Rising |
| 2026-11-11 23:05:54 | Kithulgala (Kelani Ganga) | 2.34 | 🟢 Normal | -0.031 |  |
| 2026-11-11 23:05:48 | Glencourse (Kelani Ganga) | 13.15 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-11-11 23:05:32 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-11 23:05:02 | Urawa (Nilwala Ganga) | 3.12 | 🟡 Alert | 0.097 | 🔺 Rising |
| 2026-11-11 23:04:56 | Deraniyagala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-11-11 23:04:53 | Holombuwa (Kelani Ganga) | 3.30 | 🟡 Alert | 0.418 | 🔺 Rising |
| 2026-11-11 23:04:38 | Giriulla (Maha Oya) | 2.58 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-11-11 23:04:37 | Rathnapura (Kalu Ganga) | 4.97 | 🟢 Normal | -0.030 |  |
| 2026-11-11 23:04:02 | Putupaula (Kalu Ganga) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-11-11 23:03:26 | Siyambalanduwa (Heda Oya) | 1.15 | 🟢 Normal | 0.407 | 🔺 Rising |
| 2026-11-11 23:03:23 | Manampitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.042 |  |
| 2026-11-11 23:03:05 | Thawalama (Gin Ganga) | 5.10 | 🟡 Alert | 0.115 | 🔺 Rising |
| 2026-11-11 23:02:58 | Thaldena (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.101 |  |
| 2026-11-11 23:02:57 | Thanamalwila (Kirindi Oya) | 2.46 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-11 23:02:27 | Dunamale (Aththanagalu Oya) | 3.98 | 🟡 Alert | 0.084 | 🔺 Rising |
| 2026-11-11 23:02:24 | Kuda Oya (Kirindi Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-11-11 23:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.44 | 🟡 Alert | -0.011 |  |
| 2026-11-11 23:02:13 | Hanwella (Kelani Ganga) | 4.58 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-11-11 23:02:07 | Moraketiya (Walawe Ganga) | 4.15 | 🟡 Alert | 0.000 |  |
| 2026-11-11 23:01:54 | Thalgahagoda (Nilwala Ganga) | 1.78 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 23:01:46 | Ellagawa (Kalu Ganga) | 8.38 | 🟢 Normal | -0.010 |  |
| 2026-11-11 23:01:28 | Moragaswewa (Deduru Oya) | 3.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-11 23:01:07 | Wellawaya (Kirindi Oya) | 3.64 | 🟢 Normal | 1.005 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 23:01:54 | Thalgahagoda (Nilwala Ganga) | 1.78 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 23:10:21 | Baddegama (Gin Ganga) | 4.05 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-11 23:04:53 | Holombuwa (Kelani Ganga) | 3.30 | 🟡 Alert | 0.418 | 🔺 Rising |
| 2026-11-11 23:09:54 | Magura (Kalu Ganga) | 5.16 | 🟡 Alert | 0.123 | 🔺 Rising |
| 2026-11-11 23:03:05 | Thawalama (Gin Ganga) | 5.10 | 🟡 Alert | 0.115 | 🔺 Rising |
| 2026-11-11 23:05:02 | Urawa (Nilwala Ganga) | 3.12 | 🟡 Alert | 0.097 | 🔺 Rising |
| 2026-11-11 23:02:27 | Dunamale (Aththanagalu Oya) | 3.98 | 🟡 Alert | 0.084 | 🔺 Rising |
| 2026-11-11 23:05:55 | Panadugama (Nilwala Ganga) | 5.46 | 🟡 Alert | 0.057 | 🔺 Rising |
| 2026-11-11 23:02:07 | Moraketiya (Walawe Ganga) | 4.15 | 🟡 Alert | 0.000 |  |
| 2026-11-11 23:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.44 | 🟡 Alert | -0.011 |  |
| 2026-11-11 23:08:40 | Padiyathalawa (Maduru Oya) | 3.80 | 🟢 Normal | 2.661 | 🔺 Rising |
| 2026-11-11 23:01:07 | Wellawaya (Kirindi Oya) | 3.64 | 🟢 Normal | 1.005 | 🔺 Rising |
| 2026-11-11 23:03:26 | Siyambalanduwa (Heda Oya) | 1.15 | 🟢 Normal | 0.407 | 🔺 Rising |
| 2026-11-11 23:04:38 | Giriulla (Maha Oya) | 2.58 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-11-11 23:05:48 | Glencourse (Kelani Ganga) | 13.15 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-11-11 23:02:13 | Hanwella (Kelani Ganga) | 4.58 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-11-11 23:05:57 | Nakkala (Kumbukkan Oya) | 3.80 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-11-11 23:27:10 | Peradeniya (Mahaweli Ganga) | 4.92 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-11 23:30:47 | Pitabeddara (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-11 23:02:57 | Thanamalwila (Kirindi Oya) | 2.46 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-11 23:07:23 | Katharagama (Menik Ganga) | 1.03 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-11 23:06:29 | Badalgama (Maha Oya) | 3.52 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-11 23:34:49 | Nawalapitiya (Mahaweli Ganga) | 2.91 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-11 23:06:16 | Norwood (Kelani Ganga) | 1.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-11 23:06:06 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-11 23:05:32 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-11 23:01:28 | Moragaswewa (Deduru Oya) | 3.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-11 18:01:56 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:01:41 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-11-11 23:04:02 | Putupaula (Kalu Ganga) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-11-11 23:02:24 | Kuda Oya (Kirindi Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-11-11 18:01:30 | Thanthirimale (Malwathu Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-11-11 23:04:56 | Deraniyagala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-11-11 23:01:46 | Ellagawa (Kalu Ganga) | 8.38 | 🟢 Normal | -0.010 |  |
| 2026-11-11 22:01:29 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | -0.025 |  |
| 2026-11-11 23:04:37 | Rathnapura (Kalu Ganga) | 4.97 | 🟢 Normal | -0.030 |  |
| 2026-11-11 23:05:54 | Kithulgala (Kelani Ganga) | 2.34 | 🟢 Normal | -0.031 |  |
| 2026-11-11 23:03:23 | Manampitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.042 |  |
| 2026-11-11 23:02:58 | Thaldena (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)