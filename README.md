# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--10_03:20:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **41,424 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 03:20:37 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-10 03:19:13 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:18:53 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:14:48 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -9.931 |  |
| 2026-01-10 03:14:19 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -9.931 |  |
| 2026-01-10 03:14:05 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:14:05 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:13:14 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | -0.009 |  |
| 2026-01-10 03:12:51 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:12:36 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-01-10 03:12:09 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:09:31 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | -72.000 |  |
| 2026-01-10 03:09:30 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | -72.000 |  |
| 2026-01-10 03:08:22 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-10 03:08:04 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-10 03:08:01 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-01-10 03:07:33 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-10 03:06:51 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:06:27 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.279 |  |
| 2026-01-10 03:06:14 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:05:57 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-01-10 03:05:40 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:05:39 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:05:38 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:05:33 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 03:05:18 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 03:05:11 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:03:54 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:02:35 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:02:24 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-10 03:02:19 | Manampitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.031 |  |
| 2026-01-10 03:02:16 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-10 03:02:11 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:01:55 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-01-10 03:01:28 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:01:11 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:01:08 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:00:42 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-01-10 03:00:37 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.025 |  |
| 2026-01-10 02:45:11 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.175 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 03:12:36 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-01-10 03:07:33 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-10 03:02:16 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-10 02:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-10 03:02:24 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-09 17:13:03 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-10 03:08:22 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-10 03:05:18 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 03:05:33 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 03:08:04 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-10 03:20:37 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-10 03:02:35 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:18:53 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:06:14 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:03:54 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:19:13 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:01:28 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:03:29 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-10 00:01:50 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:02:11 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:01:11 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:14:05 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:12:09 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:12:51 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:05:40 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:06:51 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-10 03:13:14 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | -0.009 |  |
| 2026-01-10 03:05:57 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-01-10 03:08:01 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-01-09 18:00:08 | Weraganthota (Mahaweli Ganga) | -1.21 | 🟢 Normal | -0.010 |  |
| 2026-01-09 18:08:00 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-01-10 03:01:55 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-01-10 03:00:42 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-01-10 03:00:37 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.025 |  |
| 2026-01-10 03:02:19 | Manampitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.031 |  |
| 2026-01-10 03:06:27 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.279 |  |
| 2026-01-10 03:14:48 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -9.931 |  |
| 2026-01-10 03:09:31 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)