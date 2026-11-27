# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--27_16:03:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **327,192 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 16:03:00 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | -0.041 |  |
| 2026-11-27 16:02:59 | Moragaswewa (Deduru Oya) | 4.29 | 🟢 Normal | 0.954 | 🔺 Rising |
| 2026-11-27 16:02:43 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-11-27 16:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.26 | 🟡 Alert | -0.020 |  |
| 2026-11-27 16:02:30 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-27 16:02:27 | Ellagawa (Kalu Ganga) | 6.48 | 🟢 Normal | -0.079 |  |
| 2026-11-27 16:02:26 | Dunamale (Aththanagalu Oya) | 3.70 | 🟡 Alert | -0.071 |  |
| 2026-11-27 16:02:14 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-11-27 16:02:07 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-27 16:02:02 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 16:02:02 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-27 16:02:01 | Rathnapura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.061 |  |
| 2026-11-27 16:01:44 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-11-27 16:01:38 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-11-27 16:01:08 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-27 16:00:34 | Weraganthota (Mahaweli Ganga) | -1.89 | 🟢 Normal | 0.000 |  |
| 2026-11-27 15:59:26 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-27 15:26:59 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.007 |  |
| 2026-11-27 15:17:21 | Urawa (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-27 15:14:43 | Panadugama (Nilwala Ganga) | 4.24 | 🟢 Normal | 0.000 |  |
| 2026-11-27 15:12:19 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-27 15:11:41 | Magura (Kalu Ganga) | 3.88 | 🟢 Normal | -0.093 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 16:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.26 | 🟡 Alert | -0.020 |  |
| 2026-11-27 15:01:58 | Moraketiya (Walawe Ganga) | 3.05 | 🟡 Alert | -0.022 |  |
| 2026-11-27 16:02:26 | Dunamale (Aththanagalu Oya) | 3.70 | 🟡 Alert | -0.071 |  |
| 2026-11-27 16:02:59 | Moragaswewa (Deduru Oya) | 4.29 | 🟢 Normal | 0.954 | 🔺 Rising |
| 2026-11-27 15:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-11-27 15:04:55 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-27 16:02:30 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-27 15:04:40 | Putupaula (Kalu Ganga) | 1.55 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-27 15:01:24 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-11-27 16:00:34 | Weraganthota (Mahaweli Ganga) | -1.89 | 🟢 Normal | 0.000 |  |
| 2026-11-27 15:01:59 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-27 16:02:02 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 16:02:07 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-27 15:02:45 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-27 16:02:43 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-11-27 15:03:47 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-11-27 15:14:43 | Panadugama (Nilwala Ganga) | 4.24 | 🟢 Normal | 0.000 |  |
| 2026-11-27 15:59:26 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-27 16:01:08 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-27 15:17:21 | Urawa (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-27 16:02:02 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-27 15:02:32 | Kuda Oya (Kirindi Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-11-27 15:26:59 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.007 |  |
| 2026-11-27 15:06:28 | Katharagama (Menik Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-11-27 15:05:22 | Peradeniya (Mahaweli Ganga) | 3.39 | 🟢 Normal | -0.010 |  |
| 2026-11-27 16:01:38 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-11-27 16:02:14 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-11-27 16:01:44 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-11-27 15:06:43 | Holombuwa (Kelani Ganga) | 1.27 | 🟢 Normal | -0.039 |  |
| 2026-11-27 15:03:14 | Thanamalwila (Kirindi Oya) | 2.21 | 🟢 Normal | -0.039 |  |
| 2026-11-27 16:03:00 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | -0.041 |  |
| 2026-11-27 15:02:08 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | -0.043 |  |
| 2026-11-27 15:04:03 | Hanwella (Kelani Ganga) | 3.08 | 🟢 Normal | -0.060 |  |
| 2026-11-27 16:02:01 | Rathnapura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.061 |  |
| 2026-11-27 15:06:39 | Badalgama (Maha Oya) | 4.51 | 🟢 Normal | -0.069 |  |
| 2026-11-27 16:02:27 | Ellagawa (Kalu Ganga) | 6.48 | 🟢 Normal | -0.079 |  |
| 2026-11-27 15:11:41 | Magura (Kalu Ganga) | 3.88 | 🟢 Normal | -0.093 |  |
| 2026-11-27 15:06:57 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | -0.102 |  |
| 2026-11-27 15:03:40 | Giriulla (Maha Oya) | 3.43 | 🟢 Normal | -0.122 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)