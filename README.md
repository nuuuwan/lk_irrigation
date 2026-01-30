# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--30_10:26:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **59,631 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-30 10:26:31 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:21:51 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:13:46 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:12:06 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:11:35 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:09:43 | Thawalama (Gin Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:09:25 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:09:07 | Thawalama (Gin Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:06:52 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-30 10:06:28 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-01-30 10:06:06 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:05:31 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.261 |  |
| 2026-01-30 10:05:09 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-01-30 10:05:08 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-30 10:04:53 | Weraganthota (Mahaweli Ganga) | -2.23 | 🟢 Normal | -0.068 |  |
| 2026-01-30 10:04:46 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:04:30 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-01-30 10:04:22 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:04:03 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 10:03:33 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:03:33 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-30 10:03:31 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | -0.020 |  |
| 2026-01-30 10:03:19 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:02:55 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-01-30 10:02:55 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:02:50 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:02:45 | Manampitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.050 |  |
| 2026-01-30 10:02:39 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:02:31 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:02:28 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:02:22 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-30 10:02:22 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-01-30 10:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.35 | 🟢 Normal | -0.050 |  |
| 2026-01-30 10:02:05 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 10:01:48 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:01:45 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 10:01:40 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 10:00:45 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.032 |  |
| 2026-01-30 10:00:40 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-30 10:06:28 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-01-30 10:02:55 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-01-30 10:05:08 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-30 10:03:33 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-30 10:02:22 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-30 10:04:03 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 10:01:45 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 10:02:05 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 10:01:40 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 10:06:52 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-30 10:02:22 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-01-30 10:01:48 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-30 09:00:47 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:04:22 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:04:46 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:11:35 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:02:39 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:21:51 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:06:06 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:02:55 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:26:31 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:09:25 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:12:06 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:02:50 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:03:19 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:02:31 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:02:28 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:09:43 | Thawalama (Gin Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:13:46 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:03:33 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:00:40 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-30 10:05:09 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-01-30 10:04:30 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-01-30 10:03:31 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | -0.020 |  |
| 2026-01-30 10:00:45 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.032 |  |
| 2026-01-30 10:02:45 | Manampitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.050 |  |
| 2026-01-30 10:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.35 | 🟢 Normal | -0.050 |  |
| 2026-01-30 10:04:53 | Weraganthota (Mahaweli Ganga) | -2.23 | 🟢 Normal | -0.068 |  |
| 2026-01-30 10:05:31 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.261 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)