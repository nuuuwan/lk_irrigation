# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--19_15:17:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **183,696 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 15:17:18 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:09:15 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:06:59 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-06-19 15:06:19 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | -0.025 |  |
| 2026-06-19 15:06:17 | Nagalagam Street (Kelani Ganga) | 0.75 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-06-19 15:06:06 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-19 15:05:44 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | -0.010 |  |
| 2026-06-19 15:05:26 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.019 |  |
| 2026-06-19 15:05:20 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | -0.011 |  |
| 2026-06-19 15:05:10 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:05:08 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:04:40 | Dunamale (Aththanagalu Oya) | 2.17 | 🟢 Normal | -0.100 |  |
| 2026-06-19 15:04:35 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:04:12 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:03:58 | Rathnapura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-06-19 15:03:57 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.012 |  |
| 2026-06-19 15:03:46 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-06-19 15:03:31 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:03:26 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:03:24 | Hanwella (Kelani Ganga) | 2.48 | 🟢 Normal | -0.020 |  |
| 2026-06-19 15:03:18 | Glencourse (Kelani Ganga) | 10.46 | 🟢 Normal | -0.020 |  |
| 2026-06-19 15:03:10 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:03:03 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-06-19 15:02:23 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:02:18 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-19 15:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.06 | 🟢 Normal | -0.010 |  |
| 2026-06-19 15:02:12 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:02:12 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:02:00 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:01:56 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:01:19 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:01:12 | Ellagawa (Kalu Ganga) | 5.94 | 🟢 Normal | -0.011 |  |
| 2026-06-19 15:01:05 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:01:00 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:00:43 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-06-19 15:00:26 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:00:23 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-06-19 15:00:13 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | -0.010 |  |
| 2026-06-19 15:00:06 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-19 14:59:58 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.054 |  |
| 2026-06-19 14:34:26 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 15:06:17 | Nagalagam Street (Kelani Ganga) | 0.75 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-06-19 15:02:18 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-19 15:06:06 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-19 15:05:10 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:02:12 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:00:06 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:03:26 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:01:00 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:01:19 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:01:05 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:17:18 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:01:56 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:02:12 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:04:12 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:00:26 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:02:23 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:03:10 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:03:31 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:02:00 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:04:35 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:05:08 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-19 15:03:46 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-06-19 15:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.06 | 🟢 Normal | -0.010 |  |
| 2026-06-19 15:00:13 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | -0.010 |  |
| 2026-06-19 15:05:44 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | -0.010 |  |
| 2026-06-19 15:06:59 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-06-19 15:03:03 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-06-19 15:00:23 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-06-19 15:03:58 | Rathnapura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-06-19 15:00:43 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-06-19 15:05:20 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | -0.011 |  |
| 2026-06-19 15:01:12 | Ellagawa (Kalu Ganga) | 5.94 | 🟢 Normal | -0.011 |  |
| 2026-06-19 15:03:57 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.012 |  |
| 2026-06-19 15:05:26 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.019 |  |
| 2026-06-19 15:03:24 | Hanwella (Kelani Ganga) | 2.48 | 🟢 Normal | -0.020 |  |
| 2026-06-19 15:03:18 | Glencourse (Kelani Ganga) | 10.46 | 🟢 Normal | -0.020 |  |
| 2026-06-19 15:06:19 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | -0.025 |  |
| 2026-06-19 14:59:58 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.054 |  |
| 2026-06-19 15:04:40 | Dunamale (Aththanagalu Oya) | 2.17 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)