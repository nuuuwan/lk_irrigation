# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--23_09:11:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **213,908 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-23 09:11:06 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:10:08 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:09:03 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:08:04 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:06:43 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:05:43 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:05:06 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.019 |  |
| 2026-07-23 09:05:04 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-07-23 09:04:55 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:04:50 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-07-23 09:04:45 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:04:23 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:04:00 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:03:58 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:03:55 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.019 |  |
| 2026-07-23 09:03:47 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:03:43 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:03:26 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-07-23 09:03:26 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:03:09 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:02:52 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-23 09:02:43 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-07-23 09:02:43 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:02:41 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:02:39 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:02:33 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | -0.060 |  |
| 2026-07-23 09:02:26 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:02:26 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:02:19 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:02:06 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:01:48 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:01:48 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:01:47 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:01:36 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:01:30 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:01:25 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:00:54 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:00:50 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-07-23 09:00:49 | Nawalapitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:00:15 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-23 09:00:50 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-07-23 09:04:50 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-07-23 09:02:52 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-23 09:04:23 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:02:26 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:03:09 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:04:55 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:00:49 | Nawalapitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:01:47 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:02:06 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:09:03 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:04:45 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:03:43 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:03:47 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:06:43 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:01:25 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:08:04 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:05:43 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:00:15 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:00:54 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:02:43 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:02:33 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:01:30 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:03:58 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:02:41 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:01:48 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:02:39 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:03:26 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:04:00 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:11:06 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:01:36 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:02:26 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-23 09:05:04 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-07-23 08:00:45 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-07-23 09:02:43 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-07-23 09:03:55 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.019 |  |
| 2026-07-23 09:05:06 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.019 |  |
| 2026-07-23 09:03:26 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-07-23 09:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)