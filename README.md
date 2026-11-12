# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--12_10:19:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,705 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 10:19:56 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 10:17:12 | Wellawaya (Kirindi Oya) | 1.79 | 🟢 Normal | -0.016 |  |
| 2026-11-12 10:11:33 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-12 10:10:51 | Panadugama (Nilwala Ganga) | 5.97 | 🟡 Alert | -0.009 |  |
| 2026-11-12 10:10:36 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | -0.046 |  |
| 2026-11-12 10:09:39 | Urawa (Nilwala Ganga) | 1.82 | 🟢 Normal | -0.184 |  |
| 2026-11-12 10:08:49 | Rathnapura (Kalu Ganga) | 5.30 | 🟡 Alert | -0.067 |  |
| 2026-11-12 10:08:41 | Thanamalwila (Kirindi Oya) | 2.55 | 🟢 Normal | -0.115 |  |
| 2026-11-12 10:08:06 | Glencourse (Kelani Ganga) | 13.20 | 🟢 Normal | -0.190 |  |
| 2026-11-12 10:07:45 | Kuda Oya (Kirindi Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-12 10:07:39 | Badalgama (Maha Oya) | 4.43 | 🟢 Normal | -0.072 |  |
| 2026-11-12 10:06:58 | Magura (Kalu Ganga) | 5.44 | 🟡 Alert | -0.021 |  |
| 2026-11-12 10:05:59 | Holombuwa (Kelani Ganga) | 1.76 | 🟢 Normal | -0.060 |  |
| 2026-11-12 10:05:53 | Dunamale (Aththanagalu Oya) | 4.25 | 🟡 Alert | 0.000 |  |
| 2026-11-12 10:05:26 | Putupaula (Kalu Ganga) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-11-12 10:05:13 | Peradeniya (Mahaweli Ganga) | 4.94 | 🟢 Normal | -0.108 |  |
| 2026-11-12 10:04:22 | Thaldena (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-11-12 10:03:57 | Ellagawa (Kalu Ganga) | 8.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-12 10:03:46 | Moraketiya (Walawe Ganga) | 3.92 | 🟡 Alert | 0.000 |  |
| 2026-11-12 10:03:35 | Kuda Oya (Kirindi Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-12 10:03:33 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-12 10:03:18 | Hanwella (Kelani Ganga) | 5.60 | 🟢 Normal | -0.050 |  |
| 2026-11-12 10:03:12 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-12 10:02:55 | Deraniyagala (Kelani Ganga) | 1.17 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-12 10:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.33 | 🟡 Alert | 0.000 |  |
| 2026-11-12 10:02:39 | Giriulla (Maha Oya) | 3.08 | 🟢 Normal | -0.079 |  |
| 2026-11-12 10:02:28 | Pitabeddara (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.105 |  |
| 2026-11-12 10:02:27 | Norwood (Kelani Ganga) | 1.42 | 🟢 Normal | -0.041 |  |
| 2026-11-12 10:02:13 | Kithulgala (Kelani Ganga) | 2.27 | 🟢 Normal | -0.061 |  |
| 2026-11-12 10:02:07 | Katharagama (Menik Ganga) | 0.61 | 🟢 Normal | -0.053 |  |
| 2026-11-12 10:02:01 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | -0.097 |  |
| 2026-11-12 10:01:56 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-11-12 10:01:51 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.016 |  |
| 2026-11-12 10:01:44 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-12 10:01:35 | Thawalama (Gin Ganga) | 3.70 | 🟢 Normal | -0.347 |  |
| 2026-11-12 10:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.040 |  |
| 2026-11-12 10:01:14 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-12 10:00:55 | Siyambalanduwa (Heda Oya) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-11-12 10:00:23 | Nakkala (Kumbukkan Oya) | 1.64 | 🟢 Normal | -0.050 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 10:03:33 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-12 10:19:56 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 10:03:46 | Moraketiya (Walawe Ganga) | 3.92 | 🟡 Alert | 0.000 |  |
| 2026-11-12 10:05:53 | Dunamale (Aththanagalu Oya) | 4.25 | 🟡 Alert | 0.000 |  |
| 2026-11-12 10:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.33 | 🟡 Alert | 0.000 |  |
| 2026-11-12 10:10:51 | Panadugama (Nilwala Ganga) | 5.97 | 🟡 Alert | -0.009 |  |
| 2026-11-12 10:06:58 | Magura (Kalu Ganga) | 5.44 | 🟡 Alert | -0.021 |  |
| 2026-11-12 10:08:49 | Rathnapura (Kalu Ganga) | 5.30 | 🟡 Alert | -0.067 |  |
| 2026-11-12 10:02:55 | Deraniyagala (Kelani Ganga) | 1.17 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-12 10:01:14 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-12 10:03:12 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-12 10:03:57 | Ellagawa (Kalu Ganga) | 8.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-12 10:11:33 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-12 10:01:44 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-12 10:07:45 | Kuda Oya (Kirindi Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-12 10:05:26 | Putupaula (Kalu Ganga) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-11-12 10:01:51 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.016 |  |
| 2026-11-12 10:17:12 | Wellawaya (Kirindi Oya) | 1.79 | 🟢 Normal | -0.016 |  |
| 2026-11-12 10:00:55 | Siyambalanduwa (Heda Oya) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-11-12 10:01:56 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-11-12 10:04:22 | Thaldena (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-11-12 10:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.040 |  |
| 2026-11-12 10:02:27 | Norwood (Kelani Ganga) | 1.42 | 🟢 Normal | -0.041 |  |
| 2026-11-12 10:10:36 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | -0.046 |  |
| 2026-11-12 10:03:18 | Hanwella (Kelani Ganga) | 5.60 | 🟢 Normal | -0.050 |  |
| 2026-11-12 10:00:23 | Nakkala (Kumbukkan Oya) | 1.64 | 🟢 Normal | -0.050 |  |
| 2026-11-12 10:02:07 | Katharagama (Menik Ganga) | 0.61 | 🟢 Normal | -0.053 |  |
| 2026-11-12 10:05:59 | Holombuwa (Kelani Ganga) | 1.76 | 🟢 Normal | -0.060 |  |
| 2026-11-12 10:02:13 | Kithulgala (Kelani Ganga) | 2.27 | 🟢 Normal | -0.061 |  |
| 2026-11-12 10:07:39 | Badalgama (Maha Oya) | 4.43 | 🟢 Normal | -0.072 |  |
| 2026-11-12 10:02:39 | Giriulla (Maha Oya) | 3.08 | 🟢 Normal | -0.079 |  |
| 2026-11-12 09:06:05 | Moragaswewa (Deduru Oya) | 3.44 | 🟢 Normal | -0.084 |  |
| 2026-11-12 10:02:01 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | -0.097 |  |
| 2026-11-12 10:02:28 | Pitabeddara (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.105 |  |
| 2026-11-12 10:05:13 | Peradeniya (Mahaweli Ganga) | 4.94 | 🟢 Normal | -0.108 |  |
| 2026-11-12 10:08:41 | Thanamalwila (Kirindi Oya) | 2.55 | 🟢 Normal | -0.115 |  |
| 2026-11-12 10:09:39 | Urawa (Nilwala Ganga) | 1.82 | 🟢 Normal | -0.184 |  |
| 2026-11-12 10:08:06 | Glencourse (Kelani Ganga) | 13.20 | 🟢 Normal | -0.190 |  |
| 2026-11-12 10:01:35 | Thawalama (Gin Ganga) | 3.70 | 🟢 Normal | -0.347 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)