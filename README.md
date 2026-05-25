# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--25_19:14:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **161,504 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 19:14:19 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-25 19:10:20 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:10:06 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-05-25 19:09:17 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:06:34 | Putupaula (Kalu Ganga) | 2.79 | 🟢 Normal | -0.009 |  |
| 2026-05-25 19:06:31 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.028 |  |
| 2026-05-25 19:05:36 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.010 |  |
| 2026-05-25 19:05:36 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-05-25 19:05:14 | Dunamale (Aththanagalu Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-05-25 19:04:50 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:04:43 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:04:38 | Hanwella (Kelani Ganga) | 4.23 | 🟢 Normal | -0.080 |  |
| 2026-05-25 19:04:37 | Ellagawa (Kalu Ganga) | 8.80 | 🟢 Normal | -0.039 |  |
| 2026-05-25 19:04:18 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-25 19:04:10 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:04:03 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:04:02 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-05-25 19:04:02 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:03:50 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:03:44 | Glencourse (Kelani Ganga) | 11.48 | 🟢 Normal | -0.011 |  |
| 2026-05-25 19:02:52 | Deraniyagala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-05-25 19:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.021 |  |
| 2026-05-25 19:02:48 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.012 |  |
| 2026-05-25 19:02:37 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:02:34 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:02:31 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:02:19 | Rathnapura (Kalu Ganga) | 3.88 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-05-25 19:02:09 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:01:58 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:01:43 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-05-25 19:01:43 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:01:13 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:00:57 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 18:03:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.15 | 🟡 Alert | -0.040 |  |
| 2026-05-25 19:05:36 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-05-25 19:10:06 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-05-25 19:04:02 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-05-25 19:02:19 | Rathnapura (Kalu Ganga) | 3.88 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-05-25 19:04:18 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-25 18:01:35 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 19:14:19 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-25 19:04:50 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:04:10 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:01:43 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:02:09 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:02:34 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:01:13 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:04:43 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:03:50 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:00:57 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:01:58 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:04:02 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:10:20 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:02:31 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:05:21 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:09:17 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:04:03 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:02:37 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 19:06:34 | Putupaula (Kalu Ganga) | 2.79 | 🟢 Normal | -0.009 |  |
| 2026-05-25 19:05:14 | Dunamale (Aththanagalu Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-05-25 19:05:36 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.010 |  |
| 2026-05-25 19:02:52 | Deraniyagala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-05-25 18:01:32 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-05-25 19:01:43 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-05-25 19:03:44 | Glencourse (Kelani Ganga) | 11.48 | 🟢 Normal | -0.011 |  |
| 2026-05-25 18:02:07 | Galgamuwa (Mee Oya) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-05-25 19:02:48 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.012 |  |
| 2026-05-25 18:01:42 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-05-25 19:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.021 |  |
| 2026-05-25 19:06:31 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.028 |  |
| 2026-05-25 19:04:37 | Ellagawa (Kalu Ganga) | 8.80 | 🟢 Normal | -0.039 |  |
| 2026-05-25 19:04:38 | Hanwella (Kelani Ganga) | 4.23 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)