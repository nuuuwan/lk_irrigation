# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--26_04:19:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **161,821 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 04:19:21 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.008 |  |
| 2026-05-26 04:17:24 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-26 04:12:39 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.008 |  |
| 2026-05-26 04:11:32 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-05-26 04:10:52 | Putupaula (Kalu Ganga) | 2.63 | 🟢 Normal | -0.020 |  |
| 2026-05-26 04:09:02 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | -0.018 |  |
| 2026-05-26 04:07:04 | Rathnapura (Kalu Ganga) | 4.77 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-05-26 04:06:48 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-05-26 04:06:25 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-05-26 04:06:00 | Baddegama (Gin Ganga) | 1.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-26 04:05:15 | Hanwella (Kelani Ganga) | 3.86 | 🟢 Normal | -0.011 |  |
| 2026-05-26 04:05:05 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-05-26 04:04:44 | Deraniyagala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-05-26 04:04:37 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-26 04:04:24 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | -0.021 |  |
| 2026-05-26 04:04:07 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-26 04:04:03 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 04:03:50 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-26 04:02:49 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.020 |  |
| 2026-05-26 04:02:38 | Magura (Kalu Ganga) | 2.69 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-26 04:02:27 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-05-26 04:02:27 | Dunamale (Aththanagalu Oya) | 2.55 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-26 04:02:26 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-05-26 04:02:03 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-26 04:01:50 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-26 04:01:49 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-26 04:01:32 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 04:01:27 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-05-26 04:01:23 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 04:01:11 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-26 04:01:10 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 04:00:43 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | 0.053 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 03:06:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.036 | 🔺 Rising |
| 2026-05-26 03:05:03 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.483 | 🔺 Rising |
| 2026-05-26 04:04:44 | Deraniyagala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-05-26 04:07:04 | Rathnapura (Kalu Ganga) | 4.77 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-05-26 04:05:05 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-05-26 03:04:49 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-05-26 04:11:32 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-05-26 04:00:43 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-26 04:04:07 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-26 04:04:37 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-26 04:02:38 | Magura (Kalu Ganga) | 2.69 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-26 04:02:27 | Dunamale (Aththanagalu Oya) | 2.55 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-26 04:06:00 | Baddegama (Gin Ganga) | 1.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-26 04:01:11 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-26 04:06:25 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-05-26 04:02:03 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-26 04:04:03 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 04:01:23 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 04:01:50 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-26 04:01:49 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-26 04:17:24 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-26 04:01:10 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 03:06:19 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-26 04:03:50 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-26 04:06:48 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-05-26 04:02:26 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-05-26 04:01:32 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 04:19:21 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.008 |  |
| 2026-05-26 04:12:39 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.008 |  |
| 2026-05-26 04:02:27 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-05-26 04:01:27 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-05-25 18:01:32 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-05-26 04:05:15 | Hanwella (Kelani Ganga) | 3.86 | 🟢 Normal | -0.011 |  |
| 2026-05-25 18:02:07 | Galgamuwa (Mee Oya) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-05-26 04:09:02 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | -0.018 |  |
| 2026-05-25 18:01:42 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-05-26 04:02:49 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.020 |  |
| 2026-05-26 04:10:52 | Putupaula (Kalu Ganga) | 2.63 | 🟢 Normal | -0.020 |  |
| 2026-05-26 04:04:24 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | -0.021 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)