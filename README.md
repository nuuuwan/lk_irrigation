# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_03:46:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **130,703 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 03:46:32 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | 240.000 | 🔺 Rising |
| 2026-04-21 03:46:29 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | 240.000 | 🔺 Rising |
| 2026-04-21 03:45:01 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.025 |  |
| 2026-04-21 03:33:20 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-21 03:33:19 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-21 03:18:27 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-21 03:14:49 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-21 03:07:56 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | -0.123 |  |
| 2026-04-21 03:07:42 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.127 |  |
| 2026-04-21 03:06:21 | Rathnapura (Kalu Ganga) | 3.17 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-04-21 03:06:05 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 03:02:32 | Thanamalwila (Kirindi Oya) | 4.27 | 🟡 Alert | -0.101 |  |
| 2026-04-21 03:46:32 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | 240.000 | 🔺 Rising |
| 2026-04-21 02:48:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.345 | 🔺 Rising |
| 2026-04-21 03:03:00 | Glencourse (Kelani Ganga) | 10.62 | 🟢 Normal | 0.321 | 🔺 Rising |
| 2026-04-21 03:06:21 | Rathnapura (Kalu Ganga) | 3.17 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-04-20 18:03:54 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-21 03:04:09 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-04-21 02:02:44 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-04-21 03:04:17 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-04-21 03:04:38 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-04-21 03:03:34 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-21 02:22:05 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-21 03:02:53 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-20 18:11:39 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-21 03:14:49 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-21 03:06:05 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 03:02:32 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 03:02:34 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-21 02:01:17 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-21 03:01:53 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-21 03:18:27 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-21 03:33:20 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-21 03:01:10 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-21 02:02:03 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-21 03:03:52 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-20 18:01:44 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-04-21 03:05:11 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.019 |  |
| 2026-04-21 03:45:01 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.025 |  |
| 2026-04-21 03:04:01 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.029 |  |
| 2026-04-21 03:03:25 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.039 |  |
| 2026-04-21 03:02:24 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | -0.040 |  |
| 2026-04-21 03:02:53 | Manampitiya (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.049 |  |
| 2026-04-21 03:05:17 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | -0.067 |  |
| 2026-04-21 03:07:56 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | -0.123 |  |
| 2026-04-21 03:07:42 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.127 |  |
| 2026-04-21 03:03:46 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | -0.184 |  |
| 2026-04-21 02:11:43 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.216 |  |
| 2026-04-21 03:03:19 | Peradeniya (Mahaweli Ganga) | 2.36 | 🟢 Normal | -0.399 |  |
| 2026-04-21 03:05:05 | Kuda Oya (Kirindi Oya) | 3.58 | 🟢 Normal | -0.583 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)