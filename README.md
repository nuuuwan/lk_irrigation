# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--16_00:21:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **207,325 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-16 00:21:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-07-16 00:21:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-07-16 00:20:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-07-16 00:12:31 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-07-16 00:08:06 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-07-16 00:06:48 | Putupaula (Kalu Ganga) | 0.19 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-07-16 00:05:24 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:05:07 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:04:57 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-07-16 00:04:50 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:04:26 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:04:22 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:04:06 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-07-16 00:03:41 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:03:40 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:03:17 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:02:58 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:02:57 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:02:48 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:02:46 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:02:37 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-07-16 00:02:34 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:02:21 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:02:16 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:02:08 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:02:07 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.048 |  |
| 2026-07-16 00:01:57 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:01:53 | Glencourse (Kelani Ganga) | 9.06 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-07-16 00:00:58 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-07-16 00:00:55 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:00:51 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:00:28 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:00:23 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-16 00:21:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-07-16 00:01:53 | Glencourse (Kelani Ganga) | 9.06 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-07-16 00:04:57 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-07-16 00:12:31 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-07-16 00:06:48 | Putupaula (Kalu Ganga) | 0.19 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-07-16 00:02:21 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-07-15 23:01:09 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:00:51 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:00:54 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:02:08 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:03:41 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:02:48 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-15 18:02:45 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 23:04:47 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:05:07 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:04:22 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:04:50 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:00:23 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:05:24 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:00:28 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:03:17 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:02:34 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:02:58 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:02:16 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:03:40 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:01:57 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:00:55 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:02:57 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:09:20 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:02:46 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-16 00:04:26 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-15 18:14:35 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | -0.008 |  |
| 2026-07-16 00:08:06 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-07-16 00:04:06 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-07-16 00:00:58 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-07-15 23:03:37 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-07-16 00:02:37 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-07-16 00:02:07 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.048 |  |
| 2026-07-15 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)