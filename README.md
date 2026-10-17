# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--18_00:06:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **290,796 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Norwood — Alert; 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 00:06:22 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.009 |  |
| 2026-10-18 00:06:19 | Ellagawa (Kalu Ganga) | 7.33 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-10-18 00:06:00 | Peradeniya (Mahaweli Ganga) | 4.38 | 🟢 Normal | 0.959 | 🔺 Rising |
| 2026-10-18 00:04:40 | Thawalama (Gin Ganga) | 3.86 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-10-18 00:04:27 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-10-18 00:04:27 | Norwood (Kelani Ganga) | 1.51 | 🟡 Alert | -0.087 |  |
| 2026-10-18 00:04:15 | Urawa (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-18 00:04:09 | Hanwella (Kelani Ganga) | 3.94 | 🟢 Normal | 0.431 | 🔺 Rising |
| 2026-10-18 00:03:57 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | -0.201 |  |
| 2026-10-18 00:03:42 | Dunamale (Aththanagalu Oya) | 2.72 | 🟢 Normal | -0.050 |  |
| 2026-10-18 00:03:35 | Pitabeddara (Nilwala Ganga) | 3.49 | 🟢 Normal | 0.000 |  |
| 2026-10-18 00:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.44 | 🟡 Alert | -0.023 |  |
| 2026-10-18 00:03:28 | Panadugama (Nilwala Ganga) | 6.20 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-10-18 00:03:16 | Thaldena (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.111 |  |
| 2026-10-18 00:03:10 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | -0.021 |  |
| 2026-10-18 00:02:48 | Glencourse (Kelani Ganga) | 13.30 | 🟢 Normal | 0.000 |  |
| 2026-10-18 00:02:41 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-18 00:02:34 | Moragaswewa (Deduru Oya) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-10-18 00:02:25 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.032 |  |
| 2026-10-18 00:02:22 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.169 |  |
| 2026-10-18 00:02:06 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-10-18 00:02:06 | Baddegama (Gin Ganga) | 3.13 | 🟢 Normal | -0.020 |  |
| 2026-10-18 00:01:55 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-18 00:01:52 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-10-18 00:01:46 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-18 00:01:45 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.179 |  |
| 2026-10-18 00:00:26 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 00:03:28 | Panadugama (Nilwala Ganga) | 6.20 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-10-17 23:03:38 | Thalgahagoda (Nilwala Ganga) | 2.02 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 00:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.44 | 🟡 Alert | -0.023 |  |
| 2026-10-18 00:04:27 | Norwood (Kelani Ganga) | 1.51 | 🟡 Alert | -0.087 |  |
| 2026-10-17 23:03:11 | Rathnapura (Kalu Ganga) | 6.17 | 🟡 Alert | -0.128 |  |
| 2026-10-18 00:06:00 | Peradeniya (Mahaweli Ganga) | 4.38 | 🟢 Normal | 0.959 | 🔺 Rising |
| 2026-10-18 00:04:09 | Hanwella (Kelani Ganga) | 3.94 | 🟢 Normal | 0.431 | 🔺 Rising |
| 2026-10-18 00:02:06 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-10-18 00:04:40 | Thawalama (Gin Ganga) | 3.86 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-10-18 00:06:19 | Ellagawa (Kalu Ganga) | 7.33 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-10-17 23:03:48 | Moraketiya (Walawe Ganga) | 1.55 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-17 23:04:37 | Horowpothana (Yan Oya) | 2.82 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-17 23:03:34 | Manampitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-18 00:04:15 | Urawa (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 18:02:22 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-10-18 00:00:26 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-10-18 00:01:46 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-18 00:02:41 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-18 00:03:35 | Pitabeddara (Nilwala Ganga) | 3.49 | 🟢 Normal | 0.000 |  |
| 2026-10-18 00:02:48 | Glencourse (Kelani Ganga) | 13.30 | 🟢 Normal | 0.000 |  |
| 2026-10-17 23:07:56 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-18 00:01:55 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-17 23:07:11 | Putupaula (Kalu Ganga) | 2.07 | 🟢 Normal | -0.009 |  |
| 2026-10-18 00:06:22 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.009 |  |
| 2026-10-17 21:21:56 | Galgamuwa (Mee Oya) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-10-18 00:01:52 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-10-18 00:04:27 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-10-18 00:02:34 | Moragaswewa (Deduru Oya) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-10-18 00:02:06 | Baddegama (Gin Ganga) | 3.13 | 🟢 Normal | -0.020 |  |
| 2026-10-18 00:03:10 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | -0.021 |  |
| 2026-10-18 00:02:25 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.032 |  |
| 2026-10-17 23:04:02 | Magura (Kalu Ganga) | 2.59 | 🟢 Normal | -0.033 |  |
| 2026-10-17 18:01:56 | Thanthirimale (Malwathu Oya) | 2.41 | 🟢 Normal | -0.040 |  |
| 2026-10-18 00:03:42 | Dunamale (Aththanagalu Oya) | 2.72 | 🟢 Normal | -0.050 |  |
| 2026-10-18 00:03:16 | Thaldena (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.111 |  |
| 2026-10-18 00:02:22 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.169 |  |
| 2026-10-18 00:01:45 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.179 |  |
| 2026-10-18 00:03:57 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | -0.201 |  |
| 2026-10-17 23:07:04 | Holombuwa (Kelani Ganga) | 2.16 | 🟢 Normal | -0.526 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)