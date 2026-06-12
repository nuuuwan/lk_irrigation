# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--12_21:20:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **177,691 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **4** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 21:20:08 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.008 |  |
| 2026-06-12 21:10:26 | Rathnapura (Kalu Ganga) | 6.71 | 🟡 Alert | -0.039 |  |
| 2026-06-12 21:08:58 | Holombuwa (Kelani Ganga) | 1.72 | 🟢 Normal | -0.020 |  |
| 2026-06-12 21:08:43 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.029 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 21:01:58 | Magura (Kalu Ganga) | 4.68 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-06-12 21:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.08 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-06-12 21:10:26 | Rathnapura (Kalu Ganga) | 6.71 | 🟡 Alert | -0.039 |  |
| 2026-06-12 21:06:08 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.328 | 🔺 Rising |
| 2026-06-12 21:03:21 | Urawa (Nilwala Ganga) | 1.82 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-06-12 21:04:51 | Glencourse (Kelani Ganga) | 11.90 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-06-12 21:00:54 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-06-12 21:02:29 | Panadugama (Nilwala Ganga) | 4.31 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-06-12 21:03:14 | Thawalama (Gin Ganga) | 3.67 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-06-12 21:05:06 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-12 21:05:05 | Ellagawa (Kalu Ganga) | 8.31 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-12 18:04:11 | Galgamuwa (Mee Oya) | 0.51 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-12 21:07:32 | Baddegama (Gin Ganga) | 2.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 21:01:27 | Putupaula (Kalu Ganga) | 2.19 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-12 18:02:22 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-12 21:01:24 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-12 21:01:18 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-12 20:07:38 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-12 21:02:07 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-12 21:01:35 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-12 21:00:26 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-12 21:03:11 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-12 21:01:08 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-12 21:02:41 | Dunamale (Aththanagalu Oya) | 3.06 | 🟢 Normal | 0.000 |  |
| 2026-06-12 21:03:24 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-12 21:02:43 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-06-12 21:03:57 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:19:51 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-12 21:02:43 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-12 21:20:08 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.008 |  |
| 2026-06-12 21:03:27 | Giriulla (Maha Oya) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-06-12 21:02:46 | Badalgama (Maha Oya) | 3.49 | 🟢 Normal | -0.011 |  |
| 2026-06-12 21:08:58 | Holombuwa (Kelani Ganga) | 1.72 | 🟢 Normal | -0.020 |  |
| 2026-06-12 21:02:34 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-06-12 21:04:15 | Hanwella (Kelani Ganga) | 3.82 | 🟢 Normal | -0.021 |  |
| 2026-06-12 21:08:43 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.029 |  |
| 2026-06-12 21:04:00 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.092 |  |
| 2026-06-12 21:02:52 | Nawalapitiya (Mahaweli Ganga) | 2.21 | 🟢 Normal | -0.113 |  |
| 2026-06-12 21:02:33 | Deraniyagala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.172 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)