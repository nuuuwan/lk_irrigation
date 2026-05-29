# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--29_18:08:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **165,033 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **6** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 18:08:18 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:08:13 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-05-29 18:07:54 | Magura (Kalu Ganga) | 4.08 | 🟡 Alert | -0.134 |  |
| 2026-05-29 18:07:22 | Panadugama (Nilwala Ganga) | 4.44 | 🟢 Normal | -0.030 |  |
| 2026-05-29 18:06:46 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:06:09 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.061 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 18:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-29 18:07:54 | Magura (Kalu Ganga) | 4.08 | 🟡 Alert | -0.134 |  |
| 2026-05-29 18:08:13 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-05-29 18:00:20 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-29 18:04:34 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-29 18:03:18 | Dunamale (Aththanagalu Oya) | 1.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-29 18:02:28 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 18:00:30 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 18:02:01 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:03:07 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:04:37 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:02:14 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:04:21 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:02:19 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:02:22 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:02:24 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:02:28 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:05:15 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:08:18 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:06:46 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:01:26 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:02:17 | Putupaula (Kalu Ganga) | 2.72 | 🟢 Normal | -0.010 |  |
| 2026-05-29 18:02:36 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-05-29 18:01:51 | Baddegama (Gin Ganga) | 3.33 | 🟢 Normal | -0.010 |  |
| 2026-05-29 18:01:31 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-05-29 18:02:15 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.012 |  |
| 2026-05-29 18:04:53 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.014 |  |
| 2026-05-29 18:04:17 | Ellagawa (Kalu Ganga) | 8.50 | 🟢 Normal | -0.019 |  |
| 2026-05-29 18:04:44 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-05-29 18:02:28 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-05-29 18:01:46 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.022 |  |
| 2026-05-29 18:07:22 | Panadugama (Nilwala Ganga) | 4.44 | 🟢 Normal | -0.030 |  |
| 2026-05-29 18:02:31 | Deraniyagala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.030 |  |
| 2026-05-29 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.034 |  |
| 2026-05-29 18:02:18 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | -0.045 |  |
| 2026-05-29 18:04:32 | Glencourse (Kelani Ganga) | 11.25 | 🟢 Normal | -0.054 |  |
| 2026-05-29 18:03:27 | Hanwella (Kelani Ganga) | 3.60 | 🟢 Normal | -0.057 |  |
| 2026-05-29 18:06:09 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.061 |  |
| 2026-05-29 18:04:36 | Rathnapura (Kalu Ganga) | 3.98 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)