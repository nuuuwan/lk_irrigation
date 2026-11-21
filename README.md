# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--21_09:32:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **321,697 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 09:32:10 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.021 |  |
| 2026-11-21 09:14:37 | Horowpothana (Yan Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-11-21 09:10:29 | Thawalama (Gin Ganga) | 2.54 | 🟢 Normal | -0.056 |  |
| 2026-11-21 09:09:34 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.244 |  |
| 2026-11-21 09:08:53 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-21 09:08:27 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-11-21 09:07:11 | Holombuwa (Kelani Ganga) | 1.65 | 🟢 Normal | 0.339 | 🔺 Rising |
| 2026-11-21 09:06:58 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.009 |  |
| 2026-11-21 09:06:41 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-21 09:05:57 | Panadugama (Nilwala Ganga) | 5.33 | 🟡 Alert | -0.019 |  |
| 2026-11-21 09:05:52 | Urawa (Nilwala Ganga) | 1.37 | 🟢 Normal | -0.089 |  |
| 2026-11-21 09:05:47 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-21 09:05:43 | Glencourse (Kelani Ganga) | 9.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 09:05:11 | Moraketiya (Walawe Ganga) | 2.93 | 🟢 Normal | 0.000 |  |
| 2026-11-21 09:05:01 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-21 09:04:54 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-11-21 09:04:27 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2026-11-21 09:04:16 | Rathnapura (Kalu Ganga) | 3.14 | 🟢 Normal | -0.071 |  |
| 2026-11-21 09:03:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.74 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-21 09:03:37 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-21 09:03:29 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.030 |  |
| 2026-11-21 09:03:12 | Pitabeddara (Nilwala Ganga) | 2.79 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-21 09:02:41 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 09:02:40 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-21 09:02:39 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 09:02:32 | Thanamalwila (Kirindi Oya) | 2.00 | 🟢 Normal | -0.080 |  |
| 2026-11-21 09:02:15 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.701 |  |
| 2026-11-21 09:02:03 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-11-21 09:01:55 | Peradeniya (Mahaweli Ganga) | 3.26 | 🟢 Normal | -0.172 |  |
| 2026-11-21 09:01:54 | Manampitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-11-21 09:01:47 | Wellawaya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 09:01:34 | Giriulla (Maha Oya) | 3.86 | 🟢 Normal | 1.163 | 🔺 Rising |
| 2026-11-21 09:01:33 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-21 09:01:19 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 09:01:16 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-11-21 09:00:58 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-21 09:00:58 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-21 09:00:45 | Kuda Oya (Kirindi Oya) | 2.15 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 09:05:57 | Panadugama (Nilwala Ganga) | 5.33 | 🟡 Alert | -0.019 |  |
| 2026-11-21 09:01:34 | Giriulla (Maha Oya) | 3.86 | 🟢 Normal | 1.163 | 🔺 Rising |
| 2026-11-21 09:07:11 | Holombuwa (Kelani Ganga) | 1.65 | 🟢 Normal | 0.339 | 🔺 Rising |
| 2026-11-21 09:04:27 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2026-11-21 09:04:54 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-11-21 09:06:41 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-21 09:03:12 | Pitabeddara (Nilwala Ganga) | 2.79 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-21 09:03:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.74 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-21 09:01:33 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-21 09:08:53 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-21 09:05:47 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-21 09:05:01 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-21 09:02:41 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 09:05:43 | Glencourse (Kelani Ganga) | 9.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 09:00:58 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-21 09:01:47 | Wellawaya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 09:02:39 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 09:00:58 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-21 09:01:19 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 09:14:37 | Horowpothana (Yan Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-11-21 09:08:27 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-21 09:05:11 | Moraketiya (Walawe Ganga) | 2.93 | 🟢 Normal | 0.000 |  |
| 2026-11-21 09:02:40 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-21 09:03:37 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-21 09:06:58 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.009 |  |
| 2026-11-21 09:01:54 | Manampitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-11-21 09:00:45 | Kuda Oya (Kirindi Oya) | 2.15 | 🟢 Normal | -0.011 |  |
| 2026-11-21 09:02:03 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-11-21 09:32:10 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.021 |  |
| 2026-11-21 09:01:16 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-11-21 09:03:29 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.030 |  |
| 2026-11-21 09:10:29 | Thawalama (Gin Ganga) | 2.54 | 🟢 Normal | -0.056 |  |
| 2026-11-21 09:04:16 | Rathnapura (Kalu Ganga) | 3.14 | 🟢 Normal | -0.071 |  |
| 2026-11-21 09:02:32 | Thanamalwila (Kirindi Oya) | 2.00 | 🟢 Normal | -0.080 |  |
| 2026-11-21 09:05:52 | Urawa (Nilwala Ganga) | 1.37 | 🟢 Normal | -0.089 |  |
| 2026-11-21 09:01:55 | Peradeniya (Mahaweli Ganga) | 3.26 | 🟢 Normal | -0.172 |  |
| 2026-11-21 09:09:34 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.244 |  |
| 2026-11-21 09:02:15 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.701 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)