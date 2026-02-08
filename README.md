# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--09_02:34:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **67,956 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 02:34:34 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-09 02:34:06 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-09 02:24:17 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-09 02:21:12 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | 11.058 | 🔺 Rising |
| 2026-02-09 02:11:13 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 11.058 | 🔺 Rising |
| 2026-02-09 02:09:17 | Peradeniya (Mahaweli Ganga) | 2.17 | 🟢 Normal | -0.211 |  |
| 2026-02-09 02:09:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-02-09 02:07:43 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.013 |  |
| 2026-02-09 02:07:24 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-09 02:05:57 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 02:04:45 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-09 02:04:24 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.022 |  |
| 2026-02-09 02:03:44 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-02-09 02:03:17 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-09 02:03:03 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-09 02:03:01 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-09 02:02:42 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-02-09 02:02:39 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.030 |  |
| 2026-02-09 02:02:36 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-02-09 02:02:30 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-09 02:02:20 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-02-09 02:02:16 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-02-09 02:01:48 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-09 02:01:39 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-09 02:01:27 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.010 |  |
| 2026-02-09 02:01:00 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-02-09 01:47:30 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 02:21:12 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | 11.058 | 🔺 Rising |
| 2026-02-09 02:02:36 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-02-09 02:02:16 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-02-09 02:09:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-02-09 02:24:17 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-09 02:03:01 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-09 00:10:45 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-09 02:01:39 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-09 01:28:08 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-09 02:07:24 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-09 02:03:03 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:02:44 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-09 02:34:34 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-08 22:03:44 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-09 02:02:30 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-09 02:03:17 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:05:11 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-09 02:05:57 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 02:34:06 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-09 02:04:45 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:30:39 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-09 01:01:09 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-09 02:01:48 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-09 02:03:44 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-02-08 18:03:48 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-02-09 02:02:42 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-02-09 01:01:14 | Manampitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-02-09 02:01:27 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.010 |  |
| 2026-02-09 02:01:00 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-02-09 01:00:49 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-02-09 01:03:30 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-02-09 02:07:43 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.013 |  |
| 2026-02-09 01:13:08 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | -0.018 |  |
| 2026-02-09 02:02:20 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-02-09 02:04:24 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.022 |  |
| 2026-02-09 02:02:39 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.030 |  |
| 2026-02-08 18:02:12 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.187 |  |
| 2026-02-09 02:09:17 | Peradeniya (Mahaweli Ganga) | 2.17 | 🟢 Normal | -0.211 |  |
| 2026-02-09 00:04:00 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)