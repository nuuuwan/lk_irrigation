# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--21_18:10:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **212,448 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-21 18:10:46 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:09:35 | Baddegama (Gin Ganga) | 0.74 | 🟢 Normal | -0.040 |  |
| 2026-07-21 18:08:00 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:07:58 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:07:53 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:07:24 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:07:04 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-21 18:06:51 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:06:44 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.047 |  |
| 2026-07-21 18:05:47 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:04:58 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.028 |  |
| 2026-07-21 18:03:57 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:03:51 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:03:51 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:03:37 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:03:37 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.025 |  |
| 2026-07-21 18:03:21 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:02:34 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:02:22 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-07-21 18:02:16 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:02:15 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-07-21 18:02:04 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-07-21 18:02:01 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-07-21 18:02:00 | Thanthirimale (Malwathu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:01:58 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:01:26 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:01:23 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:01:16 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:01:12 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-07-21 18:01:10 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:01:10 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:00:56 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.354 | 🔺 Rising |
| 2026-07-21 18:00:46 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.014 |  |
| 2026-07-21 18:00:22 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-07-21 18:00:09 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-07-21 18:00:08 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-07-21 17:55:46 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-21 18:00:56 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.354 | 🔺 Rising |
| 2026-07-21 18:01:12 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-07-21 18:00:08 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-07-21 18:00:09 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-07-21 18:00:22 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-07-21 18:07:04 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-21 18:10:46 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:01:58 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:02:34 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-21 17:01:46 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:03:51 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:01:10 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:03:57 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:03:51 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:01:16 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:03:37 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:01:26 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:03:21 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:06:51 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:02:22 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:07:53 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:05:47 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:01:10 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:08:00 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:02:00 | Thanthirimale (Malwathu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:07:24 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:07:58 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:01:23 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:02:16 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-21 18:02:04 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-07-21 18:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-07-21 18:02:01 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-07-21 18:00:46 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.014 |  |
| 2026-07-21 18:02:15 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-07-21 18:03:37 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.025 |  |
| 2026-07-21 18:04:58 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.028 |  |
| 2026-07-21 18:09:35 | Baddegama (Gin Ganga) | 0.74 | 🟢 Normal | -0.040 |  |
| 2026-07-21 18:06:44 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.047 |  |
| 2026-07-21 17:02:10 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.073 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)