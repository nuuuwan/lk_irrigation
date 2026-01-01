# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--01_07:40:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **33,498 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 07:40:34 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-01 07:19:29 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-01 07:16:40 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-01 07:13:33 | Moragaswewa (Deduru Oya) | 0.89 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-01 07:12:57 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-01 07:11:05 | Glencourse (Kelani Ganga) | 9.18 | 🟢 Normal | -0.035 |  |
| 2026-01-01 07:10:28 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-01 07:10:27 | Horowpothana (Yan Oya) | 2.79 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-01 07:09:58 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-01 07:08:21 | Galgamuwa (Mee Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-01 07:07:16 | Kuda Oya (Kirindi Oya) | 2.06 | 🟢 Normal | -0.019 |  |
| 2026-01-01 07:07:08 | Katharagama (Menik Ganga) | 0.42 | 🟢 Normal | -0.290 |  |
| 2026-01-01 07:06:10 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.093 |  |
| 2026-01-01 07:05:48 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | -0.018 |  |
| 2026-01-01 07:05:15 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-01-01 07:05:06 | Hanwella (Kelani Ganga) | 0.96 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-01 07:04:36 | Dunamale (Aththanagalu Oya) | 0.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-01 07:04:29 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.047 |  |
| 2026-01-01 07:04:12 | Manampitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-01-01 07:03:51 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | -0.032 |  |
| 2026-01-01 07:03:48 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-01 07:03:24 | Thanamalwila (Kirindi Oya) | 1.92 | 🟢 Normal | -0.022 |  |
| 2026-01-01 07:03:10 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | -0.035 |  |
| 2026-01-01 07:03:03 | Siyambalanduwa (Heda Oya) | 1.84 | 🟢 Normal | -0.080 |  |
| 2026-01-01 07:02:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.389 |  |
| 2026-01-01 07:01:46 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | -0.023 |  |
| 2026-01-01 07:01:44 | Thanthirimale (Malwathu Oya) | 1.97 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-01-01 07:01:38 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-01 07:01:19 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-01-01 07:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.032 |  |
| 2026-01-01 07:00:46 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-01 07:00:46 | Peradeniya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.011 |  |
| 2026-01-01 07:00:26 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.040 |  |
| 2026-01-01 07:00:15 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | -0.046 |  |
| 2026-01-01 07:00:11 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | -0.032 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 07:04:12 | Manampitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-01-01 07:10:28 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-01 07:10:27 | Horowpothana (Yan Oya) | 2.79 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-01 07:01:44 | Thanthirimale (Malwathu Oya) | 1.97 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-01-01 07:19:29 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-01 07:04:36 | Dunamale (Aththanagalu Oya) | 0.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-01 07:05:06 | Hanwella (Kelani Ganga) | 0.96 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-01 07:13:33 | Moragaswewa (Deduru Oya) | 0.89 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-01 07:12:57 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-01 07:08:21 | Galgamuwa (Mee Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-01 07:09:58 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-01 07:00:46 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-01 07:05:15 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-01-01 07:01:38 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-01 07:03:48 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-01 07:16:40 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-01 07:40:34 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-01 06:05:05 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-01-01 06:02:29 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-01-01 07:00:46 | Peradeniya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.011 |  |
| 2026-01-01 07:05:48 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | -0.018 |  |
| 2026-01-01 07:07:16 | Kuda Oya (Kirindi Oya) | 2.06 | 🟢 Normal | -0.019 |  |
| 2026-01-01 06:07:30 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | -0.019 |  |
| 2026-01-01 07:01:19 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-01-01 07:03:24 | Thanamalwila (Kirindi Oya) | 1.92 | 🟢 Normal | -0.022 |  |
| 2026-01-01 07:01:46 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | -0.023 |  |
| 2026-01-01 07:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.032 |  |
| 2026-01-01 07:03:51 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | -0.032 |  |
| 2026-01-01 07:00:11 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | -0.032 |  |
| 2026-01-01 07:11:05 | Glencourse (Kelani Ganga) | 9.18 | 🟢 Normal | -0.035 |  |
| 2026-01-01 07:03:10 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | -0.035 |  |
| 2026-01-01 07:00:26 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.040 |  |
| 2026-01-01 07:00:15 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | -0.046 |  |
| 2026-01-01 07:04:29 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.047 |  |
| 2026-01-01 07:03:03 | Siyambalanduwa (Heda Oya) | 1.84 | 🟢 Normal | -0.080 |  |
| 2026-01-01 07:06:10 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.093 |  |
| 2026-01-01 07:07:08 | Katharagama (Menik Ganga) | 0.42 | 🟢 Normal | -0.290 |  |
| 2026-01-01 07:02:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.389 |  |
| 2026-01-01 06:08:09 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)