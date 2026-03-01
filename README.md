# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--01_08:05:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **86,067 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-01 08:05:47 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-01 08:05:14 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:04:56 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.096 |  |
| 2026-03-01 08:04:20 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:04:13 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 08:04:09 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-01 08:03:47 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:03:34 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:03:32 | Hanwella (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:03:15 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:02:51 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-03-01 08:02:51 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:02:23 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:02:10 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-03-01 08:01:57 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:01:36 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | -0.041 |  |
| 2026-03-01 08:01:35 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:01:32 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:01:31 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:01:27 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.408 | 🔺 Rising |
| 2026-03-01 08:01:16 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-01 08:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:01:02 | Weraganthota (Mahaweli Ganga) | -1.67 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-01 08:00:59 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:00:51 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:00:12 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 07:45:30 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-01 07:17:52 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-03-01 07:13:51 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | -0.008 |  |
| 2026-03-01 07:13:23 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-01 07:12:05 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-01 07:11:09 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-01 07:11:05 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-01 08:01:27 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.408 | 🔺 Rising |
| 2026-03-01 07:06:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-03-01 07:07:25 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-03-01 08:01:02 | Weraganthota (Mahaweli Ganga) | -1.67 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-01 08:04:09 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-01 08:05:47 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-01 08:01:16 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-01 08:04:13 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 08:01:31 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:00:51 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:02:23 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:03:15 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:00:12 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:04:20 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:05:14 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:03:32 | Hanwella (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:01:32 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-01 07:17:52 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:01:35 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:03:34 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:03:47 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:02:51 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-01 07:07:29 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-01 07:03:22 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:00:59 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 07:45:30 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-01 08:01:57 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 07:13:51 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | -0.008 |  |
| 2026-03-01 07:04:38 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.009 |  |
| 2026-03-01 08:02:51 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-03-01 07:04:59 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.019 |  |
| 2026-03-01 07:05:34 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.019 |  |
| 2026-03-01 08:02:10 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-03-01 08:01:36 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | -0.041 |  |
| 2026-03-01 07:00:51 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.052 |  |
| 2026-03-01 07:05:17 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.061 |  |
| 2026-03-01 07:08:45 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.071 |  |
| 2026-03-01 08:04:56 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)