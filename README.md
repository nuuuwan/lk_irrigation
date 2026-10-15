# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--15_23:30:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **288,968 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Thawalama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 23:30:01 | Moragaswewa (Deduru Oya) | 2.71 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-10-15 23:18:41 | Ellagawa (Kalu Ganga) | 7.70 | 🟢 Normal | -0.071 |  |
| 2026-10-15 23:11:16 | Rathnapura (Kalu Ganga) | 3.26 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-10-15 23:10:50 | Putupaula (Kalu Ganga) | 2.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 23:10:45 | Thawalama (Gin Ganga) | 4.02 | 🟡 Alert | -0.038 |  |
| 2026-10-15 23:08:57 | Pitabeddara (Nilwala Ganga) | 4.71 | 🟡 Alert | -0.047 |  |
| 2026-10-15 23:08:26 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | -0.048 |  |
| 2026-10-15 23:07:48 | Baddegama (Gin Ganga) | 2.85 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-15 23:07:26 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-15 23:07:16 | Giriulla (Maha Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-10-15 23:06:43 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-15 23:06:21 | Magura (Kalu Ganga) | 3.92 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-15 23:06:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.85 | 🟡 Alert | 0.000 |  |
| 2026-10-15 23:05:07 | Glencourse (Kelani Ganga) | 11.39 | 🟢 Normal | -0.010 |  |
| 2026-10-15 23:04:52 | Badalgama (Maha Oya) | 3.42 | 🟢 Normal | -0.010 |  |
| 2026-10-15 23:04:42 | Panadugama (Nilwala Ganga) | 6.54 | 🟠 Minor Flood | 0.060 | 🔺 Rising |
| 2026-10-15 23:04:41 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 23:04:35 | Manampitiya (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 23:04:33 | Holombuwa (Kelani Ganga) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 23:04:17 | Norwood (Kelani Ganga) | 1.44 | 🟢 Normal | -0.042 |  |
| 2026-10-15 23:04:15 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-15 23:04:02 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-15 23:03:55 | Dunamale (Aththanagalu Oya) | 3.81 | 🟡 Alert | 0.000 |  |
| 2026-10-15 23:03:39 | Urawa (Nilwala Ganga) | 2.62 | 🟡 Alert | -0.052 |  |
| 2026-10-15 23:03:35 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-15 23:03:35 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-15 23:03:17 | Katharagama (Menik Ganga) | 0.20 | 🟢 Normal | -0.011 |  |
| 2026-10-15 23:03:04 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-15 23:02:24 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | -0.030 |  |
| 2026-10-15 23:02:18 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 23:02:18 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-10-15 23:02:11 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-15 23:02:11 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-10-15 23:01:57 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-15 23:01:28 | Moraketiya (Walawe Ganga) | 2.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 23:01:04 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-10-15 22:59:18 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 23:04:42 | Panadugama (Nilwala Ganga) | 6.54 | 🟠 Minor Flood | 0.060 | 🔺 Rising |
| 2026-10-15 23:01:57 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-15 23:03:55 | Dunamale (Aththanagalu Oya) | 3.81 | 🟡 Alert | 0.000 |  |
| 2026-10-15 23:06:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.85 | 🟡 Alert | 0.000 |  |
| 2026-10-15 23:10:45 | Thawalama (Gin Ganga) | 4.02 | 🟡 Alert | -0.038 |  |
| 2026-10-15 23:08:57 | Pitabeddara (Nilwala Ganga) | 4.71 | 🟡 Alert | -0.047 |  |
| 2026-10-15 23:03:39 | Urawa (Nilwala Ganga) | 2.62 | 🟡 Alert | -0.052 |  |
| 2026-10-15 23:11:16 | Rathnapura (Kalu Ganga) | 3.26 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-10-15 18:04:44 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-15 23:30:01 | Moragaswewa (Deduru Oya) | 2.71 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-10-15 23:06:21 | Magura (Kalu Ganga) | 3.92 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-15 23:07:48 | Baddegama (Gin Ganga) | 2.85 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-15 23:02:11 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-15 23:10:50 | Putupaula (Kalu Ganga) | 2.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 23:01:28 | Moraketiya (Walawe Ganga) | 2.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 23:02:18 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 23:04:02 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-15 18:18:48 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-15 23:04:33 | Holombuwa (Kelani Ganga) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 23:04:41 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 23:04:35 | Manampitiya (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 23:03:35 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-15 18:02:23 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-10-15 23:06:43 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-15 23:03:04 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-15 23:07:16 | Giriulla (Maha Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-10-15 23:01:04 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-10-15 23:07:26 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-15 23:03:35 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-15 23:04:15 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-15 23:05:07 | Glencourse (Kelani Ganga) | 11.39 | 🟢 Normal | -0.010 |  |
| 2026-10-15 23:04:52 | Badalgama (Maha Oya) | 3.42 | 🟢 Normal | -0.010 |  |
| 2026-10-15 23:02:11 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-10-15 23:03:17 | Katharagama (Menik Ganga) | 0.20 | 🟢 Normal | -0.011 |  |
| 2026-10-15 23:02:18 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-10-15 23:02:24 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | -0.030 |  |
| 2026-10-15 23:04:17 | Norwood (Kelani Ganga) | 1.44 | 🟢 Normal | -0.042 |  |
| 2026-10-15 23:08:26 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | -0.048 |  |
| 2026-10-15 23:18:41 | Ellagawa (Kalu Ganga) | 7.70 | 🟢 Normal | -0.071 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)