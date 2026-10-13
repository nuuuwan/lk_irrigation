# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--13_23:08:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **287,134 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Panadugama — Alert; 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 23:08:14 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-10-13 23:07:16 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 23:07:03 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | -0.010 |  |
| 2026-10-13 23:06:11 | Nagalagam Street (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-13 23:05:42 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-13 23:05:39 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.363 |  |
| 2026-10-13 23:05:06 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-10-13 23:05:05 | Putupaula (Kalu Ganga) | 1.75 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-13 23:05:04 | Urawa (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.301 |  |
| 2026-10-13 23:04:22 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-13 23:04:21 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.019 |  |
| 2026-10-13 23:03:53 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-13 23:03:50 | Giriulla (Maha Oya) | 1.57 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-13 23:03:43 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-13 23:03:37 | Glencourse (Kelani Ganga) | 11.11 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-10-13 23:03:26 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | 0.000 |  |
| 2026-10-13 23:03:26 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-13 23:03:05 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-13 23:02:58 | Moraketiya (Walawe Ganga) | 1.87 | 🟢 Normal | -0.040 |  |
| 2026-10-13 23:02:35 | Thawalama (Gin Ganga) | 3.57 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-10-13 23:02:21 | Ellagawa (Kalu Ganga) | 7.42 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-13 23:02:15 | Hanwella (Kelani Ganga) | 3.06 | 🟢 Normal | -0.030 |  |
| 2026-10-13 23:02:07 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-10-13 23:01:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.00 | 🟡 Alert | 0.000 |  |
| 2026-10-13 23:01:26 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-13 23:01:24 | Pitabeddara (Nilwala Ganga) | 3.10 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-10-13 23:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-10-13 23:01:05 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-10-13 23:00:53 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-10-13 23:00:09 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-13 22:59:24 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-13 22:45:25 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 22:05:29 | Magura (Kalu Ganga) | 4.56 | 🟡 Alert | 0.337 | 🔺 Rising |
| 2026-10-13 22:02:16 | Panadugama (Nilwala Ganga) | 5.79 | 🟡 Alert | 0.095 | 🔺 Rising |
| 2026-10-13 22:04:19 | Thalgahagoda (Nilwala Ganga) | 1.63 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-10-13 23:01:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.00 | 🟡 Alert | 0.000 |  |
| 2026-10-13 23:02:35 | Thawalama (Gin Ganga) | 3.57 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-10-13 22:05:58 | Rathnapura (Kalu Ganga) | 4.15 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-10-13 23:01:24 | Pitabeddara (Nilwala Ganga) | 3.10 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-10-13 23:03:37 | Glencourse (Kelani Ganga) | 11.11 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-10-13 23:05:06 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-10-13 23:08:14 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-10-13 23:03:26 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-13 23:03:50 | Giriulla (Maha Oya) | 1.57 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-13 23:02:21 | Ellagawa (Kalu Ganga) | 7.42 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-13 23:05:05 | Putupaula (Kalu Ganga) | 1.75 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-13 23:07:16 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 23:04:22 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-13 23:03:05 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-13 22:01:11 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-10-13 23:00:53 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-10-13 22:04:43 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 23:00:09 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:05:16 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-13 23:03:43 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-13 23:06:11 | Nagalagam Street (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-13 23:01:26 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-13 23:03:53 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-13 23:05:42 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-13 23:03:26 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:04:16 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-13 23:07:03 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | -0.010 |  |
| 2026-10-13 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.010 |  |
| 2026-10-13 23:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-10-13 23:04:21 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.019 |  |
| 2026-10-13 23:02:07 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-10-13 23:01:05 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-10-13 23:02:15 | Hanwella (Kelani Ganga) | 3.06 | 🟢 Normal | -0.030 |  |
| 2026-10-13 23:02:58 | Moraketiya (Walawe Ganga) | 1.87 | 🟢 Normal | -0.040 |  |
| 2026-10-13 23:05:04 | Urawa (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.301 |  |
| 2026-10-13 23:05:39 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.363 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)