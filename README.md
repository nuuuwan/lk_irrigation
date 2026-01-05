# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--06_04:35:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **37,862 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 04:35:57 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-06 04:15:15 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-06 04:14:56 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-06 04:09:47 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.005 |  |
| 2026-01-06 04:09:46 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | -0.013 |  |
| 2026-01-06 04:09:34 | Rathnapura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-06 04:09:19 | Siyambalanduwa (Heda Oya) | 2.63 | 🟢 Normal | 0.388 | 🔺 Rising |
| 2026-01-06 04:07:33 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-06 04:07:23 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.173 |  |
| 2026-01-06 04:06:56 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.388 |  |
| 2026-01-06 04:06:49 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-06 04:06:09 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-06 04:06:00 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-06 04:05:08 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-06 04:04:41 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-06 04:04:08 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-01-06 04:04:04 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-06 04:03:48 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -1.674 |  |
| 2026-01-06 04:03:30 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 04:03:23 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-06 04:03:11 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-06 04:03:05 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -1.674 |  |
| 2026-01-06 04:03:03 | Peradeniya (Mahaweli Ganga) | 1.94 | 🟢 Normal | -0.244 |  |
| 2026-01-06 04:03:00 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.096 |  |
| 2026-01-06 04:02:57 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-06 04:02:56 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-06 04:02:45 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -1.674 |  |
| 2026-01-06 04:02:21 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-06 04:02:16 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.011 |  |
| 2026-01-06 04:02:13 | Padiyathalawa (Maduru Oya) | 2.60 | 🟢 Normal | 0.663 | 🔺 Rising |
| 2026-01-06 04:01:28 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-06 04:01:15 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-01-06 04:01:08 | Thaldena (Mahaweli Ganga) | 0.93 | 🟢 Normal | 126.000 | 🔺 Rising |
| 2026-01-06 04:01:06 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | 126.000 | 🔺 Rising |
| 2026-01-06 04:00:40 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.139 |  |
| 2026-01-06 04:00:32 | Manampitiya (Mahaweli Ganga) | 2.22 | 🟢 Normal | 0.073 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 04:01:08 | Thaldena (Mahaweli Ganga) | 0.93 | 🟢 Normal | 126.000 | 🔺 Rising |
| 2026-01-06 04:02:13 | Padiyathalawa (Maduru Oya) | 2.60 | 🟢 Normal | 0.663 | 🔺 Rising |
| 2026-01-06 04:09:19 | Siyambalanduwa (Heda Oya) | 2.63 | 🟢 Normal | 0.388 | 🔺 Rising |
| 2026-01-06 03:14:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-01-05 18:04:03 | Weraganthota (Mahaweli Ganga) | -1.35 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-01-06 04:04:08 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-01-06 04:00:32 | Manampitiya (Mahaweli Ganga) | 2.22 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-01-06 02:34:27 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-06 04:06:00 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-06 04:04:41 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-06 04:04:04 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-06 04:05:08 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-06 04:02:56 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-06 04:06:49 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-06 03:10:34 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-06 04:06:09 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-06 04:14:56 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-06 04:02:21 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-06 04:03:11 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:12:56 | Galgamuwa (Mee Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-06 04:07:33 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-06 04:01:15 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-01-06 04:35:57 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-06 04:01:28 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-06 04:02:57 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-06 04:03:30 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 04:09:34 | Rathnapura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-06 03:03:46 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-06 04:09:47 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.005 |  |
| 2026-01-06 04:03:23 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-05 18:04:30 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.011 |  |
| 2026-01-06 04:02:16 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.011 |  |
| 2026-01-06 04:09:46 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | -0.013 |  |
| 2026-01-06 04:03:00 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.096 |  |
| 2026-01-06 04:00:40 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.139 |  |
| 2026-01-06 04:07:23 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.173 |  |
| 2026-01-06 04:03:03 | Peradeniya (Mahaweli Ganga) | 1.94 | 🟢 Normal | -0.244 |  |
| 2026-01-06 04:06:56 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.388 |  |
| 2026-01-06 04:03:48 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -1.674 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)