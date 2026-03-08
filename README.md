# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--08_15:15:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **92,641 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-08 15:15:10 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:13:55 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:09:17 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.047 |  |
| 2026-03-08 15:08:09 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | -0.020 |  |
| 2026-03-08 15:06:45 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:06:04 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-03-08 15:05:29 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:05:22 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:04:52 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.026 |  |
| 2026-03-08 15:04:39 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:04:39 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:03:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | -0.022 |  |
| 2026-03-08 15:03:38 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:03:33 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-08 15:03:31 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:03:24 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | -0.081 |  |
| 2026-03-08 15:03:19 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-03-08 15:03:18 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-03-08 15:03:16 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-08 15:03:05 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.035 |  |
| 2026-03-08 15:03:04 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:02:52 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:02:52 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.022 |  |
| 2026-03-08 15:02:46 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:02:45 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:02:35 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:02:31 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-03-08 15:02:12 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | -0.030 |  |
| 2026-03-08 15:01:54 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-03-08 15:01:46 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:01:17 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-03-08 15:01:16 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:01:08 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.030 |  |
| 2026-03-08 15:01:02 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 15:01:01 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:01:00 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:00:41 | Thanthirimale (Malwathu Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-03-08 14:56:45 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-08 15:03:18 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-03-08 15:02:31 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-03-08 15:06:04 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-03-08 15:01:02 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 15:03:33 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-08 15:04:39 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:02:45 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:05:22 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:02:46 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:01:01 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-08 14:02:03 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:13:55 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:05:29 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-08 13:03:11 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:01:00 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:01:46 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:02:35 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:02:52 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:03:31 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:15:10 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:03:38 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:04:39 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:03:04 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:06:45 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:01:16 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-08 15:03:19 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-03-08 15:03:16 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-08 15:00:41 | Thanthirimale (Malwathu Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-03-08 15:01:54 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-03-08 15:01:17 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-03-08 15:08:09 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | -0.020 |  |
| 2026-03-08 15:02:52 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.022 |  |
| 2026-03-08 15:03:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | -0.022 |  |
| 2026-03-08 15:04:52 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.026 |  |
| 2026-03-08 15:02:12 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | -0.030 |  |
| 2026-03-08 15:01:08 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.030 |  |
| 2026-03-08 15:03:05 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.035 |  |
| 2026-03-08 15:09:17 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.047 |  |
| 2026-03-08 15:03:24 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)