# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--04_19:08:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **36,666 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 19:08:01 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-04 19:07:57 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-01-04 19:07:45 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.089 |  |
| 2026-01-04 19:07:22 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.027 |  |
| 2026-01-04 19:06:57 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-04 19:06:04 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-04 19:05:30 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-01-04 19:05:11 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.019 |  |
| 2026-01-04 19:05:06 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.056 |  |
| 2026-01-04 19:05:04 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.066 |  |
| 2026-01-04 19:05:02 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-04 19:04:48 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.039 |  |
| 2026-01-04 19:04:48 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-01-04 19:04:37 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-04 19:04:35 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-04 19:04:34 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-01-04 19:04:27 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-01-04 19:04:10 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-04 19:04:04 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-04 19:03:18 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-01-04 19:03:14 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-01-04 19:03:08 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-01-04 19:03:03 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 19:02:58 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-01-04 19:02:46 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-04 19:02:22 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.041 |  |
| 2026-01-04 19:02:12 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.050 |  |
| 2026-01-04 19:02:11 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-04 19:02:07 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-01-04 19:01:57 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-04 19:01:21 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-01-04 19:00:51 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-04 19:00:32 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.110 |  |
| 2026-01-04 19:00:16 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:58:12 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:28:43 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.066 |  |
| 2026-01-04 18:27:40 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.110 |  |
| 2026-01-04 18:23:00 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.027 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 19:07:57 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-01-04 19:04:35 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-04 19:06:04 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-04 18:04:42 | Weraganthota (Mahaweli Ganga) | -1.62 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-04 19:03:03 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 19:03:14 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-01-04 19:00:16 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-04 19:00:51 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-04 19:05:02 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-04 19:02:11 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-04 19:03:18 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-01-04 19:02:46 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-04 19:01:57 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-04 19:04:04 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:58:12 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.000 |  |
| 2026-01-04 19:04:10 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-04 19:08:01 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-04 19:06:57 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:02:32 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-04 19:04:37 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-04 19:05:30 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-01-04 19:02:58 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-01-04 19:03:08 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-01-04 19:04:27 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-01-04 19:02:07 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-01-04 19:01:21 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-01-04 19:04:48 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-01-04 19:05:11 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.019 |  |
| 2026-01-04 19:04:34 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-01-04 19:07:22 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.027 |  |
| 2026-01-04 19:04:48 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.039 |  |
| 2026-01-04 19:02:22 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.041 |  |
| 2026-01-04 18:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.59 | 🟢 Normal | -0.044 |  |
| 2026-01-04 18:15:36 | Galgamuwa (Mee Oya) | 2.40 | 🟢 Normal | -0.048 |  |
| 2026-01-04 19:02:12 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.050 |  |
| 2026-01-04 19:05:06 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.056 |  |
| 2026-01-04 19:05:04 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.066 |  |
| 2026-01-04 19:07:45 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.089 |  |
| 2026-01-04 19:00:32 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)