# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--15_17:13:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **207,076 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-15 17:13:21 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:11:05 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:09:36 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:08:54 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-07-15 17:07:18 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.019 |  |
| 2026-07-15 17:07:01 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:06:32 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.146 |  |
| 2026-07-15 17:06:15 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:05:22 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.020 |  |
| 2026-07-15 17:05:12 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-07-15 17:05:05 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:05:03 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:03:54 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:03:53 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:03:51 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-07-15 17:03:24 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:03:16 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:03:09 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:03:09 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-15 17:03:00 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.109 |  |
| 2026-07-15 17:02:57 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-15 17:02:54 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | -0.011 |  |
| 2026-07-15 17:02:43 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:02:35 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | -0.010 |  |
| 2026-07-15 17:02:15 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.060 |  |
| 2026-07-15 17:02:06 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-15 17:02:05 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.132 |  |
| 2026-07-15 17:02:00 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:01:58 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-07-15 17:01:50 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-15 17:01:50 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-07-15 17:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:01:24 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:01:09 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-07-15 17:01:08 | Thanthirimale (Malwathu Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-07-15 17:01:08 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:00:59 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:00:48 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:00:13 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-15 16:37:21 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-15 17:01:58 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-07-15 17:03:09 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-15 17:01:50 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-15 17:02:57 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-15 17:02:06 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-15 17:02:00 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:02:43 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:00:13 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:06:15 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:09:36 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:11:05 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:01:08 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:03:53 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:03:16 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:13:21 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-07-15 16:05:34 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:03:24 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:03:54 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:00:48 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:05:05 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:00:59 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:03:09 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:07:01 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-15 17:05:12 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-07-15 17:01:50 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-07-15 17:01:08 | Thanthirimale (Malwathu Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-07-15 17:02:35 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | -0.010 |  |
| 2026-07-15 17:01:09 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-07-15 17:02:54 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | -0.011 |  |
| 2026-07-15 17:07:18 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.019 |  |
| 2026-07-15 17:03:51 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-07-15 17:08:54 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-07-15 17:05:22 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.020 |  |
| 2026-07-15 16:11:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.038 |  |
| 2026-07-15 17:02:15 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.060 |  |
| 2026-07-15 17:03:00 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.109 |  |
| 2026-07-15 17:02:05 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.132 |  |
| 2026-07-15 17:06:32 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.146 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)