# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--12_05:10:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **70,741 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 05:10:31 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:09:52 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-02-12 05:08:26 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:05:50 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:04:42 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-12 05:04:26 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 05:04:11 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:04:03 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-02-12 05:04:00 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-02-12 05:03:59 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | -0.011 |  |
| 2026-02-12 05:03:59 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-02-12 05:03:58 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-02-12 05:03:57 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-02-12 05:03:56 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-02-12 05:03:55 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-02-12 05:03:53 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-02-12 05:03:34 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:03:27 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:03:14 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:02:53 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:02:50 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:02:20 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:02:07 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-12 05:01:49 | Kithulgala (Kelani Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:01:31 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:01:21 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:01:09 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:01:07 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-02-12 05:01:05 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:01:05 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.111 |  |
| 2026-02-12 05:00:58 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:00:48 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:00:32 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-02-12 04:29:50 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-02-12 04:28:24 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-12 04:22:08 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 05:04:00 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-02-12 04:06:54 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-02-12 04:29:50 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-02-12 05:04:42 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-12 05:04:26 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 04:04:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 04:02:59 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-02-12 05:01:49 | Kithulgala (Kelani Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:01:09 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:00:58 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:02:20 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:02:50 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:02:53 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:01:05 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:03:14 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:01:21 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:10:31 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:01:23 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:08:26 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:00:59 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:03:34 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:04:34 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:12:13 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:04:11 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:00:48 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:01:31 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:05:50 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:09:52 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-02-12 05:03:59 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-02-12 05:04:03 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-02-11 18:05:25 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-02-12 05:02:07 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-11 18:01:13 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-02-12 05:00:32 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-02-11 18:04:22 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | -0.010 |  |
| 2026-02-12 04:04:05 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.011 |  |
| 2026-02-12 05:03:59 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | -0.011 |  |
| 2026-02-12 05:01:07 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-02-12 05:01:05 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)