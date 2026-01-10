# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--11_01:43:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **42,252 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 01:43:27 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-11 01:36:14 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-11 01:31:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-11 01:14:49 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-11 01:11:40 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-11 01:08:06 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-11 01:07:02 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.028 |  |
| 2026-01-11 01:06:57 | Katharagama (Menik Ganga) | 0.59 | 🟢 Normal | -0.068 |  |
| 2026-01-11 01:05:43 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 01:03:54 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-01-11 01:03:37 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | -0.011 |  |
| 2026-01-11 01:03:32 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-11 01:03:30 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-01-11 01:03:30 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-11 01:03:25 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-11 01:02:58 | Horowpothana (Yan Oya) | 2.68 | 🟢 Normal | -0.010 |  |
| 2026-01-11 01:02:52 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-11 01:02:50 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-01-11 01:02:40 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | 0.000 |  |
| 2026-01-11 01:02:37 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-01-11 01:02:30 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.091 |  |
| 2026-01-11 01:02:21 | Padiyathalawa (Maduru Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-01-11 01:02:08 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 01:01:55 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-01-11 01:01:46 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-11 01:01:16 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.101 |  |
| 2026-01-11 01:01:12 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-01-11 01:01:09 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-11 01:01:06 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 23:57:45 | Urawa (Nilwala Ganga) | 5.00 | 🟠 Minor Flood | 5.266 | 🔺 Rising |
| 2026-01-11 01:31:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-11 01:36:14 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-11 01:03:32 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-11 01:05:43 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 01:43:27 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-11 01:03:54 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-01-11 01:08:06 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-11 00:01:28 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 01:02:08 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 00:01:09 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-11 01:11:40 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:04:22 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-11 01:14:49 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-11 01:03:25 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-11 01:02:40 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | 0.000 |  |
| 2026-01-11 01:03:30 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-01-11 01:01:46 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-11 01:03:30 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-11 00:13:17 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-11 01:01:06 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:01:35 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-11 00:01:29 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-11 01:01:09 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-11 01:02:52 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-11 00:04:08 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-01-11 01:01:12 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-01-11 01:02:21 | Padiyathalawa (Maduru Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-01-11 01:01:55 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-01-11 01:02:58 | Horowpothana (Yan Oya) | 2.68 | 🟢 Normal | -0.010 |  |
| 2026-01-11 00:04:34 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-01-11 01:03:37 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | -0.011 |  |
| 2026-01-10 18:02:45 | Weraganthota (Mahaweli Ganga) | -1.40 | 🟢 Normal | -0.020 |  |
| 2026-01-11 01:02:50 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-01-11 01:02:37 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-01-11 01:07:02 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.028 |  |
| 2026-01-11 01:06:57 | Katharagama (Menik Ganga) | 0.59 | 🟢 Normal | -0.068 |  |
| 2026-01-11 01:02:30 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.091 |  |
| 2026-01-11 01:01:16 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)