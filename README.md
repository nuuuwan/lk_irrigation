# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--12_15:09:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **177,464 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 15:09:24 | Rathnapura (Kalu Ganga) | 5.34 | 🟡 Alert | -0.018 |  |
| 2026-06-12 15:09:15 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-12 15:09:15 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-06-12 15:09:08 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-12 15:07:58 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-06-12 15:07:54 | Ellagawa (Kalu Ganga) | 8.14 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-12 15:07:03 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.009 |  |
| 2026-06-12 15:06:21 | Holombuwa (Kelani Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-12 15:06:18 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-12 15:06:15 | Dunamale (Aththanagalu Oya) | 3.20 | 🟢 Normal | -0.019 |  |
| 2026-06-12 15:06:11 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-06-12 15:06:10 | Glencourse (Kelani Ganga) | 11.83 | 🟢 Normal | -0.096 |  |
| 2026-06-12 15:05:50 | Magura (Kalu Ganga) | 4.77 | 🟡 Alert | -0.032 |  |
| 2026-06-12 15:05:31 | Badalgama (Maha Oya) | 3.55 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 15:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.83 | 🟡 Alert | 0.060 | 🔺 Rising |
| 2026-06-12 15:09:24 | Rathnapura (Kalu Ganga) | 5.34 | 🟡 Alert | -0.018 |  |
| 2026-06-12 15:05:50 | Magura (Kalu Ganga) | 4.77 | 🟡 Alert | -0.032 |  |
| 2026-06-12 15:09:15 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-06-12 15:03:27 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-12 14:18:57 | Baddegama (Gin Ganga) | 2.75 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-12 15:01:11 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-12 15:05:31 | Badalgama (Maha Oya) | 3.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-12 15:09:15 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-12 15:02:51 | Putupaula (Kalu Ganga) | 2.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-12 15:02:43 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 15:06:18 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-12 15:07:54 | Ellagawa (Kalu Ganga) | 8.14 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-12 15:03:15 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-12 15:00:41 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-12 15:00:29 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-12 15:01:39 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-12 15:02:43 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-12 15:09:08 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-12 15:01:34 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-12 15:03:14 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-06-12 15:06:21 | Holombuwa (Kelani Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-12 15:02:59 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-12 15:03:58 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-12 15:06:11 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-06-12 15:07:03 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.009 |  |
| 2026-06-12 15:03:33 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-06-12 15:02:07 | Panadugama (Nilwala Ganga) | 4.14 | 🟢 Normal | -0.010 |  |
| 2026-06-12 15:03:47 | Hanwella (Kelani Ganga) | 4.02 | 🟢 Normal | -0.010 |  |
| 2026-06-12 15:00:26 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.010 |  |
| 2026-06-12 15:02:24 | Giriulla (Maha Oya) | 2.49 | 🟢 Normal | -0.011 |  |
| 2026-06-12 15:06:15 | Dunamale (Aththanagalu Oya) | 3.20 | 🟢 Normal | -0.019 |  |
| 2026-06-12 15:07:58 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-06-12 15:01:09 | Peradeniya (Mahaweli Ganga) | 2.21 | 🟢 Normal | -0.031 |  |
| 2026-06-12 15:04:34 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.060 |  |
| 2026-06-12 15:02:02 | Moraketiya (Walawe Ganga) | 1.51 | 🟢 Normal | -0.070 |  |
| 2026-06-12 15:02:41 | Thawalama (Gin Ganga) | 2.94 | 🟢 Normal | -0.083 |  |
| 2026-06-12 15:03:04 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.089 |  |
| 2026-06-12 15:06:10 | Glencourse (Kelani Ganga) | 11.83 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)