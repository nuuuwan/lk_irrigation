# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--11_18:12:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **203,557 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 18:12:40 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | -0.008 |  |
| 2026-07-11 18:11:40 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:10:03 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.038 |  |
| 2026-07-11 18:08:51 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:08:44 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.099 |  |
| 2026-07-11 18:07:46 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:06:56 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:05:41 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:04:54 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:04:48 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-07-11 18:04:47 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:04:28 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:04:24 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:04:05 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-07-11 18:04:00 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 18:03:55 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:03:08 | Hanwella (Kelani Ganga) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 18:03:07 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-07-11 18:03:06 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:02:57 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:02:55 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 18:02:52 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:02:44 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:02:37 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | -0.077 |  |
| 2026-07-11 18:02:37 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:02:33 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:02:27 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.012 |  |
| 2026-07-11 18:02:21 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 18:02:17 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | -0.010 |  |
| 2026-07-11 18:02:13 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.030 |  |
| 2026-07-11 18:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.040 |  |
| 2026-07-11 18:02:05 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.046 |  |
| 2026-07-11 18:02:04 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:02:01 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:01:56 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.020 |  |
| 2026-07-11 18:01:56 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-11 18:01:23 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:01:10 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:00:48 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:00:10 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.066 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 18:01:56 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-11 17:01:05 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-11 18:02:55 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 18:02:21 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 18:03:08 | Hanwella (Kelani Ganga) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 18:04:00 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 18:01:23 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:01:10 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:02:52 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:05:41 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:02:44 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:03:55 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:04:28 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:07:46 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:02:37 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:11:40 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:04:54 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:02:57 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:08:51 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:04:24 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:04:47 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:00:48 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:02:04 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:06:56 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:03:06 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:12:40 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | -0.008 |  |
| 2026-07-11 18:04:48 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-07-11 18:04:05 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-07-11 18:02:17 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | -0.010 |  |
| 2026-07-11 18:03:07 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-07-11 18:02:27 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.012 |  |
| 2026-07-11 18:01:56 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.020 |  |
| 2026-07-11 18:02:13 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.030 |  |
| 2026-07-11 18:10:03 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.038 |  |
| 2026-07-11 18:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.040 |  |
| 2026-07-11 18:02:05 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.046 |  |
| 2026-07-11 18:00:10 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.066 |  |
| 2026-07-11 18:02:37 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | -0.077 |  |
| 2026-07-11 18:08:44 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.099 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)