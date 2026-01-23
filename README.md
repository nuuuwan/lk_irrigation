# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--24_02:14:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **53,936 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-24 02:14:15 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:14:01 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-24 02:12:46 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:10:22 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:08:52 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-01-24 02:08:42 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:08:30 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-01-24 02:07:46 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:07:37 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:07:06 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:07:02 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:06:53 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:06:51 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:06:44 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:04:19 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-01-24 02:03:38 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:03:15 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 02:03:11 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.331 |  |
| 2026-01-24 02:03:03 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-01-24 02:02:50 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:02:17 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:01:57 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:01:29 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:00:38 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-24 02:08:30 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-01-24 02:08:52 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-01-24 02:14:01 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-24 02:03:15 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 01:01:39 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 00:01:16 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:03:38 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:02:50 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-24 01:02:01 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:02:17 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:01:57 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-01-23 18:03:40 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:08:42 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:00:38 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | 0.000 |  |
| 2026-01-24 01:06:30 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-24 01:11:42 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:06:53 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:07:46 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:06:44 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:14:15 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:07:37 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:10:22 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:12:46 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:01:29 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-24 01:12:31 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-24 00:03:40 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-01-24 02:07:02 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-23 20:01:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-24 01:05:10 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-01-23 18:01:34 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-01-24 02:03:03 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-01-24 01:02:33 | Padiyathalawa (Maduru Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-01-24 02:04:19 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-01-23 23:00:15 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.012 |  |
| 2026-01-24 01:03:14 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.043 |  |
| 2026-01-24 00:06:51 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.052 |  |
| 2026-01-24 01:04:37 | Peradeniya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.059 |  |
| 2026-01-23 18:01:26 | Weraganthota (Mahaweli Ganga) | -2.21 | 🟢 Normal | -0.081 |  |
| 2026-01-24 02:03:11 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.331 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)