# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--15_12:15:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **261,542 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 12:15:47 | Baddegama (Gin Ganga) | 3.20 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-09-15 12:13:21 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.053 |  |
| 2026-09-15 12:09:46 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 12:08:53 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-15 12:06:57 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-15 12:06:15 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-15 12:06:02 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-09-15 12:05:49 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-15 12:05:46 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-15 12:05:45 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-09-15 12:05:42 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-15 12:05:40 | Glencourse (Kelani Ganga) | 10.58 | 🟢 Normal | -0.134 |  |
| 2026-09-15 12:05:37 | Dunamale (Aththanagalu Oya) | 3.30 | 🟡 Alert | -0.029 |  |
| 2026-09-15 12:05:33 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.041 |  |
| 2026-09-15 12:05:31 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-09-15 12:05:26 | Panadugama (Nilwala Ganga) | 4.02 | 🟢 Normal | -0.125 |  |
| 2026-09-15 12:05:07 | Magura (Kalu Ganga) | 4.88 | 🟡 Alert | -0.039 |  |
| 2026-09-15 12:04:55 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-09-15 12:04:24 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-15 12:03:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.83 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-15 12:03:23 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-15 12:03:20 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-09-15 12:03:18 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | -0.351 |  |
| 2026-09-15 12:03:13 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-09-15 12:03:07 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-09-15 12:02:50 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | -0.092 |  |
| 2026-09-15 12:02:47 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 12:02:47 | Manampitiya (Mahaweli Ganga) | -0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-15 12:02:45 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-09-15 12:02:33 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-15 12:02:29 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | -0.082 |  |
| 2026-09-15 12:02:12 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 12:02:04 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-09-15 12:02:01 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.042 |  |
| 2026-09-15 12:01:43 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.033 |  |
| 2026-09-15 12:01:37 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | -0.011 |  |
| 2026-09-15 12:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-09-15 12:00:41 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 12:05:37 | Dunamale (Aththanagalu Oya) | 3.30 | 🟡 Alert | -0.029 |  |
| 2026-09-15 12:05:07 | Magura (Kalu Ganga) | 4.88 | 🟡 Alert | -0.039 |  |
| 2026-09-15 12:06:02 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-09-15 12:15:47 | Baddegama (Gin Ganga) | 3.20 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-09-15 12:05:46 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-15 12:05:49 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-15 12:03:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.83 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-15 12:02:47 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 12:03:07 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-09-15 12:00:41 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 12:03:23 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-15 12:09:46 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 12:04:55 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-09-15 12:06:57 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-15 12:05:42 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-15 12:06:15 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-15 12:02:33 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-15 12:04:24 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-15 12:05:31 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-09-15 12:02:47 | Manampitiya (Mahaweli Ganga) | -0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-15 12:02:12 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 12:08:53 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-15 11:15:58 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-09-15 12:05:45 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-09-15 12:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-09-15 12:02:45 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-09-15 12:01:37 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | -0.011 |  |
| 2026-09-15 12:03:13 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-09-15 12:03:20 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-09-15 12:02:04 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-09-15 12:01:43 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.033 |  |
| 2026-09-15 12:05:33 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.041 |  |
| 2026-09-15 12:02:01 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.042 |  |
| 2026-09-15 12:13:21 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.053 |  |
| 2026-09-15 12:02:29 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | -0.082 |  |
| 2026-09-15 12:02:50 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | -0.092 |  |
| 2026-09-15 12:05:26 | Panadugama (Nilwala Ganga) | 4.02 | 🟢 Normal | -0.125 |  |
| 2026-09-15 12:05:40 | Glencourse (Kelani Ganga) | 10.58 | 🟢 Normal | -0.134 |  |
| 2026-09-15 12:03:18 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | -0.351 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)