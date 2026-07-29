# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--29_22:20:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **219,766 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-29 22:20:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -0.032 |  |
| 2026-07-29 22:15:11 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.011 |  |
| 2026-07-29 22:10:18 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:09:45 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-07-29 22:09:34 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.067 |  |
| 2026-07-29 22:08:13 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:07:00 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:06:33 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:06:12 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.041 |  |
| 2026-07-29 22:06:05 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-07-29 22:05:48 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.030 |  |
| 2026-07-29 22:05:17 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:04:59 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:04:13 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.112 |  |
| 2026-07-29 22:03:50 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.019 |  |
| 2026-07-29 22:03:30 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:03:20 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:03:14 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:03:05 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:02:43 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:02:43 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:02:42 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 22:02:29 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:02:16 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:02:02 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:01:34 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:01:32 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 22:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-07-29 22:01:15 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:01:15 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | -0.042 |  |
| 2026-07-29 22:01:12 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:00:48 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-29 21:04:42 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.315 | 🔺 Rising |
| 2026-07-29 22:06:05 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-07-29 22:09:45 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-07-29 21:00:39 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-29 22:01:32 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 22:02:42 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 22:01:34 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:02:02 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:00:48 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:04:13 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:02:16 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:01:12 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 18:01:46 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:10:18 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:02:43 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:03:20 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:05:17 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:08:13 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:03:09 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:07:00 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:02:43 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:03:14 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:04:59 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:06:33 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:03:05 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:03:56 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:01:15 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:03:30 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-29 18:01:01 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | -0.005 |  |
| 2026-07-29 22:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-07-29 22:15:11 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.011 |  |
| 2026-07-29 22:03:50 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.019 |  |
| 2026-07-29 22:05:48 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.030 |  |
| 2026-07-29 22:20:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -0.032 |  |
| 2026-07-29 18:00:16 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.034 |  |
| 2026-07-29 22:06:12 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.041 |  |
| 2026-07-29 22:01:15 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | -0.042 |  |
| 2026-07-29 22:09:34 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.067 |  |
| 2026-07-29 22:04:13 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)