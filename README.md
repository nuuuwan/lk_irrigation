# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--03_15:26:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **196,238 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-03 15:26:42 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:13:36 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:11:47 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:09:33 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:07:46 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-03 15:07:38 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:07:15 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:07:09 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.013 |  |
| 2026-07-03 15:06:43 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 15:06:34 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-07-03 15:05:39 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:05:35 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:05:13 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:04:44 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:04:43 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:04:40 | Hanwella (Kelani Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:04:38 | Moragaswewa (Deduru Oya) | 0.09 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-03 15:04:17 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:04:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | -0.019 |  |
| 2026-07-03 15:04:04 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-07-03 15:03:45 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:03:43 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:03:18 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-03 15:03:03 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-03 15:02:57 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-07-03 15:02:34 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:02:34 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:02:32 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:02:21 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-03 15:02:12 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:01:41 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:01:39 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:01:34 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:01:30 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.085 |  |
| 2026-07-03 15:01:30 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:01:20 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-07-03 15:01:19 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:01:00 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-07-03 15:00:56 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:00:40 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.031 |  |
| 2026-07-03 15:00:13 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-03 15:04:04 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-07-03 15:02:57 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-07-03 15:02:21 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-03 15:01:20 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-07-03 15:03:18 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-03 15:03:03 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-03 15:06:43 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 15:07:46 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-03 15:04:38 | Moragaswewa (Deduru Oya) | 0.09 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-03 15:04:17 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:26:42 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:02:32 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:01:19 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:05:13 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:00:56 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:07:38 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:01:41 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:03:45 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:04:40 | Hanwella (Kelani Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:01:39 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:13:36 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:01:30 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:02:34 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:04:43 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:04:44 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:09:33 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:07:15 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:02:12 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:05:35 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:02:34 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:05:39 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:11:47 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-03 15:01:00 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-07-03 15:06:34 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-07-03 15:00:13 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.010 |  |
| 2026-07-03 15:07:09 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.013 |  |
| 2026-07-03 15:04:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | -0.019 |  |
| 2026-07-03 15:00:40 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.031 |  |
| 2026-07-03 15:01:30 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.085 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)