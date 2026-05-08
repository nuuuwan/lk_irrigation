# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_17:20:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **146,358 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 17:20:47 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.018 |  |
| 2026-05-08 17:15:17 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-08 17:12:55 | Galgamuwa (Mee Oya) | 0.50 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-08 17:12:46 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.043 |  |
| 2026-05-08 17:10:38 | Moragaswewa (Deduru Oya) | 1.41 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-05-08 17:09:40 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | 0.399 | 🔺 Rising |
| 2026-05-08 17:09:21 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-05-08 17:08:15 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-08 17:07:33 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-08 17:06:12 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-08 17:05:37 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-08 17:05:21 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-08 17:05:18 | Panadugama (Nilwala Ganga) | 3.62 | 🟢 Normal | -0.139 |  |
| 2026-05-08 17:04:51 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.060 |  |
| 2026-05-08 17:04:41 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-05-08 17:04:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.50 | 🟢 Normal | -0.042 |  |
| 2026-05-08 17:04:19 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-05-08 17:04:17 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-08 17:03:53 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.407 | 🔺 Rising |
| 2026-05-08 17:03:30 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-05-08 17:03:22 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-08 17:03:21 | Glencourse (Kelani Ganga) | 9.58 | 🟢 Normal | -0.090 |  |
| 2026-05-08 17:03:17 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-05-08 17:03:12 | Thanamalwila (Kirindi Oya) | 1.73 | 🟢 Normal | -0.030 |  |
| 2026-05-08 17:03:00 | Katharagama (Menik Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-08 17:02:42 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-08 17:02:39 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-05-08 17:02:35 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | -0.061 |  |
| 2026-05-08 17:02:10 | Badalgama (Maha Oya) | 2.86 | 🟢 Normal | -0.030 |  |
| 2026-05-08 17:02:08 | Nawalapitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | 0.740 | 🔺 Rising |
| 2026-05-08 17:01:57 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-05-08 17:01:52 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-08 17:01:44 | Thanthirimale (Malwathu Oya) | 2.06 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-08 17:01:01 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | -0.031 |  |
| 2026-05-08 17:00:58 | Weraganthota (Mahaweli Ganga) | -2.91 | 🟢 Normal | -0.010 |  |
| 2026-05-08 17:00:57 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-05-08 17:00:11 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | -0.011 |  |
| 2026-05-08 17:00:11 | Thalgahagoda (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 17:02:08 | Nawalapitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | 0.740 | 🔺 Rising |
| 2026-05-08 17:03:53 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.407 | 🔺 Rising |
| 2026-05-08 17:09:40 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | 0.399 | 🔺 Rising |
| 2026-05-08 17:04:19 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-05-08 17:10:38 | Moragaswewa (Deduru Oya) | 1.41 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-05-08 17:04:41 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-05-08 17:03:17 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-05-08 17:03:22 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-08 17:12:55 | Galgamuwa (Mee Oya) | 0.50 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-08 17:15:17 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-08 17:01:44 | Thanthirimale (Malwathu Oya) | 2.06 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-08 17:05:21 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-08 17:04:17 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-08 17:07:33 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-08 17:08:15 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-08 17:01:52 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-08 17:02:42 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-08 17:05:37 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-08 17:06:12 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-08 17:03:00 | Katharagama (Menik Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-08 17:00:11 | Thalgahagoda (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-08 17:03:30 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-05-08 17:02:39 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-05-08 17:09:21 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-05-08 17:00:58 | Weraganthota (Mahaweli Ganga) | -2.91 | 🟢 Normal | -0.010 |  |
| 2026-05-08 17:00:11 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | -0.011 |  |
| 2026-05-08 17:20:47 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.018 |  |
| 2026-05-08 17:01:57 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-05-08 17:00:57 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-05-08 17:03:12 | Thanamalwila (Kirindi Oya) | 1.73 | 🟢 Normal | -0.030 |  |
| 2026-05-08 17:02:10 | Badalgama (Maha Oya) | 2.86 | 🟢 Normal | -0.030 |  |
| 2026-05-08 17:01:01 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | -0.031 |  |
| 2026-05-08 16:03:52 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.040 |  |
| 2026-05-08 17:04:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.50 | 🟢 Normal | -0.042 |  |
| 2026-05-08 17:12:46 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.043 |  |
| 2026-05-08 17:04:51 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.060 |  |
| 2026-05-08 17:02:35 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | -0.061 |  |
| 2026-05-08 17:03:21 | Glencourse (Kelani Ganga) | 9.58 | 🟢 Normal | -0.090 |  |
| 2026-05-08 17:05:18 | Panadugama (Nilwala Ganga) | 3.62 | 🟢 Normal | -0.139 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)