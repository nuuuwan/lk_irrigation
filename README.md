# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_17:13:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **140,168 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 17:13:19 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-05-01 17:13:07 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | -0.009 |  |
| 2026-05-01 17:11:40 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-01 17:11:23 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-01 17:11:01 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | -0.018 |  |
| 2026-05-01 17:10:16 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-05-01 17:08:22 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.673 | 🔺 Rising |
| 2026-05-01 17:07:30 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 17:07:06 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.046 |  |
| 2026-05-01 17:06:52 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-05-01 17:06:25 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 17:06:23 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-01 17:05:15 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.011 |  |
| 2026-05-01 17:05:12 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-05-01 17:05:00 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-05-01 17:04:58 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-05-01 17:04:45 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-05-01 17:04:29 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-01 17:03:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-05-01 17:03:21 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-01 17:03:07 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2026-05-01 17:02:49 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-05-01 17:02:25 | Thanthirimale (Malwathu Oya) | 2.62 | 🟢 Normal | -0.032 |  |
| 2026-05-01 17:02:18 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-01 17:02:15 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-01 17:02:12 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-05-01 17:02:07 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-01 17:01:55 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-01 17:01:54 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 17:01:51 | Moragaswewa (Deduru Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-05-01 17:01:47 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-01 17:01:45 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | -0.094 |  |
| 2026-05-01 17:01:40 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.039 |  |
| 2026-05-01 17:01:37 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -0.011 |  |
| 2026-05-01 17:01:36 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-01 17:01:23 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-01 17:01:17 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-01 17:00:45 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.183 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 17:08:22 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.673 | 🔺 Rising |
| 2026-05-01 17:03:07 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2026-05-01 17:02:12 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-05-01 17:10:16 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-05-01 17:04:58 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-05-01 17:04:29 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-01 17:11:40 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-01 17:02:15 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-01 17:03:21 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-01 17:01:54 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 17:11:23 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-01 17:06:23 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-01 17:06:25 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 17:01:55 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-01 17:07:30 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 17:13:19 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-05-01 17:02:07 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-01 17:01:23 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-01 17:01:17 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-01 17:01:36 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-01 17:01:47 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-01 17:02:18 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-01 17:13:07 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | -0.009 |  |
| 2026-05-01 17:05:00 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-05-01 17:03:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-05-01 17:01:51 | Moragaswewa (Deduru Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-05-01 17:02:49 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-05-01 17:06:52 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-05-01 17:05:12 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-05-01 17:01:37 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -0.011 |  |
| 2026-05-01 17:05:15 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.011 |  |
| 2026-05-01 15:00:08 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | -0.014 |  |
| 2026-05-01 17:11:01 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | -0.018 |  |
| 2026-05-01 17:04:45 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-05-01 17:02:25 | Thanthirimale (Malwathu Oya) | 2.62 | 🟢 Normal | -0.032 |  |
| 2026-05-01 17:01:40 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.039 |  |
| 2026-05-01 17:07:06 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.046 |  |
| 2026-05-01 17:01:45 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | -0.094 |  |
| 2026-05-01 17:00:45 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.183 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)