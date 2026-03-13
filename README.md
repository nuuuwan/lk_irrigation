# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--14_00:14:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **96,669 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 00:14:12 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.109 |  |
| 2026-03-14 00:10:22 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -36.000 |  |
| 2026-03-14 00:10:21 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | -36.000 |  |
| 2026-03-14 00:10:20 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | -36.000 |  |
| 2026-03-14 00:09:15 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-14 00:07:54 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-03-14 00:07:20 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-14 00:06:50 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | -0.028 |  |
| 2026-03-14 00:06:45 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 00:05:23 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-14 00:05:18 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 00:05:14 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-03-14 00:04:55 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.092 |  |
| 2026-03-14 00:04:37 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.019 |  |
| 2026-03-14 00:04:23 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-14 00:04:15 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 00:04:09 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 00:03:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-14 00:03:49 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.030 |  |
| 2026-03-14 00:03:43 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.040 |  |
| 2026-03-14 00:03:43 | Badalgama (Maha Oya) | 1.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 00:03:41 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-03-14 00:02:57 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-03-14 00:02:49 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 00:02:49 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | -0.060 |  |
| 2026-03-14 00:02:34 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-03-14 00:02:10 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 00:01:52 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-03-14 00:01:38 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-14 00:01:35 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-14 00:00:55 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-03-13 23:24:02 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.028 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 00:02:34 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-03-14 00:03:41 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-03-14 00:00:55 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-03-14 00:05:14 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-03-14 00:03:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-14 00:04:09 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 00:06:45 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-13 23:01:21 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-14 00:02:49 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 00:05:18 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 00:03:43 | Badalgama (Maha Oya) | 1.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 00:04:15 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 23:07:45 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-14 00:05:23 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-14 00:01:38 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-14 00:01:35 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-14 00:07:20 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:00:33 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:03:14 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:13:35 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-03-14 00:04:23 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-14 00:07:54 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-03-14 00:02:10 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:02:49 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:05:00 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:02:59 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-14 00:09:15 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-14 00:01:52 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-03-14 00:02:57 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-03-13 22:06:58 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-03-14 00:04:37 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.019 |  |
| 2026-03-14 00:06:50 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | -0.028 |  |
| 2026-03-14 00:03:49 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.030 |  |
| 2026-03-14 00:03:43 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.040 |  |
| 2026-03-14 00:02:49 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | -0.060 |  |
| 2026-03-13 18:03:30 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.078 |  |
| 2026-03-14 00:04:55 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.092 |  |
| 2026-03-14 00:14:12 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.109 |  |
| 2026-03-14 00:10:22 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)