# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--22_23:17:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **104,686 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-22 23:17:31 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-03-22 23:14:54 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | -0.010 |  |
| 2026-03-22 23:14:31 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.009 |  |
| 2026-03-22 23:11:04 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:10:45 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.096 |  |
| 2026-03-22 23:08:32 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:08:27 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.058 |  |
| 2026-03-22 23:07:35 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.019 |  |
| 2026-03-22 23:06:10 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:05:39 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-03-22 23:05:26 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-22 23:04:21 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:03:22 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:03:08 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-03-22 23:03:07 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:02:27 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:02:26 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:02:25 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:02:20 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:02:19 | Glencourse (Kelani Ganga) | 8.26 | 🟢 Normal | -0.020 |  |
| 2026-03-22 23:02:17 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-03-22 23:02:13 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:02:12 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.030 |  |
| 2026-03-22 23:02:02 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:02:00 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:01:30 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-03-22 23:00:43 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:00:38 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:00:15 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-03-22 22:40:36 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:34:15 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.058 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-22 23:17:31 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-03-22 23:03:08 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-03-22 23:05:26 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-22 23:02:00 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:03:07 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:02:20 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:00:38 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:04:21 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-22 18:00:06 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:03:53 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:03:22 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:08:36 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:02:02 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:01:27 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:02:25 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:02:26 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:06:10 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:02:13 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:08:32 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:00:43 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-22 18:01:37 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:11:04 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:02:27 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-22 22:02:09 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-22 23:14:31 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.009 |  |
| 2026-03-22 23:05:39 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-03-22 23:14:54 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | -0.010 |  |
| 2026-03-22 23:00:15 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-03-22 23:07:35 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.019 |  |
| 2026-03-22 23:02:19 | Glencourse (Kelani Ganga) | 8.26 | 🟢 Normal | -0.020 |  |
| 2026-03-22 23:01:30 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-03-22 23:02:17 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-03-22 22:02:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.026 |  |
| 2026-03-22 23:02:12 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.030 |  |
| 2026-03-22 18:01:26 | Weraganthota (Mahaweli Ganga) | -2.91 | 🟢 Normal | -0.051 |  |
| 2026-03-22 23:08:27 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.058 |  |
| 2026-03-22 22:34:15 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.058 |  |
| 2026-03-22 23:10:45 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)