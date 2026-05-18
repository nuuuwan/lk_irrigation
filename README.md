# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--18_12:06:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **155,170 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 12:06:39 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:06:29 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-05-18 12:06:11 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-05-18 12:05:55 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:04:32 | Glencourse (Kelani Ganga) | 10.02 | 🟢 Normal | -0.010 |  |
| 2026-05-18 12:04:10 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:04:08 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:04:02 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-05-18 12:04:01 | Hanwella (Kelani Ganga) | 2.32 | 🟢 Normal | -0.059 |  |
| 2026-05-18 12:04:01 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:04:00 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-05-18 12:03:53 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-05-18 12:03:49 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:03:29 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:03:24 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-18 12:03:23 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-18 12:02:54 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-05-18 12:02:48 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.054 |  |
| 2026-05-18 12:02:42 | Galgamuwa (Mee Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:02:42 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:02:41 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:02:28 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-05-18 12:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.69 | 🟡 Alert | -0.070 |  |
| 2026-05-18 12:02:17 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | -0.023 |  |
| 2026-05-18 12:02:14 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:02:14 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:02:10 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.010 |  |
| 2026-05-18 12:01:58 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:01:28 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 12:01:27 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:01:25 | Thanthirimale (Malwathu Oya) | 3.07 | 🟢 Normal | -0.030 |  |
| 2026-05-18 12:01:22 | Ellagawa (Kalu Ganga) | 6.16 | 🟢 Normal | -0.040 |  |
| 2026-05-18 12:00:31 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:00:16 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.021 |  |
| 2026-05-18 11:15:19 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | -0.018 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 12:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.69 | 🟡 Alert | -0.070 |  |
| 2026-05-18 12:06:11 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-05-18 12:03:24 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-18 12:03:23 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-18 12:01:28 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 12:01:58 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:00:31 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:04:08 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:05:55 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:02:42 | Galgamuwa (Mee Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:04:10 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:03:49 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-18 09:00:58 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-18 11:06:36 | Putupaula (Kalu Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:02:14 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:01:27 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:03:29 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:06:39 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-18 11:10:48 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:02:42 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:02:14 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-18 12:06:29 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-05-18 12:04:02 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-05-18 12:02:10 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.010 |  |
| 2026-05-18 12:04:32 | Glencourse (Kelani Ganga) | 10.02 | 🟢 Normal | -0.010 |  |
| 2026-05-18 11:01:39 | Horowpothana (Yan Oya) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-05-18 12:03:53 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-05-18 12:04:00 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-05-18 11:15:19 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | -0.018 |  |
| 2026-05-18 12:02:54 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-05-18 12:00:16 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.021 |  |
| 2026-05-18 12:02:17 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | -0.023 |  |
| 2026-05-18 12:02:28 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-05-18 11:04:45 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.030 |  |
| 2026-05-18 12:01:25 | Thanthirimale (Malwathu Oya) | 3.07 | 🟢 Normal | -0.030 |  |
| 2026-05-18 12:01:22 | Ellagawa (Kalu Ganga) | 6.16 | 🟢 Normal | -0.040 |  |
| 2026-05-18 12:02:48 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.054 |  |
| 2026-05-18 12:04:01 | Hanwella (Kelani Ganga) | 2.32 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)