# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--12_05:18:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **95,059 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 05:18:39 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.005 |  |
| 2026-03-12 05:11:28 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.015 |  |
| 2026-03-12 05:09:41 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:08:55 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:08:38 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:08:23 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-03-12 05:06:38 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:06:24 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:06:01 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.094 |  |
| 2026-03-12 05:05:34 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.029 |  |
| 2026-03-12 05:05:24 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:05:24 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:04:40 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 05:04:27 | Thawalama (Gin Ganga) | 0.84 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-12 05:04:02 | Badalgama (Maha Oya) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-03-12 05:03:50 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:03:24 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-03-12 05:03:15 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-03-12 05:02:55 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 05:02:55 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:02:41 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.018 |  |
| 2026-03-12 05:02:38 | Glencourse (Kelani Ganga) | 9.59 | 🟢 Normal | 1.232 | 🔺 Rising |
| 2026-03-12 05:02:34 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:02:25 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:02:11 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:02:11 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 05:02:08 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:01:59 | Peradeniya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.078 |  |
| 2026-03-12 05:01:48 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:01:05 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-12 05:00:58 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:58:27 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:56:14 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 05:02:38 | Glencourse (Kelani Ganga) | 9.59 | 🟢 Normal | 1.232 | 🔺 Rising |
| 2026-03-12 05:01:05 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-12 05:04:27 | Thawalama (Gin Ganga) | 0.84 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-12 04:08:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-12 05:03:15 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-03-12 03:00:16 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-12 05:02:55 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 05:04:40 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 05:02:11 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 05:18:39 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.005 |  |
| 2026-03-12 05:05:24 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:02:11 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:01:48 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:02:08 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:08:55 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:02:34 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:02:23⌛ | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:06:24 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:02:55 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:02:25 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:03:50 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:06:38 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:01:35 | Moraketiya (Walawe Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 04:03:51 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:08:38 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:05:24 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:09:41 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:00:58 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:00:47⌛ | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:04:02 | Badalgama (Maha Oya) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-03-12 05:08:23 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-03-12 05:03:24 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-03-12 05:11:28 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.015 |  |
| 2026-03-12 05:02:41 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.018 |  |
| 2026-03-12 05:05:34 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.029 |  |
| 2026-03-12 05:01:59 | Peradeniya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.078 |  |
| 2026-03-10 18:02:53⌛ | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | -0.088 |  |
| 2026-03-12 05:06:01 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.094 |  |
| 2026-03-12 03:12:26 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -35.426 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)