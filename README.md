# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--07_23:14:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **200,135 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-07 23:14:07 | Ellagawa (Kalu Ganga) | 4.61 | 🟢 Normal | -0.009 |  |
| 2026-07-07 23:13:54 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.009 |  |
| 2026-07-07 23:13:27 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:10:24 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:09:58 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:07:21 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.052 |  |
| 2026-07-07 23:07:05 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 1.456 | 🔺 Rising |
| 2026-07-07 23:06:08 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | -0.011 |  |
| 2026-07-07 23:05:26 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:04:48 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:04:41 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:04:38 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:04:37 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:04:24 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:03:58 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:03:31 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-07-07 23:03:10 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-07-07 23:03:09 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-07-07 23:03:02 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:03:01 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:02:45 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-07-07 23:02:25 | Hanwella (Kelani Ganga) | 1.29 | 🟢 Normal | -0.030 |  |
| 2026-07-07 23:02:22 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:02:09 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-07 23:01:44 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-07 23:01:39 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:01:26 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:01:08 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:00:55 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:00:17 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:59:40 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 1.456 | 🔺 Rising |
| 2026-07-07 22:41:31 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-07 23:07:05 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 1.456 | 🔺 Rising |
| 2026-07-07 23:02:45 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-07-07 23:02:09 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-07 23:01:44 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-07 22:06:57 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-07 18:04:20 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:00:17 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:01:08 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:01:52 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:04:38 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:01:39 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:00:55 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:03:00 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:06:25 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:10:24 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:03:01 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:14:00 | Glencourse (Kelani Ganga) | 9.58 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:03:02 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:04:24 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:02:22 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:03:58 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:04:41 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:13:27 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:09:58 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:04:37 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:01:02 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:05:26 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:01:26 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:01:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:13:54 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.009 |  |
| 2026-07-07 23:14:07 | Ellagawa (Kalu Ganga) | 4.61 | 🟢 Normal | -0.009 |  |
| 2026-07-07 23:03:09 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-07-07 23:03:10 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-07-07 23:03:31 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-07-07 23:06:08 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | -0.011 |  |
| 2026-07-07 23:02:25 | Hanwella (Kelani Ganga) | 1.29 | 🟢 Normal | -0.030 |  |
| 2026-07-07 21:02:22 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.031 |  |
| 2026-07-07 23:07:21 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.052 |  |
| 2026-07-07 22:02:08 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.124 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)