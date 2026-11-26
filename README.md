# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--26_10:15:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **326,093 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 10:15:18 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.008 |  |
| 2026-11-26 10:14:18 | Kithulgala (Kelani Ganga) | 1.39 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-11-26 10:12:37 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-11-26 10:11:47 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | -0.028 |  |
| 2026-11-26 10:10:34 | Moraketiya (Walawe Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-11-26 10:09:43 | Magura (Kalu Ganga) | 3.44 | 🟢 Normal | -0.073 |  |
| 2026-11-26 10:09:40 | Peradeniya (Mahaweli Ganga) | 3.14 | 🟢 Normal | -0.069 |  |
| 2026-11-26 10:08:39 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.073 |  |
| 2026-11-26 10:07:20 | Moragaswewa (Deduru Oya) | 4.30 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-26 10:07:19 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-11-26 10:07:08 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-26 10:06:58 | Badalgama (Maha Oya) | 4.33 | 🟢 Normal | -0.041 |  |
| 2026-11-26 10:06:18 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-26 10:05:18 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.043 |  |
| 2026-11-26 10:04:58 | Putupaula (Kalu Ganga) | 1.33 | 🟢 Normal | -0.081 |  |
| 2026-11-26 10:04:38 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 10:04:02 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-11-26 10:03:58 | Ellagawa (Kalu Ganga) | 6.13 | 🟢 Normal | -0.028 |  |
| 2026-11-26 10:03:56 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-11-26 10:03:46 | Glencourse (Kelani Ganga) | 11.12 | 🟢 Normal | -0.118 |  |
| 2026-11-26 10:03:43 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.073 |  |
| 2026-11-26 10:03:25 | Dunamale (Aththanagalu Oya) | 3.94 | 🟡 Alert | -0.010 |  |
| 2026-11-26 10:03:16 | Panadugama (Nilwala Ganga) | 3.84 | 🟢 Normal | -0.066 |  |
| 2026-11-26 10:02:53 | Manampitiya (Mahaweli Ganga) | 2.32 | 🟢 Normal | -0.019 |  |
| 2026-11-26 10:02:39 | Hanwella (Kelani Ganga) | 3.68 | 🟢 Normal | -0.101 |  |
| 2026-11-26 10:02:35 | Giriulla (Maha Oya) | 3.18 | 🟢 Normal | -0.121 |  |
| 2026-11-26 10:02:26 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-26 10:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.12 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-26 10:02:18 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-26 10:02:18 | Thanamalwila (Kirindi Oya) | 1.69 | 🟢 Normal | -0.020 |  |
| 2026-11-26 10:02:04 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-11-26 10:01:56 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-26 10:00:43 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | -0.020 |  |
| 2026-11-26 10:00:33 | Weraganthota (Mahaweli Ganga) | -1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-26 10:00:18 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.011 |  |
| 2026-11-26 09:59:13 | Weraganthota (Mahaweli Ganga) | -1.92 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 10:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.12 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-26 10:03:25 | Dunamale (Aththanagalu Oya) | 3.94 | 🟡 Alert | -0.010 |  |
| 2026-11-26 10:07:20 | Moragaswewa (Deduru Oya) | 4.30 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-26 10:14:18 | Kithulgala (Kelani Ganga) | 1.39 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-11-26 10:01:56 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-26 10:00:33 | Weraganthota (Mahaweli Ganga) | -1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-26 10:07:08 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-26 10:04:38 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 10:02:26 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-26 10:10:34 | Moraketiya (Walawe Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-11-26 10:06:18 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-26 10:02:18 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-26 10:15:18 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.008 |  |
| 2026-11-26 10:12:37 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-11-26 10:02:04 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-11-26 10:04:02 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-11-26 10:07:19 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-11-26 10:03:56 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-11-26 10:00:18 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.011 |  |
| 2026-11-26 09:12:56 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.012 |  |
| 2026-11-26 10:02:53 | Manampitiya (Mahaweli Ganga) | 2.32 | 🟢 Normal | -0.019 |  |
| 2026-11-26 09:04:34 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.019 |  |
| 2026-11-26 10:00:43 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | -0.020 |  |
| 2026-11-26 10:02:18 | Thanamalwila (Kirindi Oya) | 1.69 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-26 10:03:58 | Ellagawa (Kalu Ganga) | 6.13 | 🟢 Normal | -0.028 |  |
| 2026-11-26 10:11:47 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | -0.028 |  |
| 2026-11-26 10:06:58 | Badalgama (Maha Oya) | 4.33 | 🟢 Normal | -0.041 |  |
| 2026-11-26 10:05:18 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.043 |  |
| 2026-11-26 10:03:16 | Panadugama (Nilwala Ganga) | 3.84 | 🟢 Normal | -0.066 |  |
| 2026-11-26 10:09:40 | Peradeniya (Mahaweli Ganga) | 3.14 | 🟢 Normal | -0.069 |  |
| 2026-11-26 10:03:43 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.073 |  |
| 2026-11-26 10:09:43 | Magura (Kalu Ganga) | 3.44 | 🟢 Normal | -0.073 |  |
| 2026-11-26 10:08:39 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.073 |  |
| 2026-11-26 10:04:58 | Putupaula (Kalu Ganga) | 1.33 | 🟢 Normal | -0.081 |  |
| 2026-11-26 10:02:39 | Hanwella (Kelani Ganga) | 3.68 | 🟢 Normal | -0.101 |  |
| 2026-11-26 10:03:46 | Glencourse (Kelani Ganga) | 11.12 | 🟢 Normal | -0.118 |  |
| 2026-11-26 10:02:35 | Giriulla (Maha Oya) | 3.18 | 🟢 Normal | -0.121 |  |
| 2026-11-26 09:04:48 | Galgamuwa (Mee Oya) | 1.28 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)