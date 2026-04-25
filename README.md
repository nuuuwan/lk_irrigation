# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_18:14:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **134,871 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 18:14:42 | Moragaswewa (Deduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-25 18:14:21 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.008 |  |
| 2026-04-25 18:13:20 | Katharagama (Menik Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-25 18:11:51 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-25 18:10:58 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | -0.054 |  |
| 2026-04-25 18:08:59 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.019 |  |
| 2026-04-25 18:08:35 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-25 18:07:56 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-25 18:06:46 | Katharagama (Menik Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-25 18:05:40 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | -0.020 |  |
| 2026-04-25 18:05:19 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-25 18:04:54 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-25 18:03:59 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.011 |  |
| 2026-04-25 18:03:42 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-25 18:03:16 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 18:03:16 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-04-25 18:03:12 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-04-25 18:03:06 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-25 18:03:04 | Glencourse (Kelani Ganga) | 8.94 | 🟢 Normal | -0.010 |  |
| 2026-04-25 18:02:56 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | -0.011 |  |
| 2026-04-25 18:02:55 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-04-25 18:02:42 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 18:02:39 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-04-25 18:02:32 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | -0.014 |  |
| 2026-04-25 18:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-04-25 18:02:22 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 18:02:08 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-25 18:02:07 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-25 18:02:06 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-25 18:01:38 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-25 18:01:25 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-25 18:01:22 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-04-25 18:01:21 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-25 18:01:12 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.061 |  |
| 2026-04-25 18:01:09 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-04-25 18:00:50 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.050 |  |
| 2026-04-25 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.020 |  |
| 2026-04-25 18:00:24 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-25 18:00:18 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-25 18:00:18 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-04-25 17:48:46 | Dunamale (Aththanagalu Oya) | 0.86 | 🟢 Normal | -0.054 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 18:00:24 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-25 18:11:51 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-25 18:04:54 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-25 18:05:19 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-25 18:01:25 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-25 18:02:42 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 18:01:21 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-25 18:02:06 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-25 18:14:42 | Moragaswewa (Deduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-25 18:02:22 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 18:03:16 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 18:01:38 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-25 18:03:42 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-25 18:02:08 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-25 18:02:07 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-25 18:13:20 | Katharagama (Menik Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-25 18:08:35 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-25 18:07:56 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-25 18:03:06 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-25 18:14:21 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.008 |  |
| 2026-04-25 18:00:18 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-25 18:00:18 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-04-25 18:01:22 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-04-25 18:02:55 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-04-25 18:03:04 | Glencourse (Kelani Ganga) | 8.94 | 🟢 Normal | -0.010 |  |
| 2026-04-25 18:03:59 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.011 |  |
| 2026-04-25 18:02:56 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | -0.011 |  |
| 2026-04-25 18:02:32 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | -0.014 |  |
| 2026-04-25 18:08:59 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.019 |  |
| 2026-04-25 18:02:39 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-04-25 18:05:40 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | -0.020 |  |
| 2026-04-25 18:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-04-25 18:03:12 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-04-25 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.020 |  |
| 2026-04-25 18:03:16 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-04-25 18:01:09 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-04-25 18:00:50 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.050 |  |
| 2026-04-25 18:10:58 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | -0.054 |  |
| 2026-04-25 18:01:12 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)