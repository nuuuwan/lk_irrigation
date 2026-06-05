# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--05_19:21:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **171,372 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-05 19:21:56 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:20:24 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:12:53 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:10:56 | Putupaula (Kalu Ganga) | 1.53 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-05 19:10:29 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-06-05 19:09:13 | Holombuwa (Kelani Ganga) | 1.18 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-06-05 19:09:09 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:08:45 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:08:39 | Glencourse (Kelani Ganga) | 11.05 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-05 19:08:38 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.018 |  |
| 2026-06-05 19:07:03 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:07:02 | Hanwella (Kelani Ganga) | 3.24 | 🟢 Normal | -0.056 |  |
| 2026-06-05 19:06:56 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-05 19:06:43 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-05 19:05:45 | Deraniyagala (Kelani Ganga) | 1.28 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-06-05 19:05:31 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:05:18 | Ellagawa (Kalu Ganga) | 7.15 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-05 19:05:15 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:04:56 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-06-05 19:04:54 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:04:54 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-06-05 19:04:18 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-05 19:04:01 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | -0.011 |  |
| 2026-06-05 19:03:54 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.031 |  |
| 2026-06-05 19:02:46 | Dunamale (Aththanagalu Oya) | 2.51 | 🟢 Normal | -0.021 |  |
| 2026-06-05 19:02:32 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:02:32 | Giriulla (Maha Oya) | 1.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 19:02:25 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:01:59 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:01:52 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:01:50 | Rathnapura (Kalu Ganga) | 2.85 | 🟢 Normal | -0.061 |  |
| 2026-06-05 19:01:39 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-05 19:01:13 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | -0.020 |  |
| 2026-06-05 19:01:11 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:01:09 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:00:56 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:00:44 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:58:58 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-05 19:04:56 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-06-05 19:09:13 | Holombuwa (Kelani Ganga) | 1.18 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-06-05 19:05:45 | Deraniyagala (Kelani Ganga) | 1.28 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-06-05 19:01:39 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-05 19:10:56 | Putupaula (Kalu Ganga) | 1.53 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-05 19:04:18 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-05 19:06:56 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-05 19:06:43 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-05 19:02:32 | Giriulla (Maha Oya) | 1.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 18:01:21 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 19:05:18 | Ellagawa (Kalu Ganga) | 7.15 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-05 19:08:39 | Glencourse (Kelani Ganga) | 11.05 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-05 19:01:59 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:02:25 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:09:09 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:01:52 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:00:44 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:06:46 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:21:56 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:01:11 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:05:31 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:07:03 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:02:32 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:05:15 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:04:54 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:08:45 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:00:56 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:01:09 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:12:53 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-05 19:10:29 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-06-05 18:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.22 | 🟢 Normal | -0.010 |  |
| 2026-06-05 19:04:01 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | -0.011 |  |
| 2026-06-05 19:08:38 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.018 |  |
| 2026-06-05 18:01:42 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-06-05 19:01:13 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | -0.020 |  |
| 2026-06-05 19:02:46 | Dunamale (Aththanagalu Oya) | 2.51 | 🟢 Normal | -0.021 |  |
| 2026-06-05 19:03:54 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.031 |  |
| 2026-06-05 19:07:02 | Hanwella (Kelani Ganga) | 3.24 | 🟢 Normal | -0.056 |  |
| 2026-06-05 19:01:50 | Rathnapura (Kalu Ganga) | 2.85 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)