# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--27_12:07:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **327,057 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert; 🟡 Magura — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 12:07:49 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | -0.046 |  |
| 2026-11-27 12:06:14 | Glencourse (Kelani Ganga) | 10.93 | 🟢 Normal | -0.068 |  |
| 2026-11-27 12:06:09 | Badalgama (Maha Oya) | 4.76 | 🟢 Normal | -0.069 |  |
| 2026-11-27 12:05:20 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 12:04:56 | Putupaula (Kalu Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-11-27 12:04:39 | Magura (Kalu Ganga) | 4.18 | 🟡 Alert | -0.115 |  |
| 2026-11-27 12:04:33 | Panadugama (Nilwala Ganga) | 4.30 | 🟢 Normal | -0.022 |  |
| 2026-11-27 12:04:23 | Katharagama (Menik Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-11-27 12:04:11 | Galgamuwa (Mee Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-27 12:03:55 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | -0.040 |  |
| 2026-11-27 12:03:42 | Hanwella (Kelani Ganga) | 3.26 | 🟢 Normal | -0.069 |  |
| 2026-11-27 12:03:35 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | -0.065 |  |
| 2026-11-27 12:03:23 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-11-27 12:03:21 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-27 12:03:20 | Moraketiya (Walawe Ganga) | 3.28 | 🟡 Alert | -0.280 |  |
| 2026-11-27 12:03:18 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.066 |  |
| 2026-11-27 12:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.32 | 🟡 Alert | -0.010 |  |
| 2026-11-27 12:03:08 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-11-27 12:03:01 | Nagalagam Street (Kelani Ganga) | 0.53 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-27 12:02:49 | Moragaswewa (Deduru Oya) | 3.37 | 🟢 Normal | -0.032 |  |
| 2026-11-27 12:02:36 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-11-27 12:02:29 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | -0.040 |  |
| 2026-11-27 12:02:23 | Giriulla (Maha Oya) | 3.75 | 🟢 Normal | -0.105 |  |
| 2026-11-27 12:02:19 | Dunamale (Aththanagalu Oya) | 3.94 | 🟡 Alert | -0.020 |  |
| 2026-11-27 12:02:18 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-11-27 12:02:15 | Thanamalwila (Kirindi Oya) | 2.32 | 🟢 Normal | -0.080 |  |
| 2026-11-27 12:02:09 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-27 12:02:01 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-11-27 12:01:57 | Rathnapura (Kalu Ganga) | 2.65 | 🟢 Normal | -0.091 |  |
| 2026-11-27 12:01:55 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.025 |  |
| 2026-11-27 12:01:50 | Ellagawa (Kalu Ganga) | 6.68 | 🟢 Normal | -0.041 |  |
| 2026-11-27 12:01:50 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | -0.164 |  |
| 2026-11-27 12:01:37 | Wellawaya (Kirindi Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-11-27 12:01:11 | Peradeniya (Mahaweli Ganga) | 3.53 | 🟢 Normal | -0.082 |  |
| 2026-11-27 12:01:06 | Manampitiya (Mahaweli Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-11-27 12:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-11-27 12:00:43 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-27 12:00:22 | Kuda Oya (Kirindi Oya) | 2.53 | 🟢 Normal | -0.041 |  |
| 2026-11-27 12:00:11 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 12:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.32 | 🟡 Alert | -0.010 |  |
| 2026-11-27 12:02:19 | Dunamale (Aththanagalu Oya) | 3.94 | 🟡 Alert | -0.020 |  |
| 2026-11-27 12:04:39 | Magura (Kalu Ganga) | 4.18 | 🟡 Alert | -0.115 |  |
| 2026-11-27 12:03:20 | Moraketiya (Walawe Ganga) | 3.28 | 🟡 Alert | -0.280 |  |
| 2026-11-27 12:02:01 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-11-27 12:03:01 | Nagalagam Street (Kelani Ganga) | 0.53 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-27 12:02:09 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-27 12:00:43 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-27 12:05:20 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 12:04:11 | Galgamuwa (Mee Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-27 12:02:18 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-11-27 12:01:06 | Manampitiya (Mahaweli Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-11-27 12:03:21 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-27 12:04:56 | Putupaula (Kalu Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-11-27 12:02:36 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-11-27 12:01:37 | Wellawaya (Kirindi Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-11-27 12:04:23 | Katharagama (Menik Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-11-27 12:03:08 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-11-27 12:00:11 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | -0.020 |  |
| 2026-11-27 12:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-11-27 12:03:23 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-11-27 12:04:33 | Panadugama (Nilwala Ganga) | 4.30 | 🟢 Normal | -0.022 |  |
| 2026-11-27 12:01:55 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.025 |  |
| 2026-11-27 12:02:49 | Moragaswewa (Deduru Oya) | 3.37 | 🟢 Normal | -0.032 |  |
| 2026-11-27 12:02:29 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | -0.040 |  |
| 2026-11-27 12:03:55 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | -0.040 |  |
| 2026-11-27 12:01:50 | Ellagawa (Kalu Ganga) | 6.68 | 🟢 Normal | -0.041 |  |
| 2026-11-27 12:00:22 | Kuda Oya (Kirindi Oya) | 2.53 | 🟢 Normal | -0.041 |  |
| 2026-11-27 12:07:49 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | -0.046 |  |
| 2026-11-27 12:03:35 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | -0.065 |  |
| 2026-11-27 12:03:18 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.066 |  |
| 2026-11-27 12:06:14 | Glencourse (Kelani Ganga) | 10.93 | 🟢 Normal | -0.068 |  |
| 2026-11-27 12:06:09 | Badalgama (Maha Oya) | 4.76 | 🟢 Normal | -0.069 |  |
| 2026-11-27 12:03:42 | Hanwella (Kelani Ganga) | 3.26 | 🟢 Normal | -0.069 |  |
| 2026-11-27 12:02:15 | Thanamalwila (Kirindi Oya) | 2.32 | 🟢 Normal | -0.080 |  |
| 2026-11-27 12:01:11 | Peradeniya (Mahaweli Ganga) | 3.53 | 🟢 Normal | -0.082 |  |
| 2026-11-27 12:01:57 | Rathnapura (Kalu Ganga) | 2.65 | 🟢 Normal | -0.091 |  |
| 2026-11-27 12:02:23 | Giriulla (Maha Oya) | 3.75 | 🟢 Normal | -0.105 |  |
| 2026-11-27 12:01:50 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | -0.164 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)