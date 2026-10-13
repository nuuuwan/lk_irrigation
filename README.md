# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--13_21:09:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **287,066 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Panadugama — Alert; 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Urawa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 21:09:59 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-13 21:09:49 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 21:08:38 | Thalgahagoda (Nilwala Ganga) | 1.62 | 🟡 Alert | 0.000 |  |
| 2026-10-13 21:07:57 | Hanwella (Kelani Ganga) | 3.15 | 🟢 Normal | -0.037 |  |
| 2026-10-13 21:06:57 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | -0.042 |  |
| 2026-10-13 21:06:53 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-10-13 21:06:05 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-13 21:05:59 | Glencourse (Kelani Ganga) | 10.79 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-10-13 21:05:45 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.042 |  |
| 2026-10-13 21:05:34 | Panadugama (Nilwala Ganga) | 5.70 | 🟡 Alert | 0.037 | 🔺 Rising |
| 2026-10-13 21:04:54 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | -0.011 |  |
| 2026-10-13 21:04:32 | Urawa (Nilwala Ganga) | 2.70 | 🟡 Alert | -0.062 |  |
| 2026-10-13 21:03:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.02 | 🟡 Alert | 0.000 |  |
| 2026-10-13 21:03:47 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 21:03:29 | Peradeniya (Mahaweli Ganga) | 3.16 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-10-13 21:03:15 | Magura (Kalu Ganga) | 4.21 | 🟡 Alert | 0.287 | 🔺 Rising |
| 2026-10-13 21:03:03 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-13 21:03:01 | Thawalama (Gin Ganga) | 3.27 | 🟢 Normal | 0.351 | 🔺 Rising |
| 2026-10-13 21:02:59 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-10-13 21:02:54 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-10-13 21:02:38 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-10-13 21:02:33 | Pitabeddara (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.875 | 🔺 Rising |
| 2026-10-13 21:02:31 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-13 21:02:23 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-13 21:02:19 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-13 21:02:17 | Ellagawa (Kalu Ganga) | 7.34 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-13 21:02:13 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 21:02:08 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-13 21:02:08 | Rathnapura (Kalu Ganga) | 3.95 | 🟢 Normal | 0.355 | 🔺 Rising |
| 2026-10-13 21:02:07 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-10-13 21:02:07 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.082 |  |
| 2026-10-13 21:02:04 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-10-13 21:01:26 | Putupaula (Kalu Ganga) | 1.67 | 🟢 Normal | -0.083 |  |
| 2026-10-13 21:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-13 21:01:05 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-13 21:00:09 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 21:03:15 | Magura (Kalu Ganga) | 4.21 | 🟡 Alert | 0.287 | 🔺 Rising |
| 2026-10-13 21:05:34 | Panadugama (Nilwala Ganga) | 5.70 | 🟡 Alert | 0.037 | 🔺 Rising |
| 2026-10-13 21:08:38 | Thalgahagoda (Nilwala Ganga) | 1.62 | 🟡 Alert | 0.000 |  |
| 2026-10-13 21:03:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.02 | 🟡 Alert | 0.000 |  |
| 2026-10-13 21:04:32 | Urawa (Nilwala Ganga) | 2.70 | 🟡 Alert | -0.062 |  |
| 2026-10-13 21:02:33 | Pitabeddara (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.875 | 🔺 Rising |
| 2026-10-13 21:02:08 | Rathnapura (Kalu Ganga) | 3.95 | 🟢 Normal | 0.355 | 🔺 Rising |
| 2026-10-13 21:03:01 | Thawalama (Gin Ganga) | 3.27 | 🟢 Normal | 0.351 | 🔺 Rising |
| 2026-10-13 21:02:54 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-10-13 21:03:29 | Peradeniya (Mahaweli Ganga) | 3.16 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-10-13 21:05:59 | Glencourse (Kelani Ganga) | 10.79 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-10-13 21:02:17 | Ellagawa (Kalu Ganga) | 7.34 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-13 21:02:19 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-13 21:09:59 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-13 21:03:47 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 21:02:13 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 21:02:04 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-10-13 21:01:05 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-13 21:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-13 21:09:49 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 21:02:23 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:05:16 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-13 21:02:31 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-13 21:06:05 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-13 21:03:03 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-13 21:02:08 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:04:16 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-13 21:02:38 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-10-13 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.010 |  |
| 2026-10-13 21:02:59 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-10-13 21:02:07 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-10-13 21:04:54 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | -0.011 |  |
| 2026-10-13 21:00:09 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.021 |  |
| 2026-10-13 21:06:53 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-10-13 21:07:57 | Hanwella (Kelani Ganga) | 3.15 | 🟢 Normal | -0.037 |  |
| 2026-10-13 21:05:45 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.042 |  |
| 2026-10-13 21:06:57 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | -0.042 |  |
| 2026-10-13 21:02:07 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.082 |  |
| 2026-10-13 21:01:26 | Putupaula (Kalu Ganga) | 1.67 | 🟢 Normal | -0.083 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)