# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--06_11:18:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **38,135 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **45** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 11:18:09 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.090 |  |
| 2026-01-06 11:15:29 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:15:19 | Manampitiya (Mahaweli Ganga) | 3.40 | 🟡 Alert | 0.048 | 🔺 Rising |
| 2026-01-06 11:14:43 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.025 |  |
| 2026-01-06 11:14:29 | Panadugama (Nilwala Ganga) | 2.92 | 🟢 Normal | -0.026 |  |
| 2026-01-06 11:14:10 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:12:19 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:06:58 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:06:48 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-06 11:06:41 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.039 |  |
| 2026-01-06 11:06:02 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 11:05:50 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.022 |  |
| 2026-01-06 11:05:34 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:05:33 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.059 |  |
| 2026-01-06 11:05:28 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:05:25 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.010 |  |
| 2026-01-06 11:05:13 | Katharagama (Menik Ganga) | 0.25 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-01-06 11:05:09 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.068 |  |
| 2026-01-06 11:05:00 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.087 |  |
| 2026-01-06 11:04:30 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-01-06 11:04:09 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:04:07 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:04:00 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:03:50 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:03:16 | Nakkala (Kumbukkan Oya) | 2.22 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-06 11:03:10 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 11:03:05 | Thaldena (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.091 |  |
| 2026-01-06 11:02:49 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:02:49 | Siyambalanduwa (Heda Oya) | 5.03 | 🟡 Alert | 0.412 | 🔺 Rising |
| 2026-01-06 11:02:26 | Yaka Wewa (Ma Oya) | 1.07 | 🟢 Normal | -0.049 |  |
| 2026-01-06 11:02:25 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:02:20 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.114 |  |
| 2026-01-06 11:02:11 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-06 11:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | -0.040 |  |
| 2026-01-06 11:01:43 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:01:26 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:01:13 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:01:12 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:01:10 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-01-06 11:01:09 | Padiyathalawa (Maduru Oya) | 2.60 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-01-06 11:00:48 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:00:11 | Weraganthota (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-06 10:44:55 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.090 |  |
| 2026-01-06 10:41:16 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-06 10:31:59 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 11:02:49 | Siyambalanduwa (Heda Oya) | 5.03 | 🟡 Alert | 0.412 | 🔺 Rising |
| 2026-01-06 11:15:19 | Manampitiya (Mahaweli Ganga) | 3.40 | 🟡 Alert | 0.048 | 🔺 Rising |
| 2026-01-06 11:01:10 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-01-06 11:05:13 | Katharagama (Menik Ganga) | 0.25 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-01-06 11:01:09 | Padiyathalawa (Maduru Oya) | 2.60 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-01-06 11:03:16 | Nakkala (Kumbukkan Oya) | 2.22 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-06 11:02:11 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-06 11:06:48 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-06 11:03:10 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 11:06:02 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 11:00:11 | Weraganthota (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:15:29 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:04:00 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:04:09 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:02:25 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:12:19 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:01:26 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:05:28 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:03:50 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:01:43 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:04:07 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:06:58 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:05:34 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:00:48 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:14:10 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-06 11:05:25 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.010 |  |
| 2026-01-06 11:04:30 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-01-06 11:05:50 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.022 |  |
| 2026-01-06 11:14:43 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.025 |  |
| 2026-01-06 11:14:29 | Panadugama (Nilwala Ganga) | 2.92 | 🟢 Normal | -0.026 |  |
| 2026-01-06 11:06:41 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.039 |  |
| 2026-01-06 11:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | -0.040 |  |
| 2026-01-06 11:02:26 | Yaka Wewa (Ma Oya) | 1.07 | 🟢 Normal | -0.049 |  |
| 2026-01-06 11:05:33 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.059 |  |
| 2026-01-06 11:05:09 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.068 |  |
| 2026-01-06 11:05:00 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.087 |  |
| 2026-01-06 11:18:09 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.090 |  |
| 2026-01-06 11:03:05 | Thaldena (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.091 |  |
| 2026-01-06 11:02:20 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.114 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)