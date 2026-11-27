# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--27_20:03:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **327,342 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 20:03:26 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-27 20:03:19 | Ellagawa (Kalu Ganga) | 6.94 | 🟢 Normal | 0.335 | 🔺 Rising |
| 2026-11-27 20:03:08 | Giriulla (Maha Oya) | 3.21 | 🟢 Normal | 0.000 |  |
| 2026-11-27 20:02:55 | Katharagama (Menik Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-11-27 20:02:50 | Pitabeddara (Nilwala Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-11-27 20:02:44 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-27 20:02:44 | Dunamale (Aththanagalu Oya) | 3.46 | 🟡 Alert | -0.041 |  |
| 2026-11-27 20:02:13 | Kuda Oya (Kirindi Oya) | 2.48 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-27 20:02:07 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.233 |  |
| 2026-11-27 20:02:06 | Thawalama (Gin Ganga) | 2.39 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-27 20:01:50 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-11-27 20:01:47 | Manampitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.060 |  |
| 2026-11-27 20:01:36 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-27 20:01:31 | Thaldena (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.707 | 🔺 Rising |
| 2026-11-27 20:00:56 | Magura (Kalu Ganga) | 3.55 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-27 20:00:11 | Wellawaya (Kirindi Oya) | 1.87 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 19:02:40 | Moraketiya (Walawe Ganga) | 3.42 | 🟡 Alert | 0.223 | 🔺 Rising |
| 2026-11-27 19:04:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.25 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-27 20:02:44 | Dunamale (Aththanagalu Oya) | 3.46 | 🟡 Alert | -0.041 |  |
| 2026-11-27 19:17:44 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-11-27 19:08:26 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | 0.872 | 🔺 Rising |
| 2026-11-27 20:01:31 | Thaldena (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.707 | 🔺 Rising |
| 2026-11-27 19:06:54 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.352 | 🔺 Rising |
| 2026-11-27 20:03:19 | Ellagawa (Kalu Ganga) | 6.94 | 🟢 Normal | 0.335 | 🔺 Rising |
| 2026-11-27 19:05:35 | Rathnapura (Kalu Ganga) | 3.47 | 🟢 Normal | 0.297 | 🔺 Rising |
| 2026-11-27 19:06:34 | Holombuwa (Kelani Ganga) | 1.70 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-11-27 20:02:13 | Kuda Oya (Kirindi Oya) | 2.48 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-27 20:00:56 | Magura (Kalu Ganga) | 3.55 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-27 20:02:06 | Thawalama (Gin Ganga) | 2.39 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-27 19:04:34 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-27 19:02:28 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-27 20:01:36 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-27 20:02:44 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-27 20:03:26 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-27 20:03:08 | Giriulla (Maha Oya) | 3.21 | 🟢 Normal | 0.000 |  |
| 2026-11-27 18:04:37 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-27 20:02:50 | Pitabeddara (Nilwala Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-11-27 20:02:55 | Katharagama (Menik Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-11-27 19:02:33 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-27 20:00:11 | Wellawaya (Kirindi Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-11-27 19:08:57 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-11-27 20:01:50 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-11-27 19:06:33 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | -0.028 |  |
| 2026-11-27 19:01:28 | Thanamalwila (Kirindi Oya) | 1.99 | 🟢 Normal | -0.030 |  |
| 2026-11-27 18:01:42 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.031 |  |
| 2026-11-27 19:08:04 | Moragaswewa (Deduru Oya) | 3.21 | 🟢 Normal | -0.040 |  |
| 2026-11-27 18:00:16 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | -0.041 |  |
| 2026-11-27 19:04:24 | Peradeniya (Mahaweli Ganga) | 3.95 | 🟢 Normal | -0.048 |  |
| 2026-11-27 19:07:00 | Putupaula (Kalu Ganga) | 1.49 | 🟢 Normal | -0.055 |  |
| 2026-11-27 20:01:47 | Manampitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.060 |  |
| 2026-11-27 19:03:24 | Badalgama (Maha Oya) | 4.22 | 🟢 Normal | -0.071 |  |
| 2026-11-27 19:05:16 | Panadugama (Nilwala Ganga) | 4.05 | 🟢 Normal | -0.081 |  |
| 2026-11-27 19:06:25 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.086 |  |
| 2026-11-27 19:05:26 | Hanwella (Kelani Ganga) | 2.74 | 🟢 Normal | -0.097 |  |
| 2026-11-27 20:02:07 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.233 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)