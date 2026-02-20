# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--21_00:34:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **78,601 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 00:34:50 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-21 00:19:08 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.014 |  |
| 2026-02-21 00:15:08 | Ellagawa (Kalu Ganga) | 4.33 | 🟢 Normal | 0.000 |  |
| 2026-02-21 00:10:31 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 3.429 | 🔺 Rising |
| 2026-02-21 00:10:10 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 3.429 | 🔺 Rising |
| 2026-02-21 00:09:06 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 00:07:44 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-21 00:06:40 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-21 00:06:14 | Magura (Kalu Ganga) | 1.99 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-02-21 00:06:03 | Glencourse (Kelani Ganga) | 8.23 | 🟢 Normal | -0.021 |  |
| 2026-02-21 00:05:15 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-21 00:05:13 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.151 |  |
| 2026-02-21 00:04:59 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-02-21 00:04:26 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 00:03:59 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-21 00:03:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.10 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-02-21 00:02:43 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-21 00:02:34 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-02-21 00:02:30 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-21 00:02:27 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-21 00:02:19 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-02-21 00:02:14 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-02-21 00:02:12 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-21 00:02:09 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 00:01:14 | Manampitiya (Mahaweli Ganga) | 3.06 | 🟡 Alert | -0.020 |  |
| 2026-02-21 00:10:31 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 3.429 | 🔺 Rising |
| 2026-02-21 00:01:26 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.279 | 🔺 Rising |
| 2026-02-21 00:03:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.10 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-02-21 00:06:14 | Magura (Kalu Ganga) | 1.99 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-02-21 00:00:18 | Padiyathalawa (Maduru Oya) | 2.03 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-02-21 00:01:27 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-21 00:04:59 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-02-21 00:02:43 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-21 00:02:12 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-21 00:01:22 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-21 00:01:28 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 00:07:44 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-21 00:02:09 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-02-21 00:05:15 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-21 00:01:30 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-21 00:04:26 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 00:01:40 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-20 18:04:38 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 00:01:31 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-21 00:02:30 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-21 00:15:08 | Ellagawa (Kalu Ganga) | 4.33 | 🟢 Normal | 0.000 |  |
| 2026-02-21 00:34:50 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-21 00:02:27 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-21 00:01:07 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-21 00:03:59 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-21 00:01:36 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-21 00:09:06 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 00:06:40 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-20 18:01:33 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:36:05 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.007 |  |
| 2026-02-21 00:02:34 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-02-21 00:02:19 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-02-21 00:00:35 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-02-21 00:02:14 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-02-21 00:19:08 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.014 |  |
| 2026-02-21 00:06:03 | Glencourse (Kelani Ganga) | 8.23 | 🟢 Normal | -0.021 |  |
| 2026-02-20 18:02:20 | Weraganthota (Mahaweli Ganga) | -1.32 | 🟢 Normal | -0.051 |  |
| 2026-02-21 00:05:13 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.151 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)