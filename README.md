# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--25_08:36:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **106,786 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-25 08:36:50 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:29:38 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.063 |  |
| 2026-03-25 08:14:49 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:07:03 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-25 08:07:01 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.028 |  |
| 2026-03-25 08:06:28 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-25 08:06:11 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-03-25 08:06:07 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.050 |  |
| 2026-03-25 08:05:30 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-03-25 08:05:27 | Weraganthota (Mahaweli Ganga) | -1.85 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-03-25 08:04:25 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:04:25 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:04:24 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:03:50 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:03:46 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-25 08:03:37 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:03:24 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-25 08:03:24 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:03:19 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-25 08:03:07 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-25 08:02:49 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:02:47 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-03-25 08:02:33 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:02:33 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | -0.041 |  |
| 2026-03-25 08:02:29 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:02:24 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.61 | 🟢 Normal | -0.060 |  |
| 2026-03-25 08:02:09 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:02:03 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.040 |  |
| 2026-03-25 08:01:56 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-03-25 08:01:52 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-03-25 08:01:50 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-03-25 08:01:47 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-25 08:05:27 | Weraganthota (Mahaweli Ganga) | -1.85 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-03-25 08:03:24 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-25 08:03:46 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-25 08:06:28 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-25 08:07:03 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-25 08:03:19 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-25 08:03:07 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-25 08:02:09 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:00:48 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:01:30 | Moragaswewa (Deduru Oya) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:01:39 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:02:33 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:00:47 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:04:25 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:04:25 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:03:24 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:03:50 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:01:47 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:04:24 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:01:28 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:02:24 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:02:49 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:03:37 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:00:55 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:14:49 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:36:50 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:02:29 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-25 08:05:30 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-03-25 08:01:52 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-03-25 08:02:47 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-03-25 08:06:11 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-03-25 08:01:50 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-03-25 08:01:56 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-03-25 08:07:01 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.028 |  |
| 2026-03-25 08:02:03 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.040 |  |
| 2026-03-25 08:02:33 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | -0.041 |  |
| 2026-03-25 08:06:07 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.050 |  |
| 2026-03-25 08:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.61 | 🟢 Normal | -0.060 |  |
| 2026-03-25 08:29:38 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.063 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)