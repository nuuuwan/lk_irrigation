# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--11_14:24:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **42,751 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 14:24:11 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:22:48 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-11 14:21:44 | Thanthirimale (Malwathu Oya) | 1.75 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-01-11 14:08:45 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-11 14:08:34 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-01-11 14:06:40 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:05:46 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.010 |  |
| 2026-01-11 14:05:42 | Peradeniya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.056 |  |
| 2026-01-11 14:05:40 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:05:09 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:04:51 | Siyambalanduwa (Heda Oya) | 1.04 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-11 14:04:38 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.038 |  |
| 2026-01-11 14:04:34 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:04:27 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:04:08 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:03:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-01-11 14:03:37 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-01-11 14:03:36 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | -36.000 |  |
| 2026-01-11 14:03:35 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | -36.000 |  |
| 2026-01-11 14:03:30 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.031 |  |
| 2026-01-11 14:03:28 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:03:10 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-11 14:03:07 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-11 14:02:45 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:02:41 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:02:16 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:01:46 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:01:40 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:01:40 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:01:38 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 14:01:33 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:01:32 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-01-11 14:01:32 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:01:30 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:01:21 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:01:13 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.011 |  |
| 2026-01-11 14:01:04 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | -0.010 |  |
| 2026-01-11 14:00:48 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:00:36 | Weraganthota (Mahaweli Ganga) | -1.47 | 🟢 Normal | -0.041 |  |
| 2026-01-11 14:00:09 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 14:04:51 | Siyambalanduwa (Heda Oya) | 1.04 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-11 14:22:48 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-11 14:03:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-01-11 14:03:07 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-11 14:08:45 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-11 14:01:38 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 14:21:44 | Thanthirimale (Malwathu Oya) | 1.75 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-01-11 14:00:48 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:00:09 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:05:09 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:04:34 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:01:40 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:01:32 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:24:11 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:02:41 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:03:28 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:04:08 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:01:40 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:01:30 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:01:33 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-11 13:13:01 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:02:16 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:06:40 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:02:45 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:05:40 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:01:21 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:04:27 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-11 14:08:34 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-01-11 14:05:46 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.010 |  |
| 2026-01-11 14:01:04 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | -0.010 |  |
| 2026-01-11 14:03:37 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-01-11 14:03:10 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-11 14:01:13 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.011 |  |
| 2026-01-11 14:01:32 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-01-11 14:03:30 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.031 |  |
| 2026-01-11 14:04:38 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.038 |  |
| 2026-01-11 14:00:36 | Weraganthota (Mahaweli Ganga) | -1.47 | 🟢 Normal | -0.041 |  |
| 2026-01-11 14:05:42 | Peradeniya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.056 |  |
| 2026-01-11 14:03:36 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)