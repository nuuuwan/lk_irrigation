# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--08_00:09:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **200,164 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-08 00:09:19 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:08:44 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:08:14 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-07-08 00:08:12 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:07:17 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.102 |  |
| 2026-07-08 00:06:52 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:06:10 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:05:40 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:05:36 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:05:15 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.351 | 🔺 Rising |
| 2026-07-08 00:04:54 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | -0.019 |  |
| 2026-07-08 00:04:51 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:04:49 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:04:23 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:04:04 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.052 |  |
| 2026-07-08 00:03:59 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-07-08 00:03:49 | Ellagawa (Kalu Ganga) | 4.61 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:03:47 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-08 00:03:22 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.075 |  |
| 2026-07-08 00:03:11 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:03:00 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-08 00:02:32 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.040 |  |
| 2026-07-08 00:02:07 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:02:02 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:01:19 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:01:02 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:00:42 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:29:56 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-07-07 23:29:08 | Glencourse (Kelani Ganga) | 9.58 | 🟢 Normal | -0.052 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-08 00:05:15 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.351 | 🔺 Rising |
| 2026-07-08 00:08:14 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-07-08 00:03:47 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-08 00:03:00 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-07 18:04:20 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:08:12 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:01:02 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:04:51 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:04:38 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:01:39 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:04:49 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:00:55 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:03:00 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:06:52 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:08:44 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:03:49 | Ellagawa (Kalu Ganga) | 4.61 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:05:36 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:01:19 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:02:22 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:06:10 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:04:41 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:02:07 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:03:11 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:00:42 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:05:40 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:01:02 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:04:23 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:01:26 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-08 00:09:19 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-07 22:01:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-07-07 23:13:54 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.009 |  |
| 2026-07-08 00:03:59 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-07-08 00:04:54 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | -0.019 |  |
| 2026-07-07 21:02:22 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.031 |  |
| 2026-07-08 00:02:32 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.040 |  |
| 2026-07-08 00:04:04 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.052 |  |
| 2026-07-07 23:07:21 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.052 |  |
| 2026-07-08 00:03:22 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.075 |  |
| 2026-07-08 00:07:17 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.102 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)