# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--14_02:18:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **96,736 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 02:18:55 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-03-14 02:12:14 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-14 02:07:30 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -36.000 |  |
| 2026-03-14 02:07:29 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -36.000 |  |
| 2026-03-14 02:07:12 | Hanwella (Kelani Ganga) | 0.83 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 02:07:02 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.188 |  |
| 2026-03-14 02:06:10 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.016 |  |
| 2026-03-14 02:05:59 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-14 02:05:40 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-14 02:04:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 3.349 | 🔺 Rising |
| 2026-03-14 02:04:45 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 02:04:31 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 02:04:24 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 02:04:19 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | -36.000 |  |
| 2026-03-14 02:04:18 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -36.000 |  |
| 2026-03-14 02:04:17 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -36.000 |  |
| 2026-03-14 02:04:14 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 02:04:06 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-14 02:04:05 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 02:04:00 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 12.375 | 🔺 Rising |
| 2026-03-14 02:03:43 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-03-14 02:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | 3.349 | 🔺 Rising |
| 2026-03-14 02:03:30 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-03-14 02:03:28 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 12.375 | 🔺 Rising |
| 2026-03-14 02:03:01 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 02:02:54 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-03-14 02:02:46 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-14 02:02:19 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-14 02:01:37 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-03-14 02:01:27 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | -0.010 |  |
| 2026-03-14 02:01:11 | Glencourse (Kelani Ganga) | 8.97 | 🟢 Normal | -0.031 |  |
| 2026-03-14 02:01:08 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 02:00:50 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-14 02:00:26 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-14 02:00:14 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.079 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 02:04:00 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 12.375 | 🔺 Rising |
| 2026-03-14 02:04:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 3.349 | 🔺 Rising |
| 2026-03-14 02:02:46 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-14 01:01:19 | Peradeniya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-14 02:18:55 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-03-14 02:02:19 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-14 02:04:31 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 02:07:12 | Hanwella (Kelani Ganga) | 0.83 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 02:04:14 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 02:04:45 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 02:03:01 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 02:02:54 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-03-14 02:00:26 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-14 02:01:08 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 02:00:50 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-14 02:12:14 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:00:33 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:03:14 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-14 02:03:43 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-03-14 01:03:52 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-14 02:03:30 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-03-14 02:04:24 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 01:02:09 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-14 02:05:59 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:02:59 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-14 01:01:51 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-14 02:04:06 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-14 00:27:36 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.007 |  |
| 2026-03-14 02:05:40 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-14 02:01:27 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | -0.010 |  |
| 2026-03-14 02:06:10 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.016 |  |
| 2026-03-14 01:02:25 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.021 |  |
| 2026-03-14 02:01:37 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-03-14 02:01:11 | Glencourse (Kelani Ganga) | 8.97 | 🟢 Normal | -0.031 |  |
| 2026-03-13 18:03:30 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.078 |  |
| 2026-03-14 02:00:14 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.079 |  |
| 2026-03-14 02:07:02 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.188 |  |
| 2026-03-14 02:07:30 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -36.000 |  |
| 2026-03-14 02:04:19 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)