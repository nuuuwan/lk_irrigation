# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--18_11:08:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **76,334 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-18 11:08:00 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-02-18 11:05:35 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:05:12 | Manampitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-02-18 11:05:10 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:04:33 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.038 |  |
| 2026-02-18 11:04:20 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:04:18 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-02-18 11:04:16 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.021 |  |
| 2026-02-18 11:04:09 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:04:01 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:03:55 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.019 |  |
| 2026-02-18 11:03:33 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-18 11:03:31 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.011 |  |
| 2026-02-18 11:03:12 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:03:11 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:03:10 | Putupaula (Kalu Ganga) | 0.24 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-18 11:03:00 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:02:59 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-02-18 11:02:46 | Thawalama (Gin Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:02:37 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:02:28 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:02:27 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:02:26 | Moragaswewa (Deduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:02:19 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-02-18 11:02:17 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | -0.030 |  |
| 2026-02-18 11:02:00 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.062 |  |
| 2026-02-18 11:01:45 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:01:45 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:01:45 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:01:26 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 11:01:23 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 11:01:10 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.066 |  |
| 2026-02-18 11:01:05 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-02-18 11:00:50 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-02-18 11:00:10 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.075 |  |
| 2026-02-18 11:00:09 | Padiyathalawa (Maduru Oya) | 2.05 | 🟢 Normal | 0.094 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-18 11:02:19 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-02-18 11:05:12 | Manampitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-02-18 11:00:09 | Padiyathalawa (Maduru Oya) | 2.05 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-02-18 11:02:59 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-02-18 11:03:10 | Putupaula (Kalu Ganga) | 0.24 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-18 11:03:33 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-18 11:01:26 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 11:01:23 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 11:02:28 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:02:26 | Moragaswewa (Deduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:10:23 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:01:45 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:04:01 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:05:35 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:02:27 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:01:45 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:03:11 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:04:09 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:04:20 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:02:17 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:03:12 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:03:00 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:05:10 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:01:45 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:02:46 | Thawalama (Gin Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-02-18 10:11:24 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:02:37 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-18 11:00:50 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-02-18 11:01:05 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-02-18 11:04:18 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-02-18 11:08:00 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-02-18 11:03:31 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.011 |  |
| 2026-02-18 11:03:55 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.019 |  |
| 2026-02-18 11:04:16 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.021 |  |
| 2026-02-18 11:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | -0.030 |  |
| 2026-02-18 11:04:33 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.038 |  |
| 2026-02-18 11:02:00 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.062 |  |
| 2026-02-18 11:01:10 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.066 |  |
| 2026-02-18 11:00:10 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.075 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)