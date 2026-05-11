# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_04:42:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **149,464 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 04:42:35 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-12 04:39:44 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | -0.217 |  |
| 2026-05-12 04:36:58 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-12 04:22:33 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.035 |  |
| 2026-05-12 04:18:37 | Glencourse (Kelani Ganga) | 10.53 | 🟢 Normal | -0.073 |  |
| 2026-05-12 04:16:26 | Rathnapura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.042 |  |
| 2026-05-12 04:11:27 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-12 04:08:32 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 04:07:14 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.103 |  |
| 2026-05-12 04:06:26 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.033 |  |
| 2026-05-12 04:05:36 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-12 04:05:18 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.051 |  |
| 2026-05-12 04:05:16 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-05-12 04:05:03 | Katharagama (Menik Ganga) | 2.30 | 🟢 Normal | -0.040 |  |
| 2026-05-12 04:04:32 | Siyambalanduwa (Heda Oya) | 1.04 | 🟢 Normal | -0.091 |  |
| 2026-05-12 04:04:15 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-12 04:03:48 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-05-12 04:03:47 | Magura (Kalu Ganga) | 2.78 | 🟢 Normal | -0.217 |  |
| 2026-05-12 04:03:42 | Moraketiya (Walawe Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-12 04:03:30 | Manampitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-05-12 04:03:22 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-12 04:03:19 | Peradeniya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.276 |  |
| 2026-05-12 04:03:15 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | -0.070 |  |
| 2026-05-12 04:03:07 | Moragaswewa (Deduru Oya) | 2.28 | 🟢 Normal | -0.091 |  |
| 2026-05-12 04:02:32 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 04:02:28 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.041 |  |
| 2026-05-12 04:02:27 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-12 04:02:21 | Hanwella (Kelani Ganga) | 1.92 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-05-12 04:02:20 | Thanamalwila (Kirindi Oya) | 2.23 | 🟢 Normal | -0.021 |  |
| 2026-05-12 04:02:20 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-05-12 04:02:16 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 04:01:37 | Kuda Oya (Kirindi Oya) | 2.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 04:01:34 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-12 04:01:11 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-12 04:00:42 | Wellawaya (Kirindi Oya) | 1.70 | 🟢 Normal | 0.139 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 04:02:21 | Hanwella (Kelani Ganga) | 1.92 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-05-12 04:00:42 | Wellawaya (Kirindi Oya) | 1.70 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-05-12 04:01:34 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-11 18:01:53 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-12 03:06:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.88 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-12 04:04:15 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-12 04:02:32 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 04:36:58 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-12 04:42:35 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-12 04:01:37 | Kuda Oya (Kirindi Oya) | 2.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 04:03:22 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-12 04:02:16 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 04:01:11 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-12 04:08:32 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 04:02:27 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-12 04:11:27 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-12 04:03:42 | Moraketiya (Walawe Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-12 04:05:36 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-12 04:03:30 | Manampitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-05-12 04:02:20 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-05-12 04:03:48 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-05-12 04:05:16 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-05-12 03:06:54 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.021 |  |
| 2026-05-12 04:02:20 | Thanamalwila (Kirindi Oya) | 2.23 | 🟢 Normal | -0.021 |  |
| 2026-05-12 04:06:26 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.033 |  |
| 2026-05-12 04:22:33 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.035 |  |
| 2026-05-12 04:05:03 | Katharagama (Menik Ganga) | 2.30 | 🟢 Normal | -0.040 |  |
| 2026-05-12 04:02:28 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.041 |  |
| 2026-05-12 04:16:26 | Rathnapura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.042 |  |
| 2026-05-11 18:02:56 | Weraganthota (Mahaweli Ganga) | -2.75 | 🟢 Normal | -0.049 |  |
| 2026-05-12 04:05:18 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.051 |  |
| 2026-05-12 04:03:15 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | -0.070 |  |
| 2026-05-12 04:18:37 | Glencourse (Kelani Ganga) | 10.53 | 🟢 Normal | -0.073 |  |
| 2026-05-11 18:06:15 | Galgamuwa (Mee Oya) | 1.40 | 🟢 Normal | -0.074 |  |
| 2026-05-12 04:03:07 | Moragaswewa (Deduru Oya) | 2.28 | 🟢 Normal | -0.091 |  |
| 2026-05-12 04:04:32 | Siyambalanduwa (Heda Oya) | 1.04 | 🟢 Normal | -0.091 |  |
| 2026-05-12 04:07:14 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.103 |  |
| 2026-05-12 04:39:44 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | -0.217 |  |
| 2026-05-12 04:03:19 | Peradeniya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.276 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)