# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--03_05:31:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **35,209 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 05:31:28 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-03 05:18:12 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-03 05:13:46 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-03 05:11:16 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-03 05:08:35 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-01-03 05:07:55 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-01-03 05:07:33 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-03 05:07:02 | Glencourse (Kelani Ganga) | 8.82 | 🟢 Normal | -0.069 |  |
| 2026-01-03 05:06:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -111.130 |  |
| 2026-01-03 05:06:16 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-03 05:06:12 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-01-03 05:06:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.81 | 🟢 Normal | -111.130 |  |
| 2026-01-03 05:05:52 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-03 05:05:49 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.024 |  |
| 2026-01-03 05:05:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.97 | 🟢 Normal | -111.130 |  |
| 2026-01-03 05:05:38 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.038 |  |
| 2026-01-03 05:05:10 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-03 05:05:01 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-03 05:04:56 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-01-03 05:04:21 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-03 05:04:01 | Siyambalanduwa (Heda Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-03 05:03:57 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-01-03 05:03:03 | Katharagama (Menik Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-01-03 05:02:42 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-03 05:02:39 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-03 05:02:29 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.092 |  |
| 2026-01-03 05:02:19 | Padiyathalawa (Maduru Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-01-03 05:02:07 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-01-03 05:01:37 | Manampitiya (Mahaweli Ganga) | 1.94 | 🟢 Normal | -0.042 |  |
| 2026-01-03 05:01:33 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 05:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-03 05:01:14 | Dunamale (Aththanagalu Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-03 05:00:54 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-01-03 04:56:11 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 05:02:39 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-03 05:05:52 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-03 05:31:28 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-03 05:11:16 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-03 04:56:11 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-03 05:01:33 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 05:07:33 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-03 05:02:42 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-03 05:04:21 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-03 05:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-03 05:05:01 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:02:12 | Galgamuwa (Mee Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-01-03 05:18:12 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-03 05:13:46 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-03 05:03:57 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-01-03 05:06:16 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-03 05:01:14 | Dunamale (Aththanagalu Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-03 05:00:54 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-01-03 05:05:10 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-03 05:07:55 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-01-03 04:08:11 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-01-03 05:02:19 | Padiyathalawa (Maduru Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-01-03 05:04:01 | Siyambalanduwa (Heda Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-03 05:02:07 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-01-03 05:04:56 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-01-03 05:03:03 | Katharagama (Menik Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-01-03 05:06:12 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-01-03 05:05:49 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.024 |  |
| 2026-01-02 18:03:09 | Thanthirimale (Malwathu Oya) | 1.78 | 🟢 Normal | -0.029 |  |
| 2026-01-03 05:08:35 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-01-03 05:05:38 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.038 |  |
| 2026-01-03 05:01:37 | Manampitiya (Mahaweli Ganga) | 1.94 | 🟢 Normal | -0.042 |  |
| 2026-01-02 18:03:09 | Weraganthota (Mahaweli Ganga) | -1.33 | 🟢 Normal | -0.049 |  |
| 2026-01-03 05:07:02 | Glencourse (Kelani Ganga) | 8.82 | 🟢 Normal | -0.069 |  |
| 2026-01-03 05:02:29 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.092 |  |
| 2026-01-03 04:03:16 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.127 |  |
| 2026-01-03 04:04:49 | Horowpothana (Yan Oya) | 2.47 | 🟢 Normal | -2.769 |  |
| 2026-01-03 04:15:57 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -36.000 |  |
| 2026-01-03 05:06:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -111.130 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)