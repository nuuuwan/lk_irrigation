# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--22_22:08:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **104,650 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-22 22:08:36 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:08:28 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.147 |  |
| 2026-03-22 22:08:26 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:07:00 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.092 |  |
| 2026-03-22 22:06:53 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-22 22:06:28 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-22 22:05:40 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.077 |  |
| 2026-03-22 22:05:35 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:05:09 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:05:01 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-03-22 22:03:53 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:03:43 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-03-22 22:03:26 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.033 |  |
| 2026-03-22 22:03:21 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:03:09 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-03-22 22:02:56 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-03-22 22:02:39 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:02:37 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-03-22 22:02:17 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-03-22 22:02:13 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:02:09 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:02:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.026 |  |
| 2026-03-22 22:01:55 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:01:33 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-22 22:01:28 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | -0.020 |  |
| 2026-03-22 22:01:27 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:01:14 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.031 |  |
| 2026-03-22 22:01:12 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:01:04 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:00:43 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-03-22 22:00:33 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-22 21:03:24 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-03-22 22:06:28 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-22 22:01:33 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-22 22:02:13 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:01:04 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-22 21:02:13 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:02:39 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:00:33 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-22 18:00:06 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:03:53 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:03:21 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-22 21:16:05 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:08:36 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:01:55 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:05:35 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:01:27 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:08:26 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:05:09 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:01:12 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-22 18:01:37 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-03-22 21:07:02 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-22 21:02:14 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:02:09 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:02:37 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-03-22 22:06:53 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-22 22:03:43 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-03-22 22:02:56 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-03-22 22:00:43 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-03-22 22:03:09 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-03-22 22:05:01 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-03-22 22:01:28 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | -0.020 |  |
| 2026-03-22 22:02:17 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-03-22 22:02:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.026 |  |
| 2026-03-22 22:01:14 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.031 |  |
| 2026-03-22 22:03:26 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.033 |  |
| 2026-03-22 18:01:26 | Weraganthota (Mahaweli Ganga) | -2.91 | 🟢 Normal | -0.051 |  |
| 2026-03-22 22:05:40 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.077 |  |
| 2026-03-22 22:07:00 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.092 |  |
| 2026-03-22 22:08:28 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.147 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)