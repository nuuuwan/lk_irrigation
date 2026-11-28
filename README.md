# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--28_05:27:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **327,674 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 05:27:51 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-11-28 05:21:13 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.053 |  |
| 2026-11-28 05:19:14 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-28 05:15:08 | Holombuwa (Kelani Ganga) | 1.60 | 🟢 Normal | -0.093 |  |
| 2026-11-28 05:11:31 | Putupaula (Kalu Ganga) | 1.51 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-11-28 05:11:23 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-28 05:10:06 | Hanwella (Kelani Ganga) | 4.22 | 🟢 Normal | -0.018 |  |
| 2026-11-28 05:08:13 | Panadugama (Nilwala Ganga) | 5.54 | 🟡 Alert | 4.101 | 🔺 Rising |
| 2026-11-28 05:07:12 | Rathnapura (Kalu Ganga) | 2.93 | 🟢 Normal | -0.122 |  |
| 2026-11-28 05:06:59 | Padiyathalawa (Maduru Oya) | 0.71 | 🟢 Normal | -0.023 |  |
| 2026-11-28 05:06:37 | Urawa (Nilwala Ganga) | 1.44 | 🟢 Normal | -0.058 |  |
| 2026-11-28 05:06:03 | Dunamale (Aththanagalu Oya) | 3.90 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-11-28 05:05:43 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-28 05:05:09 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-11-28 05:04:39 | Badalgama (Maha Oya) | 4.53 | 🟢 Normal | -0.019 |  |
| 2026-11-28 05:04:20 | Giriulla (Maha Oya) | 3.25 | 🟢 Normal | -0.100 |  |
| 2026-11-28 05:04:19 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-28 05:03:43 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-11-28 05:03:26 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | -0.050 |  |
| 2026-11-28 05:02:52 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | -0.060 |  |
| 2026-11-28 05:02:35 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-11-28 05:02:04 | Moraketiya (Walawe Ganga) | 3.65 | 🟡 Alert | -0.101 |  |
| 2026-11-28 05:01:57 | Glencourse (Kelani Ganga) | 12.19 | 🟢 Normal | -0.080 |  |
| 2026-11-28 05:01:34 | Moragaswewa (Deduru Oya) | 2.46 | 🟢 Normal | -0.127 |  |
| 2026-11-28 05:01:28 | Ellagawa (Kalu Ganga) | 7.40 | 🟢 Normal | -0.010 |  |
| 2026-11-28 05:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-11-28 05:01:22 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 05:01:08 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-11-28 05:00:59 | Magura (Kalu Ganga) | 3.96 | 🟢 Normal | -0.020 |  |
| 2026-11-28 05:00:44 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.995 | 🔺 Rising |
| 2026-11-28 05:00:16 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-11-28 04:53:00 | Panadugama (Nilwala Ganga) | 4.50 | 🟢 Normal | 4.101 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 05:08:13 | Panadugama (Nilwala Ganga) | 5.54 | 🟡 Alert | 4.101 | 🔺 Rising |
| 2026-11-28 05:06:03 | Dunamale (Aththanagalu Oya) | 3.90 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-11-28 04:01:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | -0.020 |  |
| 2026-11-28 05:02:04 | Moraketiya (Walawe Ganga) | 3.65 | 🟡 Alert | -0.101 |  |
| 2026-11-28 05:00:44 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.995 | 🔺 Rising |
| 2026-11-28 05:11:31 | Putupaula (Kalu Ganga) | 1.51 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-11-28 05:05:09 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-11-28 05:19:14 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-28 04:06:22 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 05:27:51 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-11-27 18:04:37 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-28 05:03:43 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-11-28 05:11:23 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-28 05:05:43 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-28 05:01:22 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 05:01:28 | Ellagawa (Kalu Ganga) | 7.40 | 🟢 Normal | -0.010 |  |
| 2026-11-28 05:02:35 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-11-28 05:00:16 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-11-28 05:01:08 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-11-28 05:10:06 | Hanwella (Kelani Ganga) | 4.22 | 🟢 Normal | -0.018 |  |
| 2026-11-28 05:04:39 | Badalgama (Maha Oya) | 4.53 | 🟢 Normal | -0.019 |  |
| 2026-11-28 05:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-11-28 05:00:59 | Magura (Kalu Ganga) | 3.96 | 🟢 Normal | -0.020 |  |
| 2026-11-28 05:06:59 | Padiyathalawa (Maduru Oya) | 0.71 | 🟢 Normal | -0.023 |  |
| 2026-11-27 18:01:42 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.031 |  |
| 2026-11-27 18:00:16 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | -0.041 |  |
| 2026-11-28 05:03:26 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | -0.050 |  |
| 2026-11-28 05:21:13 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.053 |  |
| 2026-11-28 05:06:37 | Urawa (Nilwala Ganga) | 1.44 | 🟢 Normal | -0.058 |  |
| 2026-11-28 05:02:52 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | -0.060 |  |
| 2026-11-28 05:01:57 | Glencourse (Kelani Ganga) | 12.19 | 🟢 Normal | -0.080 |  |
| 2026-11-28 05:15:08 | Holombuwa (Kelani Ganga) | 1.60 | 🟢 Normal | -0.093 |  |
| 2026-11-28 05:04:20 | Giriulla (Maha Oya) | 3.25 | 🟢 Normal | -0.100 |  |
| 2026-11-28 05:07:12 | Rathnapura (Kalu Ganga) | 2.93 | 🟢 Normal | -0.122 |  |
| 2026-11-28 05:01:34 | Moragaswewa (Deduru Oya) | 2.46 | 🟢 Normal | -0.127 |  |
| 2026-11-28 04:20:50 | Thanamalwila (Kirindi Oya) | 2.88 | 🟢 Normal | -0.187 |  |
| 2026-11-28 04:02:20 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.243 |  |
| 2026-11-28 04:02:57 | Kuda Oya (Kirindi Oya) | 3.18 | 🟢 Normal | -0.270 |  |
| 2026-11-28 03:12:56 | Pitabeddara (Nilwala Ganga) | 1.77 | 🟢 Normal | -0.961 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)