# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--07_16:05:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **118,732 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 16:05:05 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:05:02 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-07 16:04:44 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:03:48 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-07 16:03:34 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-07 16:03:27 | Manampitiya (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-04-07 16:03:24 | Panadugama (Nilwala Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:03:19 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-04-07 16:03:18 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:03:14 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:03:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:03:04 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-04-07 16:03:03 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:03:01 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:02:59 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:02:59 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:02:49 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:02:42 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.040 |  |
| 2026-04-07 16:02:41 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:02:40 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-07 16:02:08 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:02:00 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 16:01:51 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.132 |  |
| 2026-04-07 16:01:43 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:00:59 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:00:50 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 15:01:36 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-04-07 16:03:19 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-04-07 16:03:27 | Manampitiya (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-04-07 16:02:40 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-07 15:06:24 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-07 16:05:02 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-07 16:03:34 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-07 15:05:12 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-07 16:02:00 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 15:02:32 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 16:02:08 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:03:14 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:01:43 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:03:18 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:02:59 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:00:50 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:02:49 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:02:41 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:03:24 | Panadugama (Nilwala Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:03:01 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:04:44 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:05:05 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-07 15:05:00 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:00:59 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-04-07 15:07:44 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-07 14:08:46 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-07 15:07:08 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:03:03 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-07 15:04:08 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:03:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-04-07 16:03:48 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-07 16:03:04 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-04-07 15:02:55 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-04-07 15:04:13 | Rathnapura (Kalu Ganga) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-04-07 15:01:02 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | -0.013 |  |
| 2026-04-07 15:01:44 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | -0.020 |  |
| 2026-04-07 15:01:03 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | -0.022 |  |
| 2026-04-07 16:02:42 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.040 |  |
| 2026-04-07 16:01:51 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.132 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)