# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--21_12:05:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **157,838 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 12:05:24 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-21 12:05:17 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:04:40 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:04:34 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:04:24 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:04:24 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.039 |  |
| 2026-05-21 12:04:20 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:03:43 | Moragaswewa (Deduru Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:03:40 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:03:30 | Hanwella (Kelani Ganga) | 1.87 | 🟢 Normal | -0.070 |  |
| 2026-05-21 12:03:25 | Thanthirimale (Malwathu Oya) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-05-21 12:03:13 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-05-21 12:03:11 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-05-21 12:03:06 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:03:03 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.11 | 🟢 Normal | -0.010 |  |
| 2026-05-21 12:02:38 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-05-21 12:02:36 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:02:34 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | -0.011 |  |
| 2026-05-21 12:02:28 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:02:25 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:02:20 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:01:39 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-05-21 12:01:35 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:01:13 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:01:10 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:01:09 | Peradeniya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:01:08 | Ellagawa (Kalu Ganga) | 5.59 | 🟢 Normal | -0.030 |  |
| 2026-05-21 12:01:08 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:00:40 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:00:22 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:00:17 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.020 |  |
| 2026-05-21 12:00:10 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 11:01:58 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-05-21 12:05:24 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-21 12:01:13 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:00:10 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:03:43 | Moragaswewa (Deduru Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:00:22 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:03:03 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:00:40 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:02:28 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 11:04:29 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:02:36 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:03:40 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:02:20 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-21 11:03:03 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-05-21 11:01:18 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:04:24 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:01:35 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:01:08 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:01:10 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:03:06 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:05:17 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:04:20 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:01:09 | Peradeniya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:04:40 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:04:34 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-21 11:03:12 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-05-21 12:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.11 | 🟢 Normal | -0.010 |  |
| 2026-05-21 12:03:11 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-05-21 12:02:38 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-05-21 11:08:58 | Rathnapura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-05-21 12:02:34 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | -0.011 |  |
| 2026-05-21 12:03:25 | Thanthirimale (Malwathu Oya) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-05-21 12:00:17 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.020 |  |
| 2026-05-21 12:01:39 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-05-21 12:03:13 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-05-21 11:08:04 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.028 |  |
| 2026-05-21 12:01:08 | Ellagawa (Kalu Ganga) | 5.59 | 🟢 Normal | -0.030 |  |
| 2026-05-21 12:04:24 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.039 |  |
| 2026-05-21 12:03:30 | Hanwella (Kelani Ganga) | 1.87 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)