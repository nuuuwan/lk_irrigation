# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--05_07:22:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **143,314 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 07:22:43 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-05 07:21:28 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-05 07:14:41 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-05 07:14:12 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-05 07:13:24 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-05 07:13:16 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.026 |  |
| 2026-05-05 07:11:50 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.098 |  |
| 2026-05-05 07:11:49 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-05-05 07:10:37 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.026 |  |
| 2026-05-05 07:09:19 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.165 |  |
| 2026-05-05 07:08:42 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.019 |  |
| 2026-05-05 07:07:36 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.112 |  |
| 2026-05-05 07:07:27 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-05-05 07:06:01 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-05 07:05:51 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.005 |  |
| 2026-05-05 07:05:29 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.065 |  |
| 2026-05-05 07:05:21 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | -0.012 |  |
| 2026-05-05 07:05:12 | Hanwella (Kelani Ganga) | 1.50 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-05 07:05:08 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-05 07:04:53 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.019 |  |
| 2026-05-05 07:04:39 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-05 07:04:16 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-05 07:04:12 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-05 07:04:05 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-05 07:03:58 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-05-05 07:03:43 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-05 07:03:42 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-05-05 07:03:36 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.019 |  |
| 2026-05-05 07:02:51 | Peradeniya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.031 |  |
| 2026-05-05 07:02:34 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.089 |  |
| 2026-05-05 07:02:30 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.060 |  |
| 2026-05-05 07:02:28 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | -0.021 |  |
| 2026-05-05 07:02:22 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | -0.021 |  |
| 2026-05-05 07:02:19 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-05 07:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.041 |  |
| 2026-05-05 07:02:16 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-05 07:02:02 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-05-05 07:01:24 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-05 07:01:05 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 07:03:42 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-05-05 07:05:12 | Hanwella (Kelani Ganga) | 1.50 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-05 07:06:01 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-05 07:02:16 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-05 07:01:05 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-05 07:01:24 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-05 07:21:28 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-05 06:18:41 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-05 07:04:39 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-05 07:04:12 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-05 07:04:05 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-05 07:13:24 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-05 07:14:41 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-05 06:06:19 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-05 07:05:08 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-05 07:22:43 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-05 07:03:58 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-05-05 07:14:12 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-05 07:02:19 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-05 07:05:51 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.005 |  |
| 2026-05-05 07:07:27 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-05-05 07:02:02 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-05-05 07:11:49 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-05-05 07:05:21 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | -0.012 |  |
| 2026-05-05 07:08:42 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.019 |  |
| 2026-05-05 07:04:53 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.019 |  |
| 2026-05-05 07:03:36 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.019 |  |
| 2026-05-05 07:02:22 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | -0.021 |  |
| 2026-05-05 07:02:28 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | -0.021 |  |
| 2026-05-05 07:13:16 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.026 |  |
| 2026-05-05 07:10:37 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.026 |  |
| 2026-05-05 07:02:51 | Peradeniya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.031 |  |
| 2026-05-05 07:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.041 |  |
| 2026-05-05 07:02:30 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.060 |  |
| 2026-05-05 07:05:29 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.065 |  |
| 2026-05-05 07:02:34 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.089 |  |
| 2026-05-05 07:11:50 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.098 |  |
| 2026-05-05 07:07:36 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.112 |  |
| 2026-05-05 07:09:19 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.165 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)