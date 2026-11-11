# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--11_19:03:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,135 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Magura — Alert; 🟡 Dunamale — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 19:03:30 | Glencourse (Kelani Ganga) | 12.19 | 🟢 Normal | 0.304 | 🔺 Rising |
| 2026-11-11 19:03:25 | Norwood (Kelani Ganga) | 1.42 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-11 19:03:18 | Dunamale (Aththanagalu Oya) | 3.78 | 🟡 Alert | 0.000 |  |
| 2026-11-11 19:02:52 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-11 19:02:35 | Thanamalwila (Kirindi Oya) | 2.26 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-11-11 19:02:03 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-11-11 19:01:59 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.090 |  |
| 2026-11-11 19:01:45 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | -0.019 |  |
| 2026-11-11 19:01:40 | Moraketiya (Walawe Ganga) | 3.15 | 🟡 Alert | 0.735 | 🔺 Rising |
| 2026-11-11 19:01:31 | Kuda Oya (Kirindi Oya) | 2.19 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-11 19:01:09 | Pitabeddara (Nilwala Ganga) | 1.69 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-11 19:00:58 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-11-11 19:00:24 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 18:00:27 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 18:06:37 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | -0.021 |  |
| 2026-11-11 19:01:40 | Moraketiya (Walawe Ganga) | 3.15 | 🟡 Alert | 0.735 | 🔺 Rising |
| 2026-11-11 18:02:00 | Magura (Kalu Ganga) | 4.36 | 🟡 Alert | 0.596 | 🔺 Rising |
| 2026-11-11 19:03:18 | Dunamale (Aththanagalu Oya) | 3.78 | 🟡 Alert | 0.000 |  |
| 2026-11-11 18:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.49 | 🟡 Alert | -0.010 |  |
| 2026-11-11 18:05:44 | Panadugama (Nilwala Ganga) | 5.40 | 🟡 Alert | -0.022 |  |
| 2026-11-11 18:08:01 | Deraniyagala (Kelani Ganga) | 3.16 | 🟢 Normal | 1.868 | 🔺 Rising |
| 2026-11-11 18:04:20 | Holombuwa (Kelani Ganga) | 2.16 | 🟢 Normal | 0.654 | 🔺 Rising |
| 2026-11-11 18:05:16 | Thawalama (Gin Ganga) | 3.29 | 🟢 Normal | 0.580 | 🔺 Rising |
| 2026-11-11 18:01:48 | Peradeniya (Mahaweli Ganga) | 4.15 | 🟢 Normal | 0.366 | 🔺 Rising |
| 2026-11-11 19:03:30 | Glencourse (Kelani Ganga) | 12.19 | 🟢 Normal | 0.304 | 🔺 Rising |
| 2026-11-11 18:02:53 | Rathnapura (Kalu Ganga) | 4.41 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-11-11 18:06:25 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-11 19:02:03 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-11-11 18:00:43 | Moragaswewa (Deduru Oya) | 3.46 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-11-11 19:02:35 | Thanamalwila (Kirindi Oya) | 2.26 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-11-11 19:01:09 | Pitabeddara (Nilwala Ganga) | 1.69 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-11 19:01:31 | Kuda Oya (Kirindi Oya) | 2.19 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-11 19:03:25 | Norwood (Kelani Ganga) | 1.42 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-11 18:03:10 | Padiyathalawa (Maduru Oya) | 1.01 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-11 18:04:19 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-11 19:02:52 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-11 19:00:24 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 18:01:56 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:03:23 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:01:13 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:01:41 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:01:37 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:03:12 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-11-11 18:03:27 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-11-11 18:01:30 | Thanthirimale (Malwathu Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-11-11 18:04:48 | Badalgama (Maha Oya) | 3.38 | 🟢 Normal | -0.010 |  |
| 2026-11-11 19:01:45 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | -0.019 |  |
| 2026-11-11 19:00:58 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-11-11 18:01:49 | Manampitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.039 |  |
| 2026-11-11 18:02:35 | Ellagawa (Kalu Ganga) | 8.41 | 🟢 Normal | -0.039 |  |
| 2026-11-11 18:07:36 | Kithulgala (Kelani Ganga) | 2.27 | 🟢 Normal | -0.074 |  |
| 2026-11-11 19:01:59 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)