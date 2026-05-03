# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_15:07:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **141,868 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 15:07:49 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:07:28 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-03 15:07:12 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:06:46 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:06:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.039 |  |
| 2026-05-03 15:06:05 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.066 |  |
| 2026-05-03 15:05:49 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:05:19 | Rathnapura (Kalu Ganga) | 1.16 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-03 15:05:12 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:04:58 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | -0.010 |  |
| 2026-05-03 15:04:48 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:04:45 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:04:41 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | -0.032 |  |
| 2026-05-03 15:04:18 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-03 15:03:48 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-05-03 15:03:29 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:03:17 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:03:13 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-03 15:03:09 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-03 15:03:08 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:03:04 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-03 15:02:56 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.045 |  |
| 2026-05-03 15:02:41 | Ellagawa (Kalu Ganga) | 4.72 | 🟢 Normal | -0.010 |  |
| 2026-05-03 15:02:29 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:02:29 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-03 15:02:27 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:02:24 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.055 |  |
| 2026-05-03 15:02:16 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:01:52 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:01:51 | Thanthirimale (Malwathu Oya) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-05-03 15:01:49 | Dunamale (Aththanagalu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:01:48 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:01:42 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:01:24 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:01:20 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:00:47 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-03 15:00:16 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.050 |  |
| 2026-05-03 15:00:06 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-03 14:32:54 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-03 14:18:45 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.052 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 15:03:13 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-03 15:05:19 | Rathnapura (Kalu Ganga) | 1.16 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-03 15:07:28 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-03 15:03:09 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-03 15:02:29 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-03 15:03:04 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-03 15:01:42 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:01:52 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:01:20 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:04:45 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:00:06 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-03 14:05:16 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:01:24 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:04:48 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:03:29 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:03:08 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:01:49 | Dunamale (Aththanagalu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:02:29 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:02:27 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:03:17 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:02:16 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:06:46 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:07:49 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:07:12 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:01:48 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:05:12 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:04:18 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-03 15:01:51 | Thanthirimale (Malwathu Oya) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-05-03 15:00:47 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-03 15:04:58 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | -0.010 |  |
| 2026-05-03 15:02:41 | Ellagawa (Kalu Ganga) | 4.72 | 🟢 Normal | -0.010 |  |
| 2026-05-03 15:03:48 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-05-03 14:05:24 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | -0.019 |  |
| 2026-05-03 15:04:41 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | -0.032 |  |
| 2026-05-03 15:06:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.039 |  |
| 2026-05-03 15:02:56 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.045 |  |
| 2026-05-03 15:00:16 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.050 |  |
| 2026-05-03 15:02:24 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.055 |  |
| 2026-05-03 15:06:05 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.066 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)