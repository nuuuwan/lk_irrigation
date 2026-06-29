# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--29_14:15:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **192,615 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 14:15:18 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-06-29 14:14:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.44 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-29 14:12:35 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.043 |  |
| 2026-06-29 14:10:23 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-29 14:09:59 | Magura (Kalu Ganga) | 3.22 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-06-29 14:08:06 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-29 14:08:01 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-29 14:07:50 | Glencourse (Kelani Ganga) | 11.53 | 🟢 Normal | 0.380 | 🔺 Rising |
| 2026-06-29 14:07:38 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-29 14:06:33 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-06-29 14:06:17 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-29 14:06:05 | Peradeniya (Mahaweli Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-06-29 14:05:57 | Hanwella (Kelani Ganga) | 2.31 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-06-29 14:05:54 | Panadugama (Nilwala Ganga) | 4.40 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-06-29 14:05:34 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-06-29 14:05:30 | Peradeniya (Mahaweli Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-06-29 14:04:59 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.179 |  |
| 2026-06-29 14:04:50 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-29 14:04:46 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-29 14:04:36 | Baddegama (Gin Ganga) | 2.80 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-06-29 14:04:22 | Pitabeddara (Nilwala Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-06-29 14:04:14 | Rathnapura (Kalu Ganga) | 6.02 | 🟡 Alert | 0.327 | 🔺 Rising |
| 2026-06-29 14:03:50 | Ellagawa (Kalu Ganga) | 6.58 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-06-29 14:03:27 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-29 14:03:14 | Putupaula (Kalu Ganga) | 1.07 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-29 14:03:04 | Nawalapitiya (Mahaweli Ganga) | 2.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 14:03:01 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-29 14:02:38 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-06-29 14:02:36 | Deraniyagala (Kelani Ganga) | 1.99 | 🟢 Normal | -0.105 |  |
| 2026-06-29 14:02:33 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-29 14:02:31 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-29 14:02:11 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-06-29 14:01:52 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.010 |  |
| 2026-06-29 14:01:43 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 14:01:42 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 14:01:17 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-06-29 14:01:04 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-29 14:00:55 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-29 14:00:50 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.011 |  |
| 2026-06-29 14:00:01 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 14:04:14 | Rathnapura (Kalu Ganga) | 6.02 | 🟡 Alert | 0.327 | 🔺 Rising |
| 2026-06-29 14:07:50 | Glencourse (Kelani Ganga) | 11.53 | 🟢 Normal | 0.380 | 🔺 Rising |
| 2026-06-29 14:03:50 | Ellagawa (Kalu Ganga) | 6.58 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-06-29 14:05:57 | Hanwella (Kelani Ganga) | 2.31 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-06-29 14:09:59 | Magura (Kalu Ganga) | 3.22 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-06-29 14:04:36 | Baddegama (Gin Ganga) | 2.80 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-06-29 14:05:54 | Panadugama (Nilwala Ganga) | 4.40 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-06-29 14:04:46 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-29 14:03:14 | Putupaula (Kalu Ganga) | 1.07 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-29 14:14:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.44 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-29 14:06:17 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-29 14:08:06 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-29 13:20:36 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-29 14:07:38 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-29 14:00:01 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 14:03:04 | Nawalapitiya (Mahaweli Ganga) | 2.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 14:01:43 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 14:04:50 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-29 14:01:42 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 14:03:27 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-29 14:10:23 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-29 14:04:22 | Pitabeddara (Nilwala Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-06-29 14:08:01 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-29 14:00:55 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-29 14:03:01 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-29 14:02:33 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-29 14:05:34 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-06-29 14:01:04 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-29 14:06:05 | Peradeniya (Mahaweli Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-06-29 14:06:33 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-06-29 14:02:11 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-06-29 14:02:38 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-06-29 14:01:52 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.010 |  |
| 2026-06-29 14:01:17 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-06-29 14:00:50 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.011 |  |
| 2026-06-29 14:15:18 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-06-29 14:12:35 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.043 |  |
| 2026-06-29 14:02:36 | Deraniyagala (Kelani Ganga) | 1.99 | 🟢 Normal | -0.105 |  |
| 2026-06-29 14:04:59 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.179 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)