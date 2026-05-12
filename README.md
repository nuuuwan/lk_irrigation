# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_20:07:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **150,071 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 20:07:24 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.091 |  |
| 2026-05-12 20:06:20 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 20:04:13 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-12 20:04:11 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | -0.081 |  |
| 2026-05-12 20:03:44 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-12 20:03:40 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 20:03:33 | Katharagama (Menik Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-05-12 20:03:09 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 20:03:07 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | -0.010 |  |
| 2026-05-12 20:03:06 | Kuda Oya (Kirindi Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-05-12 20:03:01 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-05-12 20:03:00 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-12 20:02:44 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | 0.340 | 🔺 Rising |
| 2026-05-12 20:02:25 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-12 20:02:24 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-05-12 20:02:12 | Thanamalwila (Kirindi Oya) | 1.87 | 🟢 Normal | -0.030 |  |
| 2026-05-12 20:01:39 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-05-12 20:01:28 | Ellagawa (Kalu Ganga) | 5.46 | 🟢 Normal | -0.010 |  |
| 2026-05-12 20:01:24 | Thaldena (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.124 |  |
| 2026-05-12 20:01:07 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-05-12 20:01:06 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.050 |  |
| 2026-05-12 20:00:46 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 20:00:33 | Nakkala (Kumbukkan Oya) | 4.10 | 🟢 Normal | 1.114 | 🔺 Rising |
| 2026-05-12 20:00:13 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-12 19:17:45 | Magura (Kalu Ganga) | 3.58 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-05-12 19:15:08 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | -0.016 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 20:00:33 | Nakkala (Kumbukkan Oya) | 4.10 | 🟢 Normal | 1.114 | 🔺 Rising |
| 2026-05-12 20:02:44 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | 0.340 | 🔺 Rising |
| 2026-05-12 19:09:23 | Rathnapura (Kalu Ganga) | 3.05 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-05-12 20:03:01 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-05-12 19:17:45 | Magura (Kalu Ganga) | 3.58 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-05-12 19:04:45 | Glencourse (Kelani Ganga) | 10.38 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-12 19:10:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.12 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-05-12 19:01:23 | Panadugama (Nilwala Ganga) | 3.86 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-05-12 20:02:25 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-12 18:05:40 | Padiyathalawa (Maduru Oya) | 0.50 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-12 20:04:13 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-12 20:00:13 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-12 20:03:44 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-12 19:08:54 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-12 20:06:20 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 20:00:46 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 18:00:31 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-12 20:03:09 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 20:01:07 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-05-12 20:03:40 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 20:03:00 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-12 20:01:39 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-05-12 19:07:01 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-12 20:02:24 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-05-12 20:03:06 | Kuda Oya (Kirindi Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-05-12 20:03:33 | Katharagama (Menik Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-05-12 20:03:07 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | -0.010 |  |
| 2026-05-12 20:01:28 | Ellagawa (Kalu Ganga) | 5.46 | 🟢 Normal | -0.010 |  |
| 2026-05-12 19:15:08 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | -0.016 |  |
| 2026-05-12 19:12:15 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.018 |  |
| 2026-05-12 18:01:07 | Thanthirimale (Malwathu Oya) | 3.38 | 🟢 Normal | -0.020 |  |
| 2026-05-12 20:02:12 | Thanamalwila (Kirindi Oya) | 1.87 | 🟢 Normal | -0.030 |  |
| 2026-05-12 18:02:40 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.031 |  |
| 2026-05-12 20:01:06 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.050 |  |
| 2026-05-12 19:02:13 | Moragaswewa (Deduru Oya) | 1.80 | 🟢 Normal | -0.072 |  |
| 2026-05-12 20:04:11 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | -0.081 |  |
| 2026-05-12 20:07:24 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.091 |  |
| 2026-05-12 20:01:24 | Thaldena (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.124 |  |
| 2026-05-12 19:07:02 | Thawalama (Gin Ganga) | 3.49 | 🟢 Normal | -0.473 |  |

## River Water Level Charts by Station

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)