# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--06_19:27:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **144,662 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 19:27:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.014 |  |
| 2026-05-06 19:19:01 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-06 19:17:13 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-06 19:13:09 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-06 19:09:50 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-06 19:09:49 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.368 | 🔺 Rising |
| 2026-05-06 19:09:39 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | -0.009 |  |
| 2026-05-06 19:09:24 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-06 19:08:40 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.049 |  |
| 2026-05-06 19:06:39 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-05-06 19:06:11 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-06 19:05:26 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-06 19:05:05 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-05-06 19:04:58 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-06 19:04:50 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.096 |  |
| 2026-05-06 19:03:33 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-06 19:03:28 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.011 |  |
| 2026-05-06 19:03:08 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-05-06 19:03:07 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-06 19:03:03 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-06 19:03:03 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-06 19:02:44 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-06 19:02:40 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.058 |  |
| 2026-05-06 19:02:34 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.049 |  |
| 2026-05-06 19:02:33 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.021 |  |
| 2026-05-06 19:02:25 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | -0.010 |  |
| 2026-05-06 19:02:22 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-06 19:02:17 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-06 19:02:07 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-06 19:01:34 | Manampitiya (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-06 19:01:20 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-06 19:01:13 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-05-06 19:01:00 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-06 19:00:46 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-06 19:00:24 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-05-06 19:00:14 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 19:09:49 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.368 | 🔺 Rising |
| 2026-05-06 19:03:08 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-05-06 19:02:07 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-06 19:03:03 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-06 19:01:34 | Manampitiya (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-06 19:02:22 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-06 19:04:58 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-06 19:03:33 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-06 19:02:44 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-06 18:05:19 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 19:13:09 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-06 19:00:14 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-06 19:01:00 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-06 19:09:24 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-06 19:05:26 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-06 19:17:13 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-06 19:09:50 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-06 19:03:03 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-06 19:03:07 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-06 19:00:46 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-06 19:02:17 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-06 19:06:11 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-06 19:19:01 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-06 19:01:20 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-06 19:09:39 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | -0.009 |  |
| 2026-05-06 19:06:39 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-05-06 18:02:21 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:01:28 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-06 19:05:05 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-05-06 19:02:25 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | -0.010 |  |
| 2026-05-06 19:00:24 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-05-06 19:01:13 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-05-06 19:03:28 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.011 |  |
| 2026-05-06 19:27:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.014 |  |
| 2026-05-06 19:02:33 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.021 |  |
| 2026-05-06 19:08:40 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.049 |  |
| 2026-05-06 19:02:34 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.049 |  |
| 2026-05-06 19:02:40 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.058 |  |
| 2026-05-06 19:04:50 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)