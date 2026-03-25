# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--25_12:07:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **106,941 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-25 12:07:00 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:06:07 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-25 12:06:06 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:05:38 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:05:24 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-25 12:05:20 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-03-25 12:04:35 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:04:23 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:04:19 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.023 |  |
| 2026-03-25 12:04:18 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-25 12:03:58 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:03:43 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:03:39 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:03:30 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.049 |  |
| 2026-03-25 12:03:30 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:03:24 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-03-25 12:03:12 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:03:07 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-03-25 12:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-03-25 12:02:58 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-25 12:02:55 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:02:51 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:02:29 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.041 |  |
| 2026-03-25 12:02:23 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.012 |  |
| 2026-03-25 12:02:08 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-03-25 12:01:59 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:01:56 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-25 12:01:36 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:01:31 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:01:28 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:01:24 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.067 |  |
| 2026-03-25 12:01:23 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:01:18 | Weraganthota (Mahaweli Ganga) | -2.29 | 🟢 Normal | -0.229 |  |
| 2026-03-25 12:00:45 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:00:36 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:00:20 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.084 |  |
| 2026-03-25 12:00:09 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-03-25 11:49:47 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-25 11:37:57 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-25 11:18:00 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-25 11:16:27 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.067 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-25 12:06:07 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-25 12:01:56 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-25 11:06:33 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-25 12:05:24 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-25 12:02:58 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-25 12:04:18 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-25 12:03:43 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:00:45 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-25 11:37:57 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:01:23 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:01:59 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:07:00 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:01:28 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:06:06 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:03:12 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:03:30 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:01:36 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:02:51 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:02:55 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:03:58 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:04:23 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:03:39 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:04:35 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:00:36 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-25 11:05:21 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:05:38 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:03:24 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-03-25 12:05:20 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-03-25 12:00:09 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-03-25 12:02:23 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.012 |  |
| 2026-03-25 12:02:08 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-03-25 12:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-03-25 12:03:07 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-03-25 12:04:19 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.023 |  |
| 2026-03-25 12:02:29 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.041 |  |
| 2026-03-25 12:03:30 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.049 |  |
| 2026-03-25 12:01:24 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.067 |  |
| 2026-03-25 12:00:20 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.084 |  |
| 2026-03-25 12:01:18 | Weraganthota (Mahaweli Ganga) | -2.29 | 🟢 Normal | -0.229 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)