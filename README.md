# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--12_12:14:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **177,347 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **3** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 12:14:04 | Thalgahagoda (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-12 12:08:34 | Pitabeddara (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.056 |  |
| 2026-06-12 12:08:24 | Giriulla (Maha Oya) | 2.53 | 🟢 Normal | -0.018 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 12:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.66 | 🟡 Alert | 0.060 | 🔺 Rising |
| 2026-06-12 12:05:36 | Magura (Kalu Ganga) | 4.81 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-06-12 12:04:35 | Rathnapura (Kalu Ganga) | 5.54 | 🟡 Alert | -0.117 |  |
| 2026-06-12 12:01:10 | Ellagawa (Kalu Ganga) | 8.04 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-12 12:04:53 | Badalgama (Maha Oya) | 3.41 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-06-12 12:03:59 | Putupaula (Kalu Ganga) | 2.02 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-06-12 12:14:04 | Thalgahagoda (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-12 12:03:10 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-06-12 12:01:07 | Panadugama (Nilwala Ganga) | 4.10 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-12 12:03:38 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-12 12:05:08 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-12 12:05:28 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-12 12:03:21 | Hanwella (Kelani Ganga) | 4.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 12:01:30 | Nagalagam Street (Kelani Ganga) | 0.96 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-12 12:02:07 | Moraketiya (Walawe Ganga) | 1.60 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-12 12:02:16 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-12 12:00:20 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-12 12:01:35 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-12 12:03:13 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-12 11:00:32 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-12 12:01:12 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-12 12:05:10 | Dunamale (Aththanagalu Oya) | 3.22 | 🟢 Normal | 0.000 |  |
| 2026-06-12 12:01:21 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-12 11:05:44 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-12 12:00:13 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.010 |  |
| 2026-06-12 12:03:30 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-06-12 12:08:24 | Giriulla (Maha Oya) | 2.53 | 🟢 Normal | -0.018 |  |
| 2026-06-12 12:03:05 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.020 |  |
| 2026-06-12 12:02:51 | Nawalapitiya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.020 |  |
| 2026-06-12 12:02:43 | Glencourse (Kelani Ganga) | 12.08 | 🟢 Normal | -0.041 |  |
| 2026-06-12 12:06:55 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.050 |  |
| 2026-06-12 12:03:05 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.051 |  |
| 2026-06-12 12:07:29 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.051 |  |
| 2026-06-12 12:02:07 | Deraniyagala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.051 |  |
| 2026-06-12 12:00:57 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.051 |  |
| 2026-06-12 12:08:34 | Pitabeddara (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.056 |  |
| 2026-06-12 12:01:09 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | -0.065 |  |
| 2026-06-12 12:05:22 | Holombuwa (Kelani Ganga) | 1.38 | 🟢 Normal | -0.093 |  |
| 2026-06-12 12:05:27 | Thawalama (Gin Ganga) | 3.23 | 🟢 Normal | -0.248 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)