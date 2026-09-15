# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--15_11:07:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **261,496 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 11:07:03 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.080 |  |
| 2026-09-15 11:07:03 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-15 11:06:50 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.067 |  |
| 2026-09-15 11:06:21 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-15 11:05:58 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-09-15 11:05:31 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-09-15 11:05:31 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.019 |  |
| 2026-09-15 11:05:31 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.067 |  |
| 2026-09-15 11:04:56 | Nagalagam Street (Kelani Ganga) | 0.35 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-15 11:04:52 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-09-15 11:04:40 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.114 |  |
| 2026-09-15 11:04:25 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-15 11:04:12 | Ellagawa (Kalu Ganga) | 6.13 | 🟢 Normal | -0.072 |  |
| 2026-09-15 11:04:06 | Hanwella (Kelani Ganga) | 2.99 | 🟢 Normal | -0.099 |  |
| 2026-09-15 11:03:50 | Magura (Kalu Ganga) | 4.92 | 🟡 Alert | -0.033 |  |
| 2026-09-15 11:03:39 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-09-15 11:03:30 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-09-15 11:03:26 | Dunamale (Aththanagalu Oya) | 3.33 | 🟡 Alert | -0.029 |  |
| 2026-09-15 11:03:25 | Thawalama (Gin Ganga) | 2.66 | 🟢 Normal | -0.176 |  |
| 2026-09-15 11:03:22 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.000 |  |
| 2026-09-15 11:03:06 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-15 11:03:05 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 11:02:39 | Manampitiya (Mahaweli Ganga) | -0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-15 11:02:37 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-15 11:02:20 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-09-15 11:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.81 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-15 11:02:07 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-09-15 11:01:58 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-09-15 11:00:57 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 11:00:46 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-15 11:00:46 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 11:03:26 | Dunamale (Aththanagalu Oya) | 3.33 | 🟡 Alert | -0.029 |  |
| 2026-09-15 11:03:50 | Magura (Kalu Ganga) | 4.92 | 🟡 Alert | -0.033 |  |
| 2026-09-15 11:02:07 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-09-15 10:09:15 | Baddegama (Gin Ganga) | 3.05 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-15 11:04:56 | Nagalagam Street (Kelani Ganga) | 0.35 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-15 11:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.81 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-15 11:03:06 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-15 11:06:21 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-15 11:03:22 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.000 |  |
| 2026-09-15 11:01:58 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-09-15 11:00:57 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 11:00:46 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-15 11:03:05 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 11:04:52 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-09-15 11:02:37 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-15 11:07:03 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-15 11:04:25 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:02:49 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-15 11:00:46 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:00:08 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-15 11:02:39 | Manampitiya (Mahaweli Ganga) | -0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:15:25 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-15 10:03:36 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-15 11:05:31 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-09-15 11:03:39 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-09-15 11:02:20 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-09-15 11:03:30 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-09-15 11:05:58 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-09-15 10:05:17 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | -0.010 |  |
| 2026-09-15 11:05:31 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.019 |  |
| 2026-09-15 11:05:31 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.067 |  |
| 2026-09-15 11:06:50 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.067 |  |
| 2026-09-15 11:04:12 | Ellagawa (Kalu Ganga) | 6.13 | 🟢 Normal | -0.072 |  |
| 2026-09-15 10:01:04 | Panadugama (Nilwala Ganga) | 4.22 | 🟢 Normal | -0.080 |  |
| 2026-09-15 11:07:03 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.080 |  |
| 2026-09-15 11:04:06 | Hanwella (Kelani Ganga) | 2.99 | 🟢 Normal | -0.099 |  |
| 2026-09-15 11:04:40 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.114 |  |
| 2026-09-15 10:02:03 | Glencourse (Kelani Ganga) | 10.87 | 🟢 Normal | -0.174 |  |
| 2026-09-15 11:03:25 | Thawalama (Gin Ganga) | 2.66 | 🟢 Normal | -0.176 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)