# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--27_10:19:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **56,933 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-27 10:19:49 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.017 |  |
| 2026-01-27 10:18:04 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:12:07 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:09:06 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:08:02 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-27 10:07:58 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:05:41 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:05:31 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.074 |  |
| 2026-01-27 10:05:02 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:04:27 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:04:27 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-27 10:04:20 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:04:08 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | -0.020 |  |
| 2026-01-27 10:03:50 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-01-27 10:03:46 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.021 |  |
| 2026-01-27 10:03:37 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:03:32 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:03:22 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-01-27 10:03:15 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:03:11 | Manampitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-27 10:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | -0.039 |  |
| 2026-01-27 10:03:11 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:02:42 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:02:38 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:02:27 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-01-27 10:02:18 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:02:18 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 10:02:17 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.137 |  |
| 2026-01-27 10:01:45 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:01:38 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:01:30 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:01:29 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-01-27 10:01:28 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:01:20 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:01:14 | Thanthirimale (Malwathu Oya) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-01-27 10:01:06 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:00:43 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | -2.092 |  |
| 2026-01-27 10:00:19 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:00:18 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-27 10:02:27 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-01-27 10:01:29 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-01-27 10:03:11 | Manampitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-27 10:04:27 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-27 10:02:18 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 10:08:02 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-27 10:00:18 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:02:18 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:04:27 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:00:19 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:01:38 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:01:20 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:01:28 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:01:06 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:18:04 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:12:07 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:03:15 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:03:37 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:09:06 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:07:58 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:02:38 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:01:30 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:03:11 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:01:45 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:05:02 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:04:20 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:03:32 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:05:41 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:01:14 | Thanthirimale (Malwathu Oya) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-01-27 10:03:50 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-01-27 10:19:49 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.017 |  |
| 2026-01-27 09:08:59 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-01-27 10:03:22 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-01-27 10:04:08 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | -0.020 |  |
| 2026-01-27 10:03:46 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.021 |  |
| 2026-01-27 10:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | -0.039 |  |
| 2026-01-27 10:05:31 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.074 |  |
| 2026-01-27 10:02:17 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.137 |  |
| 2026-01-27 10:00:43 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | -2.092 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)