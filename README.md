# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--04_22:20:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,984 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 22:20:08 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.008 |  |
| 2026-11-04 22:12:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.16 | 🟡 Alert | 0.037 | 🔺 Rising |
| 2026-11-04 22:12:11 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | -0.028 |  |
| 2026-11-04 22:11:30 | Panadugama (Nilwala Ganga) | 4.16 | 🟢 Normal | -0.009 |  |
| 2026-11-04 22:10:00 | Ellagawa (Kalu Ganga) | 6.56 | 🟢 Normal | -54.000 |  |
| 2026-11-04 22:09:58 | Ellagawa (Kalu Ganga) | 6.59 | 🟢 Normal | -54.000 |  |
| 2026-11-04 22:09:44 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.018 |  |
| 2026-11-04 22:08:49 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.142 |  |
| 2026-11-04 22:07:27 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-04 22:07:23 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-04 22:07:05 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-04 22:07:01 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-04 22:06:16 | Urawa (Nilwala Ganga) | 1.82 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-04 22:05:31 | Holombuwa (Kelani Ganga) | 1.46 | 🟢 Normal | -0.067 |  |
| 2026-11-04 22:05:26 | Badalgama (Maha Oya) | 3.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 22:05:18 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-04 22:05:13 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-11-04 22:05:02 | Thanamalwila (Kirindi Oya) | 2.83 | 🟢 Normal | 0.472 | 🔺 Rising |
| 2026-11-04 22:04:11 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.072 |  |
| 2026-11-04 22:03:54 | Magura (Kalu Ganga) | 2.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 22:03:44 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | -0.010 |  |
| 2026-11-04 22:03:29 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-11-04 22:03:20 | Giriulla (Maha Oya) | 2.58 | 🟢 Normal | 0.303 | 🔺 Rising |
| 2026-11-04 22:03:08 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-04 22:02:54 | Putupaula (Kalu Ganga) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 22:02:45 | Pitabeddara (Nilwala Ganga) | 1.74 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-04 22:02:36 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-04 22:02:36 | Hanwella (Kelani Ganga) | 2.36 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-04 22:02:16 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-11-04 22:01:59 | Padiyathalawa (Maduru Oya) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-11-04 22:01:47 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-04 22:01:41 | Moraketiya (Walawe Ganga) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-11-04 22:01:39 | Rathnapura (Kalu Ganga) | 2.33 | 🟢 Normal | -0.040 |  |
| 2026-11-04 22:01:37 | Kuda Oya (Kirindi Oya) | 4.10 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-11-04 22:01:06 | Moragaswewa (Deduru Oya) | 4.16 | 🟢 Normal | -0.041 |  |
| 2026-11-04 22:00:43 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-11-04 22:00:22 | Wellawaya (Kirindi Oya) | 2.65 | 🟢 Normal | -0.050 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 22:12:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.16 | 🟡 Alert | 0.037 | 🔺 Rising |
| 2026-11-04 22:05:02 | Thanamalwila (Kirindi Oya) | 2.83 | 🟢 Normal | 0.472 | 🔺 Rising |
| 2026-11-04 22:03:20 | Giriulla (Maha Oya) | 2.58 | 🟢 Normal | 0.303 | 🔺 Rising |
| 2026-11-04 22:01:37 | Kuda Oya (Kirindi Oya) | 4.10 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-11-04 22:02:16 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-11-04 22:03:29 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-11-04 22:07:05 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-04 22:02:36 | Hanwella (Kelani Ganga) | 2.36 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-04 22:06:16 | Urawa (Nilwala Ganga) | 1.82 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-04 22:02:45 | Pitabeddara (Nilwala Ganga) | 1.74 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-04 22:03:54 | Magura (Kalu Ganga) | 2.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 22:02:54 | Putupaula (Kalu Ganga) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 22:05:26 | Badalgama (Maha Oya) | 3.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 22:07:27 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-04 22:07:23 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-04 22:05:18 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-04 22:07:01 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-04 22:03:08 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-04 22:02:36 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-04 22:01:47 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:00:12 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-11-04 22:20:08 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.008 |  |
| 2026-11-04 22:11:30 | Panadugama (Nilwala Ganga) | 4.16 | 🟢 Normal | -0.009 |  |
| 2026-11-04 22:05:13 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-11-04 22:03:44 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | -0.010 |  |
| 2026-11-04 22:00:43 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-11-04 22:01:59 | Padiyathalawa (Maduru Oya) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-11-04 22:09:44 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.018 |  |
| 2026-11-04 22:01:41 | Moraketiya (Walawe Ganga) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-11-04 22:12:11 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | -0.028 |  |
| 2026-11-04 18:02:29 | Galgamuwa (Mee Oya) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-11-04 18:03:43 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.038 |  |
| 2026-11-04 22:01:39 | Rathnapura (Kalu Ganga) | 2.33 | 🟢 Normal | -0.040 |  |
| 2026-11-04 22:01:06 | Moragaswewa (Deduru Oya) | 4.16 | 🟢 Normal | -0.041 |  |
| 2026-11-04 22:00:22 | Wellawaya (Kirindi Oya) | 2.65 | 🟢 Normal | -0.050 |  |
| 2026-11-04 22:05:31 | Holombuwa (Kelani Ganga) | 1.46 | 🟢 Normal | -0.067 |  |
| 2026-11-04 22:04:11 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.072 |  |
| 2026-11-04 22:08:49 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.142 |  |
| 2026-11-04 22:10:00 | Ellagawa (Kalu Ganga) | 6.56 | 🟢 Normal | -54.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)