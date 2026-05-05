# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--05_05:18:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **143,238 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 05:18:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.025 |  |
| 2026-05-05 05:17:23 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-05 05:17:01 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-05 05:14:34 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.049 |  |
| 2026-05-05 05:10:14 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-05 05:09:20 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-05 05:07:34 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-05 05:07:12 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.245 |  |
| 2026-05-05 05:06:18 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-05 05:05:59 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.075 |  |
| 2026-05-05 05:05:47 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-05 05:05:32 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-05 05:05:29 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-05 05:05:27 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-05 05:05:23 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-05-05 05:05:21 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.069 |  |
| 2026-05-05 05:04:45 | Glencourse (Kelani Ganga) | 10.09 | 🟢 Normal | -0.160 |  |
| 2026-05-05 05:04:32 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-05 05:04:17 | Hanwella (Kelani Ganga) | 1.33 | 🟢 Normal | 0.257 | 🔺 Rising |
| 2026-05-05 05:03:56 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-05-05 05:03:48 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-05 05:03:47 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.039 |  |
| 2026-05-05 05:03:44 | Rathnapura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.120 |  |
| 2026-05-05 05:03:41 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-05 05:03:39 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-05 05:02:50 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-05 05:02:50 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-05-05 05:02:36 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.020 |  |
| 2026-05-05 05:02:27 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | -0.020 |  |
| 2026-05-05 05:02:11 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-05 05:01:21 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-05 05:00:39 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-05 05:00:09 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-05 05:00:03 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.386 | 🔺 Rising |
| 2026-05-05 04:47:53 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.069 |  |
| 2026-05-05 04:42:41 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.245 |  |
| 2026-05-05 04:41:42 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 05:00:03 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.386 | 🔺 Rising |
| 2026-05-05 05:04:17 | Hanwella (Kelani Ganga) | 1.33 | 🟢 Normal | 0.257 | 🔺 Rising |
| 2026-05-05 05:09:20 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-05 05:03:48 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-05 05:05:32 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-05 05:00:09 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-05 04:06:42 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-05 05:05:27 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-04 18:02:41 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.000 |  |
| 2026-05-05 05:07:34 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-05 05:00:39 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-05 05:02:11 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-05 05:02:50 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-04 18:01:37 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-05 05:17:23 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-05 05:01:21 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-05 05:05:47 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-05 05:17:01 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-05 05:06:18 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-05 05:05:29 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-05 05:03:41 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-05 05:05:23 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-05-04 18:03:48 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-05 05:03:39 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-05 05:04:32 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:29:23 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | -0.004 |  |
| 2026-05-05 05:10:14 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-05 05:03:56 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-05-05 05:02:36 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.020 |  |
| 2026-05-05 05:02:50 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-05-05 05:02:27 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | -0.020 |  |
| 2026-05-05 05:18:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.025 |  |
| 2026-05-05 05:03:47 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.039 |  |
| 2026-05-05 05:14:34 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.049 |  |
| 2026-05-05 05:05:21 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.069 |  |
| 2026-05-05 05:05:59 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.075 |  |
| 2026-05-05 05:03:44 | Rathnapura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.120 |  |
| 2026-05-05 05:04:45 | Glencourse (Kelani Ganga) | 10.09 | 🟢 Normal | -0.160 |  |
| 2026-05-05 05:07:12 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.245 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)