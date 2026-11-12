# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--12_07:29:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,588 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 07:29:19 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 07:18:34 | Thawalama (Gin Ganga) | 4.65 | 🟡 Alert | -0.198 |  |
| 2026-11-12 07:13:07 | Thaldena (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.055 |  |
| 2026-11-12 07:12:16 | Pitabeddara (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.102 |  |
| 2026-11-12 07:12:10 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 07:09:38 | Glencourse (Kelani Ganga) | 13.71 | 🟢 Normal | -0.082 |  |
| 2026-11-12 07:09:22 | Magura (Kalu Ganga) | 5.46 | 🟡 Alert | -0.009 |  |
| 2026-11-12 07:09:02 | Holombuwa (Kelani Ganga) | 2.03 | 🟢 Normal | -0.078 |  |
| 2026-11-12 07:08:13 | Badalgama (Maha Oya) | 4.55 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-11-12 07:07:55 | Dunamale (Aththanagalu Oya) | 4.23 | 🟡 Alert | 0.046 | 🔺 Rising |
| 2026-11-12 07:06:03 | Nakkala (Kumbukkan Oya) | 1.84 | 🟢 Normal | -0.112 |  |
| 2026-11-12 07:05:36 | Moraketiya (Walawe Ganga) | 3.75 | 🟡 Alert | 0.234 | 🔺 Rising |
| 2026-11-12 07:04:57 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | -0.047 |  |
| 2026-11-12 07:04:41 | Hanwella (Kelani Ganga) | 5.65 | 🟢 Normal | 0.039 | 🔺 Rising |
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

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 07:12:10 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 07:29:19 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 07:05:36 | Moraketiya (Walawe Ganga) | 3.75 | 🟡 Alert | 0.234 | 🔺 Rising |
| 2026-11-12 07:07:55 | Dunamale (Aththanagalu Oya) | 4.23 | 🟡 Alert | 0.046 | 🔺 Rising |
| 2026-11-12 07:03:41 | Panadugama (Nilwala Ganga) | 5.97 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-11-12 07:09:22 | Magura (Kalu Ganga) | 5.46 | 🟡 Alert | -0.009 |  |
| 2026-11-12 07:03:57 | Rathnapura (Kalu Ganga) | 5.45 | 🟡 Alert | -0.019 |  |
| 2026-11-12 07:03:53 | Norwood (Kelani Ganga) | 1.54 | 🟡 Alert | -0.020 |  |
| 2026-11-12 07:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.33 | 🟡 Alert | -0.030 |  |
| 2026-11-12 07:01:10 | Peradeniya (Mahaweli Ganga) | 5.21 | 🟡 Alert | -0.166 |  |
| 2026-11-12 07:18:34 | Thawalama (Gin Ganga) | 4.65 | 🟡 Alert | -0.198 |  |
| 2026-11-12 07:08:13 | Badalgama (Maha Oya) | 4.55 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-11-12 07:01:41 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-12 07:04:41 | Hanwella (Kelani Ganga) | 5.65 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-12 07:02:38 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-11-12 07:02:08 | Galgamuwa (Mee Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-12 07:04:16 | Ellagawa (Kalu Ganga) | 8.33 | 🟢 Normal | 0.000 |  |
| 2026-11-12 07:03:15 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-12 07:01:36 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | -0.002 |  |
| 2026-11-12 07:04:14 | Putupaula (Kalu Ganga) | 2.58 | 🟢 Normal | -0.030 |  |
| 2026-11-12 07:00:41 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.034 |  |
| 2026-11-12 07:04:57 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | -0.047 |  |
| 2026-11-12 07:02:50 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.049 |  |
| 2026-11-12 07:13:07 | Thaldena (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.055 |  |
| 2026-11-12 07:01:13 | Moragaswewa (Deduru Oya) | 3.56 | 🟢 Normal | -0.060 |  |
| 2026-11-12 07:02:32 | Deraniyagala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.062 |  |
| 2026-11-12 07:03:02 | Urawa (Nilwala Ganga) | 2.19 | 🟢 Normal | -0.068 |  |
| 2026-11-12 07:09:02 | Holombuwa (Kelani Ganga) | 2.03 | 🟢 Normal | -0.078 |  |
| 2026-11-12 07:09:38 | Glencourse (Kelani Ganga) | 13.71 | 🟢 Normal | -0.082 |  |
| 2026-11-12 07:03:24 | Wellawaya (Kirindi Oya) | 1.94 | 🟢 Normal | -0.087 |  |
| 2026-11-12 07:02:30 | Siyambalanduwa (Heda Oya) | 1.38 | 🟢 Normal | -0.098 |  |
| 2026-11-12 07:02:58 | Katharagama (Menik Ganga) | 0.77 | 🟢 Normal | -0.100 |  |
| 2026-11-12 07:12:16 | Pitabeddara (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.102 |  |
| 2026-11-12 07:06:03 | Nakkala (Kumbukkan Oya) | 1.84 | 🟢 Normal | -0.112 |  |
| 2026-11-12 07:02:31 | Giriulla (Maha Oya) | 3.33 | 🟢 Normal | -0.128 |  |
| 2026-11-12 07:02:56 | Weraganthota (Mahaweli Ganga) | -1.24 | 🟢 Normal | -0.170 |  |
| 2026-11-12 07:03:44 | Kuda Oya (Kirindi Oya) | 3.11 | 🟢 Normal | -0.173 |  |
| 2026-11-12 07:03:51 | Thanamalwila (Kirindi Oya) | 3.10 | 🟢 Normal | -0.431 |  |
| 2026-11-12 07:01:52 | Padiyathalawa (Maduru Oya) | 1.51 | 🟢 Normal | -576.000 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)