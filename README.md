# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--12_07:04:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,574 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert; 🟡 Magura — Alert; 🟡 Rathnapura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 07:04:16 | Ellagawa (Kalu Ganga) | 8.33 | 🟢 Normal | 0.000 |  |
| 2026-11-12 07:04:14 | Putupaula (Kalu Ganga) | 2.58 | 🟢 Normal | -0.030 |  |
| 2026-11-12 07:03:57 | Rathnapura (Kalu Ganga) | 5.45 | 🟡 Alert | -0.019 |  |
| 2026-11-12 07:03:53 | Norwood (Kelani Ganga) | 1.54 | 🟡 Alert | -0.020 |  |
| 2026-11-12 07:03:51 | Thanamalwila (Kirindi Oya) | 3.10 | 🟢 Normal | -0.431 |  |
| 2026-11-12 07:03:44 | Kuda Oya (Kirindi Oya) | 3.11 | 🟢 Normal | -0.173 |  |
| 2026-11-12 07:03:41 | Panadugama (Nilwala Ganga) | 5.97 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-11-12 07:03:24 | Wellawaya (Kirindi Oya) | 1.94 | 🟢 Normal | -0.087 |  |
| 2026-11-12 07:03:15 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-12 07:03:02 | Urawa (Nilwala Ganga) | 2.19 | 🟢 Normal | -0.068 |  |
| 2026-11-12 07:02:58 | Katharagama (Menik Ganga) | 0.77 | 🟢 Normal | -0.100 |  |
| 2026-11-12 07:02:56 | Weraganthota (Mahaweli Ganga) | -1.24 | 🟢 Normal | -0.170 |  |
| 2026-11-12 07:02:50 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.049 |  |
| 2026-11-12 07:02:38 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-11-12 07:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.33 | 🟡 Alert | -0.030 |  |
| 2026-11-12 07:02:32 | Deraniyagala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.062 |  |
| 2026-11-12 07:02:31 | Giriulla (Maha Oya) | 3.33 | 🟢 Normal | -0.128 |  |
| 2026-11-12 07:02:30 | Siyambalanduwa (Heda Oya) | 1.38 | 🟢 Normal | -0.098 |  |
| 2026-11-12 07:02:08 | Galgamuwa (Mee Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-12 07:01:52 | Padiyathalawa (Maduru Oya) | 1.51 | 🟢 Normal | -576.000 |  |
| 2026-11-12 07:01:50 | Padiyathalawa (Maduru Oya) | 1.83 | 🟢 Normal | -576.000 |  |
| 2026-11-12 07:01:41 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-12 07:01:36 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | -0.002 |  |
| 2026-11-12 07:01:13 | Moragaswewa (Deduru Oya) | 3.56 | 🟢 Normal | -0.060 |  |
| 2026-11-12 07:01:10 | Peradeniya (Mahaweli Ganga) | 5.21 | 🟡 Alert | -0.166 |  |
| 2026-11-12 07:00:41 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.034 |  |
| 2026-11-12 06:40:13 | Galgamuwa (Mee Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-12 06:36:42 | Galgamuwa (Mee Oya) | 0.65 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 06:09:36 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-12 06:03:32 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 06:02:51 | Dunamale (Aththanagalu Oya) | 4.18 | 🟡 Alert | 0.061 | 🔺 Rising |
| 2026-11-12 07:03:41 | Panadugama (Nilwala Ganga) | 5.97 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-11-12 06:02:36 | Magura (Kalu Ganga) | 5.47 | 🟡 Alert | 0.000 |  |
| 2026-11-12 07:03:57 | Rathnapura (Kalu Ganga) | 5.45 | 🟡 Alert | -0.019 |  |
| 2026-11-12 07:03:53 | Norwood (Kelani Ganga) | 1.54 | 🟡 Alert | -0.020 |  |
| 2026-11-12 07:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.33 | 🟡 Alert | -0.030 |  |
| 2026-11-12 06:02:57 | Thawalama (Gin Ganga) | 4.90 | 🟡 Alert | -0.141 |  |
| 2026-11-12 07:01:10 | Peradeniya (Mahaweli Ganga) | 5.21 | 🟡 Alert | -0.166 |  |
| 2026-11-12 06:01:26 | Moraketiya (Walawe Ganga) | 3.50 | 🟡 Alert | -0.701 |  |
| 2026-11-12 06:04:33 | Badalgama (Maha Oya) | 4.48 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-11-12 06:02:42 | Hanwella (Kelani Ganga) | 5.61 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-12 07:01:41 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-12 07:02:38 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-11-12 07:02:08 | Galgamuwa (Mee Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-12 07:04:16 | Ellagawa (Kalu Ganga) | 8.33 | 🟢 Normal | 0.000 |  |
| 2026-11-12 07:03:15 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-12 07:01:36 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | -0.002 |  |
| 2026-11-12 07:04:14 | Putupaula (Kalu Ganga) | 2.58 | 🟢 Normal | -0.030 |  |
| 2026-11-12 07:00:41 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.034 |  |
| 2026-11-12 06:01:10 | Yaka Wewa (Ma Oya) | 0.97 | 🟢 Normal | -0.036 |  |
| 2026-11-12 07:02:50 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.049 |  |
| 2026-11-12 07:01:13 | Moragaswewa (Deduru Oya) | 3.56 | 🟢 Normal | -0.060 |  |
| 2026-11-12 07:02:32 | Deraniyagala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.062 |  |
| 2026-11-12 07:03:02 | Urawa (Nilwala Ganga) | 2.19 | 🟢 Normal | -0.068 |  |
| 2026-11-12 07:03:24 | Wellawaya (Kirindi Oya) | 1.94 | 🟢 Normal | -0.087 |  |
| 2026-11-12 06:01:43 | Nakkala (Kumbukkan Oya) | 1.96 | 🟢 Normal | -0.090 |  |
| 2026-11-12 07:02:30 | Siyambalanduwa (Heda Oya) | 1.38 | 🟢 Normal | -0.098 |  |
| 2026-11-12 07:02:58 | Katharagama (Menik Ganga) | 0.77 | 🟢 Normal | -0.100 |  |
| 2026-11-12 07:02:31 | Giriulla (Maha Oya) | 3.33 | 🟢 Normal | -0.128 |  |
| 2026-11-12 06:04:08 | Glencourse (Kelani Ganga) | 13.80 | 🟢 Normal | -0.136 |  |
| 2026-11-12 07:02:56 | Weraganthota (Mahaweli Ganga) | -1.24 | 🟢 Normal | -0.170 |  |
| 2026-11-12 07:03:44 | Kuda Oya (Kirindi Oya) | 3.11 | 🟢 Normal | -0.173 |  |
| 2026-11-12 06:07:42 | Thaldena (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.174 |  |
| 2026-11-12 06:07:25 | Holombuwa (Kelani Ganga) | 2.11 | 🟢 Normal | -0.209 |  |
| 2026-11-12 06:01:50 | Pitabeddara (Nilwala Ganga) | 3.02 | 🟢 Normal | -0.248 |  |
| 2026-11-12 07:03:51 | Thanamalwila (Kirindi Oya) | 3.10 | 🟢 Normal | -0.431 |  |
| 2026-11-12 07:01:52 | Padiyathalawa (Maduru Oya) | 1.51 | 🟢 Normal | -576.000 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)