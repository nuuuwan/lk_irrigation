# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--26_06:38:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **298,205 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 06:38:46 | Galgamuwa (Mee Oya) | 2.26 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-10-26 06:16:29 | Dunamale (Aththanagalu Oya) | 3.13 | 🟢 Normal | 0.000 |  |
| 2026-10-26 06:12:45 | Horowpothana (Yan Oya) | 2.34 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-26 06:08:38 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-26 06:08:27 | Badalgama (Maha Oya) | 4.05 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-26 06:08:13 | Baddegama (Gin Ganga) | 2.68 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-26 06:08:04 | Hanwella (Kelani Ganga) | 4.23 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-26 06:07:20 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-26 06:07:17 | Giriulla (Maha Oya) | 3.08 | 🟢 Normal | -0.103 |  |
| 2026-10-26 06:07:11 | Pitabeddara (Nilwala Ganga) | 1.88 | 🟢 Normal | -0.021 |  |
| 2026-10-26 06:06:41 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | -0.040 |  |
| 2026-10-26 06:06:31 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.028 |  |
| 2026-10-26 06:06:17 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | -0.013 |  |
| 2026-10-26 06:06:11 | Norwood (Kelani Ganga) | 1.47 | 🟢 Normal | -0.053 |  |
| 2026-10-26 06:06:10 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-10-26 06:06:10 | Glencourse (Kelani Ganga) | 12.38 | 🟢 Normal | -0.086 |  |
| 2026-10-26 06:05:44 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 06:05:32 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-10-26 06:05:03 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | -0.096 |  |
| 2026-10-26 06:04:50 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | -0.021 |  |
| 2026-10-26 06:04:35 | Peradeniya (Mahaweli Ganga) | 3.39 | 🟢 Normal | -0.255 |  |
| 2026-10-26 06:04:13 | Dunamale (Aththanagalu Oya) | 3.13 | 🟢 Normal | 0.000 |  |
| 2026-10-26 06:03:57 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-26 06:03:42 | Ellagawa (Kalu Ganga) | 8.19 | 🟢 Normal | -0.019 |  |
| 2026-10-26 06:03:28 | Magura (Kalu Ganga) | 4.25 | 🟡 Alert | 0.080 | 🔺 Rising |
| 2026-10-26 06:03:21 | Rathnapura (Kalu Ganga) | 5.68 | 🟡 Alert | -0.072 |  |
| 2026-10-26 06:03:20 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.040 |  |
| 2026-10-26 06:03:17 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-10-26 06:02:48 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 06:02:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.20 | 🟡 Alert | 0.078 | 🔺 Rising |
| 2026-10-26 06:02:40 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.077 |  |
| 2026-10-26 06:02:33 | Kithulgala (Kelani Ganga) | 2.21 | 🟢 Normal | -0.092 |  |
| 2026-10-26 06:02:24 | Thawalama (Gin Ganga) | 3.25 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-26 06:02:21 | Panadugama (Nilwala Ganga) | 4.82 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-26 06:01:57 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-26 06:01:16 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-26 06:00:55 | Nawalapitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.062 |  |
| 2026-10-26 06:00:54 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.045 |  |
| 2026-10-26 06:00:46 | Moragaswewa (Deduru Oya) | 3.54 | 🟢 Normal | 0.330 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 06:03:28 | Magura (Kalu Ganga) | 4.25 | 🟡 Alert | 0.080 | 🔺 Rising |
| 2026-10-26 06:02:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.20 | 🟡 Alert | 0.078 | 🔺 Rising |
| 2026-10-26 06:03:21 | Rathnapura (Kalu Ganga) | 5.68 | 🟡 Alert | -0.072 |  |
| 2026-10-26 06:00:46 | Moragaswewa (Deduru Oya) | 3.54 | 🟢 Normal | 0.330 | 🔺 Rising |
| 2026-10-26 06:05:32 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-10-26 06:03:17 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-10-26 06:08:27 | Badalgama (Maha Oya) | 4.05 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-26 06:08:04 | Hanwella (Kelani Ganga) | 4.23 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-26 06:07:20 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-26 06:02:24 | Thawalama (Gin Ganga) | 3.25 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-26 06:08:13 | Baddegama (Gin Ganga) | 2.68 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-26 06:08:38 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-26 06:01:16 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-26 06:38:46 | Galgamuwa (Mee Oya) | 2.26 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-10-26 06:02:21 | Panadugama (Nilwala Ganga) | 4.82 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-26 06:02:48 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 06:05:44 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 06:12:45 | Horowpothana (Yan Oya) | 2.34 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-26 06:03:57 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-26 06:16:29 | Dunamale (Aththanagalu Oya) | 3.13 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:02:16 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-10-26 06:06:10 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-10-26 06:01:57 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-26 06:06:17 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | -0.013 |  |
| 2026-10-26 06:03:42 | Ellagawa (Kalu Ganga) | 8.19 | 🟢 Normal | -0.019 |  |
| 2026-10-26 06:07:11 | Pitabeddara (Nilwala Ganga) | 1.88 | 🟢 Normal | -0.021 |  |
| 2026-10-26 06:04:50 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | -0.021 |  |
| 2026-10-26 06:06:31 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.028 |  |
| 2026-10-26 06:03:20 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.040 |  |
| 2026-10-26 06:06:41 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | -0.040 |  |
| 2026-10-26 06:00:54 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.045 |  |
| 2026-10-26 06:06:11 | Norwood (Kelani Ganga) | 1.47 | 🟢 Normal | -0.053 |  |
| 2026-10-26 06:00:55 | Nawalapitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.062 |  |
| 2026-10-26 06:02:40 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.077 |  |
| 2026-10-26 06:06:10 | Glencourse (Kelani Ganga) | 12.38 | 🟢 Normal | -0.086 |  |
| 2026-10-26 06:02:33 | Kithulgala (Kelani Ganga) | 2.21 | 🟢 Normal | -0.092 |  |
| 2026-10-26 06:05:03 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | -0.096 |  |
| 2026-10-26 06:07:17 | Giriulla (Maha Oya) | 3.08 | 🟢 Normal | -0.103 |  |
| 2026-10-26 06:04:35 | Peradeniya (Mahaweli Ganga) | 3.39 | 🟢 Normal | -0.255 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)