# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--28_06:13:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,019 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Ellagawa — Alert; 🟡 Putupaula — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 06:13:46 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.166 |  |
| 2026-10-28 06:10:46 | Ellagawa (Kalu Ganga) | 10.46 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-10-28 06:08:32 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 06:08:27 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | -0.019 |  |
| 2026-10-28 06:07:15 | Urawa (Nilwala Ganga) | 1.52 | 🟢 Normal | -0.112 |  |
| 2026-10-28 06:06:06 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.016 |  |
| 2026-10-28 06:06:02 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.029 |  |
| 2026-10-28 06:05:49 | Thawalama (Gin Ganga) | 2.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-28 06:04:36 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-28 06:04:22 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-28 06:04:13 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-28 06:04:05 | Deraniyagala (Kelani Ganga) | 1.17 | 🟢 Normal | -0.011 |  |
| 2026-10-28 06:03:59 | Glencourse (Kelani Ganga) | 11.85 | 🟢 Normal | -0.088 |  |
| 2026-10-28 06:03:48 | Giriulla (Maha Oya) | 2.43 | 🟢 Normal | -0.020 |  |
| 2026-10-28 06:03:40 | Kithulgala (Kelani Ganga) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-10-28 06:03:36 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-10-28 06:02:46 | Dunamale (Aththanagalu Oya) | 4.17 | 🟡 Alert | -0.090 |  |
| 2026-10-28 06:02:40 | Panadugama (Nilwala Ganga) | 5.96 | 🟡 Alert | -0.035 |  |
| 2026-10-28 06:02:34 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-10-28 06:02:32 | Badalgama (Maha Oya) | 3.68 | 🟢 Normal | -0.079 |  |
| 2026-10-28 06:02:22 | Moragaswewa (Deduru Oya) | 3.29 | 🟢 Normal | 0.000 |  |
| 2026-10-28 06:02:16 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-28 06:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.82 | 🟠 Minor Flood | -0.041 |  |
| 2026-10-28 06:02:08 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-10-28 06:02:02 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.025 |  |
| 2026-10-28 06:01:57 | Putupaula (Kalu Ganga) | 3.58 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-10-28 06:01:53 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-10-28 06:01:51 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | -0.061 |  |
| 2026-10-28 06:01:43 | Hanwella (Kelani Ganga) | 4.70 | 🟢 Normal | -0.063 |  |
| 2026-10-28 06:01:38 | Rathnapura (Kalu Ganga) | 6.75 | 🟡 Alert | -0.073 |  |
| 2026-10-28 06:01:25 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-28 06:01:24 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-28 06:01:13 | Manampitiya (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.096 |  |
| 2026-10-28 06:01:01 | Moragaswewa (Deduru Oya) | 3.29 | 🟢 Normal | 0.000 |  |
| 2026-10-28 06:00:48 | Magura (Kalu Ganga) | 4.37 | 🟡 Alert | -0.041 |  |
| 2026-10-28 06:00:37 | Moraketiya (Walawe Ganga) | 1.48 | 🟢 Normal | -0.022 |  |
| 2026-10-28 06:00:30 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 06:02:34 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-10-28 06:08:32 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 06:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.82 | 🟠 Minor Flood | -0.041 |  |
| 2026-10-28 06:10:46 | Ellagawa (Kalu Ganga) | 10.46 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-10-28 06:01:57 | Putupaula (Kalu Ganga) | 3.58 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-10-28 06:02:40 | Panadugama (Nilwala Ganga) | 5.96 | 🟡 Alert | -0.035 |  |
| 2026-10-28 06:00:48 | Magura (Kalu Ganga) | 4.37 | 🟡 Alert | -0.041 |  |
| 2026-10-28 06:01:38 | Rathnapura (Kalu Ganga) | 6.75 | 🟡 Alert | -0.073 |  |
| 2026-10-28 06:02:46 | Dunamale (Aththanagalu Oya) | 4.17 | 🟡 Alert | -0.090 |  |
| 2026-10-28 06:04:36 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-28 06:01:25 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-28 06:01:24 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-28 06:05:49 | Thawalama (Gin Ganga) | 2.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-28 06:02:22 | Moragaswewa (Deduru Oya) | 3.29 | 🟢 Normal | 0.000 |  |
| 2026-10-28 06:02:08 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-10-28 05:10:22 | Horowpothana (Yan Oya) | 3.37 | 🟢 Normal | 0.000 |  |
| 2026-10-28 06:04:22 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-28 06:02:16 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-28 06:04:13 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-27 18:23:14 | Galgamuwa (Mee Oya) | 4.03 | 🟢 Normal | -0.008 |  |
| 2026-10-28 06:00:30 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-10-28 06:03:40 | Kithulgala (Kelani Ganga) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-10-28 06:01:53 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-10-28 06:03:36 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-10-28 06:04:05 | Deraniyagala (Kelani Ganga) | 1.17 | 🟢 Normal | -0.011 |  |
| 2026-10-28 06:06:06 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.016 |  |
| 2026-10-28 06:08:27 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | -0.019 |  |
| 2026-10-28 06:03:48 | Giriulla (Maha Oya) | 2.43 | 🟢 Normal | -0.020 |  |
| 2026-10-28 06:00:37 | Moraketiya (Walawe Ganga) | 1.48 | 🟢 Normal | -0.022 |  |
| 2026-10-28 06:02:02 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.025 |  |
| 2026-10-28 06:06:02 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.029 |  |
| 2026-10-28 06:01:51 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | -0.061 |  |
| 2026-10-28 06:01:43 | Hanwella (Kelani Ganga) | 4.70 | 🟢 Normal | -0.063 |  |
| 2026-10-28 06:02:32 | Badalgama (Maha Oya) | 3.68 | 🟢 Normal | -0.079 |  |
| 2026-10-28 06:03:59 | Glencourse (Kelani Ganga) | 11.85 | 🟢 Normal | -0.088 |  |
| 2026-10-28 06:01:13 | Manampitiya (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.096 |  |
| 2026-10-28 06:07:15 | Urawa (Nilwala Ganga) | 1.52 | 🟢 Normal | -0.112 |  |
| 2026-10-27 18:00:41 | Thanthirimale (Malwathu Oya) | 2.72 | 🟢 Normal | -0.133 |  |
| 2026-10-28 06:13:46 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.166 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)