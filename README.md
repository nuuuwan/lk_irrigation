# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--26_08:13:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **298,284 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Rathnapura — Alert; 🟡 Norwood — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 08:13:57 | Urawa (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-10-26 08:10:54 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-26 08:10:42 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-26 08:09:06 | Kithulgala (Kelani Ganga) | 2.39 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-10-26 08:08:18 | Moragaswewa (Deduru Oya) | 3.97 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-10-26 08:07:53 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-26 08:07:33 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-26 08:07:29 | Panadugama (Nilwala Ganga) | 4.83 | 🟢 Normal | 135.900 | 🔺 Rising |
| 2026-10-26 08:07:22 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-26 08:07:13 | Giriulla (Maha Oya) | 3.04 | 🟢 Normal | -0.019 |  |
| 2026-10-26 08:06:58 | Baddegama (Gin Ganga) | 2.72 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-26 08:06:53 | Pitabeddara (Nilwala Ganga) | 1.83 | 🟢 Normal | -0.031 |  |
| 2026-10-26 08:06:26 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-10-26 08:06:09 | Panadugama (Nilwala Ganga) | 1.81 | 🟢 Normal | 135.900 | 🔺 Rising |
| 2026-10-26 08:06:05 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-26 08:06:00 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-26 08:06:00 | Hanwella (Kelani Ganga) | 4.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-26 08:05:51 | Ellagawa (Kalu Ganga) | 8.36 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-10-26 08:05:43 | Thawalama (Gin Ganga) | 3.12 | 🟢 Normal | -0.070 |  |
| 2026-10-26 08:05:24 | Galgamuwa (Mee Oya) | 2.42 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-10-26 08:05:18 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.028 |  |
| 2026-10-26 08:05:06 | Glencourse (Kelani Ganga) | 12.15 | 🟢 Normal | -0.010 |  |
| 2026-10-26 08:05:02 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.032 |  |
| 2026-10-26 08:04:56 | Putupaula (Kalu Ganga) | 2.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-26 08:04:13 | Magura (Kalu Ganga) | 4.30 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-26 08:04:03 | Rathnapura (Kalu Ganga) | 5.74 | 🟡 Alert | 0.125 | 🔺 Rising |
| 2026-10-26 08:03:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.45 | 🟡 Alert | 0.192 | 🔺 Rising |
| 2026-10-26 08:03:41 | Badalgama (Maha Oya) | 4.12 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-26 08:03:33 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-26 08:03:20 | Norwood (Kelani Ganga) | 1.52 | 🟡 Alert | 0.049 | 🔺 Rising |
| 2026-10-26 08:02:53 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-26 08:02:45 | Dunamale (Aththanagalu Oya) | 3.14 | 🟢 Normal | 0.000 |  |
| 2026-10-26 08:02:42 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-10-26 08:02:28 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-26 08:02:16 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.063 |  |
| 2026-10-26 08:02:08 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.108 |  |
| 2026-10-26 08:02:03 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-10-26 08:01:32 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-26 08:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-10-26 08:01:25 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 08:03:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.45 | 🟡 Alert | 0.192 | 🔺 Rising |
| 2026-10-26 08:04:03 | Rathnapura (Kalu Ganga) | 5.74 | 🟡 Alert | 0.125 | 🔺 Rising |
| 2026-10-26 08:03:20 | Norwood (Kelani Ganga) | 1.52 | 🟡 Alert | 0.049 | 🔺 Rising |
| 2026-10-26 08:04:13 | Magura (Kalu Ganga) | 4.30 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-26 08:07:29 | Panadugama (Nilwala Ganga) | 4.83 | 🟢 Normal | 135.900 | 🔺 Rising |
| 2026-10-26 08:08:18 | Moragaswewa (Deduru Oya) | 3.97 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-10-26 08:02:03 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-10-26 08:06:26 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-10-26 08:09:06 | Kithulgala (Kelani Ganga) | 2.39 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-10-26 08:05:51 | Ellagawa (Kalu Ganga) | 8.36 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-10-26 08:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-10-26 08:05:24 | Galgamuwa (Mee Oya) | 2.42 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-10-26 08:03:33 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-26 08:07:22 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-26 08:02:28 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-26 08:07:33 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-26 08:06:58 | Baddegama (Gin Ganga) | 2.72 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-26 08:04:56 | Putupaula (Kalu Ganga) | 2.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-26 08:07:53 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-26 08:03:41 | Badalgama (Maha Oya) | 4.12 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-26 08:06:00 | Hanwella (Kelani Ganga) | 4.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-26 08:02:53 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-26 08:10:42 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-26 08:02:45 | Dunamale (Aththanagalu Oya) | 3.14 | 🟢 Normal | 0.000 |  |
| 2026-10-26 08:01:25 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-26 08:06:00 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-26 08:10:54 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-26 08:06:05 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-26 08:01:32 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-26 08:02:42 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-10-26 08:05:06 | Glencourse (Kelani Ganga) | 12.15 | 🟢 Normal | -0.010 |  |
| 2026-10-26 08:13:57 | Urawa (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-10-26 08:07:13 | Giriulla (Maha Oya) | 3.04 | 🟢 Normal | -0.019 |  |
| 2026-10-26 08:05:18 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.028 |  |
| 2026-10-26 08:06:53 | Pitabeddara (Nilwala Ganga) | 1.83 | 🟢 Normal | -0.031 |  |
| 2026-10-26 08:05:02 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.032 |  |
| 2026-10-26 08:02:16 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.063 |  |
| 2026-10-26 08:05:43 | Thawalama (Gin Ganga) | 3.12 | 🟢 Normal | -0.070 |  |
| 2026-10-26 08:02:08 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.108 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)