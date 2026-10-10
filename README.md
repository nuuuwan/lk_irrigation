# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--10_06:32:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **283,802 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 06:32:12 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.005 |  |
| 2026-10-10 06:20:27 | Rathnapura (Kalu Ganga) | 3.21 | 🟢 Normal | -0.063 |  |
| 2026-10-10 06:13:34 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-10 06:12:10 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-10 06:08:59 | Panadugama (Nilwala Ganga) | 4.59 | 🟢 Normal | -0.067 |  |
| 2026-10-10 06:08:40 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | -0.220 |  |
| 2026-10-10 06:07:26 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | -0.040 |  |
| 2026-10-10 06:06:23 | Ellagawa (Kalu Ganga) | 7.06 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-10 06:06:08 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.127 |  |
| 2026-10-10 06:06:05 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | -0.081 |  |
| 2026-10-10 06:05:32 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.087 |  |
| 2026-10-10 06:05:26 | Moragaswewa (Deduru Oya) | 2.51 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-10 06:04:38 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-10-10 06:04:28 | Baddegama (Gin Ganga) | 2.43 | 🟢 Normal | -0.025 |  |
| 2026-10-10 06:04:19 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-10 06:04:17 | Peradeniya (Mahaweli Ganga) | 3.48 | 🟢 Normal | -0.019 |  |
| 2026-10-10 06:04:08 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-10 06:03:57 | Glencourse (Kelani Ganga) | 11.52 | 🟢 Normal | -0.180 |  |
| 2026-10-10 06:03:46 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-10-10 06:03:44 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 06:03:41 | Badalgama (Maha Oya) | 4.71 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-10-10 06:03:32 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-10 06:03:25 | Dunamale (Aththanagalu Oya) | 3.36 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-10-10 06:03:18 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.031 |  |
| 2026-10-10 06:03:11 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.072 |  |
| 2026-10-10 06:02:47 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-10-10 06:02:46 | Hanwella (Kelani Ganga) | 3.89 | 🟢 Normal | -0.095 |  |
| 2026-10-10 06:02:25 | Giriulla (Maha Oya) | 4.21 | 🟢 Normal | -0.135 |  |
| 2026-10-10 06:02:01 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-10 06:01:57 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-10-10 06:01:55 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.081 |  |
| 2026-10-10 06:01:21 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-10 06:01:12 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.050 |  |
| 2026-10-10 06:01:06 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-10 06:00:37 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-10 05:58:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | -0.065 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 06:03:25 | Dunamale (Aththanagalu Oya) | 3.36 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-10-10 06:03:41 | Badalgama (Maha Oya) | 4.71 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-10-10 06:04:38 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-10-10 06:12:10 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-10 06:05:26 | Moragaswewa (Deduru Oya) | 2.51 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-10 06:04:08 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-10 06:06:23 | Ellagawa (Kalu Ganga) | 7.06 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-10 06:02:01 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-10 06:00:37 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-10 06:32:12 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.005 |  |
| 2026-10-10 06:01:21 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-10 05:05:12 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-10 06:03:44 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 06:13:34 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-10 05:03:17 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-10 06:02:47 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-10-10 06:01:06 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:01:04 | Thanthirimale (Malwathu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-10 06:04:19 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-10 06:03:46 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-10-10 06:01:57 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-10-10 05:11:47 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | -0.019 |  |
| 2026-10-10 06:04:17 | Peradeniya (Mahaweli Ganga) | 3.48 | 🟢 Normal | -0.019 |  |
| 2026-10-10 06:04:28 | Baddegama (Gin Ganga) | 2.43 | 🟢 Normal | -0.025 |  |
| 2026-10-10 06:03:18 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.031 |  |
| 2026-10-10 06:07:26 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | -0.040 |  |
| 2026-10-10 06:01:12 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.050 |  |
| 2026-10-10 06:20:27 | Rathnapura (Kalu Ganga) | 3.21 | 🟢 Normal | -0.063 |  |
| 2026-10-10 05:58:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | -0.065 |  |
| 2026-10-10 06:08:59 | Panadugama (Nilwala Ganga) | 4.59 | 🟢 Normal | -0.067 |  |
| 2026-10-10 06:03:11 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.072 |  |
| 2026-10-10 06:01:55 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.081 |  |
| 2026-10-10 06:06:05 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | -0.081 |  |
| 2026-10-10 06:05:32 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.087 |  |
| 2026-10-10 06:02:46 | Hanwella (Kelani Ganga) | 3.89 | 🟢 Normal | -0.095 |  |
| 2026-10-10 06:06:08 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.127 |  |
| 2026-10-10 06:02:25 | Giriulla (Maha Oya) | 4.21 | 🟢 Normal | -0.135 |  |
| 2026-10-10 06:03:57 | Glencourse (Kelani Ganga) | 11.52 | 🟢 Normal | -0.180 |  |
| 2026-10-10 06:08:40 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | -0.220 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)