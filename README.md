# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--25_15:05:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **55,349 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-25 15:05:30 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:05:14 | Thawalama (Gin Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:04:58 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:04:43 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-25 15:04:38 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:04:21 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.010 |  |
| 2026-01-25 15:04:19 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-25 15:04:11 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:03:58 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:03:56 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-01-25 15:03:53 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:03:48 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-01-25 15:03:43 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-01-25 15:03:41 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:03:29 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-01-25 15:03:26 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:03:23 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-25 15:03:16 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:03:14 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-25 15:02:30 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:02:15 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:02:15 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-01-25 15:02:14 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:02:07 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.079 |  |
| 2026-01-25 15:01:50 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-01-25 15:01:48 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:01:48 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:01:34 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-25 15:01:20 | Yaka Wewa (Ma Oya) | 1.12 | 🟢 Normal | -0.041 |  |
| 2026-01-25 15:01:08 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | -0.011 |  |
| 2026-01-25 15:00:57 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:00:50 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 15:00:08 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | -0.014 |  |
| 2026-01-25 14:35:14 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-25 14:24:00 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-25 14:17:38 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | -0.014 |  |
| 2026-01-25 14:16:30 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 14:12:55 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-25 14:09:17 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-25 14:05:25 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-01-25 15:02:15 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-01-25 15:01:34 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-25 15:03:14 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-25 15:04:43 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-25 15:00:50 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 15:00:57 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:01:48 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:02:15 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:03:16 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:04:11 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:04:58 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:03:26 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:02:30 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-25 14:35:14 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-25 14:02:55 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:03:53 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:03:41 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:02:14 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:03:58 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-25 14:12:55 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:05:14 | Thawalama (Gin Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:04:38 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:01:48 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:05:30 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:03:56 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-01-25 15:03:43 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-01-25 15:03:48 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-01-25 15:04:21 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.010 |  |
| 2026-01-25 15:03:23 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-25 15:01:50 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-01-25 15:04:19 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-25 15:01:08 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | -0.011 |  |
| 2026-01-25 15:00:08 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | -0.014 |  |
| 2026-01-25 15:03:29 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-01-25 14:01:05 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | -0.040 |  |
| 2026-01-25 15:01:20 | Yaka Wewa (Ma Oya) | 1.12 | 🟢 Normal | -0.041 |  |
| 2026-01-25 14:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.20 | 🟢 Normal | -0.047 |  |
| 2026-01-25 15:02:07 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)