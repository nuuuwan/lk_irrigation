# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--15_13:07:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **261,573 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 13:07:33 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-09-15 13:07:26 | Magura (Kalu Ganga) | 4.84 | 🟡 Alert | -0.039 |  |
| 2026-09-15 13:06:55 | Peradeniya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.065 |  |
| 2026-09-15 13:06:31 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-15 13:06:27 | Ellagawa (Kalu Ganga) | 5.94 | 🟢 Normal | -0.103 |  |
| 2026-09-15 13:06:11 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-15 13:06:07 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-09-15 13:05:41 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-15 13:05:27 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-15 13:05:02 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-09-15 13:04:17 | Thanthirimale (Malwathu Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-09-15 13:03:44 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | -0.089 |  |
| 2026-09-15 13:03:14 | Hanwella (Kelani Ganga) | 2.80 | 🟢 Normal | -0.099 |  |
| 2026-09-15 13:02:51 | Dunamale (Aththanagalu Oya) | 3.28 | 🟢 Normal | -0.021 |  |
| 2026-09-15 13:02:31 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-09-15 13:02:26 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-09-15 13:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-15 13:02:20 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-15 13:02:11 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 13:02:05 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | -0.031 |  |
| 2026-09-15 13:02:02 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 13:01:58 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-09-15 13:01:55 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 13:01:55 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-15 13:01:50 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.011 |  |
| 2026-09-15 13:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-09-15 13:01:20 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-15 13:01:18 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 13:01:14 | Manampitiya (Mahaweli Ganga) | -0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-15 13:01:12 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.061 |  |
| 2026-09-15 13:00:58 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 13:07:26 | Magura (Kalu Ganga) | 4.84 | 🟡 Alert | -0.039 |  |
| 2026-09-15 13:06:07 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-09-15 12:15:47 | Baddegama (Gin Ganga) | 3.20 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-09-15 13:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-15 13:02:20 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-15 13:06:11 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-15 13:01:18 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 13:02:11 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 13:02:02 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 13:07:33 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-09-15 12:00:41 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 13:01:55 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 13:06:31 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-15 13:00:58 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-15 13:01:20 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-15 13:01:55 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-15 13:05:41 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-15 13:05:02 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-09-15 13:01:14 | Manampitiya (Mahaweli Ganga) | -0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-15 13:05:27 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-15 13:02:31 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-09-15 13:04:17 | Thanthirimale (Malwathu Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-09-15 13:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-09-15 12:05:45 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-09-15 13:02:26 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-09-15 13:01:50 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.011 |  |
| 2026-09-15 13:01:58 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-09-15 12:03:20 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-09-15 13:02:51 | Dunamale (Aththanagalu Oya) | 3.28 | 🟢 Normal | -0.021 |  |
| 2026-09-15 13:02:05 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | -0.031 |  |
| 2026-09-15 12:05:33 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.041 |  |
| 2026-09-15 12:13:21 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.053 |  |
| 2026-09-15 13:01:12 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.061 |  |
| 2026-09-15 13:06:55 | Peradeniya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.065 |  |
| 2026-09-15 13:03:44 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | -0.089 |  |
| 2026-09-15 13:03:14 | Hanwella (Kelani Ganga) | 2.80 | 🟢 Normal | -0.099 |  |
| 2026-09-15 13:06:27 | Ellagawa (Kalu Ganga) | 5.94 | 🟢 Normal | -0.103 |  |
| 2026-09-15 12:05:26 | Panadugama (Nilwala Ganga) | 4.02 | 🟢 Normal | -0.125 |  |
| 2026-09-15 12:05:40 | Glencourse (Kelani Ganga) | 10.58 | 🟢 Normal | -0.134 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)