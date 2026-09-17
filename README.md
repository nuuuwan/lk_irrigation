# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--17_22:28:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **263,713 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 22:28:05 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:20:25 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:17:39 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-17 22:14:37 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:13:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.22 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-17 22:12:17 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:11:30 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.028 |  |
| 2026-09-17 22:09:03 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:09:01 | Panadugama (Nilwala Ganga) | 4.59 | 🟢 Normal | -0.029 |  |
| 2026-09-17 22:08:14 | Baddegama (Gin Ganga) | 3.53 | 🟡 Alert | -0.009 |  |
| 2026-09-17 22:07:38 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.373 | 🔺 Rising |
| 2026-09-17 22:07:31 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:07:02 | Magura (Kalu Ganga) | 5.02 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-09-17 22:05:59 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:05:36 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:05:27 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 22:04:52 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:04:39 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-09-17 22:04:12 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | -0.029 |  |
| 2026-09-17 22:04:02 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-09-17 22:03:34 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-17 22:02:39 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:02:29 | Dunamale (Aththanagalu Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:02:26 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:02:20 | Glencourse (Kelani Ganga) | 9.56 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:02:15 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:02:09 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-09-17 22:02:08 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:02:02 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-17 22:02:00 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:01:48 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:01:42 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.039 |  |
| 2026-09-17 22:01:39 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.062 |  |
| 2026-09-17 22:01:31 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-09-17 22:00:35 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 22:07:02 | Magura (Kalu Ganga) | 5.02 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-09-17 22:08:14 | Baddegama (Gin Ganga) | 3.53 | 🟡 Alert | -0.009 |  |
| 2026-09-17 22:07:38 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.373 | 🔺 Rising |
| 2026-09-17 22:03:34 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-17 22:13:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.22 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-17 22:02:02 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-17 22:05:27 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 22:17:39 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-17 18:01:37 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:02:26 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:09:03 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:01:48 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:07:31 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:00:35 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:02:18 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:02:08 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:02:00 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:28:05 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:02:20 | Glencourse (Kelani Ganga) | 9.56 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:02:39 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-17 21:01:20 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:02:29 | Dunamale (Aththanagalu Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-09-17 21:03:21 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:14:37 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:04:52 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:20:25 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:22 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:12:17 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:02:15 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:05:36 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:04:39 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-09-17 22:04:02 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-09-17 22:02:09 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-09-17 22:01:31 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-09-17 22:11:30 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.028 |  |
| 2026-09-17 22:09:01 | Panadugama (Nilwala Ganga) | 4.59 | 🟢 Normal | -0.029 |  |
| 2026-09-17 22:04:12 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | -0.029 |  |
| 2026-09-17 22:01:42 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.039 |  |
| 2026-09-17 22:01:39 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)