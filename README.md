# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_03:13:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **149,429 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 03:13:37 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-12 03:12:11 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 03:11:03 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 03:10:41 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.055 |  |
| 2026-05-12 03:08:53 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.018 |  |
| 2026-05-12 03:07:00 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-12 03:06:55 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -4.000 |  |
| 2026-05-12 03:06:54 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.021 |  |
| 2026-05-12 03:06:37 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -4.000 |  |
| 2026-05-12 03:06:30 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-12 03:06:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.88 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-12 03:05:38 | Magura (Kalu Ganga) | 2.77 | 🟢 Normal | 324.000 | 🔺 Rising |
| 2026-05-12 03:05:37 | Magura (Kalu Ganga) | 2.68 | 🟢 Normal | 324.000 | 🔺 Rising |
| 2026-05-12 03:05:28 | Thanamalwila (Kirindi Oya) | 2.25 | 🟢 Normal | -0.019 |  |
| 2026-05-12 03:05:06 | Siyambalanduwa (Heda Oya) | 1.13 | 🟢 Normal | -0.239 |  |
| 2026-05-12 03:04:55 | Katharagama (Menik Ganga) | 2.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 03:04:32 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.214 |  |
| 2026-05-12 03:04:31 | Rathnapura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.040 |  |
| 2026-05-12 03:04:27 | Glencourse (Kelani Ganga) | 10.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 03:04:22 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.019 |  |
| 2026-05-12 03:04:12 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.023 |  |
| 2026-05-12 03:03:57 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-12 03:03:55 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.052 |  |
| 2026-05-12 03:03:50 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | -0.033 |  |
| 2026-05-12 03:03:44 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.025 |  |
| 2026-05-12 03:03:38 | Nakkala (Kumbukkan Oya) | 1.36 | 🟢 Normal | -0.049 |  |
| 2026-05-12 03:03:33 | Moragaswewa (Deduru Oya) | 2.37 | 🟢 Normal | -0.081 |  |
| 2026-05-12 03:03:28 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-12 03:03:12 | Manampitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.039 |  |
| 2026-05-12 03:02:59 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-12 03:02:56 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-12 03:02:37 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-05-12 03:02:35 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-12 03:02:26 | Kuda Oya (Kirindi Oya) | 2.35 | 🟢 Normal | -0.040 |  |
| 2026-05-12 03:02:20 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | -0.020 |  |
| 2026-05-12 03:02:11 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 03:01:31 | Moraketiya (Walawe Ganga) | 1.29 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 03:05:38 | Magura (Kalu Ganga) | 2.77 | 🟢 Normal | 324.000 | 🔺 Rising |
| 2026-05-12 03:02:37 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-05-11 18:01:53 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-12 03:06:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.88 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-12 03:02:35 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-12 03:07:00 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-12 03:02:59 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-12 03:02:56 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-12 03:04:55 | Katharagama (Menik Ganga) | 2.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 03:04:27 | Glencourse (Kelani Ganga) | 10.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 03:02:11 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 03:03:28 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-12 03:13:37 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-12 03:12:11 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 03:11:03 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 03:03:57 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-12 03:06:30 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-12 03:01:31 | Moraketiya (Walawe Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-05-12 03:08:53 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.018 |  |
| 2026-05-12 03:05:28 | Thanamalwila (Kirindi Oya) | 2.25 | 🟢 Normal | -0.019 |  |
| 2026-05-12 03:04:22 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.019 |  |
| 2026-05-12 03:02:20 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | -0.020 |  |
| 2026-05-12 03:06:54 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.021 |  |
| 2026-05-12 03:04:12 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.023 |  |
| 2026-05-12 03:03:44 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.025 |  |
| 2026-05-12 03:03:50 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | -0.033 |  |
| 2026-05-12 03:03:12 | Manampitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.039 |  |
| 2026-05-12 03:02:26 | Kuda Oya (Kirindi Oya) | 2.35 | 🟢 Normal | -0.040 |  |
| 2026-05-12 03:04:31 | Rathnapura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.040 |  |
| 2026-05-11 18:02:56 | Weraganthota (Mahaweli Ganga) | -2.75 | 🟢 Normal | -0.049 |  |
| 2026-05-12 03:03:38 | Nakkala (Kumbukkan Oya) | 1.36 | 🟢 Normal | -0.049 |  |
| 2026-05-12 03:03:55 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.052 |  |
| 2026-05-12 03:10:41 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.055 |  |
| 2026-05-11 18:06:15 | Galgamuwa (Mee Oya) | 1.40 | 🟢 Normal | -0.074 |  |
| 2026-05-12 03:03:33 | Moragaswewa (Deduru Oya) | 2.37 | 🟢 Normal | -0.081 |  |
| 2026-05-12 02:16:28 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.085 |  |
| 2026-05-12 03:04:32 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.214 |  |
| 2026-05-12 03:05:06 | Siyambalanduwa (Heda Oya) | 1.13 | 🟢 Normal | -0.239 |  |
| 2026-05-12 03:06:55 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -4.000 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)