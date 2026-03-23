# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--23_10:21:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **105,084 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-23 10:21:00 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.055 |  |
| 2026-03-23 10:19:03 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-03-23 10:16:04 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-23 10:12:42 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-23 10:10:46 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-03-23 10:05:53 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-23 10:05:39 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-23 10:05:39 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.040 |  |
| 2026-03-23 10:05:30 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-23 10:05:17 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-03-23 10:05:06 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-03-23 10:04:48 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | -0.820 |  |
| 2026-03-23 10:04:22 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.039 |  |
| 2026-03-23 10:04:18 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-03-23 10:04:04 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-03-23 10:03:37 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.029 |  |
| 2026-03-23 10:03:33 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-23 10:03:28 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-23 10:03:25 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-23 10:03:22 | Nagalagam Street (Kelani Ganga) | 0.09 | 🟢 Normal | -0.034 |  |
| 2026-03-23 10:03:21 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.102 |  |
| 2026-03-23 10:03:20 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-23 10:03:17 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-23 10:02:35 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.030 |  |
| 2026-03-23 10:02:29 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-23 10:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.63 | 🟢 Normal | -0.050 |  |
| 2026-03-23 10:02:22 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-03-23 10:02:20 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.005 |  |
| 2026-03-23 10:02:15 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-23 10:02:11 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | -0.040 |  |
| 2026-03-23 10:02:10 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-03-23 10:01:51 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-23 10:01:35 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-23 10:01:32 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-23 10:01:26 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-23 10:01:16 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.104 |  |
| 2026-03-23 10:01:15 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-23 10:00:09 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | 0.200 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-23 10:05:17 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-03-23 10:00:09 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-03-23 10:03:33 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-23 10:05:30 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-23 10:19:03 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-03-23 10:03:25 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-23 10:01:26 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-23 10:03:20 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-23 10:12:42 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-23 10:01:35 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-23 10:01:15 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-23 10:01:51 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:01:52 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-23 10:16:04 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-23 10:05:39 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-23 10:02:15 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-23 10:03:28 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-23 10:04:18 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-03-23 10:10:46 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-03-23 10:01:32 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-23 10:02:29 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-23 10:03:17 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-23 10:04:04 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-03-23 10:05:53 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-23 10:02:20 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.005 |  |
| 2026-03-23 10:02:22 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-03-23 10:02:10 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-03-23 10:05:06 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-03-23 10:03:37 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.029 |  |
| 2026-03-23 10:02:35 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.030 |  |
| 2026-03-23 10:03:22 | Nagalagam Street (Kelani Ganga) | 0.09 | 🟢 Normal | -0.034 |  |
| 2026-03-23 10:04:22 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.039 |  |
| 2026-03-23 10:05:39 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.040 |  |
| 2026-03-23 10:02:11 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | -0.040 |  |
| 2026-03-23 10:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.63 | 🟢 Normal | -0.050 |  |
| 2026-03-23 10:21:00 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.055 |  |
| 2026-03-23 10:03:21 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.102 |  |
| 2026-03-23 10:01:16 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.104 |  |
| 2026-03-23 10:04:48 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | -0.820 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)