# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--24_05:11:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **81,489 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 05:11:20 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-24 05:10:06 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-24 05:09:33 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.075 |  |
| 2026-02-24 05:08:20 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-24 05:08:11 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.018 |  |
| 2026-02-24 05:07:37 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | -0.005 |  |
| 2026-02-24 05:07:27 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.018 |  |
| 2026-02-24 05:06:09 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.100 |  |
| 2026-02-24 05:05:49 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-02-24 05:05:47 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-02-24 05:05:44 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-24 05:05:40 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-02-24 05:03:59 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.048 |  |
| 2026-02-24 05:03:18 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-02-24 05:03:07 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-24 05:03:02 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.059 |  |
| 2026-02-24 05:03:01 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-02-24 05:03:00 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-02-24 05:02:55 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-02-24 05:02:45 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-02-24 05:02:24 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 05:02:11 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 1.002 | 🔺 Rising |
| 2026-02-24 05:01:52 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-02-24 05:01:16 | Ellagawa (Kalu Ganga) | 4.54 | 🟢 Normal | -0.020 |  |
| 2026-02-24 05:01:11 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-02-24 05:01:09 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-02-24 05:00:37 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-24 05:00:27 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-24 05:00:12 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | -0.051 |  |
| 2026-02-24 04:23:39 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 05:05:49 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-02-24 05:02:11 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 1.002 | 🔺 Rising |
| 2026-02-24 04:07:55 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-24 04:08:23 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-02-24 04:02:44 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-24 05:02:24 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 05:00:27 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-24 05:00:37 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:02:59 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-24 05:03:07 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-24 05:08:20 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-24 05:11:20 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-24 05:05:44 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-24 05:10:06 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-24 04:01:11 | Manampitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:02:43 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-02-24 03:13:45 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-02-24 05:07:37 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | -0.005 |  |
| 2026-02-24 05:02:55 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-02-24 05:05:40 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-02-24 05:02:45 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-02-24 05:01:11 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-02-24 05:03:18 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-02-24 05:03:00 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-02-24 04:03:37 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-02-24 05:01:52 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-02-24 05:01:09 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-02-24 05:03:01 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-02-24 04:01:35 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.014 |  |
| 2026-02-24 05:08:11 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.018 |  |
| 2026-02-24 05:07:27 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.018 |  |
| 2026-02-24 05:01:16 | Ellagawa (Kalu Ganga) | 4.54 | 🟢 Normal | -0.020 |  |
| 2026-02-23 18:03:52 | Weraganthota (Mahaweli Ganga) | -1.92 | 🟢 Normal | -0.028 |  |
| 2026-02-24 05:03:59 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.048 |  |
| 2026-02-24 05:00:12 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | -0.051 |  |
| 2026-02-24 05:03:02 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.059 |  |
| 2026-02-24 05:09:33 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.075 |  |
| 2026-02-24 04:09:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.42 | 🟢 Normal | -0.085 |  |
| 2026-02-24 05:06:09 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)