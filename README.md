# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--16_11:04:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **98,845 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 11:04:23 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-03-16 11:03:35 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-16 11:03:32 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-03-16 11:03:32 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-16 11:03:17 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.030 |  |
| 2026-03-16 11:03:05 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-16 11:02:57 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-16 11:02:46 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-03-16 11:02:43 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-03-16 11:02:35 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-03-16 11:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.41 | 🟢 Normal | -0.040 |  |
| 2026-03-16 11:02:06 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-16 11:01:50 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-03-16 11:01:49 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-16 11:01:48 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-16 11:01:37 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-16 11:01:18 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.023 |  |
| 2026-03-16 11:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-03-16 11:01:09 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 11:01:09 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-03-16 11:01:05 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 11:00:59 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-16 11:00:55 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 11:00:50 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-03-16 11:00:34 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-03-16 11:00:23 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | -0.125 |  |
| 2026-03-16 10:17:41 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -0.017 |  |
| 2026-03-16 10:13:04 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:11:09 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:10:46 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | -0.009 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 11:04:23 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-03-16 11:01:50 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-03-16 11:00:34 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-03-16 11:00:50 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-03-16 11:03:32 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-16 11:01:49 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-16 10:02:01 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-16 10:04:56 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-16 11:01:05 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 11:01:09 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 11:03:35 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-16 11:00:55 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:11:09 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:13:04 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:07:30 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 11:02:57 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:08:42 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:03:13 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-16 11:03:05 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-16 11:02:06 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-16 11:01:37 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:04:31 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:03:24 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 11:00:59 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-16 09:05:43 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-16 11:02:46 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:10:46 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | -0.009 |  |
| 2026-03-16 11:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-03-16 11:03:32 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-03-16 10:01:40 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-03-16 11:02:35 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-03-16 11:01:09 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-03-16 11:02:43 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-03-16 10:17:41 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -0.017 |  |
| 2026-03-16 11:01:18 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.023 |  |
| 2026-03-16 11:03:17 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.030 |  |
| 2026-03-16 11:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.41 | 🟢 Normal | -0.040 |  |
| 2026-03-16 10:06:48 | Baddegama (Gin Ganga) | 0.71 | 🟢 Normal | -0.061 |  |
| 2026-03-16 11:00:23 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | -0.125 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)