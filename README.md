# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--18_23:32:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **101,097 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-18 23:32:05 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-18 23:15:14 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.019 |  |
| 2026-03-18 23:11:55 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.037 |  |
| 2026-03-18 23:10:54 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 23:08:45 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-18 23:08:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-18 23:06:10 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-18 23:05:29 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-18 23:05:28 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-03-18 23:05:25 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-18 23:05:07 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 23:04:23 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-18 23:04:22 | Peradeniya (Mahaweli Ganga) | 2.36 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-18 23:04:02 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 23:03:47 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-18 23:03:41 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-18 23:03:09 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-18 23:03:01 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-18 23:02:57 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-03-18 23:02:54 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-18 23:02:52 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-18 23:02:36 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-18 23:02:35 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.005 |  |
| 2026-03-18 23:02:32 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 23:02:21 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-03-18 23:01:48 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-18 23:01:46 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 23:01:42 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-18 23:01:34 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-03-18 23:01:18 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 23:01:15 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-18 23:00:42 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-18 23:05:28 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-03-18 23:01:34 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-03-18 23:04:23 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-18 23:04:22 | Peradeniya (Mahaweli Ganga) | 2.36 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-18 23:08:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-18 23:01:15 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-18 23:02:36 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-18 23:02:52 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-18 23:05:25 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-18 23:08:45 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-18 23:01:18 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 23:02:32 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 23:04:02 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 23:02:35 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.005 |  |
| 2026-03-18 23:03:41 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-18 23:32:05 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-18 23:01:42 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-18 23:01:48 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-18 23:03:09 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:00:49 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 18:02:16 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 23:06:10 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:03:03 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:03:30 | Panadugama (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-03-18 23:10:54 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 23:03:01 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-18 23:05:29 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-18 23:03:47 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-18 23:02:54 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-18 23:05:07 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 18:02:03 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-18 23:01:46 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 23:00:42 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | -0.011 |  |
| 2026-03-18 23:15:14 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.019 |  |
| 2026-03-18 23:02:57 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-03-18 23:02:21 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-03-18 23:11:55 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.037 |  |
| 2026-03-18 18:02:41 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.088 |  |
| 2026-03-18 22:07:41 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)