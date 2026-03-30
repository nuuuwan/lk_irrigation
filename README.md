# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_02:46:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **111,941 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-31 02:46:36 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:15:46 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-03-31 02:11:25 | Hanwella (Kelani Ganga) | 0.20 | 🟢 Normal | -0.018 |  |
| 2026-03-31 02:09:23 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:06:51 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-31 02:06:05 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:06:00 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 02:05:52 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:05:26 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:04:57 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 02:04:49 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 02:04:33 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:04:03 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:03:57 | Badalgama (Maha Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:03:56 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.029 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-31 02:01:11 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-03-31 02:06:51 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-31 02:03:26 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 02:01:00 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 02:04:57 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 02:06:00 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 02:04:49 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 18:07:18 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-31 02:02:33 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:05:52 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:03:08 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:00:15 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:03:03 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:02:10 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:46:36 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-31 01:06:07 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:06:05 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:01:42 | Ellagawa (Kalu Ganga) | 3.67 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:03:20 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:04:33 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-31 01:01:17 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:02:17 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:04:03 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:03:57 | Badalgama (Maha Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:00:50 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:00:22 | Manampitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:00:31 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:05:26 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:09:23 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:02:46 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-30 21:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:15:46 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-03-31 02:11:25 | Hanwella (Kelani Ganga) | 0.20 | 🟢 Normal | -0.018 |  |
| 2026-03-31 01:02:52 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.021 |  |
| 2026-03-31 02:03:56 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.029 |  |
| 2026-03-31 02:02:27 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | -0.032 |  |
| 2026-03-30 18:03:12 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.049 |  |
| 2026-03-31 02:01:07 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.050 |  |
| 2026-03-31 02:00:11 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.158 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)