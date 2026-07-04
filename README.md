# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--04_16:24:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **197,170 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 16:24:33 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 16:21:05 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:15:36 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-04 16:09:56 | Holombuwa (Kelani Ganga) | 1.58 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-07-04 16:09:22 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-04 16:08:44 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:08:23 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:08:21 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:06:59 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:06:54 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-07-04 16:06:19 | Dunamale (Aththanagalu Oya) | 1.68 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-07-04 16:05:43 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 16:05:43 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:05:22 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:05:22 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:05:02 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:04:19 | Hanwella (Kelani Ganga) | 2.59 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-07-04 16:04:02 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-07-04 16:03:59 | Deraniyagala (Kelani Ganga) | 1.36 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-04 16:03:37 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-07-04 16:03:33 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-07-04 16:03:28 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:03:28 | Nawalapitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-04 16:03:02 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-04 16:02:55 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-07-04 16:02:43 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-07-04 16:02:23 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:02:19 | Glencourse (Kelani Ganga) | 11.38 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-04 16:02:13 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-04 16:02:12 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 16:02:11 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:02:08 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:01:48 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-07-04 16:01:35 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:01:22 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.030 |  |
| 2026-07-04 16:00:46 | Rathnapura (Kalu Ganga) | 2.27 | 🟢 Normal | -0.124 |  |
| 2026-07-04 16:00:45 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:00:34 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:00:30 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:00:19 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 16:04:19 | Hanwella (Kelani Ganga) | 2.59 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-07-04 16:03:33 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-07-04 16:04:02 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-07-04 16:02:43 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-07-04 16:03:37 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-07-04 16:03:59 | Deraniyagala (Kelani Ganga) | 1.36 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-04 16:09:56 | Holombuwa (Kelani Ganga) | 1.58 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-07-04 16:06:19 | Dunamale (Aththanagalu Oya) | 1.68 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-07-04 16:03:02 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-04 16:02:19 | Glencourse (Kelani Ganga) | 11.38 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-04 16:03:28 | Nawalapitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-04 16:09:22 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-04 16:15:36 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-04 16:02:13 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-04 16:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 16:05:43 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 16:24:33 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 16:00:19 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:00:34 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:05:02 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:01:35 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:00:30 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:05:22 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:06:59 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:02:23 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:02:08 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:05:22 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:08:44 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:02:12 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:00:45 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:03:28 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:08:23 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:21:05 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:05:43 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:06:54 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-07-04 16:01:48 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-07-04 16:02:55 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-07-04 16:01:22 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.030 |  |
| 2026-07-04 16:00:46 | Rathnapura (Kalu Ganga) | 2.27 | 🟢 Normal | -0.124 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)