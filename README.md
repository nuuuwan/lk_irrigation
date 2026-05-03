# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_06:31:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **141,518 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 06:31:32 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | -0.002 |  |
| 2026-05-03 06:26:36 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | -0.007 |  |
| 2026-05-03 06:14:42 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.083 |  |
| 2026-05-03 06:14:41 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | 24.750 | 🔺 Rising |
| 2026-05-03 06:14:25 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | 24.750 | 🔺 Rising |
| 2026-05-03 06:14:05 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | 24.750 | 🔺 Rising |
| 2026-05-03 06:10:53 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-05-03 06:07:43 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-03 06:07:15 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.054 |  |
| 2026-05-03 06:07:14 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-05-03 06:06:29 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-03 06:06:20 | Weraganthota (Mahaweli Ganga) | 2.97 | 🟢 Normal | 0.503 | 🔺 Rising |
| 2026-05-03 06:06:04 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-03 06:05:34 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-03 06:05:14 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-05-03 06:04:32 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-03 06:04:01 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.124 |  |
| 2026-05-03 06:03:30 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-03 06:03:13 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-03 06:03:10 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-03 06:03:03 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | -0.071 |  |
| 2026-05-03 06:02:46 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.011 |  |
| 2026-05-03 06:02:43 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-05-03 06:02:38 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-03 06:02:12 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.011 |  |
| 2026-05-03 06:02:06 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.011 |  |
| 2026-05-03 06:01:56 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.214 | 🔺 Rising |
| 2026-05-03 06:01:39 | Rathnapura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.058 |  |
| 2026-05-03 06:01:34 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-03 06:01:24 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-05-03 06:01:07 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-03 06:00:50 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.114 |  |
| 2026-05-03 06:00:48 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-03 06:00:41 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.030 |  |
| 2026-05-03 06:00:36 | Manampitiya (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.011 |  |
| 2026-05-03 06:00:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -0.055 |  |
| 2026-05-03 06:00:31 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.037 |  |
| 2026-05-03 06:00:27 | Ellagawa (Kalu Ganga) | 4.62 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-05-03 06:00:26 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-03 06:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 06:14:41 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | 24.750 | 🔺 Rising |
| 2026-05-03 06:06:20 | Weraganthota (Mahaweli Ganga) | 2.97 | 🟢 Normal | 0.503 | 🔺 Rising |
| 2026-05-03 06:01:56 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.214 | 🔺 Rising |
| 2026-05-03 06:00:27 | Ellagawa (Kalu Ganga) | 4.62 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-05-03 06:07:14 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-05-03 06:03:10 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-03 06:01:07 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-03 06:06:04 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-03 06:07:43 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-03 06:00:26 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-03 06:01:34 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-03 06:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-03 06:00:48 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-03 06:03:13 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-03 06:02:38 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-03 06:04:32 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-03 06:03:30 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-03 06:06:29 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-03 06:05:34 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-03 06:31:32 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | -0.002 |  |
| 2026-05-03 06:26:36 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | -0.007 |  |
| 2026-05-03 06:05:14 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-05-03 06:10:53 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-05-02 18:01:54 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-05-03 06:02:43 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-05-03 06:01:24 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-05-03 06:02:46 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.011 |  |
| 2026-05-03 06:00:36 | Manampitiya (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.011 |  |
| 2026-05-03 06:02:06 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.011 |  |
| 2026-05-03 06:02:12 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.011 |  |
| 2026-05-03 06:00:41 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.030 |  |
| 2026-05-03 06:00:31 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.037 |  |
| 2026-05-03 06:07:15 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.054 |  |
| 2026-05-03 06:00:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -0.055 |  |
| 2026-05-03 06:01:39 | Rathnapura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.058 |  |
| 2026-05-03 06:03:03 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | -0.071 |  |
| 2026-05-03 06:14:42 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.083 |  |
| 2026-05-03 06:00:50 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.114 |  |
| 2026-05-03 06:04:01 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.124 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)